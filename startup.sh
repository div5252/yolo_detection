#!/bin/bash

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app --bind 0.0.0.0:8000