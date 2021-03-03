#!/usr/bin/env bash
###########执行构建任务###########
cd /usr/jenkins_agent/workspace/WEB_PACKAGE_DEPLOY/SDK_Web
/usr/apache-maven-3.6.3/bin/mvn clean package -Dmaven.test.skip=true
##########打印信息与生成版本文件###########
DATE=`date +%Y%m%d%k%M`
echo "打包分支：${Branch}"
echo "版本_COMMITID_打包时间：${Version}_${GIT_COMMIT}_${DATE}"
cd /usr/version_commit/WEB
echo ${Version}_${GIT_COMMIT}_${DATE} > WEB_COMMIT.txt
########FTP信息#######
host="118.194.54.240"
port=6666
user="dev"
password="GIiU1Jz8LVkIpvW7"
#######发送程序包#####
ftp -n<<!
open ${host} ${port}
user ${user} ${password}
binary
mkdir /SDK/dev/platform/WEB/SDK_WEB/${Version}_${GIT_COMMIT}_${DATE}
mkdir /SDK/dev/platform/WEB/SDK_BIG/${Version}_${GIT_COMMIT}_${DATE}
mkdir /SDK/dev/platform/WEB/SDK_Web_AutoReport/${Version}_${GIT_COMMIT}_${DATE}
mkdir /SDK/dev/platform/WEB/SDK_Web_AutoExpire/${Version}_${GIT_COMMIT}_${DATE}
cd /SDK/dev/platform/WEB/SDK_WEB/${Version}_${GIT_COMMIT}_${DATE}
lcd /usr/jenkins_agent/workspace/WEB_PACKAGE_DEPLOY/SDK_Web/SDK_Web_Base/target
prompt
put SDK.war  SDK.war
prompt
cd /SDK/dev/platform/WEB/SDK_BIG/${Version}_${GIT_COMMIT}_${DATE}
lcd /usr/jenkins_agent/workspace/WEB_PACKAGE_DEPLOY/SDK_Web/SDK_Web_Big/target
prompt
put SDKBIG.war SDKBIG.war
prompt
cd /SDK/dev/platform/WEB/SDK_Web_AutoReport/${Version}_${GIT_COMMIT}_${DATE}
/SDK/dev/platform/WEB/SDK_Web_AutoReport/${Version}_${GIT_COMMIT}_${DATE}
lcd /usr/jenkins_agent/workspace/WEB_PACKAGE_DEPLOY/SDK_Web/SDK_Web_AutoReport/target
prompt
put SDK_WEB_AUTOREPORT.jar SDK_WEB_AUTOREPORT.jar
prompt
cd /SDK/dev/platform/WEB/SDK_Web_AutoExpire/${Version}_${GIT_COMMIT}_${DATE}
lcd /usr/jenkins_agent/workspace/WEB_PACKAGE_DEPLOY/SDK_Web/SDK_Web_AutoExpire/target
prompt
put SDK_WEB_AUTOEXPIRE.jar SDK_WEB_AUTOEXPIRE.jar
prompt
cd /SDK/dev/platform/WEB
lcd /usr/version_commit/WEB
prompt
put WEB_COMMIT.txt WEB_COMMIT.txt
close
bye
!