import tkinter as tk
from tkinter import ttk
import voiceScript
import multiprocessing
import threading



voice = voiceScript.VoiceActivated()
voiceThread = threading.Thread(target=voice.run)
voiceThread.start()




window = tk.Tk()
window.geometry("200x300")
window.title("Calculator")

NumFrame=tk.Frame(window)
NumFrame.pack()


def button_click(number):
  if number == 'C':
    Screen.config(text="")
  else:
    current_text = Screen.cget("text")
    new_text = current_text + str(number)
    Screen.config(text=new_text)


def calculate():
  Screen.config(text=str(eval(Screen.cget("text"))))


Screen = tk.Label(NumFrame, text="0", width=17, height=2)
Screen.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

button1 = tk.Button(NumFrame, text="1", width=1, height=1, command=lambda: button_click(1))
button1.grid(row=1, column=0, padx=1, pady=1)

button2 = tk.Button(NumFrame,text="2", width=1, height=1, command=lambda: button_click(2) )
button2.grid(row=1, column=1, padx=1, pady=1)

button3 = tk.Button(NumFrame,text="3", width=1, height=1, command=lambda: button_click(3))
button3.grid(row=1, column=2, padx=1, pady=1)

button4 = tk.Button(NumFrame,text="4", width=1, height=1, command=lambda: button_click(4) )
button4.grid(row=2, column=0, padx=1, pady=1)

button5 = tk.Button(NumFrame,text="5", width=1, height=1, command=lambda: button_click(5) )
button5.grid(row=2, column=1, padx=1, pady=1)

button6 = tk.Button(NumFrame,text="6", width=1, height=1, command=lambda: button_click(6) )
button6.grid(row=2, column=2, padx=1, pady=1)

button7 = tk.Button(NumFrame,text="7", width=1, height=1, command=lambda: button_click(7) )
button7.grid(row=3, column=0, padx=1, pady=1)

button8 = tk.Button(NumFrame,text="8", width=1, height=1, command=lambda: button_click(8) )
button8.grid(row=3, column=1, padx=1, pady=1)

button9 = tk.Button(NumFrame,text="9", width=1, height=1, command=lambda: button_click(9) )
button9.grid(row=3, column=2, padx=1, pady=1)

button0 = tk.Button(NumFrame,text="0", width=1, height=1, command=lambda: button_click(0) )
button0.grid(row=4, column=1, padx=1, pady=1)

button_add = tk.Button(NumFrame,text="+", width=1, height=1, command=lambda: button_click('+'))
button_add.grid(row=1, column=3, padx=1, pady=1)
button_min = tk.Button(NumFrame,text="-", width=1, height=1, command=lambda: button_click('-'))
button_min.grid(row=2, column=3, padx=1, pady=1)
button_mul = tk.Button(NumFrame,text="*", width=1, height=1, command=lambda: button_click('*'))
button_mul.grid(row=3, column=3, padx=1, pady=1)
button_div = tk.Button(NumFrame,text="/", width=1, height=1, command=lambda: button_click('/'))
button_div.grid(row=4, column=2, padx=1, pady=1)

button_equal = tk.Button(NumFrame,text="=", width=1, height=1, command=lambda: calculate())
button_equal.grid(row=4, column=3, padx=1, pady=1)
button_clear = tk.Button(NumFrame,text="C", width=1, height=1, command=lambda: button_click('C'))
button_clear.grid(row=0, column=3, padx=1, pady=1)
button_dec = tk.Button(NumFrame,text=".", width=1, height=1, command=lambda: button_click('.'))
button_dec.grid(row=4, column=0, padx=1, pady=1)


now = 0
def check_modify():
  global now
  global voice
  while True:
    if voice.getAnswer() != now:
      Screen.config(text=voice.getAnswer())
      now = voice.getAnswer()

checkThread = threading.Thread(target=check_modify)
checkThread.start()

window.mainloop()
