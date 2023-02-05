import tkinter as tk
from tkinter import filedialog
import subprocess

root = tk.Tk()
root.withdraw()
Filepath = filedialog.askopenfilename()
SavedFile = filedialog.asksaveasfilename()
subprocess.call(f"powershell.exe e:\pandoc\pandoc.exe --citeproc --csl=D:\library\.pandoc\BiLan.csl --bibliography=D:\library\.zotero\Zotero.bib -M reference-section-title='参考文献' {Filepath} -o {SavedFile}", shell=True)
print('okay')
