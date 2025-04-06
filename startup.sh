#!/bin/bash

apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
apt-get install protobuf-compiler libprotoc-dev

# uvicorn app:app --reload
gunicorn -k uvicorn.workers.UvicornWorker app:app