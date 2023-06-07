import pandas as pd
import streamlit as st

st.title('Query Transcripts')

@st.cache_data
def get_companies_list():
    # Get list of companies from the database, and associated years
    cols = [
        (20, 51),    # Company
        (72, 75),    # Year
        (106, 116),  # sbert embedding
        (116, 127)   # openAI embedding
    ]
    df = pd.DataFrame([["APPLE", "2021"], ["APPLE", "2022"],["SAMSUNG", "2022"]], columns = ["CN", "YEAR"])
    return df


def top_matches():
    print(query_text, top_n)

data_load_state = st.text('Loading ...')
df = get_companies_list()

# select the unique companies for user to filter
filter_companies = st.multiselect(label='Company', options=list(
    df['CN'].sort_values().unique()))

filter_years = st.multiselect(label='Year', options=list(
    df[df['CN'].isin(filter_companies)]['YEAR'].sort_values().unique()))

# show raw data if user wants
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df[df['CN'].isin(filter_companies) & df['YEAR'].isin(filter_years)].sort_values(by='CN'))

query_text = st.text_input('Enter your query')
top_n = st.number_input('How many transcripts?',min_value=5, max_value=10)

st.button("Search", on_click=top_matches)


data_load_state.text("Done!")