import tkinter as tk
from tkinter import ttk
import threading
import subprocess
import shutil
import os

root = tk.Tk()
root.title("Парсер товаров")
root.geometry("500x250")
root.iconbitmap("run/bin/icon.ico")
root.minsize(500, 250)
root.maxsize(500, 250)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 500
window_height = 250
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

custom_style = ttk.Style()
custom_style.theme_use('default')
custom_style.configure("red.Horizontal.TProgressbar", foreground='white', bg="white", background='#7E81FF')

url_frame = tk.Frame(root)
url_frame.pack(padx=40, pady=20, fill=tk.BOTH)

url_label = tk.Label(url_frame, text="Введите сайт:", font=("Helvetica", 12))
url_label.pack(side=tk.LEFT)

url_entry = tk.Entry(url_frame, width=22)
url_entry.configure(font=("Helvetica", 12))
url_entry.pack(side=tk.LEFT, padx=10)

paste_button = tk.Button(url_frame, compound="top", text="Вставить", command=lambda: paste_from_clipboard(), bg="#1E293B", fg="white", width=10)
paste_button.pack(side=tk.LEFT, padx=(0, 10))

num_pages_frame = tk.Frame(root)
num_pages_frame.pack(padx=40, pady=20, fill=tk.BOTH)

num_pages_label = tk.Label(num_pages_frame, text="Укажите кол-во страниц на сайте:", font=("Helvetica", 12))
num_pages_label.pack(side=tk.LEFT, padx=(0, 10))

num_pages_entry = tk.Entry(num_pages_frame, width=5)
num_pages_entry.configure(font=("Helvetica", 12))
num_pages_entry.pack(side=tk.LEFT, padx=10)

run_button = tk.Button(num_pages_frame, compound="top", text="Запустить", command=lambda: threading.Thread(target=start_parser).start(), bg="#7E81FF", fg="#1E1E1E", width=10)
run_button.pack(side=tk.LEFT)

button_frame = tk.Frame(root)
button_frame.pack(pady=20, side=tk.BOTTOM)

save_button = tk.Button(button_frame, text="папка сохранений", command=lambda: threading.Thread(target=open_save_folder).start(), bg="#7E81FF", fg="white", width=20)
save_button.pack(side=tk.LEFT, padx=(0, 20))

loading_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate', style="red.Horizontal.TProgressbar")

def show_loading_bar():
    global loading_bar
    
    if loading_bar is None:
        loading_bar = ttk.Progressbar(button_frame, orient='horizontal', mode='determinate')
    
    loading_bar.pack(padx=20, pady=10)
    loading_bar.start()

def hide_loading_bar():
    loading_bar.stop()
    loading_bar.pack_forget()

def show_ready_label():
    global save_button
    
    if save_button is None:
        save_button = tk.Button(button_frame, text="папка сохранений", command=lambda: threading.Thread(target=open_save_folder).start(), bg="#7E81FF", fg="white", width=20)
    
    save_button.pack_forget()
    ready_label = tk.Label(button_frame, text="Готово ", font=("Helvetica", 12), fg="#7E81FF")
    ready_label.pack(padx=20, pady=10)
    root.after(1000, lambda: ready_label.pack_forget())
    root.after(1000, lambda: save_button.pack(side=tk.LEFT, padx=(0, 20))) 


def start_parser():
    save_button.pack_forget()
    show_loading_bar()

    url = url_entry.get()
    num_pages = int(num_pages_entry.get())
    base_url, query_params = url.split("?")

    for i in range(1, num_pages+1):
        page_url = f"{base_url}/{i}/?{query_params}"
        subprocess.run(["python", "run/bin/pars.py", page_url])

    subprocess.run(["python", "run/bin/just_file.py"])
    shutil.rmtree("run/bin/temp")
    hide_loading_bar()
    
    show_ready_label()
    
    run_button.focus_set()


def open_save_folder():
    save_folder_path = os.path.join(os.getcwd(), "save")
    os.makedirs(save_folder_path, exist_ok=True)
    subprocess.run(["explorer", save_folder_path])

def paste_from_clipboard(event=None):
    url_entry.delete(0, tk.END)
    url_entry.insert(0, root.clipboard_get())

root.mainloop()