#This class is used to display the amount of seconds you choose to play the game for.

import Square
class Pick():
    def __init__(self,tk,root):
        self.tk = tk
        self.root = root
        self.canvas = None
        self.seconds = None

    def check_type(self,value,type):
        try:
            type(value)
            return True
        except:
            return False

    def on_enter_seconds(self,event,enter_sec):
            self.seconds =  enter_sec.get()
            if self.check_type(self.seconds,float):
                self.root.unbind('<Escape>')
                enter_sec.config(state='disabled')
                self.canvas.destroy()
                game_screen = Square.Square(self.tk,self.root,self.seconds)
                game_screen.game_screen()
            else:
                 try_again = self.tk.Label(self.canvas,text='Please put in a number', font=('Arial',20), fg='black')
                 try_again.place(x = (self.root.winfo_screenwidth()/2)-150, y = (self.root.winfo_screenheight()/4))
            
    def esc_exit(self,event):
        self.root.destroy()

    def pick_screen(self):
        self.canvas = self.tk.Canvas(self.root)
        self.canvas.pack(fill=self.tk.BOTH, expand=True)
        time_label = self.tk.Label(self.canvas,text='How many seconds would you like to play?', font=('Arial',20), fg='black')
        time_label.place(x = (self.root.winfo_screenwidth()/2)-250, y = (self.root.winfo_screenheight()/3))
        enter_sec = self.tk.Entry(self.canvas,font=('Arial',20))
        enter_sec.place(x = (self.root.winfo_screenwidth()/2)-150, y = (self.root.winfo_screenheight()/2))
        label_esc = self.tk.Label(self.canvas,text=' press esc to leave', font=('Arial',12), fg='white',bg='black')
        label_esc.place(x = 0,y = self.root.winfo_screenheight() - 20)
        enter_sec.bind('<Return>',lambda event:self.on_enter_seconds(event,enter_sec))

        self.root.bind('<Escape>',self.esc_exit)
