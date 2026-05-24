from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import os

# Create the main window
master = Tk()
master.geometry("500x500")  # Set window size
master.title("Knowledge bank")

# Function to open the file making menu
def create_file():
    # Open file explorer dialog to choose location and filename
    file_path = filedialog.asksaveasfilename(
        title="Create New Text File",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        initialfile="new_file.txt"
    )
    
    # If user selected a file path (didn't cancel)
    if file_path:
        try:
            # Create and open the file in write mode (this creates the file)
            with open(file_path, 'w') as file:
                file.write("")  # Create empty file
            # Show success message
            success_window = Toplevel(master)
            success_window.title("Success")
            success_window.geometry("250x150")
            Label(success_window, text=f"File created successfully!\n{os.path.basename(file_path)}").pack(pady=20)
            Button(success_window, text="OK", command=success_window.destroy).pack()
        except Exception as e:
            # Show error message if something goes wrong
            error_window = Toplevel(master)
            error_window.title("Error")
            error_window.geometry("250x150")
            Label(error_window, text=f"Error creating file:\n{str(e)}").pack(pady=20)
            Button(error_window, text="OK", command=error_window.destroy).pack()

# Create a label and a button to open the new window
Label(master, text="This is the main window").pack(pady=10)
Button(master, text="Create New Text File", command=create_file).pack(pady=10)

# Run the Tkinter event loop
master.mainloop()