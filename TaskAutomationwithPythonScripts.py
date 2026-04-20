import os
import shutil

# Source and destination folders
source_folder = "photo.jpg"
destination_folder = "image.jpeg"

# Create destination folder if not exists
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Move all jpg files
for file in os.listdir(source_folder):

    if file.endswith(".jpg"):

        shutil.move(
            os.path.join(source_folder, file),
            os.path.join(destination_folder, file)
        )

        print(file, "moved successfully")

print("Task completed!")