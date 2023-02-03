from pytube import YouTube
import tkinter as tk
from tkinter import simpledialog, messagebox

ROOT = tk.Tk()
ROOT.withdraw()


def input_data(title, prompt):
    result = simpledialog.askstring(title, prompt)
    return result


video_link = input_data("Video Link", "Insira o link do vídeo")

yt = YouTube(video_link)

print(f'Título: {yt.title}')
print(f'Views: {yt.views}')

yd = yt.streams.get_highest_resolution()
download_path = input_data("Download", "Insira o caminho para download")

yd.download(download_path)

messagebox.showinfo("Mensagem", f'Download concluído com sucesso em {download_path}')
