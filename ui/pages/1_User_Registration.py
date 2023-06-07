import streamlit as st

def register_user():
    # Call Fast API with username and password field
    pass

st.title('User Registration')

st.subheader("Create an Account")

new_user = st.text_input('Username')
new_passwd = st.text_input('Password',type='password')
new_cnf_passwd = st.text_input('Confirm Password',type='password')
st.button("Sign Up", on_click=register_user)