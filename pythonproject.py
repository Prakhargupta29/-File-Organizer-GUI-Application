import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Applications": [".exe", ".msi", ".apk", ".dmg"]
}


def draw_gradient(canvas, width, height):
    # Start color (#00c6ff), End color (#ff6ec4)
    r1, g1, b1 = (0, 198, 255)
    r2, g2, b2 = (255, 110, 196)

    steps = 100  # number of gradient steps
    for i in range(steps):
        r = int(r1 + (r2 - r1) * i / steps)
        g = int(g1 + (g2 - g1) * i / steps)
        b = int(b1 + (b2 - b1) * i / steps)
        color = f'#{r:02x}{g:02x}{b:02x}'  # convert RGB to hex
        # Draw thin rectangles across the width
        canvas.create_rectangle(i * (width/steps), 0, (i+1) * (width/steps), height, outline="", fill=color)

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    # check if the folder exists
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "Selected folder does not exist.")
        return
    #skip the folder itself
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isdir(file_path):
            continue

# get the file extension and Determine Category
        _, ext = os.path.splitext(file_name)
        category = get_category(ext.lower())

# Create a new folder for the category if it does not exist
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)
# Move the File to the Category Folder
        try:
            shutil.move(file_path, os.path.join(category_folder, file_name))
        except Exception as e:
            print(f"Error moving {file_name}: {e}")

    messagebox.showinfo("Success", "Files organized successfully!")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, folder_selected)

def start_organizing():
    folder = entry_path.get()
    organize_folder(folder)

# GUI setup
root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")   # give the dimention to the window
root.resizable(False, False)          # Disable resizing


canvas = tk.Canvas(root, width=400, height=200, highlightthickness=0)
canvas.pack(fill="both", expand=True)
draw_gradient(canvas, 400, 200)




label = tk.Label(root, text="Select a folder to organize:", bg="lightblue", fg="darkblue") # create a label
label.pack(pady=10)  # add some space around the label

#take path of the folder from user
entry_path = tk.Entry(root, width=40, bg="white", fg="darkblue")
entry_path.pack()  



# add a button to browse the folder
browse_button = tk.Button(root, text="Browse", command=browse_folder ,fg="white",bg="red" )
browse_button.pack(pady=5)

# add a button to start organizing
organize_button = tk.Button(root, text="Organize Files", command=start_organizing,fg="black",bg="#ADF802")
organize_button.pack(pady=10)

canvas.create_window(200, 40, window=label)
canvas.create_window(200, 70, window=entry_path)
canvas.create_window(90, 110, window=browse_button)
canvas.create_window(290, 110, window=organize_button)

root.mainloop()
