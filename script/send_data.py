import requests
import json
import os
import time
import gzip
import uuid
from data import DATA_RANDOM

Base_dir = os.path.dirname(os.path.dirname(__file__))
print(Base_dir)

class HQExceptin(Exception):
    def __str__(self):
        print("config返回无m字段")
def send_config_request(appmd5, dev):
    with open(Base_dir + "/data/config_ios_crash.json", mode="rb") as f:
        # json_data=f.read()
        json_data = json.load(f)
        # print(json_data)
        json_data['h']["ai"] = appmd5
        json_data["cr"]["ci"][0]["cg"]=str(uuid.uuid1())#崩溃信息的uuid生成
        # json_data["h"]["di"]["av"]=DATA_RANDOM.random_app_version()#随机APP版本
        # json_data["h"]["di"]["ov"]=DATA_RANDOM.randjson_data["h"]["di"]["ov"]=DATA_RANDOM.om_ov_android()#随机系统版本
        # json_data["h"]["di"]["ds"] = DATA_RANDOM.random_displaySize()#随机分辨率
        # json_data["h"]["di"]["pi"] = DATA_RANDOM.random_partnerId()#随机渠道商
        #json_data["h"]["di"]["di"] = DATA_RANDOM.di_iter_1.__next__()  # 随机设备ID
        print("deviceid:"+str(json_data["h"]["di"]["di"]))
        # json_data["h"]["di"]["pm"] = DATA_RANDOM.random_phoneModel_android()#随机手机型号
        # json_data["h"]["di"]["dip"]=DATA_RANDOM.random_dip()#随机运营商
        #json_data["h"]["di"]["av"] = DATA_RANDOM.av_iter_1.__next__()
        # json_data["h"]["di"]["ov"] = DATA_RANDOM.ov_iter_1.__next__()
        # json_data["h"]["di"]["pm"] = DATA_RANDOM.pm_iter_1.__next__()
        print("config:" + str(json_data))
        # url="https://sdkupload.bonree.com/config"
        url = "http://devtest.ibr.cc:" + dev + "/config"
        #url="http://sdk.tytools.cn:"+dev+"/config"
        # url = "http://devtest.ibr.cc:20125/config"
        headers = {"ProtoType": "json", "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        config_response = requests.post(url=url, headers=headers, data=json.dumps(json_data))
        print("status:"+str(config_response.status_code))
        print("config response:"+str(config_response.json()))
        if config_response.json()["cr"]["m"]==None:
            raise HQExceptin()
        global statmainid, mt
        statmainid = config_response.json().get("cr").get("si")
        mt = config_response.json().get("cr").get("mt")
        return config_response.json()


def send_upload_request(appmd5, si, dev):
    with open(Base_dir + "/data/upload_ios.json", mode="r", encoding="utf-8") as f:
        json_data = json.load(f)
        # print(json.dumps(json_data))
        json_data.get("udr").get("d")[0]["si"] = si
        json_data.get("udr").get("d")[0]["dci"][0]["cg"]=str(uuid.uuid1())
        json_data['h']["ai"] = appmd5
        json_data.get("udr").get("d")[0]["l"][0]["cg"]=str(uuid.uuid1())
        #json_data["h"]["di"]["di"] = DATA_RANDOM.di_iter_2.__next__()
        #json_data['udr']['d'][0]['asr']['lt']=DATA_RANDOM.lt_iter_1.__next__()
        json_data["udr"]['d'][0]['amt'] = mt
        json_data["udr"]['d'][0]['cmt'] = mt
        print("mt:"+str(mt))
        #json_data["h"]["di"]["av"] = DATA_RANDOM.av_iter_2.__next__()
        # json_data["h"]["di"]["ov"] = DATA_RANDOM.ov_iter_2.__next__()
        # json_data["h"]["di"]["pm"] = DATA_RANDOM.pm_iter_2.__next__()
        print("upload:" + str(json_data))
        data_gzip = gzip.compress(bytes(str(json.dumps(json_data)), encoding='utf8'))
        # ="https://sdkupload.bonree.com/upload?key="+appmd5+"_"+"345425252"
        url = "http://devtest.ibr.cc:" + dev + "/upload?key=" + appmd5 + "_" + "345425252"
        #url="http://sdk.tytools.cn:"+dev+"/upload?key=" + appmd5 + "_" + "345425252"
        # url = "http://devtest.ibr.cc:20125/upload?key=" + appmd5 + "_" + "345425252"
        headers = {"ProtoType": "json", "brkey": si,"Br-Content-Encoding":"gzip"}
        upload_response = requests.post(url=url, headers=headers, data=data_gzip)
        print("response status:"+str(upload_response.status_code))
        print(upload_response.json())
        print("responseTime:"+str(time.time()))
        return upload_response.json()


def main(appmd5, dev):
    i = 0
    while i <=19:
        time.sleep(2)
        # c_response = send_config_request("a3b5d2bc-2550-426c-af1a-060e24679e69")
        #u_response = send_upload_request(appmd5,"4:2:"+str(uuid.uuid1()),dev)
        # i+=1
        try:
            c_response = send_config_request(appmd5, dev)
        except Exception as e:
            DATA_RANDOM.pm_iter_1 = iter(DATA_RANDOM.pm)
            DATA_RANDOM.ov_iter_1 = iter(DATA_RANDOM.ov)
            DATA_RANDOM.av_iter_1 = iter(DATA_RANDOM.av)
            DATA_RANDOM.di_iter_1 = iter(DATA_RANDOM.di)
            c_response = send_config_request(appmd5, dev)
        try:
            u_response = send_upload_request(appmd5, c_response.get("cr").get("si"), dev)
        except Exception as e:
            DATA_RANDOM.pm_iter_2 = iter(DATA_RANDOM.pm)
            DATA_RANDOM.ov_iter_2 = iter(DATA_RANDOM.ov)
            DATA_RANDOM.av_iter_2 = iter(DATA_RANDOM.av)
            DATA_RANDOM.di_iter_2 = iter(DATA_RANDOM.di)
            # DATA_RANDOM.lt_iter_1=iter(DATA_RANDOM.lt_iter_1)
            u_response = send_upload_request(appmd5, c_response.get("cr").get("si"), dev)
        if u_response.get("ur").get("rc") == 19:
            i += 1
            print(time.strftime("%Y-%m-%d %X", time.localtime()))
            print("request number:" + str(i))
        else:
            print("发送失败")
            break


if __name__ == "__main__":
    main("e1dee5ee-4ad2-4d0f-ac39-b4e2ee70277f","30035")
