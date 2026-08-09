
import os
import shutil

# Source and destination folders
source_folder = "source"
destination_folder = "destination"


def move_jpg_files(source_folder: str, destination_folder: str) -> None:
    """Move all .jpg/.jpeg files from source_folder to destination_folder."""

    # Check whether source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Get all files from source folder
    files = os.listdir(source_folder)

    moved_count = 0

    # Move .jpg / .jpeg files
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg")):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)

            # Skip directories that happen to match the extension pattern
            if not os.path.isfile(source_path):
                continue

            try:
                shutil.move(source_path, destination_path)
                print("Moved:", file)
                moved_count += 1
            except Exception as e:
                print(f"Failed to move {file}: {e}")

    if moved_count:
        print(f"All {moved_count} .jpg file(s) moved successfully!")
    else:
        print("No .jpg files found to move.")


if __name__ == "__main__":
    move_jpg_files(source_folder, destination_folder)