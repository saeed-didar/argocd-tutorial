FROM python:3.8-slim-buster
WORKDIR /devops-hobbies
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY mattermost_api.py .
# Disable SSL verification globally
ENV PYTHONHTTPSVERIFY=0
RUN python3 -c "import ssl; ssl._create_default_https_context = ssl._create_unverified_context"

