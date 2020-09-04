#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "yang";

'''
gzbd graph
'''

import plotly;
import gzbd.gzbd_storage;

def draw_line_graph():
    result = gzbd.gzbd_storage.get_gzbd_data();
    x = [];
    y_diagnosis = [];
    y_cure = [];
    y_death = [];
    for i in range(1,len(result)+1):
        if i<12:
            item = result[i];
            x.append(item[2]);
            y_diagnosis.append(item[3]);
            y_cure.append(item[5]);
            y_death.append(item[6]);

    # 准备图轨数据
    trace_1 = plotly.graph_objs.Scatter(
        x=x,
        y=y_cure,
        name="治愈数",
    );
    trace_2 = plotly.graph_objs.Scatter(
        x=x,
        y=y_diagnosis,
        name="确诊数"
    );
    trace_3 = plotly.graph_objs.Scatter(
        x=x,
        y=y_death,
        name="死亡数"
    );
    line_data = [trace_1, trace_2, trace_3];
    # 设置画布布局
    layout = plotly.graph_objs.Layout(title="gzbd折线图", xaxis={"title": "时间"}, yaxis={"title": "数量"});
    # 融合图轨数据和布局
    figure = plotly.graph_objs.Figure(data=line_data, layout=layout);
    # 输出
    plotly.offline.plot(figure, filename="/python/python_test/temp/line_graph.html", image="png");

if __name__ == '__main__':
    draw_line_graph();