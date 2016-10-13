"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

import tkinter as tk

class Application(tk.Frame):

    def __init__(self, root):
        super(Application, self).__init__(root)
        self.root = root
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello = tk.Button(self, text='Hello', command=self.say_hello)
        self.hello.pack(side='top')
        self.quit = tk.Button(self, text='Quit', command=self.root.destroy)
        self.quit.pack(side='bottom')

    def say_hello(self):
        print('Hello')
        

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
