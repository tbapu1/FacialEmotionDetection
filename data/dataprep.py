import zipfile
import os

# Define file paths
zip_path = "./data/photos/dataset.zip"
extract_path = "./data/photos/"

# Ensure the ZIP file exists
if os.path.exists(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print("Unzipping complete!")
else:
    print(f"Error: {zip_path} not found.")

#____________________________________________________________________________________________________#

import pandas as pd
from sklearn.model_selection import train_test_split

# Load CSV, note the folders
df = pd.read_csv("data/photos/data.csv")

# Drop the first column (unnamed index column)
df = df.iloc[:, 1:]  # Keeps only the 'path' and 'label' columns

# Split the dataframe: 80% for training, 20% for testing
trainingDF, testingDF = train_test_split(df, test_size=0.2, random_state=69, shuffle=True)  # have same random_state=# for cross group member testings

# Define paths
TRAINING_CSV = "data/training/training.csv"
TESTING_CSV = "data/testing/testing.csv"

# Save new CSVs, note the folders
trainingDF.to_csv(TRAINING_CSV, index=False)
testingDF.to_csv(TESTING_CSV, index=False)

print("Training and testing CSV files have been created.")

#____________________________________________________________________________________________________#

import shutil

# Define more paths
DATASET_FOLDER = "data/photos"
TRAIN_DIR = "data/training/images/"
TEST_DIR = "data/testing/images/"

# Load CSVs
train_df = pd.read_csv(TRAINING_CSV)
test_df = pd.read_csv(TESTING_CSV)

# Function to move images
def move_images(df, destination):
    for _, row in df.iterrows():
        img_path = os.path.join(DATASET_FOLDER, row["path"])
        dest_path = os.path.join(destination, os.path.basename(row["path"]))

        # Move file if it exists
        if os.path.exists(img_path):
            shutil.copy(img_path, dest_path)  # Note copying photos without deleteing from photos folder

# Move images
move_images(train_df, TRAIN_DIR)
move_images(test_df, TEST_DIR)

print("Images moved successfully!")

#____________________________________________________________________________________________________#

# Define classifications (Note must match the order in `data.yaml`)
CLASS_MAPPING = {
    "Ahegao": 0,
    "Angry": 1,
    "Happy": 2,
    "Neutral": 3,
    "Sad": 4,
    "Surprise": 5,
}

# Define even more Paths
TRAIN_LABELS_DIR = "data/training/labels/"
TEST_LABELS_DIR = "data/testing/labels/"

# Ensure label directories exist
os.makedirs(TRAIN_LABELS_DIR, exist_ok=True)
os.makedirs(TEST_LABELS_DIR, exist_ok=True)

# Function to create YOLOv8 label files
def create_yolo_labels(csv_file, labels_dir):
    df = pd.read_csv(csv_file)
    
    for _, row in df.iterrows():
        img_filename = row["path"]  # Example: "lol795~ahegao.jpg"
        class_label = row["label"]   # Example: "Ahegao"

        # Convert label to YOLO class ID
        class_id = CLASS_MAPPING.get(class_label, -1)  # Default to -1 if not found
        if class_id == -1:
            print(f"Warning: Label {class_label} not found in class mapping!")
            continue

        # Fix: Ensure label files go directly into `labels/`
        label_filename = os.path.splitext(os.path.basename(img_filename))[0] + ".txt"
        label_path = os.path.join(labels_dir, label_filename)

        # Assuming the whole image is the bounding box (full width and height)
        yolo_label = f"{class_id} 0.5 0.5 1.0 1.0\n"

        # Save to file (Fix: No class subfolder)
        with open(label_path, "w") as f:
            f.write(yolo_label)

# Generate labels for train and validation datasets
create_yolo_labels(TRAINING_CSV, TRAIN_LABELS_DIR)
create_yolo_labels(TESTING_CSV, TEST_LABELS_DIR)

print("YOLOv8 labels created successfully!")