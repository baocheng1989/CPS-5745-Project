# a demo of streamlit

import streamlit as st

# 设置页面标题
st.title("欢迎来到我的 Streamlit 应用")

# 添加一些文本
st.write("这是一个简单的 Streamlit 应用示例。")

# 添加一个滑块
age = st.slider('选择你的年龄', 0, 100, 25)
st.write(f'你的年龄是 {age} 岁')

# 添加一个输入框
name = st.text_input('请输入你的名字') or 'timmycheng'
st.write(f'你好，{name}！')
