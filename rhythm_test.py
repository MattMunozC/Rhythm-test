from pickle import FALSE
import winsound
import tkinter
from pynput import keyboard
from pynput.keyboard import Key
import threading
from threading import Thread
import ctypes
import sys
import time
from tkinter import messagebox
class aSyncSFX(Thread):
    def __init__(self):
        super().__init__()
        self.button_pressed_flag=None
        self.time=0
    def run(self):
        if (self.button_pressed_flag==True):
            self.time=0
        self.time=time.time()
        self.button_pressed_flag=False
        winsound.PlaySound("sfx\\tambourine.wav", winsound.SND_FILENAME)
#   Consigue la id del Thread, Funcion encontrada en StackOverFlow Sorry
    def get_id(self):
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id   
#   Detiene el Thread no me pregunten como chucha yo la utilice solamente
    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
class aSyncKey(Thread):
    def __init__(self):
        super().__init__()
class mainwindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.soundThread=aSyncSFX()
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        self.download_button=tkinter.Button(self,text="play",width=8,height=2,bg="#424242",fg="#ffffff",command=self.button)
        self.download_button.place(x=180,y=75)

        tkinter.Label(self, text="Presione espacio cuando escuche el tamborin",fg="#000000").place(x=80,y=20)
        self.title(sys.argv[0][:-3:])
        self.geometry("400x200")
        self.resizable(False, False)
    def button(self):
        self.soundThread=aSyncSFX()
        self.soundThread.start()
    def on_press(self,key):
        if key==Key.space and self.soundThread.button_pressed_flag==False:
            total_time=time.time()-self.soundThread.time
            print(total_time)
            self.soundThread.button_pressed_flag=True
            self.soundThread.raise_exception()
            messagebox.showinfo(message="your reaction time is {0}".format(str(total_time)[:6:]), title="rhythm test")

if __name__=="__main__":
    window=mainwindow()
    window.mainloop()


