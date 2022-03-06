# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:33:27 2022

@author: Pandora
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Bar, Line, Pie, WordCloud
from pyecharts.globals import ThemeType,SymbolType
import streamlit_echarts as st_echarts
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title='Medical Insurance Data Analysis',  layout='wide', page_icon=':ambulance:')

#header###########################################################33
t1, t2, t3 = st.columns((1,0.01,1)) 

t1.image('https://www.njglyy.com/images/logo.jpg')
t2.empty()
t3.title("医保数据监测")
t3.markdown(" **tel:** 025-83106666 **| website:** http://www.njglyy.com **| email:** glyyxfb@163.com")


## Data

with st.spinner('Total Statistcs Reporting...'):
    c1, c2, c3, c4, c5 = st.columns((1,1,1,1,1))
    
    todf = pd.read_excel('DataforMock.xlsx',sheet_name = 'Metrics2')
    v1 = todf[(todf['科室']=='全部') & (todf['metrics']== '医保交易')]   
    v2 = todf[(todf['科室']=='全部') & (todf['metrics']== '医疗费用')]   
    v3 = todf[(todf['科室']=='全部') & (todf['metrics']== '医保结算')] 
    
    c1.write('')
    c2.metric(label ='医保交易',value = str(int(v1['Value']))+" 笔", delta = str(int(v1['Previous']))+' 相较昨日')
    c3.metric(label ='医疗费用',value = str(int(v2['Value']))+" 万元", delta = str(int(v2['Previous']))+' 相较昨日')
    c4.metric(label ='医保结算',value = str(int(v3['Value']))+" 人次", delta = str(int(v3['Previous']))+' 相较昨日')
    c1.write('')
    
    g1, g2, g3 = st.columns((2,1,1))
    
    with g2:
        total_two = (
        Bar(init_opts=opts.InitOpts(bg_color=['#f8f8f8'], theme=ThemeType.WESTEROS))
        .add_xaxis(['风湿免疫科','内分泌科','消化内科','神经内科','肿瘤内科'])
        .add_yaxis("", [50,40,30,20,10], category_gap="60%")
        .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=90)),
                          title_opts=opts.TitleOpts(title="科室拒付费用Top5"))
        )
        st_echarts.st_pyecharts(total_two)
    with g1:
        total_one = (
            Line(init_opts=opts.InitOpts(bg_color=['#f8f8f8'], theme=ThemeType.WESTEROS))
            .add_xaxis(['周一','周二','周三','周四','周五','周六','周日'])
            .add_yaxis("上周",Faker.values(),areastyle_opts=opts.AreaStyleOpts(opacity=0.5),label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis("本周",Faker.values(),areastyle_opts=opts.AreaStyleOpts(opacity=0.5),label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="拒付费用统计"))
            )
        st_echarts.st_pyecharts(total_one)
    g3.metric(label ='拒付费用',value = str(123)+" 万元", delta = str(33)+' 相较上月')
    
    d1, d2, d3 = st.columns((2,1,1))
    
    with d1:
        total_one = (
            Line(init_opts=opts.InitOpts(bg_color=['#f8f8f8'], theme=ThemeType.WESTEROS))
            .add_xaxis(['周一','周二','周三','周四','周五','周六','周日'])
            .add_yaxis("上周",Faker.values(),areastyle_opts=opts.AreaStyleOpts(opacity=0.5),label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis("本周",Faker.values(),areastyle_opts=opts.AreaStyleOpts(opacity=0.5),label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="次均费用统计"))
            )
        st_echarts.st_pyecharts(total_one)
    with d2:
        total_two = (
        Bar(init_opts=opts.InitOpts(bg_color=['#f8f8f8'], theme=ThemeType.WESTEROS))
        .add_xaxis(['风湿免疫科','内分泌科','消化内科','神经内科','肿瘤内科'])
        .add_yaxis("", [56,49,37,25,14], category_gap="60%")
        .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=90)),
                          title_opts=opts.TitleOpts(title="科室次均费用Top5"))
        )
        st_echarts.st_pyecharts(total_two)
    d3.metric(label ='次均费用',value = str(165)+" 元", delta = str(-48)+' 相较上月')
    
    
