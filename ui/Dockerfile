FROM python:3.9.13
# Pull the base docker image of python with tag 3.9.13

WORKDIR /app
# Change the working dir inside the container - cd /app

COPY main.py requirements.txt ./
COPY pages ./pages
COPY utils ./utils
# Copy source code and dependency

RUN pip install -r requirements.txt
# Install the dependency

### Container Env same as local at this point
EXPOSE 8090

CMD ["streamlit", "run", "main.py", "--server.port", "8090"]