from ultralytics import YOLO
model = YOLO("yolov8x.pt")  
results = model("Images/bus.jpg", save = True) 