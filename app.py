from tkinter import *
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

def download():
    try:
        # Get the URL from input
        video_path = link.get()
        youtube = YouTube(video_path, on_progress_callback=on_progress)
        mp4 = youtube.streams.get_highest_resolution()
        
        # Set the download directory
        download_directory = os.path.expanduser("~\\Downloads")
        
        # Download the video
        mp4.download(output_path=download_directory)
        print(f"Downloaded to {download_directory}")
    except Exception as e:
        print(f"Error: {e}")
    

#หน้าจอโปรแกรม
root=Tk()
root.title("Youtube Downloader")
canvas=Canvas(root,width=400,height=200)
canvas.pack()

#ชื่อโปรแกรม
app_title=Label(root,text="ดาวน์โหลดวิดีโอจากยูทูป",font=('Arial',20,'bold'))
canvas.create_window(200,30,window=app_title)

#ระบุ link / ปุ่มกดดาวน์โหลด
label=Label(root,text="ป้อนลิงก์วิดีโอ (URL)")
canvas.create_window(200,80,window=label)
link=Entry(root,width=60)
canvas.create_window(200,100,window=link)

downloadBtn=Button(text="ดาวน์โหลด",command=download)
canvas.create_window(200,150,window=downloadBtn)

root.mainloop()