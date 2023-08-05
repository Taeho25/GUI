import tkinter

# 윈도우 창 생성 / 기본 설정
window = tkinter.Tk()
window.title("GUI")
window.geometry("640x480+100+100")
window.resizable(False, False)


# 체크박스 설정
def flash():
    checkbutton3.flash()

CheckVariety_1 = tkinter.IntVar()
CheckVariety_2 = tkinter.IntVar()
CheckVariety_3 = tkinter.IntVar()

checkbutton1 = tkinter.Checkbutton(window, text="Car", variable=CheckVariety_1, activebackground="blue")
checkbutton2 = tkinter.Checkbutton(window, text="Bus", variable=CheckVariety_2)
checkbutton3 = tkinter.Checkbutton(window, text="Texi", variable=CheckVariety_3, activebackground="red", command=flash)

checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()


# 라디오박스 설정
def check():
    label2.config(text="수용가능 인원 = " + str(RadioVariety_t1.get() + RadioVariety_t2.get() + RadioVariety_t3.get()) + "\n" +
                       "탑승 인원 = " + str(RadioVariety_g1.get() + RadioVariety_g2.get()) + "\n")

RadioVariety_t1=tkinter.IntVar()
RadioVariety_t2=tkinter.IntVar()
RadioVariety_t3=tkinter.IntVar()
RadioVariety_g1=tkinter.IntVar()
RadioVariety_g2=tkinter.IntVar()

label1 = tkinter.Label(window, text="\n자동차, 버스, 택시", height=5)

radio1=tkinter.Radiobutton(window, text="1번 Car : 최대 5명", value=5, variable=RadioVariety_t1, command=check)
radio2=tkinter.Radiobutton(window, text="2번 Bus : 최대 45명", value=45, variable=RadioVariety_t2, command=check)
radio3=tkinter.Radiobutton(window, text="3번 Texi : 최대 4명", value=4, variable=RadioVariety_t3, command=check)

label2=tkinter.Label(window, text="None", height=5)

radio4=tkinter.Radiobutton(window, text="1반 인원 : 10명", value=10, variable=RadioVariety_g1, command=check)
radio5=tkinter.Radiobutton(window, text="2반 인원 : 23명", value=23, variable=RadioVariety_g2, command=check)

label1.pack()
radio1.pack()
radio2.pack()
radio3.pack()
label2.pack()
radio4.pack()
radio5.pack()


window.mainloop()