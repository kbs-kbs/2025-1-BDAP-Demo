import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('서울 자전거 렌탈수와 기상데이터 상관관계 분석')

# 데이터 불러오기
bike_df = pd.read_csv('csv/tempby.csv')
weather_df = pd.read_csv('2024_기상데이터.csv')
weather_selected = weather_df.iloc[:, 3:10]

merged = pd.concat([bike_df, weather_selected], axis=1)

# 상관관계 분석
corr = merged.corr()

# 히트맵 시각화
st.subheader('상관관계 히트맵')
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
st.pyplot(plt)

# 상관관계 표 출력
st.subheader('상관관계 테이블')
st.write(corr)
