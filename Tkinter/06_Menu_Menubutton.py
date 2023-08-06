import tkinter

# 윈도우 창 생성 / 설정
window = tkinter.Tk()
window.title("GUI")
window.geometry("640x480+100+100")
window.resizable(True, True)


# 메뉴 생성 / 설정
### command 함수
def close():
    window.quit()
    window.destroy()

### 메뉴바
menubar = tkinter.Menu(window)

### 메뉴1 설정
menu_1 = tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label="하위 메뉴 1-1")
menu_1.add_command(label="하위 메뉴 1-2")
menu_1.add_separator()
menu_1.add_command(label="하위 메뉴 1-3(창닫기)", command=close)
menubar.add_cascade(label="상위 메뉴 1", menu=menu_1)

### 메뉴2 설정
menu_2 = tkinter.Menu(menubar, tearoff=0, selectcolor="red")
menu_2.add_radiobutton(label="하위 메뉴 2-1", state="disable")
menu_2.add_radiobutton(label="하위 메뉴 2-2")
menu_2.add_radiobutton(label="하위 메뉴 2-3")
menubar.add_cascade(label="상위 메뉴 2", menu=menu_2)

### 메뉴3 설정
menu_3 = tkinter.Menu(menubar, tearoff=0)
menu_3.add_checkbutton(label="하위 메뉴 3-1")
menu_3.add_checkbutton(label="하위 메뉴 3-2")
menubar.add_cascade(label="상위 메뉴 3", menu=menu_3)

window.config(menu=menubar)


# 메뉴 버튼 생성 / 설정
### 메뉴 버튼 생성
menubutton = tkinter.Menubutton(window,text="메뉴 버튼", relief="raised", direction="right")
menubutton.pack()

### 메뉴 버튼 속 메뉴 설정
menu_in_button = tkinter.Menu(menubutton, tearoff=0)
menu_in_button.add_command(label="하위메뉴-1")
menu_in_button.add_separator()
menu_in_button.add_command(label="하위메뉴-2")
menu_in_button.add_command(label="하위메뉴-3")

menubutton["menu"] = menu_in_button

window.mainloop()
 
print("Window Close")