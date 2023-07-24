import tkinter

# 윈도우 창 생성
window = tkinter.Tk()

# 기본 설정
window.title("Tkinter test for GUI")   # 창 제목
window.geometry("640x400+100+100")   # 너비 x 높이 + 창x좌표 + 창y좌표
window.resizable(True, True)   # 상하, 좌우

# 위젯 설정
label = tkinter.Label(window, text="GUI를 만들기 위한 Tkinter 입니다.")
label.pack()   # 위젯 배치

# 실행
window.mainloop()