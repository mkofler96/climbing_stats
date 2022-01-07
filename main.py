import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import datetime
from helper import set_bg_hack
import base64
#import seaborn as sns

CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSk9VyduRn6RXuibvKtgoGcRjrn0hGjm5iuGz5nzc8T4Jg68im8ck7hYr8nsnEeBDDJlgKVz0bSjPrV/pub?output=csv'
st.set_page_config(layout="wide")

c_h1, c_h2 = st.columns([1.5, 3])
c_h2.markdown("<h1 style='text-align: center'>Climbing Stats <a href='https://docs.google.com/spreadsheets/d/1PJJMCrKVytjHbhaXi10CH5E-LDQUj1R4Xw3UDUvMvg4/edit#gid=2044315872' target='_blank'>↗</a></h1>", unsafe_allow_html=True)
c_h1.markdown("""---""")
c_h2.markdown("""---""")
c_a1, c_a2, c_a3 = st.columns([1.5, 1.5, 1.5])
image = "climb_1.jpg"

set_bg_hack(image)
df = pd.read_csv(CSV_URL)

df['Datum'] = pd.to_datetime(df['Datum'], format='%d.%m.%Y')
df['Gewicht'] = df['Gewicht'].str[:-3].str.replace(',', '.').astype(float)
df['Dauer'] = df['Dauer'].str.replace(',', '.').astype(float)
df['Dauer'] = df['Dauer'].fillna(0)
df['Wochenschnitt'] = df['Dauer'].rolling(7).mean()
print(df)

f, ax = plt.subplots()
f.patch.set_facecolor('none')
ax.set_facecolor('none')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.grid(axis='y',zorder=0, color="white")

plt.bar(df["Datum"], df["Dauer"], color="darkslategrey", alpha=1, zorder=3)
plt.plot(df["Datum"], df["Wochenschnitt"])
ax.set_xlim([datetime.date(2022, 1, 1), datetime.date.today()])
f.autofmt_xdate()
c_a3.pyplot(f)
