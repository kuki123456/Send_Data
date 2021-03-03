import unittest
import pymysql
import os
import time
class ZeusDb(unittest.TestCase):
    def compare(self,parm01,parm02):
        for i in parm01:
            if i not in parm02:
                return False
            else:
                return True
    @classmethod
    def setUpClass(cls):
        cls.db_test = pymysql.connect(host="devtest.ibr.cc", port=20215, user="br_zeus", password="BR_zeus123",
                                     db="zeusdb", charset="utf8")
        cls.cursor_test = cls.db_test.cursor()
        cls.db_dba = pymysql.connect(host="localhost",port=5757,user="bonree",password="bonree365",db="zeusdb",charset="utf8")
        cls.cursor_dba = cls.db_dba.cursor()
    @classmethod
    def tearDownClass(cls):
        cls.cursor_test.close()
        cls.cursor_dba.close()
    def test_t_zeus_sdk_act_process(self):
        self.cursor_test.execute("select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_process\");")
        self.columns_test = self.cursor_test.fetchall()
        print(self.columns_test)
        self.cursor_dba.execute("select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_process\");")
        self.columns_dba = self.cursor_dba.fetchall()
        print(self.columns_dba)
        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)
    def test_t_zeus_sdk_act_user_usage(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_user_usage\");")
        self.columns_test = self.cursor_test.fetchall()
        print(self.columns_test)
        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_user_usage\");")
        self.columns_dba = self.cursor_dba.fetchall()
        print(self.columns_dba)
        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)
    def test_t_sdk_stat_dru_slow_domain(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"sdk_stat_dru_slow_domain\");")
        self.columns_test = self.cursor_test.fetchall()
        print(self.columns_test)
        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"sdk_stat_dru_slow_domain\");")
        self.columns_dba = self.cursor_dba.fetchall()
        print(self.columns_dba)
        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)
    def test_t_sdk_config_dru_client(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_config_dru_client\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_config_dru_client\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_active(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_active\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_active\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_anr(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_anr\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_anr\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)


    def test_t_sdk_stat_dru_cdn(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_cdn\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_cdn\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_crash(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_crash\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_crash\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_device(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_device\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_device\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_error(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_error\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_error\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_flow(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_flow\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_flow\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_h5(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_h5\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_h5\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_interact(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_interact\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_interact\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_jserror(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_jserror\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_jserror\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)


    def test_t_sdk_stat_dru_keyelement(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_keyelement\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_keyelement\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_lag(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_lag\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_lag\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_overview(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_overview\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_overview\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)


    def test_t_sdk_stat_dru_slow_domain(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_slow_domain\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_slow_domain\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_speed(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_speed\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_speed\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_view(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_view\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_view\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_visit(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_visit\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_visit\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)



    def test_t_zeus_sdk_act_page(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_page\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_page\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_dru_netperf(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_netperf\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_dru_netperf\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_account_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_account_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_account_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_active_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_active_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_active_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_anr_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_anr_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_anr_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_crash_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_crash_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_crash_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)


    def test_t_sdk_stat_error_cdn_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_error_cdn_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_error_cdn_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_error_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_error_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_error_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_h5_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_h5_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_h5_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_interact_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_interact_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_interact_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_jserror_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_jserror_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_jserror_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_key_error_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_key_error_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_key_error_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_key_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_key_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_key_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_lag_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_lag_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_lag_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_netperf_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_netperf_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_netperf_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_self_crash_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_self_crash_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_self_crash_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_sdk_stat_view_snapshot(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_view_snapshot\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_stat_view_snapshot\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)


    def test_t_sdk_track_log(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_track_log\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_sdk_track_log\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)


    def test_t_zeus_sdk_act_deviceinfo(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_deviceinfo\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_deviceinfo\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_zeus_sdk_act_event(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_event\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_event\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_zeus_sdk_act_page(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_page\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_page\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_zeus_sdk_act_process(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_process\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_process\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_zeus_sdk_act_stat_bas(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_stat_bas\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_stat_bas\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_zeus_sdk_act_user_lostandexists(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_user_lostandexists\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_user_lostandexists\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)

    def test_t_zeus_sdk_act_user_usage(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_user_usage\");")

        self.columns_test = self.cursor_test.fetchall()

        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_user_usage\");")

        self.columns_dba = self.cursor_dba.fetchall()

        self.result = self.compare(self.columns_test, self.columns_dba)
        self.assertEqual(True, self.result)








