
To train on CPU and use use best.pt

```
yolo task=detect mode=train data=data.yaml model=yolov8n.pt epochs=30 imgsz=640
```

To Train on GPU
```
yolo task=detect mode=train data=data.yaml model=yolov8n.pt epochs=30 imgsz=640 device=cuda
```

validation
```
yolo task=detect mode=val model=<path>\best.pt data=data.yaml
```

prediction
```
yolo task=detect mode=predict model=<path>\runs\detect\train\weights\best.pt conf=0.25 source=<path>

```


