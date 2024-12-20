import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_str.set(km_output)

# Main window
window = ttk.Window(themename = "darkly")
window.title("Tkinter test 1")
window.geometry("600x400")

# Title
label_1 = ttk.Label(master = window,
                    text = "Main title",
                    font = "Calibri 18")
label_1.pack()

# Input
input_frame = ttk.Frame(master = window)
input_frame.pack(pady = 10)

entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame,
                  textvariable = entry_int)
entry.pack(side = "left", padx = 10)

button = ttk.Button(master = input_frame,
                    text = "convert",
                    command = convert)
button.pack()

output_str = tk.StringVar()
output_label = ttk.Label(master = window,
                         text = "Output",
                         font = "Calibri 18",
                         textvariable = output_str)
output_label.pack(pady = 5)

window.mainloop()

