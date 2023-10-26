import matplotlib.pyplot as plt
import time
from PIL import Image, ImageDraw
import matplotlib.cm as cm
import os
import numpy as np
import openpyxl
from matplotlib.figure import Figure

# 0.library
import pandas as pd
from io import StringIO

# 1.파일읽기
with open('C:\\Users\\USER\\Desktop\\20220804\\Temperature\\temp1.txt', 'r') as file:
# 2.변수저장
    lines = file.readlines()

# 3.제거할 위치 찾기
data_start_index = 0
for i, line in enumerate(lines):
    if "Time [s]" in line:
        data_start_index = i
        break
# 4.앞부분 제거
data_table = lines[data_start_index:]

# 5.data frame으로 옮기기
df = pd.read_csv(StringIO('\n'.join(data_table)), delimiter='\t')

figure = Figure()

input_image_dir = "C:\\Users\\USER\\Desktop\\20220804\\Far Pointing"
file_names = [f for f in os.listdir(input_image_dir) if f.endswith(".cam02.png")]

# Create an empty DataFrame to store the average data
average_data = pd.DataFrame(columns=['Date Saved', 'Average X', 'Average Y'])

# Lists to store average X and Y data for plotting
average_x_values = []
average_y_values = []

# Lists to store all average points
all_average_points = []

# Lists to store colors for the legend in average_data_plot
legend_colors = []

# Process each ".cam02.png" file in the folder
for i, file_name in enumerate(file_names):
    # Construct the full file path
    file_path = os.path.join(input_image_dir, file_name)

    # Get the date the file was last modified
    date_saved = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(file_path)))

    image = Image.open(file_path)

    # Convert the image to a NumPy array for faster processing
    image_array = np.array(image)

    # Define a threshold to filter out noisy pixels
    threshold = 1000  # Adjust this threshold as needed

    # Create a list to store the top 20 significant pixel values and their coordinates
    top_pixels = []

    # Get the dimensions of the image
    height, width = image_array.shape

    # Measure the start time
    start_time = time.time()

    # Iterate through all (x, y) coordinates and check pixel values
    for x in range(width):
        for y in range(height):
            pixel_value = image_array[y, x]  # Get the pixel value (grayscale)
            if pixel_value > threshold:
                top_pixels.append((x, y, pixel_value))

    # Sort the list by pixel values in descending order
    top_pixels.sort(key=lambda x: x[2], reverse=True)

    # Get the top 20 pixel values and their coordinates
    top_20_pixels = top_pixels[:30]

    # Calculate the average (x, y) data
    average_x = sum(x for x, _, _ in top_20_pixels) / len(top_20_pixels)
    average_y = sum(y for _, y, _ in top_20_pixels) / len(top_20_pixels)

    # Append the date saved and average data to the DataFrame
    new_data = pd.DataFrame({'Date Saved': [date_saved], 'Average X': [average_x], 'Average Y': [average_y]})
    average_data = pd.concat([average_data, new_data], ignore_index=True)

    # Append average X and Y data for plotting
    average_x_values.append(average_x)
    average_y_values.append(average_y)

    # Append the average point to the list of all average points
    all_average_points.append((average_x, average_y))

    # Append a color to the legend_colors list for average_data_plot
    legend_colors.append(cm.plasma(i / len(file_names)))

    # Save the image with top 20 points highlighted
    top_points_image_path = os.path.join(input_image_dir, f'top_20_points_image_{i}.png')
    new_image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(new_image)
    for x, y, _ in top_20_pixels:
        draw.ellipse((x - 1, y - 1, x + 1, y + 1), fill=(255, 0, 0))  # Red dots
    new_image.save(top_points_image_path)

# Convert 'Time [s]' column to datetime
df['Time [s]'] = pd.to_datetime(df['Time [s]'], unit='s')
average_data['Date Saved'] = pd.to_datetime(average_data['Date Saved'])
df['Time [s]'] = df['Time [s]'].apply(lambda x: x.replace(year=average_data['Date Saved'].dt.year.values[0],month=average_data['Date Saved'].dt.month.values[0], day=average_data['Date Saved'].dt.day.values[0]))
df['Date Saved'] = df['Time [s]']

merged_df = pd.concat([average_data, df], axis=0, ignore_index=True)
merged_df = merged_df.sort_values(by='Date Saved', ascending=True)
merged_df.drop(['Date', 'Time', 'Time [s]'], axis=1, inplace=True)

print(merged_df)

plt.scatter(merged_df['Date Saved'], merged_df['Average X'], label='Average X')
plt.scatter(merged_df['Date Saved'], merged_df['Average Y'], label='Average Y')
plt.scatter(merged_df['Date Saved'], merged_df['TH1[캜]'], label='Average Y')
plt.xlabel('Date Saved')
plt.ylabel('Values')
plt.title('Merged Data: Average X and Y Over Time')
plt.legend()

merged_df.to_excel('C:\\Users\\USER\\Desktop\\save\\merged_data.xlsx', index=True)
