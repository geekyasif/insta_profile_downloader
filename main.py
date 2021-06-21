# Install these packages
# pip install instaloder
# pip install tk

import instaloader
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Instagram Profile Downloader")

def imgDownload():
    ig = instaloader.Instaloader()
    profile = entry.get()
    ig.download_profile(profile, profile_pic_only=True)
    messagebox.showinfo("Status" , "Profile Image Downloaded Successfully !")


title = Label(root, text="Instagram Profile Image Downloader", font=("Times", 20, "bold"))
title.grid(row=0, column=0, columnspan=5, padx=30, pady=10)

label1 = Label(root, text="Enter Username : ", font=("Arial", 10))
label1.grid(row=3, column=0,)

entry = Entry(root, width=40)
entry.grid(row=3, column=1, columnspan=3)

btn = Button(root, text="Download", command=imgDownload)
btn.grid(row=4, column=0, columnspan=5, pady=10)

root.mainloop()