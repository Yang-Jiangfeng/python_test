#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "yang";

'''
mysql utils
'''
import pymysql;

# 获取连接属性
def get_connect_cursor():
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db="test", charset='utf8');
    return conn,conn.cursor();

# 增删改spl
def execute_insert_update_delete(cursor,sql):
    result =cursor.execute(sql);
    return result;

# 查询sql
def execute_query(cursor,sql):
    cursor.execute(sql);
    return cursor.fetchall();

# 提交事务
def execute_commit(conn):
    conn.commit();

# 关闭连接
def execute_close(cur,conn):
    cur.close();
    conn.close();

def execute_sql(sql):
    connect,cursor = get_connect_cursor();
    result = None;
    if sql.startswith("select"):
        result = execute_query(cursor,sql);
        execute_close(connect,cursor);
    else:
        result = execute_insert_update_delete(cursor,sql);
        execute_commit(connect);
        execute_close(connect,cursor);
    return result;

if __name__ == "__main__":
    pass;