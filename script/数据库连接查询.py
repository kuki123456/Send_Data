import csv
import pymysql
import os
Base_dir=os.path.dirname(os.path.dirname(__file__))
print(Base_dir)
db=pymysql.connect(host="devtest.ibr.cc",port=20104,user="sdk",password="bonree",db="br_sdk_druid",charset="utf8")
#db=pymysql.connect(host="devtest.ibr.cc",port=30092,user="druid",password="BR_druid_123",db="br_sdk_druid",charset="utf8")
#107数据库db=pymysql.connect(host="devtest.ibr.cc",port=20215,user="br_sdk",password="BR_sdk123",db="br_sdk_druid",charset="utf8")
#db=pymysql.connect(host="devtest.ibr.cc",port=20215,user="br_zeus",password="BR_zeus123",db="zeusdb",charset="utf8")
#db=pymysql.connect(host="localhost",port=5757,user="bonree",password="bonree365",db="zeusdb",charset="utf8")
cursor=db.cursor()
#sql="select * from zeus_metadata_table where table_name='t_zeus_sdk_act_page';"
#sql="select FIELD_NAME,VALUE_TYPE,FIELD_TYPE,FIELD_DESC from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_overview\");"
###############
# sql="select ERROR_ID  from t_sdk_bas_error_code;"
# data1312=cursor.execute(sql)
# print(data1312)
# data = cursor.fetchall()
# data_iter=iter(data)
# print(data)
# data_old=[]
# for m in data:
#     data_old.append(m[0])
# print(data_old)
# different=[]
# f2=csv.reader(open("D:\send_data\data\code.csv","r",encoding="utf-8"))
# print(f2)
# for i in f2:
#     if int(i[0]) in data_old:
#         continue
#     else:
#         different.append(i[0])
# print(different)
###############
# sql2="show columns from t_sdk_bas_error "
# sql2="select * from t_sdk_bas_error where NAME='Connection timed out'"
# data2=cursor.execute(sql2)
# data2=cursor.fetchall()
# print(data2)
# data2_iter=iter(data2)
################
sql="select ERROR_ID  from t_sdk_bas_error;"
data1312=cursor.execute(sql)
code_old=cursor.fetchall()
code_old_List=[]
for i in code_old:
    code_old_List.append(i[0])
print(code_old_List)
sql02="select ERROR_ID  from t_sdk_bas_error_code;"
code_new=cursor.execute(sql02)
code_new_tuple=cursor.fetchall()
code_new_list=[]
for m in code_new_tuple:
    code_new_list.append(m[0])
print(code_new_list)
different=[]
for k in code_old_List:
    if k not in code_new_list:
        different.append(k)
        continue
print(different)
cursor.close()
