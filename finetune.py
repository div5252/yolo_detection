from ultralytics import YOLO

model = YOLO('yolov8m.pt')  # or yolov8s.pt / yolov8m.pt etc.
model.train(data='datasets/data.yaml', epochs=40, imgsz=640)

model.export(format='onnx', imgsz=640, half=True)