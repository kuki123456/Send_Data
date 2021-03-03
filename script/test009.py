test01={
	"accessModelId": 4,
	"activityEtime": 0,
	"activityId": "",
	"activityIdIsURL": 0,
	"activityName": "",
	"activityStime": 0,
	"agentMonitorTime": 1593656425000,
	"appId": 702911,
	"appMemory": 3715.47998046875,
	"appVersionId": 1677180,
	"appVersionName": "1.0.0.6",
	"brUsername": "admin",
	"channelId": 6008,
	"cityCode": 3930101,
	"clientIp": "139.117.54.125",
	"conMonitorTime": 1593656425106,
	"deviceId": "829157b67d430bdfb6cab6a2da00321e_050",
	"displaySize": "1080*1920",
	"eventId": 0,
	"fragmentName": "",
	"isQuit": 0,
	"kv": "",
	"lable": "",
	"lastExTime": 0,
	"memberId": "",
	"mobileUsage": 0.0,
	"model": 3,
	"monitorTime": 1593656425106,
	"netServiceId": 0,
	"netServiceName": "其它",
	"osVersionId": 1,
	"parentActionActivityId": "",
	"sessionId": "",
	"sessionName": "",
	"statmainId": "4:2:fc2f2fd5-85fc-8149-acb9-bdf19f90cc0d",
	"stayingTime": 0,
	"timeCallTimeUs": 0,
	"userAccessType": 1,
	"userTrackStime": 0,
	"worth": 0.0
}
test02={
	"accessModelId": 7,
	"activityEtime": 0,
	"activityId": "",
	"activityIdIsURL": 0,
	"activityName": "",
	"activityStime": 0,
	"appId": 702718,
	"appMemory": 4096.0,
	"appVersionId": 125,
	"appVersionName": "5.9.1(appv1)",
	"channelId": 521,
	"cityCode": 1102100,
	"clientIp": "112.224.2.90",
	"conMonitorTime": 1573594020000,
	"deviceId": "linlh_stable_appv1_channel1_14",
	"displaySize": "1080*1776",
	"eventId": 0,
	"fragmentName": "",
	"isQuit": 0,
	"kv": "a,b",
	"lable": "",
	"lastExTime": 0,
	"mobileUsage": 2070.0,
	"model": 1910,
	"monitorTime": 1573596000000,
	"netServiceId": 2,
	"netServiceName": "联通",
	"osVersionId": 1621,
	"parentActionActivityId": "",
	"sessionId": "",
	"sessionName": "",
	"statmainId": "4:2:e45f8974-2002-11ea-a4d3-7261e617b4e6",
	"stayingTime": 0,
	"timeCallTimeUs": 6000000,
	"userAccessType": 2,
	"userTrackStime": 0,
	"worth": 0.0
}
test03=[]
test04=[]
for key,value in test01.items():
    print(key)
    print(value)
    test03.append(key)
for key,value in test02.items():
    test04.append(key)
for i in test03:
    if i not in test02:
        print(i)
        continue