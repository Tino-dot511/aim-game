'''
This is an example of how the game would be run using the classes
'''

import tkinter as tk
import Start

root = tk.Tk() # Root is created first to then be used as argument for the classes
root.attributes('-fullscreen', True) # Allows for the game to be in fullscreen the whole time
start_game = Start.Start(tk,root) 

start_game.start_screen() # Starts the game
root.mainloop()

