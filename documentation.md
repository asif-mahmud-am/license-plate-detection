## Model Selection and Justification

The base model used for this project is YOLOv8. YOLOv8 was chosen for the following reasons:

State-of-the-art performance: It achieves high accuracy for object detection tasks.
Real-time inference: YOLOv8 is optimized for speed and performance, making it suitable for deployment on edge devices.
Ease of use: YOLOv8 offers a simple interface for training, validation, and deployment.
Pre-trained weights: The availability of pre-trained weights facilitates fine-tuning for custom datasets.

## Dataset
The dataset used for training was sourced from Roboflow:

Dataset URL: [License Plate Recognition Dataset](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4)

Details:
License Plate Recognition > resized640_aug3x-ACCURATE

Provided by a Roboflow user
License: CC BY 4.0

* `License Plate Detection` dataset images and annotations were cloned from the following projects:
	* https://universe.roboflow.com/carplates2/licenseplate_v2
	* https://universe.roboflow.com/a-stx8a/licenseplateimage_thresholdfiltered---roboflow/
	* https://universe.roboflow.com/augmented-startups/vehicle-registration-plates-trudk
	* https://universe.roboflow.com/xavier-jimenez/placas-stcpz/
	* https://universe.roboflow.com/yolo-training-jaqog/yolo-training-wis72/
	* https://universe.roboflow.com/abdullahi-ayantayo/car-license-plate-eosye/


## Training

1. Dataset Preparation: The dataset was downloaded using the Roboflow API and preprocessed to ensure compatibility with YOLOv8.

2. Training: YOLOv8 model was fine-tuned using the downloaded dataset. Training hyperparameters:

```
Epochs: 33
Batch size: 16
Image size: 640x640
```

Model Saving:

The trained weights were saved as ```best.pt``` later renamed as ```license_plate_detector.pt```

The training code can be found here: ```license_plate_training.ipynb```

## Performance Evaluation 

```
Precision: 0.9843
Recall: 0.9439
mAP@0.5: 0.9781
mAP@0.5:0.95: 0.6835
```

More metrics can be found in ```.\run\detect\val2```

## GUI 

A user-friendly GUI was implemented using PySimpleGUI:

Features:

Displays live camera feeds with real-time annotations of detected and tracked license plates.
Buttons for starting/stopping video and pausing the feed.
Shows frames per second (FPS) for performance monitoring.

Custom Input:

The GUI supports both live video from cameras and pre-recorded videos for testing purposes.

## Try live detection

1. Create a conda environment:

```
conda create -n license-plate-detection python=3.9.0
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the live detection file:

```
python live_detection.py
```


**Author: Asif Mahmud**
