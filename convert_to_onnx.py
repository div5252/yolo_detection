from ultralytics import YOLO

# Load the YOLO model
model = YOLO('yolov8n.pt')

# Export the model to ONNX format
model.export(format='onnx', imgsz=640, half=True)  # half=True for FP16 precision 