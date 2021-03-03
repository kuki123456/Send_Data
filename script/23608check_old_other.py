import json
import os
Base_dir=os.path.dirname(os.path.dirname(__file__))
print(Base_dir)
with open(Base_dir+"/data/upload_android.json",mode='r',encoding='utf-8') as f:
    init=json.load(f)
    for i in range(200,400):
        init_net=["http://dcs.coohua.com/data/v1", 0, 0, 52898, 0, 80, 421016928, 16304, 39012, 235907, 287, 1558071, 1762356, 103680000, "POST /maam/getPluginListV2.do?appId=PA01100000000_01_SDK&osVersion=4.4.4&dataVersion=&appVersion=3.10&deviceType=android_MI4LTE&userId=&deviceId=396def37d7d3a8ec3523076392bf4f752&sdkVersion=4.2.0.643 HTTP/1.1\r\nUser-Agent: linlh\r\nContent-Length: 0\r\nHost: maam-dmzstg2.linlh.com.cn:9041\r\nConnection: Keep-Alive\r\nAccept-Encoding: gzip\r\nCookie: BIGipServermaam-core_http_DMZ_Stg2Pool=478614700.5034.0000\r\n\r\n", 406, "HTTP/1.1 200 OK\r\nCache-Control: no-cache\r\nCache-Control: no-store\r\nDate: Mon, 27 Aug 2018 13:02:44 GMT\r\nPragma: no-cache\r\nTransfer-Encoding: chunked\r\nContent-Type: text/html; charset=UTF-8\r\nExpires: Thu, 01 Jan 1970 00:00:00 GMT\r\n\r\n", 123333, 200, 200, False, "application/x-gzip", 0, "", "", False, "devtest.ibr.cc", 3, 3, -1, "", "", 1, [], "60.205.86.218", "202.102.213.68", "UMTS"]
        init_net[0]="http://dcs.coohua5"+str(i)+".com/data/v1"
        init_net[18]=i
        init_net[19] = i
        init_net[32] = 1
        init["udr"]["d"][0]["nr"].append(init_net)
    for i in range(200,400):
        init_net=["http://dcs.coohua.com/data/v1", 0, 0, 52898, 0, 80, 421016928, 16304, 39012, 235907, 287, 1558071, 1762356, 103680000, "POST /maam/getPluginListV2.do?appId=PA01100000000_01_SDK&osVersion=4.4.4&dataVersion=&appVersion=3.10&deviceType=android_MI4LTE&userId=&deviceId=396def37d7d3a8ec3523076392bf4f752&sdkVersion=4.2.0.643 HTTP/1.1\r\nUser-Agent: linlh\r\nContent-Length: 0\r\nHost: maam-dmzstg2.linlh.com.cn:9041\r\nConnection: Keep-Alive\r\nAccept-Encoding: gzip\r\nCookie: BIGipServermaam-core_http_DMZ_Stg2Pool=478614700.5034.0000\r\n\r\n", 406, "HTTP/1.1 200 OK\r\nCache-Control: no-cache\r\nCache-Control: no-store\r\nDate: Mon, 27 Aug 2018 13:02:44 GMT\r\nPragma: no-cache\r\nTransfer-Encoding: chunked\r\nContent-Type: text/html; charset=UTF-8\r\nExpires: Thu, 01 Jan 1970 00:00:00 GMT\r\n\r\n", 123333, 200, 200, False, "application/x-gzip", 0, "", "", False, "devtest.ibr.cc", 3, 3, -1, "", "", 1, [], "60.205.86.218", "202.102.213.68", "UMTS"]
        init_net[0]="https://dcs.coohua6"+str(i)+".com/data/v1"
        init_net[18] = i
        init_net[19] = i
        init_net[32] = 2
        init["udr"]["d"][0]["nr"].append(init_net)
    net_err_01=["http://dcs.coohua1404.com/data/v1", 0, 0, 52898, 0, 80, 421016928, 16304, 39012, 235907, 287, 1558071, 1762356, 103680000, "POST /maam/getPluginListV2.do?appId=PA01100000000_01_SDK&osVersion=4.4.4&dataVersion=&appVersion=3.10&deviceType=android_MI4LTE&userId=&deviceId=396def37d7d3a8ec3523076392bf4f752&sdkVersion=4.2.0.643 HTTP/1.1\r\nUser-Agent: linlh\r\nContent-Length: 0\r\nHost: maam-dmzstg2.linlh.com.cn:9041\r\nConnection: Keep-Alive\r\nAccept-Encoding: gzip\r\nCookie: BIGipServermaam-core_http_DMZ_Stg2Pool=478614700.5034.0000\r\n\r\n", 406, "HTTP/1.1 200 OK\r\nCache-Control: no-cache\r\nCache-Control: no-store\r\nDate: Mon, 27 Aug 2018 13:02:44 GMT\r\nPragma: no-cache\r\nTransfer-Encoding: chunked\r\nContent-Type: text/html; charset=UTF-8\r\nExpires: Thu, 01 Jan 1970 00:00:00 GMT\r\n\r\n", 123333, 404, 404, False, "application/x-gzip", 0, "", "", False, "devtest.ibr.cc", 3, 3, -1, "", "", 1, [], "60.205.86.218", "202.102.213.68", "UMTS"]
    net_err_02 = ["https://dcs.coohua2404.com/data/v1", 0, 0, 52898, 0, 80, 421016928, 16304, 39012, 235907, 287, 1558071, 1762356, 103680000, "POST /maam/getPluginListV2.do?appId=PA01100000000_01_SDK&osVersion=4.4.4&dataVersion=&appVersion=3.10&deviceType=android_MI4LTE&userId=&deviceId=396def37d7d3a8ec3523076392bf4f752&sdkVersion=4.2.0.643 HTTP/1.1\r\nUser-Agent: linlh\r\nContent-Length: 0\r\nHost: maam-dmzstg2.linlh.com.cn:9041\r\nConnection: Keep-Alive\r\nAccept-Encoding: gzip\r\nCookie: BIGipServermaam-core_http_DMZ_Stg2Pool=478614700.5034.0000\r\n\r\n", 406, "HTTP/1.1 200 OK\r\nCache-Control: no-cache\r\nCache-Control: no-store\r\nDate: Mon, 27 Aug 2018 13:02:44 GMT\r\nPragma: no-cache\r\nTransfer-Encoding: chunked\r\nContent-Type: text/html; charset=UTF-8\r\nExpires: Thu, 01 Jan 1970 00:00:00 GMT\r\n\r\n", 123333, 404, 404, False, "application/x-gzip", 0, "", "", False, "devtest.ibr.cc", 3, 3, -1, "", "", 2, [], "60.205.86.218", "202.102.213.68", "UMTS"]
    init["udr"]["d"][0]["nr"].append(net_err_01)
    init["udr"]["d"][0]["nr"].append(net_err_02)
    print(init)
with open(Base_dir+"/data/23608-old-1-2.json","w",encoding="utf-8") as f2:
    f2.write(json.dumps(init))