import streamlit as st
from send_mail import send_mail

st.title('Contact Me')

with st.form(key='email_form'):
    user_email = st.text_input('Your email')
    description = st.text_area('Your description')
    message = f'''\
    Subject: New email by {user_email}\n
    
    From:{user_email}\n
    {description}
    '''

    button = st.form_submit_button('Submit')

    if button:
        send_mail(message)
        st.info('Your mail sent successfully.')