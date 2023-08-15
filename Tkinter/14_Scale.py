import tkinter

# 윈도우 창 생성 / 설정
window = tkinter.Tk()
window.title("GUI")
window.geometry("640x400+100+100")
window.resizable(True, True)

# 스케일 설정
def select(self):
    value="값 : "+str(scale.get())
    label.config(text=value)

var = tkinter.IntVar()

scale = tkinter.Scale(window, variable=var, command=select, orient="horizontal", showvalue=False, tickinterval=50, to=500, length=300)
scale.pack()

label = tkinter.Label(window, text="값 : 0")
label.pack()

window.mainloop()