import tkinter
from math import *

# 기본 설정
window = tkinter.Tk()
window.title("GUI")
window.geometry("640x400+100+100")
window.resizable(True, True)

# 위젯 1 : 가이드
label_head = tkinter.Label(window, text="계산식 작성 후 엔터 입력")
label_head.pack()  # 위젯 배치

# 위젯 2 : 수식 입력
def calc(event):
    label.config(text="결과 = "+str(eval(entry.get())))
entry=tkinter.Entry(window)
entry.bind("<Return>", calc)
entry.pack()

# 위젯 3 : 결과 출력
label=tkinter.Label(window)
label.pack()

window.mainloop()