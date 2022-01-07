import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import datetime
#import seaborn as sns

CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSk9VyduRn6RXuibvKtgoGcRjrn0hGjm5iuGz5nzc8T4Jg68im8ck7hYr8nsnEeBDDJlgKVz0bSjPrV/pub?output=csv'
#st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>Climbing Stats</h1>", unsafe_allow_html=True)
st.markdown("<a href='https://docs.google.com/spreadsheets/d/1PJJMCrKVytjHbhaXi10CH5E-LDQUj1R4Xw3UDUvMvg4/edit#gid=2044315872' target='_blank'>edit google sheet</a>", unsafe_allow_html=True)
st.markdown("""---""")

df = pd.read_csv(CSV_URL)
df['Datum'] = pd.to_datetime(df['Datum'], format='%d.%m.%Y')
df['Gewicht'] = df['Gewicht'].str[:-3].str.replace(',', '.').astype(float)
df['Dauer'] = df['Dauer'].str.replace(',', '.').astype(float)
df['Dauer'] = df['Dauer'].fillna(0)
df['Wochenschnitt'] = df['Dauer'].rolling(7).mean()
print(df)

f, ax = plt.subplots()
plt.bar(df["Datum"], df["Dauer"], color="aqua", alpha=0.5)
plt.plot(df["Datum"], df["Wochenschnitt"])
ax.set_xlim([datetime.date(2022, 1, 1), datetime.date(2022, 3, 1)])
f.autofmt_xdate()
st.pyplot(f)
