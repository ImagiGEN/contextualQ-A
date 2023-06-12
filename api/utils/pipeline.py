from utils import schemas
import requests
import os
from requests.auth import HTTPBasicAuth
import uuid

AIRFLOW_API_URL = os.getenv("AIRFLOW_API_URL", "http://localhost:8080/api/v1")


def trigger_fetch_transcript(userInput: schemas.FetchTranscript):
    url = f"{AIRFLOW_API_URL}/dags/fetch_transcript/dagRuns"
    data = {
        "conf": {
                "company_name": userInput.company_name,
                "year": userInput.year,
                "quarter": userInput.quarter,
                "word_limit": userInput.word_limit,
                "openai_api_key": userInput.openai_api_key
            },
        "dag_run_id": f"fetch_transcript_{uuid.uuid4().hex}",
        }
    response = requests.request("POST", url, auth=HTTPBasicAuth('airflow', 'airflow'), json=data)
    if response.status_code != 200:
        return {"message": f"Internal Server Error {response.text}"}
    return {"message": "Fetching transcript", "details": response.text}

def trigger_fetch_metadata_dag():
    url = f"{AIRFLOW_API_URL}/dags/metadata_load/dagRuns"
    data = {
        "dag_run_id": f"metadata_load_{uuid.uuid4().hex}",
        }
    response = requests.request("POST", url, auth=HTTPBasicAuth('airflow', 'airflow'), json=data)
    if response.status_code != 200:
        return {"message": f"Internal Server Error {response.text}"}
    return {"message": "Fetching transcript", "details": response.text}
