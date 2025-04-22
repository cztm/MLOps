FROM python:3.12-slim

WORKDIR /

COPY requirements.txt requirements.txt
COPY server.sh server.sh

ENV GOOGLE_APPLICATION_CREDENTIALS="./secrets/credentials"

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN chmod +x server.sh

EXPOSE 8080

CMD ["bash", "./server.sh"]

