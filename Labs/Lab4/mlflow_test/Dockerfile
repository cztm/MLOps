FROM python:3.10-slim

RUN pip install mlflow

EXPOSE 5000

CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000"]
