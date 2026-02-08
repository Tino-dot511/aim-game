import time
import random as ran
class Square():
    def __init__(self,tk,root,time):
        self.tk = tk
        self.root = root
        self.tim = time
        self.canvas = None
        self.stopwatch_start = None
        self.dict = {}
        self.lst = []
        self.hits = []
        self.shots = []
    
    def hits_or_not(self,x,y):
        dict_copy = self.dict.copy()
        for key,items in dict_copy.items():
            if (x >= items[0] and x <= items[0]+50) and (y >= items[1] and y <= items[1]+50):
                self.lst.remove(items)
                self.canvas.delete(key)
                del self.dict[key]
                self.check_coordinates()
                rect = self.canvas.create_rectangle(self.lst[-1][0],self.lst[-1][1],self.lst[-1][0]+50,self.lst[-1][1]+50,fill='red')
                self.dict[rect] = self.lst[-1]
                self.hits.append(1)

    def stop_watch(self):
        accuracy = 0
        stopwatch_end = time.time()
        time_gone = stopwatch_end-self.stopwatch_start
        if time_gone >= float(self.tim):
            self.canvas.delete('all')
            self.canvas.unbind('<Button-1>')
            label_time_taken = self.tk.Label(self.canvas,text=f'Time Taken: {time_gone:.2f} seconds',font=('Arial',12), fg='black')
            label_shots = self.tk.Label(self.canvas, text=f'Shots: {len(self.shots)}', font=('Arial',12), fg='black')
            label_hits = self.tk.Label(self.canvas, text=f'Hits: {len(self.hits)}', font=('Arial',12), fg='black')
            label_fire_rate = self.tk.Label(self.canvas, text=f'Fire Rate : {(len(self.shots)/time_gone):.2f}', font=('Arial',12), fg='black')
            if len(self.shots) == 0:
                accuracy = 0
            else:
                accuracy = (len(self.hits)/len(self.shots))*100
            label_accuracy = self.tk.Label(self.canvas, text=f'Accuracy: {(accuracy):.2f}%', font=('Arial',12), fg='black')
            label_time_taken.pack()
            label_shots.pack()
            label_hits.pack()
            label_fire_rate.pack()
            label_accuracy.pack()
            return
        self.canvas.after(1,self.stop_watch)

    def on_click(self,event):
        self.hits_or_not(event.x,event.y)
        self.shots.append(1)

    def esc_exit(self,event):
        self.root.destroy()

    def check_area(self,x1,x2,y1,y2):
        flag = True
        if (x1 < x2+50 or x2 < x1+50 ) and (y1 < y2+50 or y2 < y1+50):
            flag = False
        return flag
    
    def check_coordinates(self):
        while True:
            valid = True
            new_x = ran.randint(self.root.winfo_x(),self.root.winfo_screenwidth()-50)
            new_y = ran.randint(self.root.winfo_y(),self.root.winfo_screenheight()-50)
            if len(self.lst) == 8:
                break
            if len(self.lst) == 0:
                self.lst.append([new_x,new_y])
                continue
            else:
                for i in range(len(self.lst)):
                    x2,y2 = self.lst[i][0],self.lst[i][1]
                    if len(self.lst) == 8:
                        return
                    if self.check_area(new_x,x2,new_y,y2):
                        valid = False
                if valid:
                    self.lst.append([new_x,new_y])

    def game_screen(self):
        self.check_coordinates()
        self.canvas = self.tk.Canvas(self.root)
        self.canvas.pack(fill=self.tk.BOTH, expand=True)
        for i in range(len(self.lst)):
            rect = self.canvas.create_rectangle(self.lst[i][0],self.lst[i][1],self.lst[i][0]+50,self.lst[i][1]+50,fill='red')
            self.dict[rect] = self.lst[i]
        label_esc = self.tk.Label(self.canvas,text=' press esc to leave', font=('Arial',12), fg='white',bg='black')
        label_esc.place(x = 0,y = self.root.winfo_screenheight() - 20)
        self.stopwatch_start = time.time()
        self.canvas.bind('<Button-1>',self.on_click)
        self.root.bind('<Escape>',self.esc_exit)
        self.stop_watch()
        