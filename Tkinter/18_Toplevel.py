import tkinter

# 윈도우 창 생성 / 설정
window = tkinter.Tk()
window.title("GUI")
window.geometry("640x700+100+100")
window.resizable(True, True)

# 메뉴바 설정
menubar = tkinter.Menu(window)

menu_1 = tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label="하위 메뉴 1-1")
menu_1.add_command(label="하위 메뉴 1-2")
menu_1.add_separator()
menu_1.add_command(label="하위 메뉴 1-3")
menubar.add_cascade(label="상위 메뉴 1", menu=menu_1)

# 외부윈도우 설정
toplevel = tkinter.Toplevel(window, menu=menubar)
toplevel.geometry("320x200+820+100")

label = tkinter.Label(toplevel, text="GUI2")
label.pack()

window.mainloop()
