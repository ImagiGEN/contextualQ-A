import pandas as pd
import streamlit as st
from utils import backend_api
st.title('Query Transcripts')

# @st.cache_data
# def get_companies_list():
#     # Get list of companies from the database, and associated years
#     cols = [
#         (20, 51),    # Company
#         (72, 75),    # Year
#         (106, 116),  # sbert embedding
#         (116, 127)   # openAI embedding
#     ]
#     metadata = backend_api.fetch_metadata()
#     df = pd.DataFrame(metadata.get("company_names_years"), columns = ["CN", "YEAR"])
#     return df


def generate_summary():
    # print(query_text, top_n)
    result = backend_api.generate_summary(query_text, top_n, api_key, openai_api_key, embedding)
    st.write(result)

# data_load_state = st.text('Loading ...')
# df = get_companies_list()

# # select the unique companies for user to filter
# filter_companies = st.multiselect(label='Company', options=list(
#     df['CN'].sort_values().unique()))

# filter_years = st.multiselect(label='Year', options=list(
#     df[df['CN'].isin(filter_companies)]['YEAR'].sort_values().unique()))

# # show raw data if user wants
# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(df[df['CN'].isin(filter_companies) & df['YEAR'].isin(filter_years)].sort_values(by='CN'))
embedding = st.selectbox(label='Select the Embedding type', options=["sbert", "openai"])

api_key = st.text_input('API Key')
openai_api_key = st.text_input('OpenAI API Key')

query_text = st.text_input('Enter your query')
top_n = st.number_input('How many transcripts?',min_value=5, max_value=10)

st.button("Search", on_click=generate_summary)


# data_load_state.text("Done!")