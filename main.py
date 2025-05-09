import os
import streamlit as st
import pandas as pd

folder_path = 'csv/'
file_list = os.listdir(folder_path)
csv_files = [file for file in file_list if file.endswith('.csv')]
df = pd.DataFrame()
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    temp = pd.read_csv(file_path, encoding='euc-kr')
    df = pd.concat([df, temp], ignore_index=True)
df['대여일시'] = pd.to_datetime(df['대여일시'])
df['대여일'] = df['대여일시'].dt.date
count_df = df.groupby('대여일').size().reset_index(name='대여건수')
st.title("일별 자전거 대여 건수")
st.dataframe(count_df)
