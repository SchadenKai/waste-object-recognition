from ultralytics import YOLO
import cv2

model =YOLO('yolov8n.py')

video_path = './video/video.mp4'
cv2.VideoCapture(video_path)

