
from imageai.Detection import ObjectDetection
import os
from tensorflow.keras.layers import BatchNormalization
import keras

current_directory = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()

detector.setModelPath(os.path.join(current_directory , "yolo-tiny.h5"))
detector.loadModel()

custom = detector.CustomObjects(person=True, bicycle=True)

detections = detector.detectCustomObjectsFromImage(
                custom_objects = custom,
                input_image = os.path.join(current_directory, "traffic.jpg"),
                output_image_path = os.path.join(current_directory , "traffic_detected.jpg"),
                minimum_percentage_probability = 70
)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")
