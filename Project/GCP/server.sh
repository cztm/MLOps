#!/bin/bash  
  
echo "🔥 POSTGRESQL_URL = $POSTGRESQL_URL"  
echo "🔥 STORAGE_URL = $STORAGE_URL"  
  
if [ "$RUN_MIGRATIONS" = "true" ]; then  
  echo "Running database migrations..."  
  mlflow db upgrade "$POSTGRESQL_URL"  
else  
  echo "Skipping database migrations"  
fi  
  
mlflow server --host 0.0.0.0 --port 8080 --backend-store-uri "$POSTGRESQL_URL" --default-artifact-root "$STORAGE_URL" 
