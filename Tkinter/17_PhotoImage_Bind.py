import tkinter
import tkinter.font

# 윈도우 창 생성 / 설정
window = tkinter.Tk()
window.title("GUI")
window.geometry("640x700+100+100")
window.resizable(True, True)

# 이미지 설정
image = tkinter.PhotoImage(file=".\data\g80.png")

label = tkinter.Label(window, image=image)
label.pack()

# 이벤트 실행
width = 1

def drawing(event):
    if width>0:
        x1 = event.x - 1
        y1 = event.y - 1
        x2 = event.x + 1
        y2 = event.y + 1
        canvas.create_oval(x1, y1, x2, y2, fill="blue", width=width)

def scroll(event):
    global width
    if event.delta == 120:
        width += 1
    if event.delta == -120:
        width -= 1
    label.config(text="붓 굵기: "+str(width))

canvas = tkinter.Canvas(window, relief="solid", bd=2)
canvas.pack(expand=True, fill="both")
canvas.bind("<B1-Motion>", drawing)
canvas.bind("<MouseWheel>", scroll)

label = tkinter.Label(window, text="붓 굵기: "+str(width))
label.pack()

window.mainloop()