import tkinter as tk
import sys
from time import sleep

# http://effbot.org/tkinterbook/tkinter-hello-tkinter.htm

end_of_sentence = [".", "!", "?"]

def calc_delay(wpm):
    """
    Converts wpm delay to seconds.
    """
    return 1 / (wpm / 60)

def welcome(root, canvas, width, height, font_size):
    """
    Gives user a chance to get ready.
    """
    for i in [5, 4, 3, 2, 1]:
        canvas.create_rectangle(0, 0, width, height, fill = 'Beige')
        if i == 1: 
            canvas.create_text(width / 2, height / 2, text="Starting in " + str(i) + " second",
                              font=("Courier", font_size))
        else:
            canvas.create_text(width / 2, height / 2, text="Starting in " + str(i) + " seconds",
                                  font=("Courier", font_size))
        root.update()
        sleep(1)

def animate_text(root, canvas, filename, width, height, font_size, wpm):
    fin = open(filename, 'r')
    words = fin.read().split()
    delay = calc_delay(wpm)
    for word in words:
        canvas.create_rectangle(0, 0, width, height, fill = 'Beige')
        canvas.create_text(width / 2, height / 2, text=word, font=("Courier", font_size))
        root.update()
        if word[-1] == ",":
            sleep(delay / 2)
        elif word[-1] in end_of_sentence:
            sleep(delay)
        sleep(delay)
    return

def speed_read(filename, width, height, font_size, wpm):
    root = tk.Tk()
    canvas = tk.Canvas(root, width = width, height = height)
    canvas.pack()
    welcome(root, canvas, width, height, font_size)
    animate_text(root, canvas, filename, width, height, font_size, wpm)
    tk.mainloop()
    return

def main(args):
    if len(args) != 6:
        print("Usage: python speedreading.py [filename] [width] [height] [font_size] [wpm]")
        default = input("Use default behavior? (y/n): ")
        if default == "y" or default == "Y": 
            print("Using default options!")
            speed_read("musk.txt", 600, 300, 20, 300)
        else:
            print("Exiting.")
        return
    else:
        filename = args[1]
        width = int(args[2])
        height = int(args[3])
        font_size = int(args[4])
        wpm = int(args[5])
        speed_read(filename, width, height, font_size, wpm)

if __name__ == '__main__':
    main(sys.argv)