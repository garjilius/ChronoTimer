#Per farlo funzionare in pycharm bisogna installare il paccheto future
import tkinter as tk
import datetime

class Chrono:
    def start(self):
        self.timerCount += 1
        self.timer.config(text=datetime.timedelta(seconds=self.timerCount))
        self.timerID = self.timer.after(1000, self.start)
        self.startB['state'] = tk.DISABLED

    def stop(self):
        self.frame.after_cancel(self.timerID)
        self.startB['state'] = tk.NORMAL
        self.running = False

    def clear(self):
        self.timerCount = 0
        self.running = False
        self.timer.config(text=0)

    def __init__(self, master):
        self.master = master
        self.running = False
        self.frame = tk.Frame(self.master)
        self.timer = tk.Label(self.frame, text=0,
                      font='times 70')  # Si può aggiungere direttamente o come faccio sotto separatamente
        self.timer.grid(row=0, column=0, columnspan=2)
        self.timerCount = 0
        self.timerID = 0

        self.startB = tk.Button(self.frame, text="Start", padx=30, pady=10, command=self.start)
        self.startB.grid(row=1, column=0)
        self.stopB = tk.Button(self.frame, text="Pause", padx=30, pady=10, command=self.stop)
        self.stopB.grid(row=1, column=1)
        self.clearB = tk.Button(self.frame, text="Reset", padx=93, pady=10, command=self.clear)
        self.clearB.grid(row=2, column=0, columnspan=2)
        self.modeLabel = tk.Label(self.frame, text="Chrono mode", anchor=tk.CENTER)
        self.modeLabel.grid(row=3, column=0, columnspan=3)
        self.frame.pack()