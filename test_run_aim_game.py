import tkinter as tk
import Start

root = tk.Tk()
root.attributes('-fullscreen', True)
start_game = Start.Start(tk,root)

start_game.start_screen()