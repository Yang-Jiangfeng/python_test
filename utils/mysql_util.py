#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "yang";

'''
mysql utils
'''
import pymysql;

# 获取连接属性
def get_connect_cursor(db):
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db=db, charset='utf8');
    return conn,conn.cursor();

# 增删改spl
def execute_insert_update_delete(cursor,sql):
    result =cursor.execute(sql);
    return result;

# 查询sql
def execute_query(cursor,sql):
    cursor.execute(sql);
    return cursor.fetchall();

# 提交
def execute_commit(conn):
    conn.commit();

# 关闭连接
def execute_close(cur,conn):
    cur.close();
    conn.close();