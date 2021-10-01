import tkinter as tk;
from tkinter import *;
from git import Repo;
from tkinter import messagebox;
import tkinter.filedialog;

def enter_path():
    try:pathOnPC = tkinter.filedialog.askdirectory()+"/"+message.get();
    except:messagebox.showerror(message="что-то с директориями");

    pathToProj = "https://github.com/" + message.get()+".git";
    try:Repo.clone_from(pathToProj, pathOnPC); dw = True;
    except: messagebox.showerror(message="ошибка при скачивании"); dw = False;
    if dw:
        messagebox.showinfo(message="git repository cloned to:\n"+pathOnPC, title="successfully!");

RootWindow = tk.Tk();
RootWindow.title("K.J_App");
RootWindow.config(bg="#1e1e1e");
RootWindow.geometry("300x150");
RootWindow.resizable(False, False);

welcome = tk.Label(RootWindow, text="Welcome to K.J_App", bg="#1e1e1e", fg="#bd9164", font="roboto");
welcome.place(x=1, y=1);

lab = tk.Label(RootWindow, text="enter path to git repositry").place(x=1, y=30);
message = StringVar();
 
message_entry = Entry(RootWindow, bg="#c6c6c6", fg="#3f3d00", textvariable=message).place(x=1, y=56, width=120);

message_button = Button(text="Download", command=enter_path);
message_button.place(x=125, y=56, height=20);

labGuid = Label(RootWindow, text="example: programkeyj/port_checer", bg="#1e1e1e", fg="#bd9164").place(x=1, y=85);


RootWindow.mainloop();