#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "yang";

# 在ux中能用，编码格式，作者

'''
python base demo
'''
import re;
import math;

# ====输入输出====
# print("请输入：")
# a=input();
# print(a);#输入
a = 11;
b = "xx";
print(a);
print("hello word");
print("hello", "word");  # 逗号自带空格
print("hello %s" % a);  # 占位符%s
print("hello %s" % (a,));  # 括号加逗号效果一致
print("hello %s - %s" % (a, b));  # 不用-也行

# ====数据类型====
a = 11;
print("a = %s,数据类型是%s" % (a, type(a)));  # int
a = 11.3;
print("a = %s,数据类型是%s" % (a, type(a)));  # float
a = "11";
print("a = %s,数据类型是%s" % (a, type(a)));  # str   string
a = ['1', 1, 1.1];
print("a = %s,数据类型是%s" % (a, type(a)));  # list   数组
a = ("cdsa", 3, 3.2);
print("a = %s,数据类型是%s" % (a, type(a)));  # tuple 元组,不可变值
a = {"name": "yang", "age": 2};
print("a = %s,数据类型是%s" % (a, type(a)));  # dict  键值对
a = None;
print("a = %s,数据类型是%s" % (a, type(a)));  # NoneType  空
a = True or False;
print("a = %s,数据类型是%s" % (a, type(a)));  # bool  boolean or或and或not或>或<
a = set(["asa0", True, None, 2, 2.1])
print("a = %s,数据类型是%s" % (a, type(a)));  # set
# ====运算符====
print(2 + 1 * 2 / 3);
print(12 // 2);  # 地板除，取整
print(12 / 5);

# ====字符串====
print(u'杨');  # unicode
print(r'杨');  # utf-8
print(b'yang');  # bytes
# ----ASCLII转换----
print("98-->%s;a-->%s" % (chr(98), ord('a')));
# ----encode$$decode----编码转换和返回编码
print("aaassasa".encode("ascii"));
print("杨江峰".encode("utf-8"));
print(b'xx'.decode("ascii"));
print(b'\xe6\x9d\xa8\xe6\xb1\x9f\xe5\xb3\xb0'.decode("utf-8"));
# ----function----
print(len("aaa"));
print(len("杨"));  # 2 对于str计算字符
print(len("aaa".encode("utf-8")));
print(len("杨".encode("utf-8")));  # 6 对于bytes计算字符
print("asdddaSDDSAasdfs".replace("as", "---"));  # 替换
print("asddADDSAasddsaASSASas".find("as"));  # 第一次出现的下标
print("asddADDSAasddsaASSASas".rfind("as"));  # 最后异常出现的下标
print("asdssass".isspace());  # 是不为空
print("%s -- %2d -- %02d" % (1, 1, 1));  # 不足2位补空格和补0
print("%s -- %3d -- %03d" % (11, 11, 1));  # 不足3位补空格和补0
print("%f -- %.2f" % (2.12112, 2.122122112))  # 保留位数，四舍五入
print("%x" % 12)  # 转换成16进制
print("%d %% %d" % (5, 3));  # 转义为%
print(list("%s" % x for x in range(1, 10)));  # 遍历添加到list
print("Hi {0},成绩提高了{1:.1f}%".format("小明", 1.254));  # 占位符+保留位数
print("Hi {0},成绩提高了{1}%".format("小明", 1.254));
print("Hi {0},成绩提高了{1}%".format("小明", "%.1f" % 1.254));
print("=".join(["asa", "sa", "dss"]));# 数组转srting

# ====正则表达式====
email_re = "^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$";
if re.match(email_re, "yangjiangfeng@163.com"):
    print("ok");
else:
    print("error");
# ----切分字符----
print("a b c".split(" "));
print(re.split(r"\s+", "a b  c"));
print(re.split(r"[\s,\,\;]+", "a,b;; c    d"));
# ----分组----
# 分组提取电话号码
match = re.match(r'^(\d{3})-(\d{3,8})$', "020-123456");
print(match.group());
print(match.group(0));
print(match.group(1));
print(match.group(2));
# 分组提取数字
new_line = r' 截至9月2日0时，全省累计报告新型冠状病毒肺炎确诊病例653例' \
           r'(其中境外输入112例），累计治愈出院626例，死亡3例，目前在院隔离治疗24例，964人尚在接受医学观察。';
new_line_re = r' 截至9月2日0时，全省累计报告新型冠状病毒肺炎确诊病例(\d+)例' \
              r'\(其中境外输入(\d+)例\），累计治愈出院(\d+)例，死亡(\d+)例，目前在院隔离治疗(\d+)例，(\d+)人尚在接受医学观察。';
new_line_math = re.match(new_line_re, new_line);
print(new_line_math.group(0));
print(new_line_math.group(1));
print(new_line_math.group(2));
print(new_line_math.group(3));
print(new_line_math.group(4));
print(new_line_math.group(5));
print(new_line_math.group(6));
new_line_compile = re.compile(new_line_re);
print(re.search(new_line_compile, new_line).group(1));
print(re.search(new_line_compile, new_line).group(2));
print(re.search(new_line_compile, new_line).group(3));
print(re.search(new_line_compile, new_line).group(4));
print(re.search(new_line_compile, new_line).group(5));
print(re.search(new_line_compile, new_line).group(6));
# 贪婪匹配
print(re.match(r"^(\d+)(0*)$", "102300").groups());  # ('102300', '')
print(re.match(r"^(\d+?)(0*)$", "102300").groups());  # ('1023', '00')

# ====list $ tuple====
q = ["aaa", 12, 12.1, None, True];
print(q);
q2 = list(range(1, 10));
print(q2);
q.append("112");
print(q);
q.insert(2, "assa");
print(q);
q.pop();  # 删除最后一个元素
# pop（1）以下标删除 在list中默认删除最后一个元素，set中默认删除第一个元素
# remove（“元素内容”）以元素内容删除
print(q);
q.pop(2);  # 删除指定位置元素
print(q);
q.append(q2);
print(q);
q += q2;
print(q);
q[0] = "212";
print(q);
# 元组，初始化后不能更改
t = ("aaa", 12, 12.1, None, True, q);
print(t);
q[2] = 12321;
print(t);
t2 = tuple(range(1, 10));
print(t2);
print((1));
print((1,));  # 单个元组需要添加逗号避免被当成数学符号

# ====dict $ set====
d = {"name": "yang", "age": 18};
print(d.get("name1", "aaa"));  # 找不到时给默认值
d["name"] = "li";
d["aaa"] = "asa";
print(d);
d.pop("aaa");
print(d, len(d));
# ----set----key集合，不存储value
s = set(["asa", 123, 12.1, True]);
s.add("asda");
s.remove(1);
s.remove("asa");  # 无序，不能根据下标删除
print("set: %s,length: %s" % (s, len(s)));
s2 = set([123, "fad"]);
print(s & s2);  # 交集
print(s | s2);  # 并集

# 判断语句
a = 20;
if a < 10:
    print("aaaa");
elif a < 10:  # 范围重叠后只会执行第一个语句
    print("bbbb");
else:
    print("cccc");
a = " ";
if a and a.split():
    print(a);
else:
    print("Null string");
# ----三目运算符----
a, b, c = 1, 2, 3;
print(a if (b > c) else c);

# ====循环语句====
f = list(range(1, 10));
for i in f:
    print(i);
i = 0;
while (i < 10):
    print(i);
    i += 1;


# ====函数====
def test(a):
    a += 3;
    return a;


print(test(1));


def test_2(x, y="yang"):
    print(x, y);


def test_3(*num):  # 可变参数
    count = 0;
    for i in num:
        count += i;
    return count;


def test_4(name, **kv):
    if "city" in kv:
        print(" name:%s,city:%s" % (name, kv.get("city")));
        pass;
    else:
        print(" name:%s,city:%s" % (name, "sichuan"));


def test_5(name, *, city):
    if not isinstance(name,(str,)):
       raise TabError("Type error");
    print(" name:%s,city:%s" % (name, city));


if __name__ == "__main__":
    print(test(5));
    test_2("hello", "yang1");
    test_2("hello");  # 默认值
    print(test_3());
    print(test_3(*list(range(1, 16))));
    print(test_3(1, 2, 12));
    test_4("yang", **{"age": 3});
    test_4("yang", **{"age": 3, "city": "chengdu"});
    test_5("yang",city="beijin");
    # test_5(12,city="a");

# ==== 内置函数 ====
print(int("22")); # 数据类型转换函数，注意，如果定义变量名和函数名一样，则不会调用该函数，会报错
print(float("22.2"));
print(str(22));
print(abs(-111)); # abs函数，求绝对值
print(max(12, 34, 123.4)); # max函数，求最大值
print(min(-21, -11, 0, 22.3)); # min函数，求最小值
print(" aa bb  cc  ".strip()); # 字符串去前后空格
print("['6K-8K']".strip('[\'\']')); # 移除字符串头尾指定的字符
print(hex(12)); # hex函数，将十进制数转十六进制
print(math.sqrt(3)); # 求平方根
print(sum(range(1, 101))); # 求和
print(sum(list(range(101))));
print("cdaDcdsa".capitalize()); # 将字符串第一个字符变成大写，其他小写
