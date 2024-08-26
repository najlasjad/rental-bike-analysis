import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('all_data.csv')  
df['dteday'] = pd.to_datetime(df['dteday'])

data = {
    'dteday': df['dteday'],
    'cnt': df['cnt'],
    'season': df['season']
}
df = pd.DataFrame(data)

def get_most_rented_day(df):
    df['weekday'] = df['dteday'].dt.day_name()
    most_rented_day = df.groupby('weekday')['cnt'].sum().idxmax()
    return most_rented_day

def compare_seasonal_rentals(df):
    summer_rentals = df[df['season'] == 2]['cnt'].sum()
    winter_rentals = df[df['season'] == 4]['cnt'].sum()
    return summer_rentals, winter_rentals

st.title("Dashboard Analisis Penyewaan Sepeda🚲✨")

most_rented_day = get_most_rented_day(df)
st.subheader("Hari Penyewaan Terbanyak")
st.write(f"Hari penyewaan terbanyak adalah: **{most_rented_day}**")

summer_rentals, winter_rentals = compare_seasonal_rentals(df)
st.subheader("Perbandingan Penyewaan Musim")
st.write(f"Total Penyewaan di Musim Panas: **{summer_rentals}**")
st.write(f"Total Penyewaan di Musim Dingin: **{winter_rentals}**")

st.subheader("Visualisasi Perbandingan Penyewaan")
labels = ['Musim Panas', 'Musim Dingin']
sizes = [summer_rentals, winter_rentals]
colors = ['#FF9999', '#66B3FF']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)