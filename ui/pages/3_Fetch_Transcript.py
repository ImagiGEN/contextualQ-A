import pandas as pd
import streamlit as st
from utils import backend_api

st.title('Fetch Transcripts')

@st.cache_data
def get_companies_list():
    # Get list of companies from the database, and associated years
    cols = [
        (20, 51),    # Company
        (72, 75),    # Year
        (106, 116),  # sbert embedding
        (116, 127)   # openAI embedding
    ]
    metadata = backend_api.fetch_metadata()
    df = pd.DataFrame(metadata.get("company_names_years"), columns = ["CN", "YEAR"])
    return df

def run_dag():
    # Run Airflow DAG for selected companies
    pass

data_load_state = st.text('Loading ...')
df = get_companies_list()

# select the unique companies for user to filter
filter_companies = st.multiselect(label='Company', options=list(
    df['CN'].sort_values().unique()))

filter_years = st.multiselect(label='Year', options=list(
    df[df['CN'].isin(filter_companies)]['YEAR'].sort_values().unique()))

filter_quarter = st.multiselect(label='Year', options=[1,2,3,4])

# show raw data if user wants
# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(df[df['CN'].isin(filter_companies) & df['YEAR'].isin(filter_years)].sort_values(by='CN'))

st.button("Fetch Data", on_click=run_dag)

data_load_state.text("Done!")