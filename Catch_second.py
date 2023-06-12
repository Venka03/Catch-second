import random
import tkinter as tk
from datetime import datetime
from time import sleep


class MyGame:
    MIN_TIME = 9
    MAX_TIME = 15

    def __init__(self):
        self.counter = -1
        self.running = False
        self.t = 0

        self._create_root()
        self.root.mainloop()
    
    def _create_buttons(self):
        """
        create buttons used for game and define their actions
        """
        self.start = tk.Button(self.f, text="Start", width=6, command=self._start)
        self.stop = tk.Button(self.f, text="Stop", width=6, state="disabled", command=self._stop)
        self.reset = tk.Button(self.f, text="Repeat", width=6, state="disabled", command=self._reset)

        self.start.pack(side="left")
        self.stop.pack(side="left")
        self.reset.pack(side="left")

    def _create_root(self):
        """
        create root window with fixed size with label and button needed for game
        """
        self.root = tk.Tk()
        self.root.configure(bg="#ececec")
        self.root.title("My Game - Catch a second")
        self.root.eval("tk::PlaceWindow . center")
        self.root.minsize(width=300, height=75)
        self.root.resizable(width=False, height=False)

        self.label = tk.Label(self.root, text="Welcome!", bg="#ececec", fg="black", font="Verdana 30 bold")
        self.label.pack()

        self.f = tk.Frame(self.root)
        self.f.pack(anchor="center", pady=5)
        self._create_buttons()
        self.root.mainloop()
    
    def _start(self):
        """
        starts the game by starting counting
        """
        self.running = True
        self._rand_t()
        self.start["state"] = "disabled"
        self.stop["state"] = "normal"
        self.reset["state"] = "normal"
        self._count()

    def _stop(self):
        """
        stop the counting and inform about win or lose
        """
        self.start["state"] = "disabled"
        self.stop["state"] = "disabled"
        self.reset["state"] = "normal"
        self.running = False
        self.label["fg"] = "black"
        if self.counter == self.t + 1:
            self.label["text"] = "You won)"
        else:
            self.label["text"] = "You lost("

    def _reset(self):
        """
        restart the game on click of button
        if game finished, start it again
        if not, generate random second which should be caught and start counting from beginning
        """
        self.counter = -1
        if not self.running:
            self.start["state"] = 'normal'
            self.reset["state"] = 'disabled'
            self.label['text'] = 'Welcome!'
        else:
            self._rand_t()
            self.label["fg"] = "black"
            self.label['text'] = 'Beginning...'

    def _rand_t(self):
        """
        generate random number representing second which should be caught
        """
        self.t = random.randint(self.MIN_TIME, self.MAX_TIME)

    def _count(self):
        """
        explain when user should press stop button and count until 4 and text disappear 
        recall itself each second
        """
        if self.running:
            if self.counter == -1:
                display = f"Stop at {self.t}"
            elif self.counter == 0:
                display = "Ready..."
            else:
                tt = datetime.fromtimestamp(self.counter)
                display = tt.strftime("%S")

            if self.counter == 5:
                self.label["fg"] = "#ececec"
            
            self.label["text"] = display
            self.counter += 1
            self.label.after(1000, self._count)
try:    
    a = MyGame()
except BaseException as e:
    print(e)
