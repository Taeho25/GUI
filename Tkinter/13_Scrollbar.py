import tkinter

# 윈도우 창 생성 / 설정
window = tkinter.Tk()
window.title("GUI")
window.geometry("640x400+100+100")
window.resizable(True, True)

# 프레임 설정
frame = tkinter.Frame(window)

# 스크롤 바 설정
scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# 리스트박스 설정
listbox = tkinter.Listbox(frame, yscrollcommand = scrollbar.set)
for line in range(1,1001):
   listbox.insert(line, str(line) + "/1000")
listbox.pack(side="left")

scrollbar["command"] = listbox.yview

frame.pack()

window.mainloop()