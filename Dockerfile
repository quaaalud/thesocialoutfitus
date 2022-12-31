FROM python:3.11

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
    
WORKDIR /thesocialoutfitus

COPY / /thesocialoutfitus/

EXPOSE 8501

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=8501", "--server.headless=true"]