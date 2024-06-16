import tkinter as tk
from tkinter import ttk
import os
import sys

# Function to get the absolute path to the resource
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Default paths to the .blk files
file1_path_template = "{drive}:/SteamLibrary/steamapps/common/War Thunder/UserMissions/Ask3lad/ask3lad_testdrive.blk"
file2_path_template = "{drive}:/SteamLibrary/steamapps/common/War Thunder/content/pkg_local/gameData/units/tankmodels/userVehicles/us_m2a4.blk"

# Relative paths to the text files containing the parts of the text
file1_part1_path = resource_path("file1_part1.txt")
file1_part3_path = resource_path("file1_part3.txt")
file2_part1_path = resource_path("file2_part1.txt")
file2_part3_path = resource_path("file2_part3.txt")

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def update_files(file1_path, file2_path, second_part):
    # Read the known parts from the text files
    file1_part1 = read_file(file1_part1_path)
    file1_part3 = read_file(file1_part3_path)
    file2_part1 = read_file(file2_part1_path)
    file2_part3 = read_file(file2_part3_path)

    # Combine the parts for each file
    file1_new_text = f"{file1_part1}{second_part}{file1_part3}"
    file2_new_text = f"{file2_part1}{second_part}{file2_part3}"

    # Write the new text to the .blk files
    with open(file1_path, "w") as file1:
        file1.write(file1_new_text)

    with open(file2_path, "w") as file2:
        file2.write(file2_new_text)

    print("Files updated successfully.")

def submit():
    selected_drive = drive_var.get()
    vehicle_id = vehicle_id_var.get()

    if selected_drive and vehicle_id:
        file1_path = file1_path_template.format(drive=selected_drive)
        file2_path = file2_path_template.format(drive=selected_drive)
        update_files(file1_path, file2_path, vehicle_id)
    else:
        print("Please select a drive and enter a vehicle ID.")

# Create the main window
root = tk.Tk()
root.title("War Thunder File Update")

# Drive selection
tk.Label(root, text="Select the drive War Thunder is installed on:").pack(pady=10)
drive_var = tk.StringVar(value="D")
drives = ["C", "D", "E", "F"]
drive_menu = ttk.Combobox(root, textvariable=drive_var, values=drives, state="readonly")
drive_menu.pack(pady=10)

# Vehicle ID input
tk.Label(root, text="Enter Vehicle-ID:").pack(pady=10)
vehicle_id_var = tk.StringVar()
vehicle_id_entry = tk.Entry(root, textvariable=vehicle_id_var)
vehicle_id_entry.pack(pady=10)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=20)

root.mainloop()
