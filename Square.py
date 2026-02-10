'''
This class runs the actual game where the player clicks the square. This class deals 
with creating coordinates for the squares, and using overlapping logic, ensures the
squares don't overlap in game, then creates the squares and displays them for the game.
'''
import time
import random as ran
class Square():
    def __init__(self,tk,root,time):
        self.tk = tk # Argument that allows labels and canvas to be built
        self.root = root # Argument that allows the labels and canvas to appear on the screen
        self.tim = time # Argument that sets how long the game lasts
        self.canvas = None # Initializing value so it can be used throughout the class
        self.stopwatch_start = None # To start stopwatch
        self.num = 0 # Used to label a number for the squares
        self.lst = [] # List to save coordinates
        self.hits = [] # How many squares have been hit 
        self.shots = [] # How many shots/clicks the player has done
    
    def hits_or_not(self,x,y):
        # Checks if squares were hit
        list_copy = self.lst.copy()
        for i in range(len(list_copy)):
            if (x >= self.lst[i][1] and x <= self.lst[i][1]+50) and (y >= self.lst[i][2] and y <= self.lst[i][2]+50):
                # If a square is hit
                self.canvas.delete(self.lst[i][0]) # Canvas removes the square
                self.lst.remove(self.lst[i]) # List removes coordinates
                self.check_coordinates() # Checks new coordinate
                self.lst[-1][0] = self.canvas.create_rectangle(self.lst[-1][1],self.lst[-1][2],self.lst[-1][1]+50,self.lst[-1][2]+50,fill='red')
                list_copy[i] = self.lst[-1] # Copied list syncs with actual list
                self.hits.append(1)
                return # Returns after square is hit

    def stop_watch(self):
        # Checks time every millisecond to make sure that game time lasts for as long as the time chosen in previous class
        accuracy = 0
        stopwatch_end = time.time()
        time_gone = stopwatch_end-self.stopwatch_start # Checks the in-game time
        if time_gone >= float(self.tim): 
            self.canvas.delete('all') # The game stops and removes all squares
            self.canvas.unbind('<Button-1>') # Unbinds the left-click button so the click doesn't impact shots/clicks after the game has ended
            # Labels that display time of game, how many shots/clicks the player made, how many squares were hit, how fast they were clicking(fire rate), and accuracy.
            label_time_taken = self.tk.Label(self.canvas,text=f'Time Taken: {time_gone:.2f} seconds',font=('Arial',12), fg='black')
            label_shots = self.tk.Label(self.canvas, text=f'Shots: {len(self.shots)}', font=('Arial',12), fg='black')
            label_hits = self.tk.Label(self.canvas, text=f'Hits: {len(self.hits)}', font=('Arial',12), fg='black')
            label_fire_rate = self.tk.Label(self.canvas, text=f'Fire Rate : {(len(self.shots)/time_gone):.2f}', font=('Arial',12), fg='black')
            if len(self.shots) == 0:
                # If player didn't take shots/click, accuracy is zero
                # This avoids zero-division errors for accuracy calculations
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
        # When the player clicks, the function runs and shots/click adds to its list of shots/clicks done by the player
        self.hits_or_not(event.x,event.y)
        self.shots.append(1)

    def esc_exit(self,event):
        # Exits game if players presses escape key
        self.root.destroy()

    def check_area(self,x1,x2,y1,y2):
        # Checks that coordinates generated don't overlap 
        flag = True
        if x1 > x2+50 or x2 > x1+50 or y1 > y2+50 or y2 > y1+50:
            # If the start of x-axis of square 1 is less than the end of x-axis square 2, or vice versa
            # If the start of y-axis of square 1 is less than the end of y-axis square 2, or vice versa
            flag = False
        return flag

    def check_coordinates(self):
        # Generates coordinates and checks for overlapping coordinates
        while True:
            valid = True
            new_x = ran.randint(self.root.winfo_x(),self.root.winfo_screenwidth()-50)
            new_y = ran.randint(self.root.winfo_y(),self.root.winfo_screenheight()-50)
            # Generates random numbers so squares appear in unpredictable places
            key = f'rect{self.num}' # ID for each square
            if len(self.lst) == 8:
                # When the list reaches the max amount of squares for the game
                break
            if len(self.lst) == 0:
                # Appends the coordinates at beginning so there is no error for the for loop and because there is no overlap with one set of coordinates
                self.lst.append([key,new_x,new_y])
                self.num += 1
                continue
            else:
                for i in range(len(self.lst)):
                    # Loops through the list to check if coordinates overlap with previous coordinates in the list
                    x2,y2 = self.lst[i][1],self.lst[i][2]
                    if len(self.lst) == 8:
                        return
                    if self.check_area(new_x,x2,new_y,y2):
                        # If new coordinates overlap with any coordinate in the list, they aren't appended to the list
                        valid = False
                if valid:
                    self.lst.append([key,new_x,new_y])
                    self.num += 1
                else:
                    continue

    def game_screen(self):
        # The GUI for the game
        self.check_coordinates() # Generates and checks coordinates for the square
        self.canvas = self.tk.Canvas(self.root)
        self.canvas.pack(fill=self.tk.BOTH, expand=True)
        for i in range(len(self.lst)):         
            # Creates the square using the coordinates in the list and adds them to the dictionary of squares with their coordinates
            self.lst[i][0] = self.canvas.create_rectangle(self.lst[i][1],self.lst[i][2],self.lst[i][1]+50,self.lst[i][2]+50,fill='red')
        label_esc = self.tk.Label(self.canvas,text=' press esc to leave', font=('Arial',12), fg='white',bg='black')
        label_esc.place(x = 0,y = self.root.winfo_screenheight() - 20)
        self.stopwatch_start = time.time() # Starts the timer to check the how long the game is
        self.canvas.bind('<Button-1>',self.on_click) # If the left-click button is clicked, the on_click function will run
        self.root.bind('<Escape>',self.esc_exit) # When escape key is pressed, the player leaves the game
        self.stop_watch() # Runs the function in background to check how long the game goes

