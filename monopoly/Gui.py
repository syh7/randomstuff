import tkinter as tk
from tkinter import ttk
from  PIL import Image, ImageTk

window = tk.Tk()
window.title("monopoly")

image = Image.open("board.jpg")
imagetk = ImageTk.PhotoImage(image)
label = tk.Label(image=imagetk)
label.image = imagetk  # keeping a reference of the image
label.pack()
