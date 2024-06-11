import datetime
import streamlit as st
import pandas as pd
from CSV_grabber import reader, find_name
import os

dt = datetime.datetime.now()
ugenr = int(dt.strftime("%W"))
year = datetime.date.today().year

def creator_page(csv_file, save_csv):
    st.title(f"Teknik {year} Schedule Editor")
    if csv_file != None:
        col1, col2 = st.columns(2)

        with col1:
            st.sidebar.header("Edit Roles")
            hosts = st.text_input("Hosts (comma separated)","").split(',')
            pcs = st.text_area("PCs (comma separated)",
                               ).split(',')
            mikser = st.text_area("Mikser (comma separated)",
                                  "").split(',')
            podium = st.text_input("Podium (comma separated)", "").split(',')
        with col2:
            if st.button("View CSV"):
                csv_path = f"CSV_AND_EXCEL/TEKNIK{year}csv.csv"

                if os.path.exists(csv_path):
                    df = pd.read_csv(csv_path)
                    st.dataframe(df, hide_index=True)
                else:
                    st.error(f"CSV file {csv_path} not found.")

    else:
        weeks = list(range(1, 53))  # Weeks list
        df = pd.DataFrame({"Uge nr": weeks})  # Dataframe

        st.sidebar.header("Edit Roles")
        hosts = st.text_input("Hosts (comma separated)", "").split(',')
        pcs = st.text_area("PCs (comma separated)", "").split(',')
        mikser = st.text_area("Mikser (comma separated)", "").split(',')
        podium = st.text_input("Podium (comma separated)", "").split(',')

        df["PC"] = [pcs[i % len(pcs)] for i in range(len(df))]
        df["Mikser"] = [mikser[i % len(mikser)] for i in range(len(df))]
        df["Host"] = [hosts[i % len(hosts)] for i in range(len(df))]
        df["Podiet"] = [podium[i % len(podium)] for i in range(len(df))]

        stævneugenumre = st.text_input("Stævne ugenumre (comma separated)", "").split(",")

        stævne = {"PC": "Stævne", "Mikser": "Stævne", "Host": "Stævne", "Podiet": "Stævne"}

        for week in stævneugenumre:
            df.loc[df['Uge nr'] == int(week), stævne.keys()] = stævne.values()

        if st.button("Save CSV"):
            pass