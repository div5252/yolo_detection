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
python app.py
```

4. Open your web browser and navigate to:
```
http://localhost:8000
```

## Usage

1. Allow camera access when prompted by your browser
2. Click the "Capture & Detect" button to take a photo and run object detection
3. The detected objects will be displayed with bounding boxes and labels

## Cloud Deployment

To deploy this application to the cloud:

1. Choose a cloud provider (e.g., AWS, Google Cloud, or Azure)
2. Create a virtual machine or container instance
3. Install the required dependencies
4. Run the application with appropriate security settings
5. Configure your domain and SSL certificates if needed

## Performance Optimization

The application uses YOLOv8n (nano) model for better performance. For even better performance, you can:

1. Use a GPU-enabled instance in the cloud
2. Implement caching for frequently detected objects
3. Optimize image resolution based on your needs
4. Use a CDN for static file delivery

## Security Considerations

- Always use HTTPS in production
- Implement rate limiting
- Add authentication if needed
- Keep dependencies updated
- Use environment variables for sensitive information 