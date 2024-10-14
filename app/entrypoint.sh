#!/bin/sh

set -e

echo "----------------------------------------ingest start----------------------------------------"
cd ./app/functions/ingester/ && python ingest.py && cd ../../../
echo "----------------------------------------ingest done----------------------------------------"

echo "server start"

APP_MODULE="app.main:app"
HOST="0.0.0.0"
PORT="9000"
uvicorn $APP_MODULE --host $HOST --port $PORT

echo "initialize done"

sleep infinity

exit 1