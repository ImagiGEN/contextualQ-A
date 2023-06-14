# Assignment1
Application to aid research of investment analysts by searching through earnings call transcripts, to periodically upload text datasets, and providing features to filter by company and year.

## Project Resources
* [CodeLab Docs](https://codelabs-preview.appspot.com/?file_id=1qIzTyUo0sb034RZveDWXunu-2ih_WGXYlH1ynkr6a_Q#0)

### Link to the Live Applications
* Streamlit Application : http://35.196.112.47:8090 
* Airflow : http://35.196.112.47:8080/login/?next=http%3A%2F%2F35.196.112.47%3A8080%2Fhome

## Project Flow 

In this assignment, our team will be working on building a contextual search application for Intelligence Co, a financial research company. The goal is to create a system that leverages vector similarity search, traditional filtering, and hybrid search features to aid financial analysts in searching through earnings call transcripts. We will be using a combination of tools including Redis for data storage, Airflow for data retrieval and processing, Streamlit for the front-end application, and FastAPI for building an API service. The metadata will be extracted from the data source and stored in a PostgresSQL database. Our solution will involve data exploration, implementing a search functionality, and hosting the application and database in Docker containers. Through this assignment, we aim to provide a user-friendly and efficient application for financial researchers to analyze earnings call transcripts effectively.

## Project Tree 
```
.
├── Makefile
├── README.md
├── airflow
│   ├── Dockerfile
│   ├── config
│   ├── dags
│   │   ├── __pycache__
│   │   │   ├── fetch_transcript.cpython-37.pyc
│   │   │   └── populate_metadata.cpython-37.pyc
│   │   ├── fetch_transcript.py
│   │   └── populate_metadata.py
│   ├── plugins
│   └── requirements.txt
├── api
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── utils
│       ├── __init__.py
│       ├── common.py
│       ├── crud.py
│       ├── models.py
│       ├── pipeline.py
│       └── schemas.py
├── docker-compose-local.yml
└── ui
    ├── Dockerfile
    ├── main.py
    ├── pages
    │   ├── 1_User_Registration.py
    │   ├── 2_API_Key_Generator.py
    │   ├── 3_Fetch_Transcript.py
    │   └── 4_Query_Transcript.py
    ├── requirements.txt
    └── utils
        ├── __init__.py
        └── backend_api.py
```

## Contributions
| Contributor    | Work |
| -------- | ------- |
| Ashritha Goramane  | Backend API, Integration, and Deployment    |
| Parvati Sohani | Frontend and Documentation   |
| Rishabh Indoria    | Data extraction, Embedding, and Search |
