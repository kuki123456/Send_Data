import requests
import json
#查询启动性能#query_json={"reqType":"queryDpl","reqPara":{"dpl":"table=t_sdk_stat_dru_active appid=3970 |fields LAUNCH_NUM, app_ver_id ,STATEMAIN_ID,launch_time, 		launch_time_type, 		launch_num_type, 		launch_part1, 		launch_part2, 		launch_part3, 		launch_part4, 		launch_part5, 		launch_threshold_id ","datasource":"sdk_data_gran_minute","intervals":["2020-03-09T19:30/2020-03-09T20:05"]}}
#query_json={"reqPara":{"OperationType":"groupBy","OperationPara":{"queryJson":{"filter":{"type":"and","fields":[{"field":"APPID","type":"selector","value":50371}]},"intervals":["2020-02-27T00:00/2020-02-27T11:00","2020-02-26T00:00/2020-02-26T11:00"],"granularity":"day","dataSource":{"type":"table","dataSource":"sdk_data_action_hour.t_zeus_sdk_act_event"},"aggregations":[{"fieldName":"OCCUR_NUM","name":"occurNum","type":"longSum"},{"fieldName":"ACCESS_USER_NUM","Func":"Round","name":"accessUserNum","type":"thetaSketch"}],"queryType":"groupBy","dimensions":[{"outputName":"eventId","type":"default","dimension":"EVENT_ID"},{"outputName":"monitorTime","type":"default","dimension":"MONITOR_TIME"}]}}},"reqType":"query"}
#query_json_305104={"reqPara":{"OperationType":"groupBy","OperationPara":{"queryJson":{"filter":{"type":"and","fields":[{"field":"launch_threshold_id","type":"selector","value":1},{"field":"launch_num_type","type":"selector","value":1},{"field":"APPID","type":"selector","value":3974}]},"intervals":["2020-02-27T19:13/2020-02-27T20:13"],"granularity":"minute","dataSource":{"type":"table","dataSource":"sdk_data_gran_minute.t_sdk_stat_dru_active"},"aggregations":[{"fieldName":"statemain_id","Func":"Round","name":"launchNum","type":"thetaSketch"},{"fieldName":"launch_time","name":"launchTime","type":"doubleSum"}],"queryType":"groupBy","dimensions":[{"outputName":"monitorTime","type":"default","dimension":"monitor_time"},{"outputName":"osId","type":"default","dimension":"os_id"},{"outputName":"osName","type":"default","dimension":"os_name"}]}}},"reqType":"query"}
#query_json_305103={"reqPara":{"OperationType":"groupBy","OperationPara":{"queryJson":{"filter":{"type":"and","fields":[{"field":"launch_threshold_id","type":"selector","value":1},{"field":"launch_num_type","type":"selector","value":1},{"field":"APPID","type":"selector","value":3974}]},"intervals":["2020-02-27T19:13/2020-02-27T20:13"],"dataSource":{"type":"table","dataSource":"sdk_data_gran_minute.t_sdk_stat_dru_active"},"aggregations":[{"filter":{"field":"launch_time_type","type":"selector","value":"1"},"aggregator":{"fieldName":"launch_time","name":"launchTime","type":"doubleSum"},"type":"filtered"},{"filter":{"field":"launch_time_type","type":"selector","value":"1"},"aggregator":{"fieldName":"statemain_id","name":"launchNum","type":"thetaSketch"},"type":"filtered"},{"filter":{"field":"launch_time_type","type":"selector","value":"2"},"aggregator":{"fieldName":"launch_time","name":"slowLaunchTime","type":"doubleSum"},"type":"filtered"},{"filter":{"field":"launch_time_type","type":"selector","value":"2"},"aggregator":{"fieldName":"statemain_id","name":"slowLaunchNum","type":"thetaSketch"},"type":"filtered"}],"queryType":"groupBy","dimensions":[{"outputName":"osId","type":"default","dimension":"os_id"},{"outputName":"osName","type":"default","dimension":"os_name"}]}}},"reqType":"query"}
#query_json={"reqPara":{"OperationType":"groupBy","OperationPara":{"queryJson":{"filter":{"type":"and","fields":[{"field":"launch_threshold_id","type":"selector","value":5},{"field":"launch_num_type","type":"selector","value":2},{"field":"APPID","type":"selector","value":3939}]},"intervals":["2020-02-28T17:42/2020-02-28T18:42"],"dataSource":{"type":"table","dataSource":"sdk_data_gran_minute.t_sdk_stat_dru_active"},"aggregations":[{"fieldName":"statemain_id","Func":"Round","name":"launchNum","type":"thetaSketch"},{"fieldName":"launch_time","name":"launchTime","type":"doubleSum"}],"queryType":"groupBy","dimensions":[{"outputName":"appVerId","type":"default","dimension":"APP_VER_ID"},{"outputName":"appVerName","type":"default","dimension":"app_ver_name"}]}}},"reqType":"query"}
#query_json={"reqPara":{"OperationType":"groupBy","OperationPara":{"queryJson":{"filter":{"type":"and","fields":[{"field":"type","type":"selector","value":2},{"field":"resource_type","type":"selector","value":2},{"field":"appid","type":"selector","value":3950}]},"intervals":["2020-03-06T13:40/2020-03-06T17:00"],"dataSource":{"type":"table","dataSource":"sdk_data_gran_minute.t_sdk_stat_dru_webview"},"aggregations":[{"fieldName":"H5_PAGE_ERROR_NUM","name":"errorNum","type":"longSum"},{"fieldName":"H5_ACCESS_NUM","name":"requestNum","type":"longSum"}],"queryType":"groupBy","dimensions":[{"outputName":"objectId","type":"default","dimension":"domaincode"},{"outputName":"objectName","type":"default","dimension":"domain"}]}}},"reqType":"query"}
#query_json={"reqPara":{"OperationType":"groupBy","OperationPara":{"queryJson":{"filter":{"type":"and","fields":[{"field":"APPID","type":"selector","value":4647}]},"intervals":["2020-05-13T00:00/2020-05-13T23:59"],"having":{"aggregation":"occurNum","type":"greaterThan","value":0},"orderBy":[{"field":"occurNum","sort":"DESC"}],"dataSource":{"type":"table","dataSource":"sdk_data_action_hour.t_zeus_sdk_act_event"},"aggregations":[{"fieldName":"OCCUR_NUM","name":"occurNum","type":"longSum"}],"queryType":"groupBy","dimensions":[{"outputName":"eventId","type":"default","dimension":"EVENT_ID"},{"outputName":"appVerId","type":"default","dimension":"app_ver_id"},{"outputName":"thresholdId","type":"default","dimension":"THRESHOLD_ID"}]}}},"reqType":"query"}
#query_json={"reqPara":{"OperationType":"groupBy","OperationPara":{"queryJson":{"filter":{"type":"and","fields":[{"field":"APPID","type":"selector","value":50298}]},"intervals":["2020-05-13T00:00/2020-05-13T12:00","2020-05-12T00:00/2020-05-12T12:00"],"granularity":"day","dataSource":{"type":"table","dataSource":"sdk_data_action_hour.t_zeus_sdk_act_event"},"aggregations":[{"fieldName":"OCCUR_NUM","name":"occurNum","type":"longSum"},{"fieldName":"ACCESS_USER_NUM","Func":"Round","name":"accessUserNum","type":"thetaSketch"}],"queryType":"groupBy","dimensions":[{"outputName":"eventId","type":"default","dimension":"EVENT_ID"},{"outputName":"monitorTime","type":"default","dimension":"MONITOR_TIME"},{"outputName":"thresholdId","type":"default","dimension":"THRESHOLD_ID"}]}}},"reqType":"query"}
#query_json={ "reqPara": { "dpl": "table = t_sdk_track_log   appid=702964 |fields log_type as logType,log_info as logInfo,monitor_time as monitorTime,custom_info as cus_info,membername as userid|offset 1|head 300|sort -monitor_time",  "intervals": ["2020-07-23T16:07:00.000/2020-07-23T21:00:00.000"],  "datasource": "SDK_DATA_SNAPSHOT_none"  },  "reqType": "queryDpl"  }
# query_json={
#  		"reqPara": {
# 			"dpl": "table = t_zeus_sdk_act_deviceinfo  |fields channel_id as channel,monitor_time as monitor_time|offset 1|head 300|sort -monitor_time",
# 			"intervals": ["2020-07-21T17:00:00.000/2020-07-21T18:00:00.000"],
# 			"datasource": "sdk_data_action_source_none" 		},
# 		"reqType": "queryDpl"
# 	}
#query_json={ "reqPara": { "dpl": "table = t_sdk_track_log   appid=703153 |fields log_type as logType,log_info as logInfo,monitor_time as monitorTime,custom_info as cus_info|offset 1|head 300|sort -monitor_time",  "intervals": ["2020-07-29T00:00:00.000/2020-07-29T22:00:00.000"],  "datasource": "SDK_DATA_SNAPSHOT_none"  },  "reqType": "queryDpl"  }
#query_json={ "reqPara": { "dpl": "table = t_sdk_stat_view_snapshot   appid=703185   |offset 1|head 300|sort -monitor_time",  "intervals": ["2020-07-01T00:00:00.000/2020-08-29T21:00:00.000"],  "datasource": "SDK_DATA_SNAPSHOT_none"  },  "reqType": "queryDpl"  }
#query_json={ "reqPara": { "dpl": "table = t_sdk_track_log   appid=702964 |fields imei_num as imei_num,log_type as logType,log_info as logInfo,monitor_time as monitorTime,custom_info as cus_info,membername as userid|offset 1|head 300|sort -monitor_time", "intervals": ["2020-07-23T16:07:00.000/2020-07-23T20:00:00.000"], "datasource": "SDK_DATA_SNAPSHOT_none" }, "reqType": "queryDpl" }
query_json={ "reqPara": { "dpl": "table =t_sdk_stat_dru_netperf appid=703400|head 300|sort -monitor_time",  "intervals": ["2020-09-01/2020-09-30"],  "datasource": "sdk_data_netperf_minute"  },"reqType": "queryDpl"}
req_json=json.dumps(query_json)
body={"reqJson":req_json,"username":"12345678","token":"12345678"}
re=requests.post(data=body,url="http://devtest.ibr.cc:20036/v1")
#re=requests.post(data=body,url="http://devtest.ibr.cc:20070/v1")
print(re.json())
