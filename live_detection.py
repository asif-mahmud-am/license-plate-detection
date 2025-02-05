import PySimpleGUI as sg
import cv2
import urllib.request
import os
from ultralytics import YOLO

coco_model = YOLO("yolov8n.pt")
model = YOLO('license_plate_detector.pt')

video_path = "Cars, Busy Streets, City Traffic - No Copyright Royalty Free Stock Videos.mp4"


# Define GUI layout
layout = [
    [sg.Image(filename='', key='image')],
    [sg.Button('Play', size=(10, 1)), sg.Button('Pause', size=(10, 1)), sg.Button('Exit', size=(10, 1))]
]

# Create the GUI window
window = sg.Window('License Plate Detection', layout, finalize=True)

# Initialize variables
cap = None
playing = False
resize_width = 640  
resize_height = 360  

while True:
    event, values = window.read(timeout=10)
    
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    elif event == 'Play' and not playing:
        cap = cv2.VideoCapture(video_path)
        playing = True
    elif event == 'Pause' and playing:
        playing = False
    
    if playing and cap and cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (resize_width, resize_height))
            
            results = model(frame)

            annotated_frame = results[0].plot()

            imgbytes = cv2.imencode('.png', annotated_frame)[1].tobytes()
            window['image'].update(data=imgbytes)
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

if cap:
    cap.release()
window.close()