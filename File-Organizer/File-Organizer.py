import os
import shutil
import tkinter as tk


def reset():
    label.configure(text="Enter the absolute path")
    entry.configure(state="normal")
    b.configure(text="Organize", command=lambda: organize())


def organize():
    path = entry.get()
    print(path)
    if os.path.exists(path):
        files = os.listdir(path)
        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            if not os.path.exists(path + "/" + extension):
                os.makedirs(path + "/" + extension)
            shutil.move(path + "/" + file, path + "/" + extension + "/" + file)
        label.configure(text="Organized")
        entry.configure(state="disabled")
        b.configure(text="New path", command=lambda: reset())
    else:
        label.configure(text="Path does not exists")
        entry.configure(state="disabled")
        b.configure(text="reset", command=lambda: reset())


window = tk.Tk()
window.title("File Organizer")
window.geometry("450x300")
window.resizable(False, False)
window.configure(bg="black")

label = tk.Label(window, width=100, height=1, bg="black", fg="grey", text="Enter the absolute path",
                 font=("arial", 30))
label.pack(pady=10)
entry = tk.Entry(window, width=80, font=("arial", 14), fg="red")
entry.pack(padx=10, pady=30)
b = tk.Button(window, text="Organize", font=("arial", 30), fg="black", bg="grey", activebackground="black",
              activeforeground="grey", command=lambda: organize())
b.pack(padx=20, pady=20)
window.mainloop()
