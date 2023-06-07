import pandas as pd
import streamlit as st

st.title('Fetch Transcripts')


@st.cache_data
def get_station_list():
    # read following columns in the nexrad station dataset
    cols = [
        (20, 51),    # Name
        (72, 75),    # ST
        (106, 116),  # Lat
        (116, 127)   # Lon
    ]
    # read the dataset as a pandas dataframe using fixed width format
    df = pd.read_fwf(
        r"https://www.ncei.noaa.gov/access/homr/file/nexrad-stations.txt", colspecs=cols, skiprows=[1])
    # filter rows with are not null
    df = df[df['ST'].notna()]
    return df

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

def run_dag():
    # Run Airflow DAG for selected companies
    pass

data_load_state = st.text('Loading ...')
df = get_companies_list()

# select the unique companies for user to filter
filter_companies = st.multiselect(label='Company', options=list(
    df['CN'].sort_values().unique()))

# filter_years = st.multiselect(label='Year', options=list(
#     df[df['CN'].isin(filter_companies)]['YEAR'].sort_values().unique()))

# show raw data if user wants
# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(df[df['CN'].isin(filter_companies) & df['YEAR'].isin(filter_years)].sort_values(by='CN'))

st.button("Fetch Data", on_click=run_dag)

data_load_state.text("Done!")