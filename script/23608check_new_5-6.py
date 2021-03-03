import json
import os
Base_dir=os.path.dirname(os.path.dirname(__file__))
print(Base_dir)
with open(Base_dir+"/data/init_net_new",mode='r',encoding='utf-8') as f:
    init=json.load(f)
    for i in range(200,400):
        init_net=["ws://hqtest.com/s?name=huqi&role=test", 0, 30035, 4827267000, 0, 0, 0, 1000, 48000, 54000, 4827367000, "", 1329, "", 46, False, "application/octet-stream;charset=UTF-8", "", "", True, "devtest.ibr.cc", 38, "4.2.0_20200221 10:48", "{\"bonree1\":\"test1\",\"bonree2\":\"test2\",\"bonree3\":\"test3\",\"bonree4\":\"test4\"}", 5, ["devtest.ibr.cc"], "118.194.54.130", "116.116.116.116", "WiFi", 200, "", "", 0]
        init_net[0]="ws://hqtest5"+str(i)+".com/data/v1"
        init_net[29]=i
        init["udr"]["d"][0]["nr"].append(init_net)
    net_101_5=["ws://hqtest.com/s?name=huqi&role=test", 0, 30035, 4827267000, 0, 0, 0, 1000, 48000, 54000, 4827367000, "", 1329, "", 46, False, "application/octet-stream;charset=UTF-8", "", "", True, "devtest.ibr.cc", 38, "4.2.0_20200221 10:48", "{\"bonree1\":\"test1\",\"bonree2\":\"test2\",\"bonree3\":\"test3\",\"bonree4\":\"test4\"}", 5, ["devtest.ibr.cc"], "118.194.54.130", "116.116.116.116", "WiFi", 101, "", "", 0]
    net_102_5 =["ws://hqtest.com/s?name=huqi&role=test", 0, 30035, 4827267000, 0, 0, 0, 1000, 48000, 54000, 4827367000, "", 1329, "", 46, False, "application/octet-stream;charset=UTF-8", "", "", True, "devtest.ibr.cc", 38, "4.2.0_20200221 10:48", "{\"bonree1\":\"test1\",\"bonree2\":\"test2\",\"bonree3\":\"test3\",\"bonree4\":\"test4\"}", 5, ["devtest.ibr.cc"], "118.194.54.130", "116.116.116.116", "WiFi", 102, "", "", 0]
    net_100_5=["ws://hqtest.com/s?name=huqi&role=test", 0, 30035, 4827267000, 0, 0, 0, 1000, 48000, 54000, 4827367000, "", 1329, "", 46, False, "application/octet-stream;charset=UTF-8", "", "", True, "devtest.ibr.cc", 38, "4.2.0_20200221 10:48", "{\"bonree1\":\"test1\",\"bonree2\":\"test2\",\"bonree3\":\"test3\",\"bonree4\":\"test4\"}", 5, ["devtest.ibr.cc"], "118.194.54.130", "116.116.116.116", "WiFi", 100, "", "", 0]
    init["udr"]["d"][0]["nr"].append(net_101_5)
    init["udr"]["d"][0]["nr"].append(net_102_5)
    init["udr"]["d"][0]["nr"].append(net_100_5)
    for i in range(200,400):
        init_net = ["wss://hqtest.com/s?name=huqi&role=test", 0, 30035, 4827267000, 0, 0, 0, 1000, 48000, 54000,
                    4827367000, "", 1329, "", 46, False, "application/octet-stream;charset=UTF-8", "", "", True,
                    "devtest.ibr.cc", 38, "4.2.0_20200221 10:48",
                    "{\"bonree1\":\"test1\",\"bonree2\":\"test2\",\"bonree3\":\"test3\",\"bonree4\":\"test4\"}", 6,
                    ["devtest.ibr.cc"], "118.194.54.130", "116.116.116.116", "WiFi", 200, "", "", 0]
        init_net[0] = "wss://hqtest6" + str(i) + ".com/data/v1"
        init_net[29] = i
        init["udr"]["d"][0]["nr"].append(init_net)
    net_101_6 = ["wss://hqtest.com/s?name=huqi&role=test", 0, 30035, 4827267000, 0, 0, 0, 1000, 48000, 54000, 4827367000,
                 "", 1329, "", 46, False, "application/octet-stream;charset=UTF-8", "", "", True, "devtest.ibr.cc", 38,
                 "4.2.0_20200221 10:48",
                 "{\"bonree1\":\"test1\",\"bonree2\":\"test2\",\"bonree3\":\"test3\",\"bonree4\":\"test4\"}", 6,
                 ["devtest.ibr.cc"], "118.194.54.130", "116.116.116.116", "WiFi", 101, "", "", 0]
    net_102_6 = ["wss://hqtest.com/s?name=huqi&role=test", 0, 30035, 4827267000, 0, 0, 0, 1000, 48000, 54000, 4827367000,
                 "", 1329, "", 46, False, "application/octet-stream;charset=UTF-8", "", "", True, "devtest.ibr.cc", 38,
                 "4.2.0_20200221 10:48",
                 "{\"bonree1\":\"test1\",\"bonree2\":\"test2\",\"bonree3\":\"test3\",\"bonree4\":\"test4\"}", 6,
                 ["devtest.ibr.cc"], "118.194.54.130", "116.116.116.116", "WiFi", 102, "", "", 0]
    net_100_6 = ["wss://hqtest.com/s?name=huqi&role=test", 0, 30035, 4827267000, 0, 0, 0, 1000, 48000, 54000, 4827367000,
                 "", 1329, "", 46, False, "application/octet-stream;charset=UTF-8", "", "", True, "devtest.ibr.cc", 38,
                 "4.2.0_20200221 10:48",
                 "{\"bonree1\":\"test1\",\"bonree2\":\"test2\",\"bonree3\":\"test3\",\"bonree4\":\"test4\"}", 6,
                 ["devtest.ibr.cc"], "118.194.54.130", "116.116.116.116", "WiFi", 100, "", "", 0]
    init["udr"]["d"][0]["nr"].append(net_101_6)
    init["udr"]["d"][0]["nr"].append(net_102_6)
    init["udr"]["d"][0]["nr"].append(net_100_6)
    net_err_06=["wss://hqtest.com/s?name=huqi&role=test", 0, 30035, 4827267000, 0, 0, 0, 1000, 48000, 54000, 4827367000, "", 1329, "", 46, False, "application/octet-stream;charset=UTF-8", "", "", True, "devtest.ibr.cc", 38, "4.2.0_20200221 10:48", "{\"bonree1\":\"test1\",\"bonree2\":\"test2\",\"bonree3\":\"test3\",\"bonree4\":\"test4\"}", 6, ["devtest.ibr.cc"], "118.194.54.130", "116.116.116.116", "WiFi", 200, "", "", 0]
    net_err_05 = ["ws://hqtest.com/s?name=huqi&role=test", 0, 30035, 4827267000, 0, 0, 0, 1000, 48000, 54000, 4827367000, "", 1329, "", 46, False, "application/octet-stream;charset=UTF-8", "", "", True, "devtest.ibr.cc", 38, "4.2.0_20200221 10:48", "{\"bonree1\":\"test1\",\"bonree2\":\"test2\",\"bonree3\":\"test3\",\"bonree4\":\"test4\"}", 5, ["devtest.ibr.cc"], "118.194.54.130", "116.116.116.116", "WiFi", 404, "", "", 0]
    init["udr"]["d"][0]["nr"].append(net_err_06)
    init["udr"]["d"][0]["nr"].append(net_err_05)
    print(init)
with open(Base_dir+"/data/23608-new-5-6.json","w",encoding="utf-8") as f2:
    f2.write(json.dumps(init))