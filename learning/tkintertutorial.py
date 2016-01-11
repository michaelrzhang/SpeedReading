import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        frame = tk.Frame(master, width = 400, height = 400)
        frame.pack()
        self.button = tk.Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=tk.LEFT)

        self.hi_there = tk.Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)
    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.geometry("500x500")
app = Application(master = root)
root.mainloop()