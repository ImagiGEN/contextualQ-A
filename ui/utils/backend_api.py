import json
import requests
import os

BACKEND_API_URL = os.getenv("BACKEND_API_URL", "http://api:8095")
AIRFLOW_API_URL = os.getenv("AIRFLOW_API_URL", "http://")

headers = {'Content-Type': 'application/json'}


def register_user(username, password, confirm_password):
    url = f"{BACKEND_API_URL}/api/v1/user/register"
    payload = {
        "username": username,
        "password": password,
        "cnf_password": confirm_password
    }
    json_payload = json.dumps(payload)

    response = requests.request("POST", url, headers=headers, data=json_payload)
    return response

def generate_api_key(username, password):
    url = f"{BACKEND_API_URL}/api/v1/user/generate_key"
    payload = {
        "username": username,
        "password": password,
        "cnf_password": password
    }
    json_payload = json.dumps(payload)

    response = requests.request("POST", url, headers=headers, data=json_payload)
    return response

def fetch_metadata():
    url = f"{BACKEND_API_URL}/api/v1/company_metadata/fetch"
    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

def run_fetch_transcript_dag():
    url = f"{BACKEND_API_URL}/api/v1/company_metadata/fetch"
    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()