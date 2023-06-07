import streamlit as st

API_KEY = None

def generate_api_key():
    # Call Fast API with username and password field return API key
    api_key = "ALihuiyftydcrcfhgb"
    return api_key
    

st.title('User Registration')

st.subheader("Get API key")

new_user = st.text_input('Username')
new_passwd = st.text_input('Password',type='password')

if st.button("Generate"):
    api_key = generate_api_key()
    st.write(api_key)