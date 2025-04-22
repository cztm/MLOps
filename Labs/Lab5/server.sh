#!/bin/bash  

echo "🔥 POSTGRESQL_URL = $POSTGRESQL_URL"
echo "🔥 STORAGE_URL = $STORAGE_URL"

mlflow server --host 0.0.0.0 --port 8080 --backend-store-uri "$POSTGRESQL_URL" --default-artifact-root "$STORAGE_URL"


