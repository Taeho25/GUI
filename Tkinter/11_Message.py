import tkinter

# 윈도우 창 생성 / 설정
window = tkinter.Tk()
window.title("GUI")
window.geometry("640x400+100+100")
window.resizable(False, False)


# 메세지 설정
message = tkinter.Message(window, text="메세지입니다.", width=100, relief="solid")
message.pack()

window.mainloop()