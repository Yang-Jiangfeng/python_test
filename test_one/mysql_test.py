#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "yang";

'''
mysql test
'''
import mysql_util;


def inser_resource():
    conn, cur = mysql_util.get_connect_cursor("test");
    sql = "insert into money(name,money) values('wangliu',2000)";
    mysql_util.execute_insert_update_delete(cur,sql);
    mysql_util.execute_commit(conn);
    mysql_util.execute_close(conn, cur);

def query_resource():
    conn, cur = mysql_util.get_connect_cursor("test");
    sql = "select * from money";
    result = mysql_util.execute_query(cur, sql);
    print(result);
    mysql_util.execute_close(conn, cur);

if __name__ == "__main__":
    # inser_resource();
    query_resource();
