import os
import pandas as pd

# ✅ Full correct path to your labels folder
labels_path = r"C:\Users\91988\Downloads\crowd Density estimation.v1i.yolov8\train\labels"

# Lists to store results
frame_names = []
person_counts = []
density_levels = []

# Updated classification logic
def classify_density(count):
    if count <= 5:
        return 'Low'
    elif count <= 7:
        return 'Medium'
    else:
        return 'High'

# Go through each label file
for file in os.listdir(labels_path):
    if file.endswith('.txt'):
        filepath = os.path.join(labels_path, file)
        with open(filepath, 'r') as f:
            lines = f.readlines()
            count = len(lines)
            density = classify_density(count)
            frame_names.append(file.replace('.txt', '.jpg'))
            person_counts.append(count)
            density_levels.append(density)

# Save results
df = pd.DataFrame({
    'Frame': frame_names,
    'Person Count': person_counts,
    'Density': density_levels
})

# Save as CSV
df.to_csv('frame_density_table.csv', index=False)
print(df)
print("\n✅ Saved as frame_density_table.csv")
