from pytube import YouTube
# misc
import os
import shutil
import math
import datetime
# plots
import matplotlib.pyplot as plt

# image operation
import cv2
url='https://www.youtube.com/watch?v=lrxoJTSeKBo'


def get_available_formats(url):
    video = YouTube(url)
    availables=video.streams.filter(file_extension = "mp4").all()
    formats=["Resolution @ frames per second"]
    for el in availables:
        formats.append(str(el.resolution ) + " @ " + str(el.fps)+"fps" )
    return formats
    
def ok():
    print ("value is:" + variable.get())

    def InputBox(self):        
        dialog = tk.Toplevel(self.dialogroot)
        dialog.width = 600
        dialog.height = 100

        frame = tk.Frame(dialog,  bg='#42c2f4', bd=5)
        frame.place(relwidth=1, relheight=1)

        entry = tk.Entry(frame, font=40)
        entry.place(relwidth=0.65, rely=0.02, relheight=0.96)
        entry.focus_set()

        submit = tk.Button(frame, text='OK', font=16, command=lambda: self.DialogResult(entry.get()))
        submit.place(relx=0.7, rely=0.02, relheight=0.96, relwidth=0.3)

        root_name = self.dialogroot.winfo_pathname(self.dialogroot.winfo_id())
        dialog_name = dialog.winfo_pathname(dialog.winfo_id())

        # These two lines show a modal dialog
        self.dialogroot.tk.eval('tk::PlaceWindow {0} widget {1}'.format(dialog_name, root_name))
        self.dialogroot.mainloop()

        #This line destroys the modal dialog after the user exits/accepts it
        dialog.destroy()

        #Print and return the inputbox result
        print(self.strDialogResult)
        return self.strDialogResult




from tkinter import *


mainloop()
