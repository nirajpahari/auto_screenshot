import tkinter as tk
import pyautogui
import datetime
import os

class TimerApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.pack()

        self.label = tk.Label(self, text="", width=10)
        self.label.pack()

        self.button1 = tk.Button(text="Capture", command=self.take_screenshot, bg='blue', fg='gray', font=10)
        self.canvas.create_window(150, 150, window=self.button1)

        
        self.remaining = 0
        self.countdown(900)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="Taking Screenshot")
            self.take_screenshot()
            self.remaining = remaining
            self.after(1000, self.countdown(900))
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

    def take_screenshot(self):
        my_ss = pyautogui.screenshot()
        # For windows
        # dir_path = "C:\\Users\\niraj\\Desktop\\ss\\"
        # For linux
        dir_path = "/home/niraj/Desktop/Screenshots_auto/"
        filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".png"
        file_path = os.path.join(dir_path, filename)
        my_ss.save(file_path)

if __name__ == "__main__":
    app = TimerApp()
    app.mainloop()