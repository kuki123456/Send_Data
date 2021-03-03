import requests
import json
import os
import time
import gzip
import uuid

from data import DATA_RANDOM

Base_dir=os.path.dirname(os.path.dirname(__file__))
print(Base_dir)
def send_config_request(appmd5,dev):
    with open(Base_dir+"/data/config_android_no_crash.json",mode="rb") as f:
        #json_data=f.read()
        json_data=json.load(f)
        #print(json_data)
        json_data['h']["ai"]=appmd5
        #json_data["cr"]["ci"][0]["cg"]=str(uuid.uuid1())#崩溃信息的uuid生成
        # json_data["h"]["di"]["av"]=DATA_RANDOM.random_app_version()#随机APP版本
        # json_data["h"]["di"]["ov"]=DATA_RANDOM.randjson_data["h"]["di"]["ov"]=DATA_RANDOM.om_ov_android()#随机系统版本
        # json_data["h"]["di"]["ds"] = DATA_RANDOM.random_displaySize()#随机分辨率
        # json_data["h"]["di"]["pi"] = DATA_RANDOM.random_partnerId()#随机渠道商
        # json_data["h"]["di"]["di"] = DATA_RANDOM.random_deviceId()#随机设备ID
        # json_data["h"]["di"]["pm"] = DATA_RANDOM.random_phoneModel_android()#随机手机型号
        # json_data["h"]["di"]["dip"]=DATA_RANDOM.random_dip()#随机运营商
        #json_data["h"]["di"]["av"] = DATA_RANDOM.av_iter_1.__next__()
        # json_data["h"]["di"]["ov"] = DATA_RANDOM.ov_iter_1.__next__()
        # json_data["h"]["di"]["pm"] = DATA_RANDOM.pm_iter_1.__next__()
        print(json_data)
        # url="https://sdkupload.bonree.com/config"
        # url = "http://devtest.ibr.cc:30035/config"
        #url = "http://devtest.ibr.cc:20125/config"
        url = "http://devtest.ibr.cc:"+dev+"/config"
        headers={"ProtoTYPE":"json"}
        config_response=requests.post(url=url,headers=headers,data=json.dumps(json_data))
        print(config_response.json())
        global statmainid,mt
        statmainid=config_response.json().get("cr").get("si")
        mt=config_response.json().get("cr").get("mt")
        # print(statmainid)
        return config_response.json()
def send_upload_request(appmd5,si,dev):
    with open(Base_dir+"/data/400.txt",mode="rb") as f:
        json_data=json.load(f)
        # print(json.dumps(json_data))
        # print(json_data.get("udr").get("d"))
        json_data.get("udr").get("d")[0]["si"]=si
        json_data['h']["ai"]=appmd5
        # json_data['udr']['d'][0]['asr']['lt']=DATA_RANDOM.lt_iter_1.__next__()
        json_data["udr"]['d'][0]['amt']=mt+5000
        json_data["udr"]['d'][0]['cmt']=mt
        # json_data["h"]["di"]["av"] = DATA_RANDOM.av_iter_2.__next__()
        # json_data["h"]["di"]["ov"] = DATA_RANDOM.ov_iter_2.__next__()
        # json_data["h"]["di"]["pm"] = DATA_RANDOM.pm_iter_2.__next__()
        # print("upload:"+str(json_data))
        data_gzip=gzip.compress(bytes(str(json.dumps(json_data)), encoding='utf8'))
        # url="https://sdkupload.bonree.com/upload?key="+appmd5+"_"+"345425252"
        # url = "http://devtest.ibr.cc:30035/upload?key=" + appmd5 + "_" + "345425252"
        #url = "http://devtest.ibr.cc:20125/upload?key=" + appmd5 + "_" + "345425252"
        url = "http://devtest.ibr.cc:"+dev+"/upload?key=" + appmd5 + "_" + "345425252"
        si="4:2:"+str(uuid.uuid1())
        headers = {"ProtoTYPE": "json","brkey":si,"Br-Content-Encoding":"gzip"}
        upload_response = requests.post(url=url, headers=headers, data=data_gzip)
        print(type(upload_response))
        print(upload_response.json())
        return upload_response.json()
def main(appmd5,dev):
    i=0
    while i<=99:
        time.sleep(2)
        # c_response = send_config_request("a3b5d2bc-2550-426c-af1a-060e24679e69")
        # u_response = send_upload_request("a3b5d2bc-2550-426c-af1a-060e24679e69","4:2:"+str(uuid.uuid1()))
        # i+=1
        try:
            c_response=send_config_request(appmd5,dev)
        except Exception as e:
            DATA_RANDOM.pm_iter_1=iter(DATA_RANDOM.pm)
            DATA_RANDOM.ov_iter_1 = iter(DATA_RANDOM.ov)
            DATA_RANDOM.av_iter_1= iter(DATA_RANDOM.av)
            c_response = send_config_request(appmd5,dev)
        try:
            u_response=send_upload_request(appmd5,c_response.get("cr").get("si"),dev)
        except Exception as e:
            DATA_RANDOM.pm_iter_2=iter(DATA_RANDOM.pm)
            DATA_RANDOM.ov_iter_2 = iter(DATA_RANDOM.ov)
            DATA_RANDOM.av_iter_2 = iter(DATA_RANDOM.av)
            # DATA_RANDOM.lt_iter_1=iter(DATA_RANDOM.lt_iter_1)
            u_response = send_upload_request(appmd5,c_response.get("cr").get("si"),dev)
        if u_response.get("ur").get("rc")==19:
            i+=1
            print(time.strftime("%Y-%m-%d %X",time.localtime()))
            print("request number:"+str(i))
        else:
            print("发送失败")
            break
if __name__=="__main__":
    main("d40359f5-2bc2-4fb4-b02a-02a89e94a1f4","30035")