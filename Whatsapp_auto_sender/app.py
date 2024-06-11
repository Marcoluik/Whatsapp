import streamlit as st
from message_sender import message_sender_page
from CsvView import view_page
from creatorview import creator_page
import os

csv_dir = "user_csv_files"
if not os.path.exists(csv_dir):
    os.makedirs(csv_dir)
# Dummy users database with paths to their CSV files
users = {
    "asmteknik": {"password": "2kt1312"},
    "user2": {"password": "password2"}
}

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username]["password"] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success("Login successful!")
            st.experimental_rerun()  # Reload the page after successful login
        else:
            st.error("Invalid username or password")

def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = ""


def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['username'] = ""

    if st.session_state['logged_in']:
        st.sidebar.title(f"Welcome, {st.session_state['username']}")
        if st.sidebar.button("Logout"):
            logout()
            st.experimental_rerun()

        # Create a navigation menu
        page = st.sidebar.radio("Select a page", ["Message Sender", "Csv Viewer",])

        # Navigate to the selected page
        if page == "Message Sender":
            message_sender_page()
        elif page == "Csv Viewer":
            view_page()

    else:
        login()


if __name__ == "__main__":
    main()
