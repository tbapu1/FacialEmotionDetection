# FacialEmotionDetection

steps: (I use mac desktop and vscode, python 3.13.1)
1) download dataset.zip from https://www.kaggle.com/datasets/sujaykapadnis/emotion-recognition-dataset?select=dataset 
2) set up venv in python. then in terminal run "pip install -r requirements.txt"
3) run dataprep.py
4) note that YOLOv8 wants each image to be in format [<class_id> <x_center> <y_center> <width> <height>] our data set has the images already focused on the single face so we assume fulle photo dimensions
5) before running train.py to train model. adjust train.py like epoch and model for desired outcome. additionally use google collab for faster training

Google collab setup: bit off since changes to above
1. Sign in Google Collab and click "New Notebook", rename notebook to "EmotionFacialDetection.ipynb"
2. Enable GPU. Click "Runtime" --> "Change runtime type" --> Select GPU as the hardware accelerator --> Click "Save"
3. Create a new folder in your device Google Drive "FacialEmotionDetection"
4. Upload "data.yaml" and "train.py" to Google Drive folder
5. To upload photos since there are a thousands of photo use zip command in project terminal with "zip -r DataTrainingTesting.zip data/training data/testing"
6. Upload "DataTrainingTesting.zip" to Google Drive folder
7. In Google Collab notebook, on right side menu open folder icon, click folder with google drive icon and follow steps to allow
8. In Google Collab notebook command line, type the following:
"""
!unzip /content/drive/MyDrive/EmotionFacialDetection/DataTrainingTesting.zip -d /content/
!pip install ultralytics
!cp /content/drive/MyDrive/EmotionFacialDetection/data.yaml /content/data.yaml
!cp /content/drive/MyDrive/EmotionFacialDetection/train.py /content/train.py
!python /content/train.py
"""

9) NOT DONE YETT
10) 
11) 
