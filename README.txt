Crowd Density Estimation Assignment

Project Summary:
This project focuses on detecting people in crowd images, estimating the density, and classifying frames into Low, Medium, and High density categories based on person count.

The work includes:
- Frame extraction from videos
- Dataset annotation using Roboflow
- Model training
- Frame density classification
- Organization of data and code

---

Folder Structure:

Crowd_Project_Submission/
|
├── extracted_frames/         # Raw extracted frames from video
├── labeled_frames/            # Frames with bounding boxes (optional for visual proof)
├── Roboflow_export/           # Dataset exported from Roboflow
|     ├── train/
|     ├── test/
|     └── valid/
├── extract_frames.py          # Script to extract frames from video
├── generate_labeled_frames.py # Script to draw bounding boxes on frames
├── classify_density.py        # Script to classify frames based on person count
├── frame_density_table.csv    # Frame vs People Count vs Density Category
└── README.txt                 # This file


---

Steps Followed:
1. Extracted frames using OpenCV.
2. Uploaded frames to Roboflow for annotation (bounding boxes around persons).
3. Exported annotated dataset in YOLO format.
4. Classified images based on detected person counts:
   - Low Density: ≤ 5 persons
   - Medium Density: ≤ 7 persons
   - High Density: > 7 persons
5. Created a CSV file summarizing frame-wise density.

---

Technologies Used:
- Python
- OpenCV
- Roboflow
- Pandas
- VS Code
- jupyter Notebook(initial work)

---

How to Access:
- All project files, datasets, and results are organized in the main folder.
- The entire folder is uploaded to Google Drive with **Public Access**.

---

Submitted For:
IoT Assignment - Crowd Density Estimation  


---

End of README

