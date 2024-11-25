# a demo of streamlit

import json
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

