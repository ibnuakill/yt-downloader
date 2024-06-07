import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        
        title.configure(text=ytObject.title, text_color="white")
        fisnishlabel.configure(text="")
        video.download()
        fisnishlabel.configure(text="Downloaded!")
    except:
        fisnishlabel.configure(text="Download Error", text_color="red")
 
def on_progress(stream, chunk, bytes_remaining):
     total_size = stream.filesize
     bytes_downloaded = total_size - bytes_remaining
     percentage_of_completion = bytes_downloaded / total_size * 100
     per = str(int(percentage_of_completion))
     pPercentage.configure(text=per + '%')
     pPercentage.update()
     
     # update progress bar
     progresBar.set(float(percentage_of_completion) / 100)

#system setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# add ui element
title = customtkinter.CTkLabel(app, text="Insert Youtub Link")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40,textvariable=url_var)
link.pack()

# fisnished download
fisnishlabel = customtkinter.CTkLabel(app, text="")
fisnishlabel.pack()

# progres precentase
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progresBar = customtkinter.CTkProgressBar(app, width=400)
progresBar.set(0.5)
progresBar.pack(padx=10, pady=10)
# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#run app
app.mainloop()