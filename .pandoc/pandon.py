import tkinter as tk
from tkinter import filedialog
import subprocess

root = tk.Tk()
root.withdraw()
Filepath = filedialog.askopenfilename() #获得选择好的文件
# Folderpath = filedialog.askdirectory() #获得选择好的文件夹
SavedFile = filedialog.asksaveasfilename()
subprocess.call(f"powershell.exe e:\pandoc\pandoc.exe --citeproc --csl=D:\library\.pandoc\BiLan.csl --bibliography=D:\library\.zotero\Zotero.bib -M reference-section-title='参考文献' {Filepath} -o {SavedFile}", shell=True)
print('okay')
