from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from tkinter.ttk import *

direct = ""


def open_path():
    download_out.config(text="Wait if system shows no responding during Download",
                        font=("Bohnschrift SemiBold", 10, "bold"))
    download_name.config(text="")
    download_size.config(text="")
    download_location.config(text="")
    global direct
    direct = filedialog.askdirectory()
    path_holder.config(text=direct)


def Download():
    url = link_ent.get()
    selected = types.get()
    if len(url) < 1:
        link_error.config(text="Please insert URL")
    if len(direct) < 1:
        path_error.config(text="Please insert Path")
    else:
        link_error.config(text="")
        path_error.config(text="")
        try:
            Yt = YouTube(url)
            try:
                if selected == options[0]:
                    typ = Yt.streams.get_highest_resolution()
                elif selected == options[1]:
                    typ = Yt.streams.filter(progressive=True, file_extension="mp4").first()
                elif selected == options[2]:
                    typ = Yt.streams.filter(only_audio=True).first()
                try:
                    typ.download(direct)
                    link_ent.delete(0, "end")
                    path_holder.config(text="\t\t\t\t")
                    download_out.config(text="Downloaded")

                    name = typ.title
                    size = typ.filesize/1024000
                    size = round(size, 1)
                    download_name.config(text="Name: "+name)
                    download_size.config(text="Size: "+str(size)+"MB")
                    download_location.config(text="Path: "+direct)
                except:
                    download_out.config(text="Download Failed")
            except:
                download_out.config(text="Having problems downloading the Video")
        except:
            path_error.config(text="Please insert valid Path")


window = Tk()
window.geometry("500x650+350+20")
window.title("YouTube Video Downloader")
window.resizable(False, False)
window.config(bg="gray")

heading = Label(window, text="YouTube Video Downloader", background="gray", foreground="dark orange",
                font=("Bohnschrift SemiBold", 20, "bold"))
heading.pack(anchor="center", pady=10)

link = Label(window, text="Video Link:", background="gray", foreground="dark orange",
             font=("Bohnschrift SemiBold", 10))
link.pack(anchor="nw", padx=30, pady=25)

entry_url = StringVar()
link_ent = Entry(window, width=55, textvariable=entry_url)
link_ent.place(x=110, y=80)

link_error = Label(window, background="gray", foreground="dark orange", font=("Bohnschrift SemiBold", 10))
link_error.place(x=300, y=115)

path = Label(window, text="Path:", background="gray", foreground="dark orange", font=("Bohnschrift SemiBold", 10))
path.pack(anchor="nw", padx=30, pady=25)

path_holder = Label(window, text="\t\t\t\t", background="white", foreground="black",
                    font=("Bohnschrift SemiBold", 10))
path_holder.place(x=110, y=150)

path_style = Style()
path_style.configure("PT.TButton", background="dark orange", foreground="dark orange",
                     font=("Bohnschrift SemiBold", 10))

path_btn = Button(window, width=11, text="Select Path", style="PT.TButton", command=open_path)
path_btn.place(x=357, y=147)

path_error = Label(window, background="gray", foreground="dark orange", font=("Bohnschrift SemiBold", 10))
path_error.place(x=300, y=190)

download_type = Label(window, text="Download Type:", background="gray", foreground="dark orange",
                      font=("Bohnschrift SemiBold", 10))
download_type.pack(anchor="w", padx=30, pady=35)

options = ["High Quality", "Low Quality", "Audio"]
types = Combobox(window, values=options, width=23)
types.current(0)
types.place(x=140, y=230)

choose_type = Label(window, text="Choose Type", background="gray", foreground="dark orange",
                    font=("Bohnschrift SemiBold", 10))
choose_type.place(x=315, y=230)

download_style = Style()
download_style.configure("DD.TButton", background="dark orange", foreground="dark orange",
                         font=("Bohnschrift SemiBold", 10))

download_btn = Button(window, width=40, text="Download", style="DD.TButton", command=Download)
download_btn.pack(anchor="center", pady=30)

download_out = Label(window, background="gray",
                     foreground="dark orange", font=("Bohnschrift SemiBold", 10))
download_out.pack(anchor="center", pady=30)

download_name = Label(window, background="gray", foreground="dark orange", font=("Bohnschrift SemiBold", 10))
download_name.pack(anchor="nw", padx=30, pady=10)

download_size = Label(window, background="gray", foreground="dark orange", font=("Bohnschrift SemiBold", 10))
download_size.pack(anchor="nw", padx=30, pady=10)

download_location = Label(window, background="gray", foreground="dark orange", font=("Bohnschrift SemiBold", 10))
download_location.pack(anchor="nw", padx=30, pady=10)

mainloop()
