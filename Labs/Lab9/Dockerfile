# Use official Python image
# FROM python:3.11-slim

# Set work directory
# WORKDIR /app

# Copy model and source code
# COPY app.py .
# COPY reddit_model_pipeline.joblib .

# Install FastAPI and Uvicorn
# RUN pip install fastapi uvicorn scikit-learn joblib pandas

# Expose port
# EXPOSE 8000

# Command to run the app
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# GCP DOCKERFILE:
FROM python:3.10-slim

RUN pip install -U pip 

WORKDIR /app

COPY [ "requirements.txt", "./" ]

RUN pip install -r requirements.txt

COPY [ "reddit_model_pipeline.joblib", "app.py", "./"]

EXPOSE 8000

CMD [ "uvicorn", "app:app", "--host", "0.0.0.0" ]
