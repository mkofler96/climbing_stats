import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import datetime
from matplotlib.dates import DateFormatter
from helper import set_bg_hack
import base64
#import seaborn as sns

browns = ["#ece0d1", "#dbc1ac", "#967259", "#634832", "#38220f"]
header_color = "#0c457d"
text_color = "#0c457d"
graph_color = "#0c457d"
grid_color = "#b3ffff"

CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSk9VyduRn6RXuibvKtgoGcRjrn0hGjm5iuGz5nzc8T4Jg68im8ck7hYr8nsnEeBDDJlgKVz0bSjPrV/pub?output=csv'
st.set_page_config(layout="wide")


c_a1, c_a2, c_a3 = st.columns([1.5, 1.5, 1.5])

image = "climb_1.jpg"

set_bg_hack(image)
df = pd.read_csv(CSV_URL)

df['Datum'] = pd.to_datetime(df['Datum'], format='%d.%m.%Y')
df['Gewicht'] = df['Gewicht'].str[:-3].str.replace(',', '.').astype(float)
df['Dauer'] = df['Dauer'].str.replace(',', '.').astype(float)
df['Dauer'] = df['Dauer'].fillna(0)
df['Wochenschnitt'] = df['Dauer'].rolling(7).sum()

f, ax = plt.subplots()
f.patch.set_facecolor('none')
ax.set_facecolor('none')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_color(graph_color)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='x', colors=grid_color)
ax.tick_params(axis='y', colors=grid_color)
ax.grid(axis='y',zorder=0, color=grid_color)

plt.bar(df["Datum"], df["Dauer"], color=graph_color, alpha=1, zorder=3)
ax.set_xlim([datetime.date(2022, 1, 1), datetime.date.today()])

myFmt = DateFormatter("%d. %b")
ax.xaxis.set_major_formatter(myFmt)
f.autofmt_xdate()
c_a3.pyplot(f)
total_hours = df["Dauer"].sum()

begin = pd.Timestamp(2022, 1, 8)
end = pd.to_datetime((datetime.date.today()))
weekly_valid_hours = df["Wochenschnitt"].loc[(df["Datum"] >= begin) & (df["Datum"] <= end)]
print(weekly_valid_hours)

weekly_average = weekly_valid_hours.mean().round(1)


def html_string_big_small(number, description, color):
    number_str = f'{number:7.1f}'
    description_str = f'{description:40s}'
    number_str = number_str.replace(" ", "&nbsp")
    description_str = description_str.replace(" ", "&nbsp")
    p_start = "<p style='text-align: right; color:" + color + "'>"
    big = "<span style='font-size:4em; opacity: 0.8;'><b>" + number_str + "</b></span>"
    small = "<span style='font-size: 1.5em; opacity: 0.8; color: #b3ffff ;'>" + description_str + "</span>"
    p_end = "</p>"
    html_string = p_start + big + small + p_end
    return html_string

c_a2.markdown("<br>", unsafe_allow_html=True)
c_a2.markdown(html_string_big_small(total_hours, " ...hours climbed", text_color), unsafe_allow_html=True)
c_a2.markdown(html_string_big_small(weekly_average, " ...weekly average", text_color), unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; opacity: 0.5; font-size: 6em; color:"+header_color+"'><a href='https://docs.google.com/spreadsheets/d/1PJJMCrKVytjHbhaXi10CH5E-LDQUj1R4Xw3UDUvMvg4/edit#gid=2044315872' target='_blank' style='color: "+header_color+";text-decoration: none'>2022</a></h1>", unsafe_allow_html=True)

