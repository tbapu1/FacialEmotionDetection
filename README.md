# Facial Emotion Detection

This project aims to detect facial emotions using deep learning techniques. The following instructions will guide you through setting up and running the project on a macOS system with Python 3.13.1 and Visual Studio Code, as well as using Google Colab for faster training.

## Local Setup (macOS with VSCode)

1. **Download the Dataset**:
   - Obtain the `dataset.zip` file from [Kaggle's Emotion Recognition Dataset](https://www.kaggle.com/datasets/sujaykapadnis/emotion-recognition-dataset?select=dataset).

2. **Set Up Virtual Environment**:
   - Open a terminal and navigate to your project directory.
   - Create a virtual environment:
     ```bash
     python3 -m venv env
     ```
   - Activate the virtual environment:
     ```bash
     source env/bin/activate
     ```

3. **Install Dependencies**:
   - Install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

4. **Prepare the Data**:
   - Run the data preparation script:
     ```bash
     python dataprep.py
     ```
   - **Note**: YOLOv8 expects each image annotation in the format `[<class_id> <x_center> <y_center> <width> <height>]`. Since our dataset images are already focused on a single face, we assume the annotations cover the full photo dimensions.

5. **Train the Model**:
   - Before training, adjust the `train.py` script as needed, such as setting the number of epochs and selecting the model architecture.
   - For faster training, consider using Google Colab.

## Google Colab Setup

1. **Create a New Notebook**:
   - Sign in to [Google Colab](https://colab.research.google.com/) and create a new notebook. Rename it to "EmotionFacialDetection.ipynb".

2. **Enable GPU Acceleration**:
   - Click on "Runtime" > "Change runtime type".
   - Set "Hardware accelerator" to "GPU" and click "Save".

3. **Organize Files in Google Drive**:
   - Create a folder named "FacialEmotionDetection" in your Google Drive.
   - Upload the following files to this folder:
     - `data.yaml`
     - `train.py`
     - `dataset.zip` (downloaded from Kaggle)

4. **Mount Google Drive in Colab**:
   - In the Colab notebook, run:
     ```python
     from google.colab import drive
     drive.mount('/content/drive')
     ```

5. **Set Up the Environment and Data**:
   - Run the following commands in Colab:
     ```bash
     !unzip /content/drive/MyDrive/FacialEmotionDetection/dataset.zip -d /content/
     !pip install ultralytics
     !cp /content/drive/MyDrive/FacialEmotionDetection/data.yaml /content/data.yaml
     !cp /content/drive/MyDrive/FacialEmotionDetection/train.py /content/train.py
     ```

6. **Train the Model**:
   - Start the training process by running:
     ```bash
     !python /content/train.py
     ```
   - **Note**: Training may take a significant amount of time, potentially over an hour.

7. **NOT DONE YET**:
   

**Note**: Ensure that the paths in the Colab commands match the actual locations of your files in Google Drive. Adjust the `train.py` script parameters as needed to achieve optimal training results.
