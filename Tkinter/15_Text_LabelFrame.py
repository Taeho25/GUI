import tkinter

# 윈도우 창 생성 / 설정
window = tkinter.Tk()
window.title("GUI")
window.geometry("640x500+100+100")
window.resizable(True, True)

# 텍스트 설정
text = tkinter.Text(window)

text.insert(tkinter.CURRENT, "안녕하세요.\n")
text.insert("current", "반습니다.")
text.insert(2.1, "갑")

text.pack()

text.tag_add("강조", "1.0", "1.6")
text.tag_config("강조", background="yellow") 
text.tag_remove("강조", "1.1", "1.2")

# 라벨 프레임 설정
def check():
    label.config(text=RadioVariety_1.get())
    
labelframe = tkinter.LabelFrame(window, text="플랫폼 선택")
labelframe.pack()

RadioVariety_1 = tkinter.StringVar()
RadioVariety_1.set("미선택")

radio1 = tkinter.Radiobutton(labelframe, text="Python", value="가능", variable=RadioVariety_1, command=check)
radio1.pack()
radio2 = tkinter.Radiobutton(labelframe, text="C/C++", value="부분 가능", variable=RadioVariety_1, command=check)
radio2.pack()
radio3 = tkinter.Radiobutton(labelframe, text="JSON", value="불가능", variable=RadioVariety_1, command=check)
radio3.pack()
label = tkinter.Label(labelframe, text="None")
label.pack()

window.mainloop()