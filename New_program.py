import cv2
import os

video_folder = 'project/New_videos'
output_folder = 'New_frames'
os.makedirs(output_folder, exist_ok=True)

video_files = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.avi', '.mov'))]

frame_gap = 10
saved_count = 0

for video_file in video_files:
    video_path = os.path.join(video_folder, video_file)
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    if not cap.isOpened():
        print(f"❌ Could not open video: {video_file}")
        continue

    print(f"📽️ Extracting frames from: {video_file}")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_gap == 0:
            filename = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
            cv2.imwrite(filename, frame)
            saved_count += 1

        frame_count += 1

    cap.release()

print(f"\n✅ Done. Total frames saved: {saved_count}")
