import pywhatkit
from CSV_grabber import reader
from besked import msg, afskedmsg
import datetime
import streamlit as st
dt = datetime.datetime.now()
ugenr = int(dt.strftime("%W"))
year = datetime.date.today().year


def create_message():
    read = reader(ugenr,year)
    besked = msg()
    afsked = afskedmsg()
    PC = read[0]
    Mikser = read[1]
    Host = read[2]
    Podiet = read[3]
    Message = (f"{besked} \nuge: {ugenr}  \n@{PC} på PC \n@{Mikser} på Mikser \n@{Host} på Host \n@{Podiet} på Podiet\n{afsked}")


    return Message, besked, ugenr, PC, Mikser, Host, Podiet, afsked


def message_sender_page():
    st.title("Message Sender")
    if 'message_details' not in st.session_state:
        st.session_state['message_details'] = None

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Hent besked'):
            st.session_state['message_details'] = create_message()

        if st.session_state['message_details']:
            Message, besked, ugenr, PC, Mikser, Host, Podiet, afsked = st.session_state['message_details']
            st.text(f"Message: {besked}")
            st.text(f"Week Number: {ugenr}")
            st.text(f"PC: {PC}")
            st.text(f"Mikser: {Mikser}")
            st.text(f"Host: {Host}")
            st.text(f"Podiet: {Podiet}")
            st.text(f"Farewell: {afsked}")

    with col2:
        nummer = st.text_input("Til hvilket nummer?")
        if st.button("Send besked"):
            if st.session_state['message_details']:
                Message, _, _, _, _, _, _, _ = st.session_state['message_details']
                try:
                    full_number = f"+45{nummer}"
                    pywhatkit.sendwhatmsg_instantly(full_number, Message, 20)
                    st.success(f"Besked sendt til {full_number}")
                except Exception as e:
                    st.error(f"Der opstod en fejl: {str(e)}")
            else:
                st.error("Hent besked først!")