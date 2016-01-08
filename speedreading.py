from tkinter import *

def animate_text(root, canvas, filename, width, height, font_size, wpm):
    return

def speed_read(filename, width, height, font_size, wpm):
    root = Tk()
    return

def main(args):
    if len(args) != 6:
        print("Usage: python speedreading.py [filename] [width] [height] [font_size] [wpm]")
        default = input("Use default behavior? (y/n): ")
        if default == "y" or default == "Y": 
            print("Using default options!")
            speed_read("musk.txt", 400, 200, 18, 300)
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