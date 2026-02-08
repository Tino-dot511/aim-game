import Pick
class Start():
    def __init__(self,tk,root):
        self.tk = tk
        self.root = root
        self.canvas = None

    def on_click_start(self,event):
        self.root.unbind('<Escape>')
        self.canvas.destroy()
        new_screen = Pick.Pick(self.tk,self.root)
        new_screen.pick_screen()
        #run next function

    def on_click_exit(self,event):
        self.root.destroy()
    
    def esc_exit(self,event):
        self.root.destroy()

    def start_screen(self):
        self.canvas = self.tk.Canvas(self.root)
        self.canvas.pack(fill=self.tk.BOTH, expand=True)
        description = self.tk.Label(self.canvas,text='Aim game: Click as many targets in a time of \n  your choosing to test accuracy', font=('Arial',30), fg='black')
        description.place(x = (self.root.winfo_screenwidth()/3)-130, y = (self.root.winfo_screenheight()/3))
        start_label = self.tk.Label(self.canvas,text='Start', font=('Arial',20), fg='white',bg='black')
        start_label.place(x = (self.root.winfo_screenwidth()/3)-20, y = (self.root.winfo_screenheight()/2)-20)
        exit_label = self.tk.Label(self.canvas,text='Exit', font=('Arial',20), fg='white',bg='black')
        exit_label.place(x = (2*self.root.winfo_screenwidth()/3)-20, y = (self.root.winfo_screenheight()/2)-20)
        label_esc = self.tk.Label(self.canvas,text=' press esc to leave', font=('Arial',12), fg='white',bg='black')
        label_esc.place(x = 0,y = self.root.winfo_screenheight() - 20)
        start_label.bind('<Button-1>',self.on_click_start)
        exit_label.bind('<Button-1>',self.on_click_exit)
        self.root.bind('<Escape>',self.esc_exit)