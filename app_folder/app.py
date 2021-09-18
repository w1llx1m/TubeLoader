from pytube import YouTube
import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu


DEFAULT_OS_LOGIN = os.getlogin()
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "TubeLoader.ui")

location = (f"/home/{DEFAULT_OS_LOGIN}/Downloads")  # armazenamento


class TubeloaderApp:
    def __init__(self, master=None):
        # build ui -- user interface
        self.main_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.main_window.title("TubeLoader")
        self.frame_main = tk.Frame(self.main_window)
        self.app_name = tk.Label(self.frame_main)
        self.app_name.configure(
            background='#6464f4', font='{Droid Sans Fallback} 16 {}', foreground='#ffffff', text='TubeLoader')
        self.app_name.grid(column='0', row='0')
        self.frame_main.columnconfigure('0', pad='0')
        self.entry_url = tk.Entry(self.frame_main)
        self.entry_url.configure(
            background='#becee1', font='{Arial} 12 {}', foreground='#000000', highlightbackground='#becee1')
        self.entry_url.configure(justify='center', width='60')
        _text_ = '''paste the url here'''
        self.entry_url.delete('0', 'end')
        self.entry_url.insert('0', _text_)
        self.entry_url.grid(column='0', pady='123')
        self.frame_main.columnconfigure('0', pad='0')
        self.btn_download = tk.Button(self.frame_main)
        self.btn_download.configure(
            background='#becee1', font='{Arial} 12 {}', foreground='#000000', height='1')
        self.btn_download.configure(command=lambda: self.downloader(self.entry_url.get(), location),
                                    justify='center', text='Download', width='7')
        self.btn_download.grid(column='0', pady='12', row='2')
        self.frame_main.columnconfigure('0', pad='0')
        self.Download_span = tk.Label(self.frame_main)
        self.Download_span.configure(
            background='#6464f4', font='{Arial} 12 {}', foreground='#ffff00', width='23')
        self.Download_span.grid(column='0', row='3')
        self.frame_main.configure(
            background='#6464f4', height='600', width='800')
        self.frame_main.pack(side='top')
        self.main_window.configure(
            background='#6464f4', height='200', width='200')
        self.main_window.geometry('800x600')

        # Main widget
        self.mainwindow = self.main_window

    def run(self):
        self.mainwindow.mainloop()

    def downloader(self, link, location):
        site = YouTube(link)
        highest_resolution = site.streams.get_highest_resolution()
        self.Download_span["text"] = "Downloading..."
        highest_resolution.download(location)
        self.Download_span["text"] = "Download completed!!"


if __name__ == '__main__':
    app = TubeloaderApp()
    app.run()
