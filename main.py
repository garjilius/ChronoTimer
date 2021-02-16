import tkinter as tk
from chrono import Chrono
from timer import Timer

def main():
    def launchTimer(root):
        for widget in root.winfo_children():
            if widget.winfo_class() == 'Frame':
                widget.destroy()
        t = Timer(root)
        return t
    def launchChrono(root):
        for widget in root.winfo_children():
            if widget.winfo_class() == 'Frame':
                widget.destroy()
        c = Chrono(root)
        return c

    root = tk.Tk()
    root.title("DudeTimer")
    root.resizable(False, False)
    launchTimer(root) #Default
    menubar = tk.Menu(root)
    modemenu = tk.Menu(menubar)
    modemenu.add_command(label="Timer", command=lambda: launchTimer(root))
    modemenu.add_command(label="Chronometer", command=lambda: launchChrono(root))
    menubar.add_cascade(label="Mode", menu=modemenu)
    root.config(menu=menubar)
    root.lift()
    root.mainloop()

if __name__ == '__main__':
    main()