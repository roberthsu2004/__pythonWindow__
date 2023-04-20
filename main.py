import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()


def main()->None:
    window = Window()
    window.title("第2003第2次視窗")
    window.mainloop()

if __name__ == "__main__":
    main()