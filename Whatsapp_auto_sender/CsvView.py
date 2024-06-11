import datetime
import streamlit as st
import pandas as pd
from CSV_grabber import reader, find_name
import os

dt = datetime.datetime.now()
ugenr = int(dt.strftime("%W"))
year = datetime.date.today().year


def view_page():
    st.title("CSV Viewer")

    # Check if the CSV file exists

    csv_exists = True

    if csv_exists:
        st.subheader(f"Current Week: {ugenr}")

        # Creating columns for horizontal layout
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("User Input")
            name = st.text_input("Enter your name to find out how many weeks before you appear:")

            if st.button("Read CSV"):
                PC, Mikser, Host, Podiet = reader(ugenr, year)

                st.header("CSV Data for the Current Week")
                if PC is not None:
                    st.write(f"**PC:** {PC}")
                    st.write(f"**Mikser:** {Mikser}")
                    st.write(f"**Host:** {Host}")
                    st.write(f"**Podiet:** {Podiet}")

                    if name:
                        weeks_before = find_name(name)
                        next_week = weeks_before.get("next_week")
                        job = weeks_before.get("job")
                        st.info(f"{name} has the next job in week {next_week} as {job}")

        with col2:
            if st.button("View CSV"):
                csv_path = f"CSV_AND_EXCEL/TEKNIK{year}csv.csv"

                if os.path.exists(csv_path):
                    df = pd.read_csv(csv_path)
                    st.dataframe(df, hide_index=True)
                else:
                    st.error(f"CSV file {csv_path} not found.")
