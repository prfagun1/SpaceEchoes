import cv2
import numpy as np
import pandas as pd
import time

# Open the video
video_path = 'video.mp4'
cap = cv2.VideoCapture(video_path)

# Variables
frames_per_second = 2
quadrants = 3
#3 means 3*3 = 9 squares

desired_duration = 1000000  # In seconds

# List to store the data
data = []

# Function to divide the frame into quadrants
def divide_into_quadrants(frame, num_quadrants):
    height, width, _ = frame.shape
    step_x = width // num_quadrants
    step_y = height // num_quadrants
    quadrant_means = []

    for i in range(num_quadrants):
        for j in range(num_quadrants):
            x1 = i * step_x
            x2 = (i + 1) * step_x
            y1 = j * step_y
            y2 = (j + 1) * step_y
            quadrant = frame[y1:y2, x1:x2]
            quadrant_mean = np.mean(quadrant, axis=(0, 1)).tolist()
            quadrant_means.append(quadrant_mean)

    return quadrant_means

# Get the original video frame rate
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

# Calculate the frame interval to achieve the desired rate
interval = frame_rate // frames_per_second

# Loop through the video frames
previous_time = 0
lines = []
frame_count = 0

while True:
    ret, frame = cap.read()
        
    if not ret or cap.get(cv2.CAP_PROP_POS_MSEC) / 1000 >= desired_duration:
        break

    # Get the time in seconds
    frame_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000

    # Check if it's time to capture the frame based on the calculated interval
    if frame_count >= interval:
        frame_count = 0
        data.append({'Time (s)': frame_time, 'Data': lines})
        print("Frame: ", frame_time)
        lines = []

    # Convert the frame to a numpy array
    frame_array = np.array(frame)

    # Get information from all pixels in the frame
    height, width, _ = frame_array.shape
    
    color_mean = np.mean(frame_array, axis=(0, 1))  # Calculate the color mean
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness_mean = np.mean(gray_frame)  # Calculate the brightness mean

    # Divide the frame into quadrants and calculate color means for each
    quadrant_means = divide_into_quadrants(frame_array, quadrants)

    line = []
    for i, quadrant_mean in enumerate(quadrant_means):
        coordinate = i + 1  # Quadrants are numbered from 1 to n
        lines.append([coordinate, quadrant_mean, color_mean.tolist(), brightness_mean])

    frame_count += 1
    previous_time = int(frame_time)

# Close the video after processing
cap.release()

# Create a pandas DataFrame with the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('video_data.csv', index=False, header=False)
