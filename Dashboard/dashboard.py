import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='dark')


all_df = pd.read_csv("all_data.csv")
# Title Page
st.title("Air Quality Dashboard")

# Description 
st.write("The Air Quality Data Dashboard delivers a comprehensive overview of air quality metrics in a user-friendly interface. This interactive platform is designed to provide users with insightful information on the current state of air quality, enabling informed decisions and fostering public awareness.")

# Makesure Data in DF Already sorted
dateTimeColumns = ["date"]
all_df.sort_values(by="date",inplace=True)
all_df.reset_index(inplace=True)

for columns in dateTimeColumns:
    all_df[columns] = pd.to_datetime(all_df[columns])

minDate = all_df["date"].min()
maxDate = all_df["date"].max()

with st.sidebar:
    st.image("./assets/airquality.png")
    st.sidebar.header("Input Features")
    startDate, endDate = st.date_input(
        label="Time Span", 
        min_value=minDate, 
        max_value=maxDate, 
        value=[minDate,maxDate]
        )

main_df = all_df[(all_df["date"] >= str(startDate)) & 
                 (all_df["date"] <= str(endDate))]


# Displaying data statistics
st.subheader('Data Overview for Selected Period')
mainDeleteDate = main_df.drop(columns=['date',"index","year","month","day","No","hour"])
st.write(mainDeleteDate.describe())

st.subheader('Data Indicator Correlation')
selected_station = st.selectbox('Select Station', main_df['station'].unique())
stationSelected = main_df[main_df["station"]==selected_station]
stationSelectedDrp = stationSelected.drop(columns=["wd","station",'date',"index","year","month","day","No","hour"])
corr = stationSelectedDrp.corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, ax=ax)
st.pyplot(fig)

st.subheader("PM2.5 Polution")
groupByYear = main_df.groupby("date").mean(numeric_only=True)
fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["PM2.5"], label="PM2.5")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("PM10 Polution")
groupByYear = main_df.groupby("date").mean(numeric_only=True)
fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["PM10"], label="PM10")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("SO2 Polution")
groupByYear = main_df.groupby("date").mean(numeric_only=True)
fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["SO2"], label="SO2")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("NO2 Polution")
groupByYear = main_df.groupby("date").mean(numeric_only=True)
fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["NO2"], label="NO2")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("CO Polution")
groupByYear = main_df.groupby("date").mean(numeric_only=True)
fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["CO"], label="CO")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("O3 Polution")
groupByYear = main_df.groupby("date").mean(numeric_only=True)
fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["O3"], label="O3")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)


st.subheader("CO Polution")
groupByYear = main_df.groupby("date").mean(numeric_only=True)
fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["CO"], label="CO")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)


st.subheader("Temperature")
groupByYear = main_df.groupby("date").mean(numeric_only=True)
fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["TEMP"], label="TEMP")
plt.xlabel("Year")
plt.ylabel("°C")
plt.legend()
st.pyplot(fig)