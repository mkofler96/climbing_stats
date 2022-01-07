import csv
import requests
import pandas as pd
import matplotlib.pyplot as plt

CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSk9VyduRn6RXuibvKtgoGcRjrn0hGjm5iuGz5nzc8T4Jg68im8ck7hYr8nsnEeBDDJlgKVz0bSjPrV/pub?output=csv'

df = pd.read_csv(CSV_URL)
df['Datum'] = pd.to_datetime(df['Datum'], format='%d.%m.%Y')
df['Gewicht'] = df['Gewicht'].str[:-3].str.replace(',', '.').astype(float)
df['Dauer'] = df['Dauer'].str.replace(',', '.').astype(float)
print(df)

plt.plot(df["Datum"], df["Dauer"], '-o', linewidth=2)

plt.show()