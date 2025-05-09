

                                                    File Organizer GUI Application                       


Project Overview

 The File Organizer is a simple desktop application built using Python and Tkinter. It helps users automatically organize files in a selected folder into categorized subfolders such as Images, Documents, Videos, Music, Applications, and Others, based on their file extensions.

 
 Features
 - User-friendly GUI
- Organizes files by type
- Creates folders automatically
 - Alerts for errors/success
- Gradient background

 
 File Categories
 Images: .jpg, .jpeg, .png, .gif, .bmp
 Documents: .pdf, .docx, .txt, .xlsx, .pptx
 Videos: .mp4, .avi, .mkv, .mov
 Music: .mp3, .wav, .aac, .flac
 Applications: .exe, .msi, .apk, .dmg
 Others: Uncategorized files

 
 How It Works
 1. Launch the app
 2. Click 'Browse' to select a folder
 3. Path shows in the entry field
 4. Click 'Organize Files'
 5. Files move into categorized folders
 6. Message confirms success or error



 Code Structure
- draw_gradient(): Creates canvas gradient
- Documentation- get_category(): Finds category by extension
- organize_folder(): Organizes files
- browse_folder(): Opens dialog
- start_organizing(): Begins file organizing


 GUI Design Details:
 
 1. Window Size: 400x200
 2. Resizable: No
 3. Canvas Gradient: #00c6ff to #ff6ec4
 4. Browse Button: Red bg, White text
 5. Organize Button: Light green bg, Black text
 6. Entry & Label Colors: White bg, Dark blue text


 Requirements:
 1. Python 3.x
 2. Tkinter (standard)
 3. OS & shutil modules


 How to Run
 1. Save as file_organizer.py
 2. Run: python file_organizer.py
 3. Use the GUI to select and organize

 Notes
 - Ignores folders inside selected path
 - Won't affect files already sorted
 - Doesn't rename or delete any files

 
 



![Screenshot 2025-05-10 000447](https://github.com/user-attachments/assets/2534afa5-9792-4787-b0b9-ead18ea5ac4f)






