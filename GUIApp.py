from tkinter import *
from tkinter import filedialog
import os
from os import listdir
from os.path import isfile, join
from tkinter import messagebox
from pathlib import Path
import pyminizip
from RandomKeyGenarator import *
from SmallFunctions import *

window = Tk()
window.title("BreadCrumb Helper")
window.geometry('350x150')
window.resizable(False, False)

#================================================================================
def CreateFolderZip(path):
    Path(path+"/ZipFiles").mkdir(parents=True, exist_ok=True)

def GetListOfFiles(path):
    mypath = path
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

def ZipFiles(path,password):
    onlyfiles = GetListOfFiles(path)
    CreateFolderZip(path)
    for file in onlyfiles:
        print(file)
        file2 = file.split('.')
        filePath = path+"/"+file
        zipPath = path+"/ZipFiles/"+file2[0]+".zip"
        print(filePath)
        print(zipPath)
        pyminizip.compress(filePath, "", zipPath, password, 0)
#================================================================================

#================================================================================
FoldderPath=""
#================================================================================

#================================================================================
lbl = Label(window, text="Select Folder of Files", font=("Arial"))
lbl.grid(column=0, row=0, sticky='e')
lbl.grid(padx=10, pady=10)
#--------------------------------------------------------------------------------
def browse_button():
    global FoldderPath
    FoldderPath = filedialog.askdirectory()
    print(FoldderPath)
btn = Button(window, text="Browse", command=browse_button, font=("Arial"))
btn.grid(column=1, row=0)
btn.grid(padx=10, pady=10)
#================================================================================

#================================================================================
lbl2 = Label(window, text="Enter Password", font=("Arial"))
lbl2.grid(column=0, row=2, sticky='e')
lbl2.grid(padx=10, pady=10)
#--------------------------------------------------------------------------------
tx = Entry(window,width=10,font=("Arial"))
tx.grid(column=1, row=2)
#================================================================================

#================================================================================
def ZipAll():
    ZipFiles(FoldderPath,tx.get())
    messagebox.showinfo('Done!!','Zipping Completed')


btn3 = Button(window, text="Zip All", command=ZipAll, font=("Arial"))
btn3.grid(column=1, row=12)
btn3.grid(padx=10, pady=10)
#================================================================================

#================================================================================
def RenameFiles():
    onlyfiles = GetListOfFiles(FoldderPath)
    onlyfiles.sort()
    print(onlyfiles)
    
    i = 1
    for x in onlyfiles:
        y = x.split('.')
        ext = "." + y[1]
        oldPath = FoldderPath + "/" + x
        newPath = FoldderPath + "/" + str(i) + GetRandomAlphabet() + GenerateRandomKey(20) + ext
        os.rename(oldPath,newPath)
        i += 1
    
btn = Button(window, text="Randomise File Names", command=RenameFiles, font=("Arial"))
btn.grid(column=0, row=12)
btn.grid(padx=10, pady=10)
#================================================================================

window.mainloop()