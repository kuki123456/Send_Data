import json

import pymysql
import os
Base_dir=os.path.dirname(os.path.dirname(__file__))
print(Base_dir)
db=pymysql.connect(host="devtest.ibr.cc",port=30092,user="druid",password="BR_druid_123",db="br_sdk_druid",charset="utf8")
db=pymysql.connect(host="devtest.ibr.cc",port=20104,user="sdk",password="bonree",db="br_sdk_druid",charset="utf8")
cursor=db.cursor()
sql="select ERROR_ID from t_sdk_bas_error_code"
# sql="select ERROR_ID from t_sdk_bas_error"
cursor.execute(sql)
data = cursor.fetchall()
data_iter=iter(data)
print(data)
print(type(data))
sql2="select PARENT_ERROR_ID from t_sdk_bas_error"
sql2=""
data2=cursor.execute(sql2)
data2=cursor.fetchall()
print(data2)
data2_iter=iter(data2)
with open("t_sdk_bas_error.txt",mode='a+',encoding="utf-8") as f:
     for i in data:
          f.write(str(i)+'\n')
print(data_iter.__next__()[0])
with open(Base_dir+"/data/uoload_android.json",mode='r',encoding='utf-8') as f:
    init_json=json.load(f)
#构造netresult旧协议数据
#     j=1
#     while j <=253:
#         common = ["http://dcs.coohua.com/data/v1", 0, 0, 52898, 0, 80, 421016928, 16304, 39012, 235907, 287, 2182834,
#                   1296928, 103680000,
#                   "POST /maam/getPluginListV2.do?appId=PA01100000000_01_SDK&osVersion=4.4.4&dataVersion=&appVersion=3.10&deviceType=android_MI4LTE&userId=&deviceId=396def37d7d3a8ec3523076392bf4f752&sdkVersion=4.2.0.643 HTTP/1.1\r\nUser-Agent: linlh\r\nContent-Length: 0\r\nHost: maam-dmzstg2.linlh.com.cn:9041\r\nConnection: Keep-Alive\r\nAccept-Encoding: gzip\r\nCookie: BIGipServermaam-core_http_DMZ_Stg2Pool=478614700.5034.0000\r\n\r\n",
#                   406,
#                   "HTTP/1.1 200 OK\r\nCache-Control: no-cache\r\nCache-Control: no-store\r\nDate: Mon, 27 Aug 2018 13:02:44 GMT\r\nPragma: no-cache\r\nTransfer-Encoding: chunked\r\nContent-Type: text/html; charset=UTF-8\r\nExpires: Thu, 01 Jan 1970 00:00:00 GMT\r\n\r\n",
#                   123333, 200, 200, False, "application/x-gzip", 0, "", "", False, "devtest.ibr.cc", 3, 3, -1, "", "",
#                   1, [], "60.205.86.218", "202.102.213.68", "CTRadioAccessTechnologyHSDPA"]
#         common[0]=common[0]+str(j)
#         common[19] = data2_iter.__next__()[0]
#         common[18]=data_iter.__next__()[0]
#         init_json['udr']['d'][0]['nr'].append(common)
#         j+=1
# print(init_json)
# with open (Base_dir+"/data/1045_old_protocol_02.json",mode='w',encoding='utf-8') as f:
#     f.write(json.dumps(init_json))
#构造新协议netresult数据
    j=1
    while j<=99:
        common = ["http://hqtest.com:30035/haonan",0,30035,4827267000,120,220,100,1000,48000,54000,4827367000,"",1329,"",46,False,"application/octet-stream;charset=UTF-8","","",False,"devtest.ibr.cc",38,"4.2.0_20200221 10:48","{\"bonree1\":\"test1\",\"bonree2\":\"test2\",\"bonree3\":\"test3\",\"bonree4\":\"test4\"}",1,["devtest.ibr.cc"],"118.194.54.130","116.116.116.116","WiFi",200,"","{\"Agent\":\" con.con.order.con\",\"Host\":\" devtest.ibr.cc\",\"Bgent\":\" gzip\"}",1]
        common[0] = common[0] + str(j)
        common[29] = data_iter.__next__()[0]
        common[32]=4
        init_json['udr']['d'][0]['nr'].append(common)
        j+=1
print(init_json)
with open (Base_dir+"/data/1045_new_protocol.json",mode='w',encoding='utf-8') as f:
    f.write(json.dumps(init_json))