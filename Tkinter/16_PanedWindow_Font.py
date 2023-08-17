import tkinter
import tkinter.font

# 윈도우 창 생성 / 설정
window = tkinter.Tk()
window.title("GUI")
window.geometry("640x500+100+100")
window.resizable(True, True)

# 내부윈도우 설정
panedwindow1 = tkinter.PanedWindow(relief="raised", bd=2)
panedwindow1.pack(expand=True)
 
left = tkinter.Label(panedwindow1, text="내부윈도우-1 (좌측)")
panedwindow1.add(left)

panedwindow2 = tkinter.PanedWindow(panedwindow1, orient="vertical", relief="groove", bd=3)
panedwindow1.add(panedwindow2)

right = tkinter.Label(panedwindow1, text="내부윈도우-2 (우측)")
panedwindow1.add(right)

top = tkinter.Label(panedwindow2, text="내부윈도우-3 (상단)")
panedwindow2.add(top)

bottom = tkinter.Label(panedwindow2, text="내부윈도우-4 (하단)")
panedwindow2.add(bottom)

# 폰트 설정
font = tkinter.font.Font(family="맑은 고딕", size=20, slant="italic")

label = tkinter.Label(window, text="파이썬 3.6", font=font)
label.pack()

window.mainloop()