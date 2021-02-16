# Per farlo funzionare in pycharm bisogna installare il paccheto future
import tkinter as tk
from playsound import playsound
import os
import datetime


class Timer:
    def start(self):
        self.counterLabel.grid(row=1, column=0, columnspan=2)
        self.timeEntry.grid_forget()
        if not self.running:
            splitTime = self.timeEntry.get().split(":")
            self.startB['state'] = tk.DISABLED
            if len(splitTime) == 3:
                self.totalSeconds = int(splitTime[0]) * 60 * 60 + int(splitTime[1]) * 60 + int(splitTime[2])
            elif len(splitTime) == 2:
                self.totalSeconds = int(splitTime[0]) * 60 + int(splitTime[1])
            elif len(splitTime) == 1:
                self.totalSeconds = int(splitTime[0])
            self.running = True
        if self.totalSeconds < 0:
            self.stop()
            self.clear()
            if self.soundVar.get():
                path=os.path.dirname(os.path.abspath(__file__))
                path = path.replace(" ", "%20")
                playsound(path+os.sep+'alarm1.mp3')
                #play = threading.Thread(target=lambda:playsound(path+os.sep+'alarm1.mp3'))
                #play.start()
            return
        self.counterLabel.config(text=datetime.timedelta(seconds=self.totalSeconds), fg='SystemWindowBody')
        if self.totalSeconds<=60:
            self.counterLabel.config(fg='orange')
        if self.totalSeconds<=10:
            self.counterLabel.config(fg='red')
        self.totalSeconds -= 1
        self.timerID = self.counterLabel.after(1000, self.start)

    def stop(self):
        self.frame.after_cancel(self.timerID)
        self.startB['state'] = tk.NORMAL

    def clear(self):
        self.running = False
        self.stop()
        self.startB['state'] = tk.NORMAL
        self.timeEntry = tk.Entry(self.frame, font='times 45', width=10)
        self.timeEntry.insert(0, "HH:MM:SS")
        self.timeEntry.grid(row=0, column=0, columnspan=2)
        self.counterLabel.grid_remove()

    def __init__(self, master):
        self.master = master
        self.running = False
        self.frame = tk.Frame(self.master)
        self.timerID = 0
        self.totalSeconds = 0
        self.counterLabel = tk.Label(self.frame, font='times 45', width=10, text="hh:mm:ss")
        self.timeEntry = tk.Entry(self.frame, font='times 45', width=10)
        self.timeEntry.insert(0, "HH:MM:SS")
        self.timeEntry.grid(row=0, column=0, columnspan=2)
        self.startB = tk.Button(self.frame, text="Start", padx=30, pady=10, command=self.start)
        self.startB.grid(row=2, column=0)
        self.stopB = tk.Button(self.frame, text="Pause", padx=30, pady=10, command=self.stop)
        self.stopB.grid(row=2, column=1)
        self.clearB = tk.Button(self.frame, text="Reset", padx=93, pady=10, command=self.clear)
        self.clearB.grid(row=3, column=0, columnspan=2)
        self.modeLabel = tk.Label(self.frame, text="Timer mode", anchor=tk.CENTER)
        self.soundVar = tk.BooleanVar()
        self.alertToggler = tk.Checkbutton(self.frame, text='Play sound', variable=self.soundVar, onvalue=True, offvalue=False)
        self.alertToggler.grid(row=4, column=0, columnspan=2)
        self.modeLabel.grid(row=5, column=0, columnspan=2)
        self.frame.pack()
