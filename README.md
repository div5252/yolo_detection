# YOLO Object Detection Web App

This project provides a web interface for real-time object detection using YOLOv8. It allows users to capture images from their camera and detect objects in them.

## Features

- Real-time camera access
- YOLOv8 object detection
- Web-based interface
- FastAPI backend
- Optimized for performance

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app:app --reload
```

4. Open your web browser and navigate to:
```
http://localhost:8000
```

## Usage

1. Allow camera access when prompted by your browser
2. Click the "Capture & Detect" button to take a photo and run object detection
3. The detected objects will be displayed with bounding boxes and labels

## Performance Optimization

The application uses YOLOv8n (nano) model for better performance. For even better performance, you can:

1. Use a GPU-enabled instance in the cloud
2. Implement caching for frequently detected objects
3. Optimize image resolution based on your needs
4. Use a CDN for static file delivery
