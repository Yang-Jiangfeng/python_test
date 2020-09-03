#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "yang";

'''
graph test
'''

import plotly;

def draw_line_graph():
    # 准备图轨数据
    trace_1 = plotly.graph_objs.Scatter(
        x=[1,2,3,4],
        y=[32,44,11,65],
        name ="散点图",
        mode="markers"
    );
    trace_2 = plotly.graph_objs.Scatter(
        x=[1, 2, 3, 4],
        y=[12, 23, 57, 12],
        name="折线图",
    );
    line_date = [trace_1,trace_2];
    # 设置画布布局
    layout = plotly.graph_objs.Layout(title="折线图测试",xaxis={"title":"x"},yaxis={"title":"y"});
    # 融合图轨数据和布局
    figure = plotly.graph_objs.Figure(data=line_date,layout=layout);
    # 输出
    plotly.offline.plot(figure,filename="\python\python_test/temp/line_graph.html",image="png");

def draw_bar_graph():
    # 准备图轨数据
    trace_1 = plotly.graph_objs.Bar(
        x=[1, 2, 3, 4],
        y=[32, 44, 11, 65],
        name="第一产业",
    );
    trace_2 = plotly.graph_objs.Bar(
        x=[1, 2, 3, 4],
        y=[12, 23, 57, 12],
        name="第二产业",
    );
    trace_3 = plotly.graph_objs.Bar(
        x=[1, 2, 3, 4],
        y=[23, 14, 46, 82],
        name="第三产业",
    );
    bar_date = [trace_1, trace_2,trace_3];
    # 设置画布布局
    layout = plotly.graph_objs.Layout(title="柱状图测试", xaxis={"title": "季度"}, yaxis={"title": "产值"});
    # 融合图轨数据和布局
    figure = plotly.graph_objs.Figure(data=bar_date, layout=layout);
    # 输出
    plotly.offline.plot(figure, filename="\python\python_test/temp/bar_graph.html", image="png");

def draw_pie_graph():
    # 准备图轨数据
    trace = plotly.graph_objs.Pie(
        labels=["产品一","产品二","产品三","产品四","产品五"],
        values=[13.2,42,45.2,34.2,76.1]
    );
    pie_data = [trace];
    # 设置画布布局
    layout = plotly.graph_objs.Layout(title="饼图测试");
    # 融合图轨数据和布局
    figure = plotly.graph_objs.Figure(data=pie_data, layout=layout);
    # 输出
    plotly.offline.plot(figure, filename="\python\python_test/temp/pie_graph.html", image="png");

if __name__ == "__main__":
    draw_line_graph();
    draw_bar_graph();
    draw_pie_graph();