FROM python:3.11

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY thesocialoutfitus/ thesocialoutfitus/
COPY .env .

EXPOSE 8501

WORKDIR /thesocialoutfitus

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "Home.py"]