#Selecting Departments################################################
with st.spinner('Updating Report...'):
    
    #Metrics setting and rendering
    dep_df = pd.read_excel('DataforMock.xlsx',sheet_name = 'Department')
    dep = st.selectbox('选择科室', dep_df)
    
    m1, m2, m3, m4, m5 = st.columns((1,1,1,1,1))
    
    todf = pd.read_excel('DataforMock.xlsx',sheet_name = 'Metrics2')
    to = todf[(todf['科室']==dep) & (todf['metrics']== '医保交易')]   
    ch = todf[(todf['科室']==dep) & (todf['metrics']== '医疗费用')]   
    hl = todf[(todf['科室']==dep) & (todf['metrics']== '医保结算')]
    
    m1.write('')
    m2.metric(label ='医保交易',value = str(int(to['Value']))+" 笔", delta = str(int(to['Previous']))+' 相较昨日')
    m3.metric(label ='医疗费用',value = str(int(ch['Value']))+" 万元", delta = str(int(ch['Previous']))+' 相较昨日')
    m4.metric(label ='医保结算',value = str(int(hl['Value']))+" 人次", delta = str(int(hl['Previous']))+' 相较昨日')
    m1.write('')
    
    e1, e2, e3 = st.columns((0.2,1,0.2))
    
    e1.write('')
    
    chdf = pd.read_excel('DataforMock.xlsx',sheet_name = 'overview') 
    
    chdf = chdf[chdf['科室']==dep]
    
    fig = go.Figure(
            data = [go.Table (columnorder = [0,1,2,3,4,5,6], columnwidth = [30,30,30,30,30,30,30],
                header = dict(
                  values = list(chdf.columns),
                  font=dict(size=20, color = 'white'),
                  fill_color = '#264653',
                  align = 'left',
                  height=30
                  )
              , cells = dict(
                  values = [chdf[K].tolist() for K in chdf.columns], 
                  font=dict(size=20),
                  align = 'left',
                  fill_color='#F0F2F6',
                  height=30))]) 
        
    fig.update_layout(title_text="",title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=10), height=100)
        
    e2.plotly_chart(fig, use_container_width=True)
    
    e3.write('')
    
    s1, s2, s3 = st.columns((0.1,1,0.1))
    
    s1.write('')
    
    label = ['总金额',
              '甲类','乙类','丙类',
              '诊疗项目','药品','材料库',
              '化验', '床位', '护理费', '材料费', '检查', '治疗', '西药', '诊察费']
    source = [0,0,0,
              1,1,1,
              2,2,
              3,
              4,4,4,4,4,4,
              5,
              6,
              4,4,
              5,
              6]
    target = [1,2,3,
              4,5,6,
              4,5,
              6,
              7,8,9,11,12,14,
              13,
              10,
              7,11,
              13,
              10]
    value = [1835.4,1399.24,149.8,
              1282.1,149.1,404.2,
              77,1322.24,
              149.8,
              344,200,148,114,401.1,75,
              149.1,
              404.2,
              65,12,
              1322.24,
              149.8]
    link = dict(source = source, target = target, value = value)
    node = dict(label = label, pad=15, thickness=20)
    data = go.Sankey(link = link, node = node)
    fig_sankey = go.Figure(data)
    fig_sankey.update_layout(margin= dict(l=0,r=10,b=10,t=10), height=300)
    s2.plotly_chart(fig_sankey, use_container_width=True)
    
    s3.write('')
    
with st.expander("患者画像"):
    
    p1, p2, p3 = st.columns((0.1,1,0.1))
    
    p1.write('')
    
    with p2:
        words = [
            ("高血压", 10000),
            ("城镇职工", 6181),
            ("新农合", 4386),
            ("吸烟史", 4055),
            ("心脏病", 2467),
            ("城镇居民", 2244),
            ("江苏", 1868),
            ("安徽", 1484),
            ("浙江", 1112),
            ("男性", 865),
            ("女性", 847),
            ("糖尿病", 582),
            ("住院", 555),
            ("离休干部", 550),
            ("本科", 462),
            ("专科", 366),
            ("高中", 360),
            ("急诊", 282),
            ("初诊", 273),
            ("复诊", 265),
        ]
        c = (
            WordCloud(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
            .add("", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
        )
        st_echarts.st_pyecharts(c)
        
    p3.write('')
    
    c1, c2 = st.columns((2,1))
    
    df = pd.DataFrame(
     np.random.randn(1000, 2) / [0.8, 0.8] + [31.76, 117.4],
     columns=['lat', 'lon'])

    c1.map(df)
    
    with c2:
        age = ['0-10','10-20','20-40','40-60','>60']
        dignose = ['初诊','复诊']
        d1 = (
            Pie(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
            .add(
                "",
                [list(z) for z in zip(age, Faker.values())],
                radius=["40%", "75%"],
                center=["50%", "50%"],
                label_opts=opts.LabelOpts(is_show=False),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="患者分布"),
                legend_opts=opts.LegendOpts(pos_left="80%", orient="vertical"),
            )
            .set_series_opts()
        )
        st_echarts.st_pyecharts(d1)
        d2 = (
            Pie(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
            .add(
                "",
                [list(z) for z in zip(dignose, Faker.values())],
                radius=["40%", "75%"],
                center=["50%", "50%"],
                label_opts=opts.LabelOpts(is_show=False),
            )
            .set_global_opts(
                legend_opts=opts.LegendOpts(pos_left="80%", orient="vertical"),
            )
            .set_series_opts()
        )
        st_echarts.st_pyecharts(d2)
    

# with st.expander("医保支出预测"):
#     r1, r2 = st.columns((1,1))
    
    
    
    
    
    
    
    
    
    
    
    
    
    