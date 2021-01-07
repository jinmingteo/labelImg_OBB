#!/usr/bin/env python3
import tkinter as tk
import os
from tkinter import filedialog
from video_to_frames import get_frame_from_path

assert os.getenv('offline_annotation_repo') != None, "Please set env var at /etc/environment"

def UploadAction(event=None):
    directory = filedialog.askdirectory()
    assert os.getenv('offline_annotation_repo') != None
    output_dir = os.getenv('offline_annotation_repo')
    get_frame_from_path(directory, output_dir, images_per_sec=1)

root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

button = tk.Button(root, text='Open Video Directory', command=UploadAction)
canvas1.create_window(150, 150, window=button)

root.mainloop()