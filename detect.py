import torch
from pathlib import Path
import yaml
from yolov5 import detect, train
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


# Detect objects using a pre-trained model
def detect_objects(image_path, weights_path='best.pt', conf=0.25, iou=0.45, device='cpu'):
    detect.run(weights=weights_path, source=image_path, imgsz=640, conf_thres=conf, iou_thres=iou, device=device)

image_path = r"C:\Users\omkar\Desktop\cat_dataset\train_data\001.jpg"
image_path_str = str(image_path)
detect.run(weights=r"C:\Users\omkar\Desktop\cat_dataset\train_data\best.pt", source=image_path_str)
