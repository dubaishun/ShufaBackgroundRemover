import os
import subprocess
import tkinter as tk
from tkinter import Tk, Button, Label, filedialog, Text, Scrollbar, ttk, W, SE, RIGHT, TOP, Y, NE, N, S, BOTH
import time
import webbrowser
from add_border_module import process_images_in_directory

# 在 App 类中添加一个类属性
class App:
    # 在 App 类中添加一个类属性
    progress_text = None

    @staticmethod
    def convert_to_pbm():
        pic_dir = 'pic'
        convert_path = os.path.join('tools', 'convert.exe')
        # 对大写后缀支持
        files_to_convert = [f for f in os.listdir(pic_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        App.update_progress("第一步开始转换...\n")
        
        for filename in files_to_convert:
            file_path = os.path.join(pic_dir, filename)
            output_path = os.path.join(pic_dir, os.path.splitext(filename)[0] + '.pbm')

            if filename.endswith('.png'):
                subprocess.run([convert_path, file_path, '-background', 'white', '-flatten', '-antialias', output_path])
            else:
                subprocess.run([convert_path, file_path, output_path])

            App.update_progress(f"{filename} 已转换为 {os.path.basename(output_path)}\n")

        App.update_progress("第一步转换完成！\n")

    @staticmethod
    def process_pbm():
        pic_dir = 'pic'
        tool_dir = 'tools'
        convert_path = os.path.join(tool_dir, 'convert.exe')
        files_to_process = [f for f in os.listdir(pic_dir) if f.endswith('.pbm')]

        App.update_progress("第二步开始转换...\n")

        for filename in files_to_process:
            file_path = os.path.join(pic_dir, filename)
            output_filename = os.path.join(pic_dir, os.path.splitext(filename)[0] + '_已转换.jpg')
            subprocess.run([convert_path, '-colorspace', 'RGB', '-type', 'TrueColor', file_path, output_filename])
            App.update_progress(f"{filename} 已转换为 {output_filename}\n")

        App.update_progress("第二步转换完成！\n")

    @staticmethod
    def convertsvg_to_png():
        pic_dir = 'pic'
        potrace_path = os.path.join('tools', 'potrace.exe')
        files_to_convert = [f for f in os.listdir(pic_dir) if f.endswith('.pbm')]

        App.update_progress("第三步开始转换...\n")

        for filename in files_to_convert:
            file_path = os.path.join(pic_dir, filename)
            output_path = os.path.join(pic_dir, os.path.splitext(filename)[0] + '.svg')

            subprocess.run([potrace_path, file_path, '-s','-o', output_path])
            App.update_progress(f"{filename} 已转换为 {os.path.basename(output_path)}\n")

        App.update_progress("第三步转换完成！\n")
        App.update_progress("全部转换完成！\n")

    @staticmethod
    def add_border():
        messages = process_images_in_directory()
        App.progress_text.insert('end', "书画作品加框结果：\n")
        App.progress_text.insert('end', "\n".join(messages) + "\n")
        App.progress_text.see('end')

    @staticmethod
    def update_progress(message):
        App.progress_text.insert('end', message)
        App.progress_text.see('end')
        root.update_idletasks()
        time.sleep(0.5)

# 创建 Tkinter 窗口
root = Tk()
root.title("书法去背景")

# 设置窗口大小
window_width = 800
window_height = 510
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

# 创建 Frame 用于放置按钮
button_frame = ttk.Frame(root)
button_frame.grid(row=0, column=0, sticky="ns", padx=(20, 0), pady=(20, 50))

# 创建按钮并绑定静态方法
btn1 = Button(button_frame, text="第一步ConvertToPbm", command=App.convert_to_pbm, width=30)
btn1.grid(row=0, column=0, sticky="w", pady=20)

btn2 = Button(button_frame, text="第二步PbmTojpg", command=App.process_pbm, width=30)
btn2.grid(row=1, column=0, sticky="w", pady=20)

btn3 = Button(button_frame, text="第三步PbmToSvg", command=App.convertsvg_to_png, width=30)
btn3.grid(row=2, column=0, sticky="w", pady=20)

btn4 = Button(button_frame, text="书画作品加框", command=App.add_border, width=30)
btn4.grid(row=3, column=0, sticky="w", pady=20)

# 创建 Frame 用于放置滚动条和文本框
frame = ttk.Frame(root)
frame.grid(row=0, column=1, sticky="nsew", padx=(0, 20), pady=(20, 50))

# 创建滚动条
scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.grid(row=0, column=1, sticky="ns")

# 创建文本框，并绑定滚动条
progress_text = Text(frame, height=20, width=70, yscrollcommand=scrollbar.set)
progress_text.grid(row=0, column=0, sticky="nsew", pady=(20, 50), padx=20)

# 将 progress_text 传递给 App 类
App.progress_text = progress_text

scrollbar.config(command=progress_text.yview)

# 创建一个 Frame 用于放置底部的标签和链接
bottom_frame = ttk.Frame(root)
bottom_frame.grid(row=1, column=0, columnspan=2, pady=20)

# 创建一个文本标签，显示注释信息
comment_label = ttk.Label(bottom_frame, text="注：使用potrace位圖轉換矢量圖形，參數閥值正常，如有特殊請聯系作者！", foreground="black")
comment_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def open_url(event):
    webbrowser.open("https://www.douyin.com/user/MS4wLjABAAAAqiYlKxHAlPI_QzUANR22KZbclBuzbHruD0tqZH5EsoE")

# 添加新代码段
label_text = "關注抖音號：dubaishun12\n私信博主，獲得速光網絡原創工具"
label_font = ('Arial', 12, 'bold')
label_foreground = "blue"
label_background = "orange"

label = ttk.Label(bottom_frame, text=label_text, font=label_font, foreground=label_foreground, background=label_background,
                  cursor="hand2")
label.grid(row=1, column=0, columnspan=3, pady=20)
label.bind("<Button-1>", open_url)

# 设置行和列的权重，使它们可以随窗口大小变化而调整大小
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Tkinter 事件循环
root.mainloop()
