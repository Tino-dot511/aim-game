'''
This class is used to display a starting screen, much like in other games, that
allow the player to pick one of two options; to start the game, flowing into the pick class where 
you choose how long you play, or to quit, which closes the game.
'''

import Pick
class Start():
    def __init__(self,tk,root):
        self.tk = tk # Argument that allows labels and canvas to be built
        self.root = root # Argument that allows the labels and canvas to appear on the screen
        self.canvas = None

    def on_click_start(self,event):
        self.root.unbind('<Escape>') # Unbinds the escape key so it can't be used
        self.canvas.destroy() # Destroys the canvas so that the pick canvas can appear
        new_screen = Pick.Pick(self.tk,self.root) # Leads into Pick class so the player can choose the amount of time they play
        new_screen.pick_screen()
        # run next function

    def on_click_exit(self,event):
        self.root.destroy() # Exits the whole game if player clicks exit
    
    def esc_exit(self,event):
        self.root.destroy() # Exits game if players presses escape key

    def start_screen(self):
        self.canvas = self.tk.Canvas(self.root) # Creates the canvas to place the label and start/exit labels for the game
        self.canvas.pack(fill=self.tk.BOTH, expand=True) # Allows the canvas to be used across the fullscreen as the root is in fullscreen
        description = self.tk.Label(self.canvas,text='Aim game: Click as many targets in a time of \n  your choosing to test accuracy', font=('Arial',30), fg='black')
        # Labels that are shown like how a game has a title card
        description.place(x = (self.root.winfo_screenwidth()/3)-130, y = (self.root.winfo_screenheight()/3))
        start_label = self.tk.Label(self.canvas,text='Start', font=('Arial',20), fg='white',bg='black')
        start_label.place(x = (self.root.winfo_screenwidth()/3)-20, y = (self.root.winfo_screenheight()/2)-20)
        exit_label = self.tk.Label(self.canvas,text='Exit', font=('Arial',20), fg='white',bg='black')
        exit_label.place(x = (2*self.root.winfo_screenwidth()/3)-20, y = (self.root.winfo_screenheight()/2)-20)
        label_esc = self.tk.Label(self.canvas,text=' press esc to leave', font=('Arial',12), fg='white',bg='black')
        label_esc.place(x = 0,y = self.root.winfo_screenheight() - 20)
        start_label.bind('<Button-1>',self.on_click_start) # When the start label is clicked, on_click_start runs and the game starts
        exit_label.bind('<Button-1>',self.on_click_exit) # When the exit label is clicked, on_click_exit runs and the game ends

        self.root.bind('<Escape>',self.esc_exit) # When escape key is pressed, the player leaves the game

