import requests
import concurrent.futures
import tkinter as tk

urls = [
    'https://example.com/file1',
    'https://example.com/file2',
    'https://example.com/file3',
    'https://example.com/file4',
    'https://example.com/file5'
]

class DownloadProgressBar:
    def __init__(self, master, url):
        self.master = master
        self.url = url
        self.progress = tk.DoubleVar()
        self.progress.set(0)
        self.label = tk.Label(master, text=url)
        self.label.pack()
        self.progressbar = tk.Progressbar(master, variable=self.progress, maximum=100)
        self.progressbar.pack()

    def update_progress(self, progress):
        self.progress.set(progress)

def download_file(url, progress_bar):
    response = requests.get(url, stream=True)
    filename = url.split('/')[-1]
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    with open(filename, 'wb') as f:
        for data in response.iter_content(block_size):
            f.write(data)
            progress_bar.update_progress(min(100, int(100 * f.tell() / total_size)))
    print(f'{filename} downloaded')

root = tk.Tk()
progress_bars = []
for url in urls:
    progress_bar = DownloadProgressBar(root, url)
    progress_bars.append(progress_bar)

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url, progress_bar in zip(urls, progress_bars):
        future = executor.submit(download_file, url, progress_bar)
        futures.append(future)

root.mainloop()