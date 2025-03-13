from ultralytics import YOLO
import os

# Load YOLOv8 model 
# Use weaker model --> "yolov8n.pt" for quicker testing
# Use stronger models --> "yolov8s.pt" or "yolov8m.pt" for better accuracy
model = YOLO("yolov8n.pt")

# Get the absolute path of data.yaml
# Local
# data_path = os.path.abspath("data.yaml")
# Google Collab
data_path = "/content/data.yaml"

# Train the model
# More epochs --> longer computer time, improving accuracy, better generalization, risk overfitting
# Less epochs --> shorter computer time, low accuracy, high bias, testing if working
model.train(data=data_path, epochs=50, imgsz=640)

# Save best model for future use
model.export(format="onnx")
