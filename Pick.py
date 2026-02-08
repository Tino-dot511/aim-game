'''
This class is used to display an input screen to choose the amount of seconds
you play the game for, validate the input so that it can be used in the square class, as well as 
transitioning to the game aspect with the squares.
'''

import Square
class Pick():
    def __init__(self,tk,root):
        self.tk = tk # Argument that allows labels and canvas to be built
        self.root = root # Argument that allows the labels and canvas to appear on the screen
        self.canvas = None # Initializing value so it can be used throughout the class
        self.seconds = None

    def check_type(self,value,type):
        # Returns true or false to validate that the type of the unit entered can be converted.
        # Primarily used to avoid errors in the case that someone accidently inputs a letter instead of a number.
        try:
            type(value)
            return True
        except:
            return False

    def on_enter_seconds(self,event,enter_sec):
            # Gets the input entered by the player to check if it is a number to then be used as an argument in the square class.
            self.seconds =  enter_sec.get()
            if self.check_type(self.seconds,float):
                self.root.unbind('<Escape>') # Unbinds the escape key so it can't be used 
                enter_sec.config(state='disabled') # Disables the entry box so input can't be changed
                self.canvas.destroy()
                game_screen = Square.Square(self.tk,self.root,self.seconds) # Leads into the game
                game_screen.game_screen()
            else:
                # Displays a message to try again if the input by the player isn't a number
                 try_again = self.tk.Label(self.canvas,text='Please put in a number', font=('Arial',20), fg='black')
                 try_again.place(x = (self.root.winfo_screenwidth()/2)-150, y = (self.root.winfo_screenheight()/4))
            
    def esc_exit(self,event):
        self.root.destroy()

    def pick_screen(self):
        self.canvas = self.tk.Canvas(self.root) # Creates canvas to place label and input for choosing how long the player plays
        self.canvas.pack(fill=self.tk.BOTH, expand=True)
        time_label = self.tk.Label(self.canvas,text='How many seconds would you like to play?', font=('Arial',20), fg='black')
        time_label.place(x = (self.root.winfo_screenwidth()/2)-250, y = (self.root.winfo_screenheight()/3))
        enter_sec = self.tk.Entry(self.canvas,font=('Arial',20)) # The box used by the player to input an amount of seconds
        enter_sec.place(x = (self.root.winfo_screenwidth()/2)-150, y = (self.root.winfo_screenheight()/2))
        label_esc = self.tk.Label(self.canvas,text=' press esc to leave', font=('Arial',12), fg='white',bg='black')
        label_esc.place(x = 0,y = self.root.winfo_screenheight() - 20)
        enter_sec.bind('<Return>',lambda event:self.on_enter_seconds(event,enter_sec)) # When the enter key is pressed, it will access the on_enter_seconds function

        self.root.bind('<Escape>',self.esc_exit) # When escape key is pressed, the player leaves the game




