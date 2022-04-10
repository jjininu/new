from tkinter import *

class function:
    f = 0
    g = 0
    def __init__(self,num,entry,label):

        self.entry = entry
        self.label = label
        self.num = num


    def func1(self) :






        if self.label['text'] !='':
            self.entry.insert("end", str(self.num))
            function.f = self.entry


            self.entry.delete(0, last='end')




        else :
            self.entry.insert("end", str(self.num))
            function.g = int(self.entry.get())


