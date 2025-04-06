#!/bin/bash

apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# uvicorn app:app --reload
gunicorn -k uvicorn.workers.UvicornWorker app:app