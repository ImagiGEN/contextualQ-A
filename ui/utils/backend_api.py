import json
import requests
import os

BACKEND_API_URL = os.getenv("BACKEND_API_URL", "http://api:8095")

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

def trigger_fetch_transcript(company_name, year, quarter, word_limit, api_key, openai_api_key):
    url = f"{BACKEND_API_URL}/api/v1/transcripts/embedd"
    payload = {
                "company_name": company_name,
                "year": int(year),
                "quarter": int(quarter),
                "word_limit": int(word_limit),
                "openai_api_key": openai_api_key,
                "api_key": api_key
            }

    json_payload = json.dumps(payload)

    response = requests.request("POST", url, headers=headers, data=json_payload)
    return response.text

def trigger_fetch_metadata():
    url = f"{BACKEND_API_URL}/api/v1/dag/fetch_metadata"
    payload = {}

    json_payload = json.dumps(payload)

    response = requests.request("POST", url, headers=headers, data=json_payload)
    return response.text

def generate_summary(query, word_limit, api_key, openai_api_key, embedding):
    url = f"{BACKEND_API_URL}/api/v1/transcripts/query"
    payload = {
                "word_limit": int(word_limit),
                "openai_api_key": openai_api_key,
                "api_key": api_key,
                "query": query,
                "embedding": embedding
            }

    json_payload = json.dumps(payload)

    response = requests.request("GET", url, headers=headers, data=json_payload)
    return response.text