import streamlit as st
import datetime

st.title("Contact Us")

st.markdown("Have feedback or questions? Submit your message below:")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    date = st.date_input("Date", datetime.date.today())
    submitted = st.form_submit_button("Send")

    if submitted:
        with open("messages.csv", "a") as f:
            f.write(f"{name},{email},{date},{message}\\n")
        st.success("Message submitted successfully!")

st.caption("Built with  using Streamlit")
