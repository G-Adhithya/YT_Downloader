import tkinter
import customtkinter
from pytube import YouTube

# Appearance settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")
app.resizable(False, False)


def download():
    try:
        yt_link = link.get()
        ytObj = YouTube(yt_link, on_progress_callback=progress)
        video = ytObj.streams.get_highest_resolution()
        video.download("./Videos")

        finishLabel.configure(
            text="The video has been downloaded successfully!", text_color="white")

    except:
        finishLabel.configure(
            text="Please check the link and try again", text_color="red")


def progress(stream, chunk, bytes_remaining):
    filesize = stream.filesize
    bytes_downloaded = filesize - bytes_remaining
    completed_percentage = (bytes_downloaded / filesize) * 100
    per = str(int(completed_percentage))

    percentage.configure(text=per + "%")
    percentage.update()

    pBar.set(float(completed_percentage) / 100)

    # Label
title = customtkinter.CTkLabel(
    app, text="Insert the YouTube link below")
title.pack(padx=10, pady=10, anchor=tkinter.CENTER)

# Text input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, 450, 50, 50, textvariable=url_var)
link.pack(anchor=tkinter.CENTER)

# Button
download_btn = customtkinter.CTkButton(
    app, 150, 50, 50, text="Download", command=download)
download_btn.pack(padx=20, pady=20)

percentage = customtkinter.CTkLabel(app, text="0%")
percentage.pack(anchor=tkinter.CENTER)

pBar = customtkinter.CTkProgressBar(app, 500, corner_radius=50)
pBar.set(0)
pBar.pack(anchor=tkinter.CENTER)

# Finish label
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack(anchor=tkinter.CENTER)

# Run the app
app.mainloop()
