from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import io
import base64
import os

app = FastAPI()

model = 'yolov8n'

# Check if ONNX model exists, if not convert from PyTorch
# if not os.path.exists(f'{model}.onnx'):
#     print("Converting YOLO model to ONNX format...")
#     model = YOLO(f'{model}.pt')
#     model.export(format='onnx', imgsz=640, half=True)
#     print("Conversion complete!")

# Load the ONNX model
# model = YOLO(f'{model}.onnx')

model = YOLO('vacuum_best.pt')

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r") as f:
        return f.read()

@app.post("/detect")
async def detect_objects(file: UploadFile = File(...)):
    # Read the image file
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Run YOLO detection with optimized settings
    results = model(img, conf=0.25, iou=0.45)  # Adjust confidence and IoU thresholds
    
    # Process results
    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    
    # Convert to base64
    buffered = io.BytesIO()
    im.save(buffered, format="JPEG", quality=85)  # Slightly reduce quality for faster transfer
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return {"image": img_str}