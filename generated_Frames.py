import cv2
import os

# === Set your paths ===
images_path = 'C:/Users/91988/Downloads/crowd Density estimation.v1i.yolov8/train/images'
labels_path = 'C:/Users/91988/Downloads/crowd Density estimation.v1i.yolov8/train/labels'
output_path = 'labeled_frames'


os.makedirs(output_path, exist_ok=True)

# === Class name (only 1 class: person) ===
class_name = "person"

# === Loop through all images ===
for image_file in os.listdir(images_path):
    if not image_file.endswith('.jpg'):
        continue

    image_path = os.path.join(images_path, image_file)
    label_path = os.path.join(labels_path, image_file.replace('.jpg', '.txt'))

    # Read image
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Check if label file exists
    if not os.path.exists(label_path):
        print(f"No label for {image_file}, skipping.")
        continue

    # Read labels and draw boxes
    with open(label_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            class_id, x_center, y_center, w, h = map(float, parts)

            # Convert normalized values to pixel coordinates
            x_center *= width
            y_center *= height
            w *= width
            h *= height

            x1 = int(x_center - w / 2)
            y1 = int(y_center - h / 2)
            x2 = int(x_center + w / 2)
            y2 = int(y_center + h / 2)

            # Draw bounding box and label
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, class_name, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save annotated image
    output_file = os.path.join(output_path, image_file)
    cv2.imwrite(output_file, image)
    print(f"Saved: {output_file}")

print("\n✅ All labeled images saved in 'labeled_frames/' folder.")
