import unittest
import pymysql
import os
import time
from BeautifulReport import BeautifulReport as bf

class TestMysql_Br_sdk_druid(unittest.TestCase):
    def common(self, table_name):
        self.columns_test = self.cursor_test.execute("show columns from " + table_name)
        self.columns_dba = self.cursor_dba.execute("show columns from " + table_name)
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    @classmethod
    def setUpClass(cls):
        cls.db_test = pymysql.connect(host="devtest.ibr.cc", port=20104, user="sdk", password="bonree",
                                      db="br_sdk_druid", charset="utf8")
        cls.cursor_test = cls.db_test.cursor()
        cls.db_dba = pymysql.connect(host="devtest.ibr.cc", port=20215, user="br_sdk", password="BR_sdk123",
                                     db="br_sdk_druid", charset="utf8")
        cls.cursor_dba = cls.db_dba.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.cursor_test.close()
        cls.cursor_dba.close()

    def test_t_bas_city(self):
        self.cursor_test.execute("show columns from t_bas_city")
        self.columns_test = self.cursor_test.fetchall()
        print(self.columns_test)
        self.cursor_dba.execute("show columns from t_bas_city")
        self.columns_dba = self.cursor_dba.fetchall()
        self.assertEqual(self.columns_test, self.columns_dba)
    def test_t_bas_city_data(self):
        self.cursor_test.execute("select * from t_bas_city;")
        result_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("select * from t_bas_city;")
        result_dba = self.cursor_dba.fetchall()
        self.assertEqual(result_test, result_dba)
    def test_t_bas_function(self):
        self.cursor_test.execute("show columns from t_bas_function")
        self.columns_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("show columns from t_bas_function")
        self.columns_dba = self.cursor_dba.fetchall()
        print(self.columns_test)
        print(self.columns_dba)
        self.assertEqual(self.columns_test, self.columns_dba)

    def test_t_bas_function_data(self):
        self.cursor_test.execute("select * from t_bas_function;")
        result_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("select * from t_bas_function;")
        result_dba = self.cursor_dba.fetchall()
        self.assertEqual(result_test, result_dba)
    def test_t_bas_netservice(self):
        self.cursor_test.execute("show columns from t_bas_netservice")
        self.columns_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("show columns from t_bas_netservice")
        self.columns_dba = self.cursor_dba.fetchall()
        self.assertEqual(self.columns_test, self.columns_dba)
    def test_t_bas_netservice_data(self):
        self.cursor_test.execute("select * from t_bas_netservice;")
        result_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("select * from t_bas_netservice;")
        result_dba = self.cursor_dba.fetchall()
        self.assertEqual(result_test, result_dba)
    def test_t_bas_recipient_sendgroup(self):
        self.cursor_test.execute("show columns from t_bas_recipient_sendgroup")
        self.columns_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("show columns from t_bas_recipient_sendgroup")
        self.columns_dba = self.cursor_dba.fetchall()
        self.assertEqual(self.columns_test, self.columns_dba)

    def test_t_bas_user_info(self):
        self.cursor_test.execute("show columns from t_bas_user_info")
        self.columns_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("show columns from t_bas_user_info")
        self.columns_dba = self.cursor_dba.fetchall()
        self.assertEqual(self.columns_test, self.columns_dba)

    def test_t_bas_user_info_data(self):
        self.cursor_test.execute("select * from t_bas_user_info;")
        result_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("select * from t_bas_user_info;")
        result_dba = self.cursor_dba.fetchall()
        self.assertEqual(result_test, result_dba)
    def test_t_sdk_act_access_day(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_access_day")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_access_day")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_access_hour(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_access_hour")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_access_hour")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_access_month(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_access_month")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_access_month")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_access_week(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_access_week")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_access_week")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_activity_day(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_access_week")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_access_week")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_activity_hour(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_access_hour")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_access_hour")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_app_day(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_app_day")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_app_day")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_app_hour(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_app_hour")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_app_hour")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_app_month(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_app_month")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_app_month")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_app_week(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_app_week")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_app_week")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_brand_day(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_brand_day")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_brand_day")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_brand_hour(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_brand_hour")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_brand_hour")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_brand_month(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_brand_month")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_brand_month")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_brand_week(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_brand_week")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_brand_week")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_city_day(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_city_day")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_city_day")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_city_hour(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_city_hour")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_city_hour")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_city_month(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_city_month")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_city_month")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_city_week(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_city_week")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_city_week")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_config_channel(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_config_channel")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_config_channel")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_config_event(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_config_event")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_config_event")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_config_process(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_config_process")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_config_process")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_config_task(self):
        self.columns_test = self.cursor_test.execute("show columns from t_sdk_act_config_task")
        self.columns_dba = self.cursor_dba.execute("show columns from t_sdk_act_config_task")
        self.assertEqual(self.columns_test, self.columns_dba)
        self.assertEqual(self.cursor_test.fetchall(), self.cursor_dba.fetchall())

    def test_t_sdk_act_config_view(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_config_view")

    def test_t_sdk_act_event(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_event")

    def test_t_sdk_act_event_day(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_event_day")

    def test_t_sdk_act_event_hour(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_event_hour")

    def test_t_sdk_act_event_month(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_event_month")

    def test_t_sdk_act_event_week(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_event_week")

    def test_t_sdk_act_net_day(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_net_day")

    def test_t_sdk_act_net_hour(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_net_day")

    def test_t_sdk_act_net_month(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_net_month")

    def test_t_sdk_act_net_week(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_net_week")

    def test_t_sdk_act_os_day(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_net_week")

    def test_t_sdk_act_os_hour(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_os_hour")

    def test_t_sdk_act_os_month(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_os_month")

    def test_t_sdk_act_os_week(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_os_week")

    def test_t_sdk_act_process_day(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_process_day")

    def test_t_sdk_act_process_month(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_process_month")

    def test_t_sdk_t_sdk_act_process_week(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_process_week")

    def test_t_sdk_t_sdk_act_px_day(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_px_day")

    def test_t_sdk_act_px_hour(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_px_hour")

    def test_t_sdk_act_px_month(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_px_month")

    def test_t_sdk_act_px_week(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_px_week")

    def test_t_sdk_act_retention_day(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_retention_day")

    def test_t_sdk_act_retention_month(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_retention_month")

    def test_t_sdk_act_retention_week(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_retention_week")

    def test_t_sdk_act_view_day(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_view_day")

    def test_t_sdk_act_view_hour(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_view_hour")

    def test_t_sdk_act_view_month(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_view_month")

    def test_t_sdk_act_view_week(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_act_view_week")

    def test_t_sdk_agent_release_log(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_agent_release_log")

    def test_t_sdk_agent_release_log_data(self):
        self.cursor_test.execute("select * from t_sdk_agent_release_log;")
        result_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("select * from t_sdk_agent_release_log;")
        result_dba = self.cursor_dba.fetchall()
        self.assertEqual(result_test, result_dba)
    def test_t_sdk_app(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_app")

    def test_t_sdk_bas_brand(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_bas_brand")
    def test_t_sdk_bas_accessmodel(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_bas_accessmodel")
    def test_t_sdk_bas_accessmodel_data(self):
        self.cursor_test.execute("select * from t_sdk_bas_accessmodel;")
        result_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("select * from t_sdk_bas_accessmodel;")
        result_dba = self.cursor_dba.fetchall()
        self.assertEqual(result_test, result_dba)
    def test_t_sdk_bas_error(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_bas_error")

    def test_t_sdk_bas_error_data(self):
        self.cursor_test.execute("select * from t_sdk_bas_error;")
        result_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("select * from t_sdk_bas_error;")
        result_dba = self.cursor_dba.fetchall()
        self.assertEqual(result_test, result_dba)

    def test_t_sdk_bas_error_code(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_bas_error_code")

    def test_t_sdk_bas_error_code_data(self):
        self.cursor_test.execute("select * from t_sdk_bas_error_code;")
        result_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("select * from t_sdk_bas_error_code;")
        result_dba = self.cursor_dba.fetchall()
        self.assertEqual(result_test, result_dba)

    def test_t_sdk_bas_menu(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_bas_menu")

    def test_t_sdk_bas_menu_data(self):
        self.cursor_test.execute("select * from t_sdk_bas_menu;")
        result_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("select * from t_sdk_bas_menu;")
        result_dba = self.cursor_dba.fetchall()
        print(result_dba)
        print(result_dba)
        self.assertEqual(result_test, result_dba)

    def test_t_sdk_bas_os(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_bas_os")

    def test_t_sdk_bas_px(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_bas_px")

    def test_t_sdk_config_alert(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_alert")

    def test_t_sdk_config_alert_log(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_alert_log")

    def test_t_sdk_config_alert_log_detail(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_alert_log_detail")

    def test_t_sdk_config_alert_old(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_alert_old")

    def test_t_sdk_config_alert_strategy(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_alert_strategy")

    def test_t_sdk_config_app(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_app")

    def test_t_sdk_config_app_ext(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_app_ext")

    def test_t_sdk_config_app_mapping(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_app_mapping")

    def test_t_sdk_config_app_route(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_app_route")

    def test_t_sdk_config_app_version(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_app_version")

    def test_t_sdk_config_app_version_ext(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_app_version_ext")

    def test_t_sdk_config_auotreport(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_auotreport")

    def test_t_sdk_config_bizgroup(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_bizgroup")

    def test_t_sdk_config_bizgroup_ext(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_bizgroup_ext")

    def test_t_sdk_config_blacklist(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_blacklist")

    def test_t_sdk_config_cdn(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_cdn")
    def test_t_sdk_config_cdn_data(self):
        self.cursor_test.execute("select * from t_sdk_config_cdn;")
        result_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("select * from t_sdk_config_cdn;")
        result_dba = self.cursor_dba.fetchall()
        self.assertEqual(result_test, result_dba)
    def test_t_sdk_config_chart(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_chart")

    def test_t_sdk_config_check(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_check")

    def test_t_sdk_config_check_data(self):
        self.cursor_test.execute("select * from t_sdk_config_check;")
        result_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("select * from t_sdk_config_check;")
        result_dba = self.cursor_dba.fetchall()
        print(result_dba)
        print(result_dba)
        self.assertEqual(result_test, result_dba)
    def test_t_sdk_config_client(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_client")

    def test_t_sdk_config_cname(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_cname")

    def test_t_sdk_config_cname_data(self):
        self.cursor_test.execute("select * from t_sdk_config_cname;")
        result_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("select * from t_sdk_config_cname;")
        result_dba = self.cursor_dba.fetchall()
        print(result_dba)
        print(result_dba)
        self.assertEqual(result_test, result_dba)
    def test_t_sdk_config_crashtack_merge(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_crashtack_merge")

    def test_t_sdk_config_custom_header(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_custom_header")

    def test_t_sdk_config_domain(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_domain")

    def test_t_sdk_config_domain_bak(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_domain_bak")

    def test_t_sdk_config_filtdomain(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_filtdomain")

    def test_t_sdk_config_filter(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_filter")

    def test_t_sdk_config_filter_ext(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_filter_ext")

    def test_t_sdk_config_h5_url(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_h5_url")

    def test_t_sdk_config_ip(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_ip")

    def test_t_sdk_config_jserror_file(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_jserror_file")

    def test_t_sdk_config_keyele(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_keyele")

    def test_t_sdk_config_link(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_link")

    def test_t_sdk_config_notice(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_notice")

    def test_t_sdk_config_page(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_page")

    def test_t_sdk_config_preferences(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_preferences")

    def test_t_sdk_config_recipient(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_recipient")

    def test_t_sdk_config_request_url(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_request_url")

    def test_t_sdk_config_retain_url(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_retain_url")

    def test_t_sdk_config_self_domain(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_self_domain")

    def test_t_sdk_config_sendgroup(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_sendgroup")

    def test_t_sdk_config_socket(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_socket")

    def test_t_sdk_config_sendgroup1(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_sendgroup1")

    def test_t_sdk_config_speed(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_speed")

    def test_t_sdk_config_strategy(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_strategy")

    def test_t_sdk_config_thd_source(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_thd_source")

    def test_t_sdk_config_thd_source_data(self):
        self.cursor_test.execute("select * from t_sdk_config_thd_source;")
        result_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("select * from t_sdk_config_thd_source;")
        result_dba = self.cursor_dba.fetchall()
        print(result_dba)
        print(result_dba)
        self.assertEqual(result_test, result_dba)
    def test_t_sdk_config_urlmerge(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_urlmerge")

    def test_t_sdk_config_use_client(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_use_client")

    def test_t_sdk_config_view(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_view")

    def test_t_sdk_config_view_white(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_view_white")

    def test_t_sdk_config_vip(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_vip")

    def test_t_sdk_config_webviewmerge(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_config_webviewmerge")

    def test_t_sdk_crash_note(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_crash_note")

    def test_t_sdk_crash_note_event(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_crash_note_event")

    def test_t_sdk_newestversion(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_newestversion")

    def test_t_sdk_operate_log(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_operate_log")

    def test_t_sdk_packages(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_packages")

    def test_t_sdk_packages_data(self):
        self.cursor_test.execute("select * from t_sdk_packages;")
        result_test = self.cursor_test.fetchall()
        self.cursor_dba.execute("select * from t_sdk_packages;")
        result_dba = self.cursor_dba.fetchall()
        print(result_dba)
        print(result_dba)
        self.assertEqual(result_test, result_dba)
    def test_t_sdk_role(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_role")

    def test_t_sdk_role_menu(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_role_menu")

    def test_t_sdk_self_crash_note(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_self_crash_note")

    def test_t_sdk_self_crash_note_event(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_self_crash_note_event")

    def test_t_sdk_sharding_info(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_sharding_info")

    def test_t_sdk_stat_active(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_stat_active")

    def test_t_sdk_stat_active_device(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_stat_active_device")

    def test_t_sdk_stat_active_num(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_stat_active_num")

    def test_t_sdk_stat_anr_fix(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_stat_anr_fix")

    def test_t_sdk_stat_crash(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_stat_crash")

    def test_t_sdk_stat_crash_fix(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_stat_crash_fix")

    def test_t_sdk_stat_file_download(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_stat_file_download")

    def test_t_sdk_stat_interact_fix(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_stat_interact_fix")

    def test_t_sdk_stat_lag_fix(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_stat_lag_fix")

    def test_t_sdk_stat_not_sdkinfo(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_stat_not_sdkinfo")

    def test_t_sdk_stat_sdkinfo(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_stat_sdkinfo")

    def test_t_sdk_stat_self_crash_fix(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_stat_self_crash_fix")

    def test_t_sdk_stat_url(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_stat_url")

    def test_t_sdk_umname(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_umname")

    def test_t_sdk_user_app(self):
        TestMysql_Br_sdk_druid.common(self, "t_sdk_user_app")

