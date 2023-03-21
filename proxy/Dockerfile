FROM python:3.8.3-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True
ENV SECONDS_BEFORE_PASSING_REQUEST "2"
ENV DESTINATION_URL "https://orbitalvar1.chasepaymentech.com/cws/1/debundle/api"
ENV FAILED_ATTEMPTS_BEFORE_SUCCESS "4"

COPY . /app
WORKDIR /app 
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm requirements.txt && \
    apt-get update && apt-get install -y libgomp1 gcc

EXPOSE 5000 

CMD flask run --host=0.0.0.0