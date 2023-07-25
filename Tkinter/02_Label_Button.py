import tkinter

# 윈도우 창 생성
window = tkinter.Tk()

# 기본 설정
window.title("Tkinter test for GUI")   # 창 제목
window.geometry("640x400+100+100")   # 너비 x 높이 + 창x좌표 + 창y좌표
window.resizable(True, True)   # 상하, 좌우

# 위젯 설정
#label = tkinter.Label(window, text="Tkinter TEST", width=30, height=5, padx=0, fg="green", bg="yellow", relief="groove")
label = tkinter.Label(window, text="버튼클릭횟수: 0")
label.pack()  # 위젯 배치

# 버튼 설정
count = 0

def countUP():
    global count
    count +=1
    label.config(text="버튼클릭횟수: "+str(count))

button = tkinter.Button(window, overrelief="solid", width=15, height=10, bd=3, text="버튼", bg="yellow", fg="red", relief="solid", command=countUP, repeatdelay=1000, repeatinterval=100)
button.pack()

# 실행
window.mainloop()