# a demo of streamlit

import json
from click import option
import streamlit as st
from streamlit_echarts import st_echarts,Map

# 设置页面标题
st.title("Cybersecurity Attacks Visualization")

# 指标
metrics=st.columns(4)
metrics[0].metric("Total IPs",2000)
metrics[1].metric("Malicious IPs",1000)
metrics[2].metric("Malicious %",'50%')
metrics[3].metric("Attacks per Day",100)

# 饼图


# 世界地图

# st.map()
with open('./data/worldEN.json',encoding='utf-8') as f:
    map=Map("world",json.load(f))
options = {
    "title": {
        "text": "World Map",
    },
    "tooltip": {"trigger": "item"},
    "visualMap": {"max": 500},
    "series": [
        {
            "name": "Attckers",
            "map": "world",
            "type": "map",
            "roam": True,
            "data":[
                {"name":"China","value":1000}
            ]
        }
    ]  
}
st_echarts(options,map=map)

# st.metric("Total","3,400")
# st.metric("Total","3,400")
# st.metric("Total","3,400")
# st.metric("Total","3,400")
# st.metric("Total","3,400")
# st.metric("Total","3,400")
# st.metric("Total","3,400")

# col1,col2,col3,col4=st.columns(4)

# with col1:
#     card1=card(title="3,400", text="Total",styles={'card':{"width":"200px","height":"200px"}})
# with col2:
#     card2=card(title="Card Title2", text="This is a card with a title and text.")
# with col3:
#     card3=card(title="Card Title3", text="This is a card with a title and text.")
# with col4:
#     card4=card(title="Card Title4", text="This is a card with a title and text.")


# # 添加一些文本
# st.write("这是一个简单的 Streamlit 应用示例。")
# # 添加一个滑块
# age = st.slider('选择你的年龄', 0, 100, 25)
# st.write(f'你的年龄是 {age} 岁')

# # 添加一个输入框
# name = st.text_input('请输入你的名字') or 'timmycheng'
# st.write(f'你好，{name}！')
