from tkinter.filedialog import *
import tkinter as tkt

window = tkt.Tk()
window.title('Notepad')
window.geometry('400x400+800+300')
window.resizable(0,0)

window.iconbitmap("C:\\Users\\choij\\Documents\\카카오톡 받은 파일\\memo.ico")
# photo = tkt.PhotoImage(file="C:\\Users\\choij\\Documents\\카카오톡 받은 파일\\해달 로고.png")
# window.iconphoto(False, photo)

text_area = tkt.Text(window)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky= tkt.N + tkt.E + tkt.S + tkt.W)

def new_file():
    text_area.delete(1.0, tkt.END)
def save_file():
    f = asksaveasfile(mode='w', defaultextension='.txt', filetypes=[('Text files', '.txt')])
    text_save = str(text_area.get(1.0, tkt.END))
    f.write(text_save)
    f.close()
def maker():
    help_view = tkt.Toplevel(window)
    help_view.geometry('300x50+850+400')
    help_view.title('만든이')
    lb = tkt.Label(help_view, text='\n최진호')
    lb.pack()

#메뉴 생성
menuMaker = tkt.Menu(window)
#첫번째 메뉴 만들기
first_menu = tkt.Menu(menuMaker, tearoff=0)
#첫번째 메뉴의 세부메뉴 추가 및 함수 연결
first_menu.add_command(label = '새 파일', command = new_file)
first_menu.add_command(label = '저장', command = save_file)
#메뉴 바 추가
menuMaker.add_cascade(label='파일', menu=first_menu)

window.config(menu = menuMaker)

first_menu.add_separator()
first_menu.add_command(label = '종료', command=window.destroy)
#메뉴 구성

# ㅠㅠ gpt ㅠㅠ

#두번째 메뉴 추가 
second_menu = tkt.Menu(menuMaker, tearoff=0)
#세부 메뉴 추가, 함수 연결
second_menu.add_command(label = '만든 이', command = maker)
#메뉴 바 추가
menuMaker.add_cascade(label='정보', menu = second_menu)

window.mainloop() # 창 실행!

# 새 파일 누르면 내용 지우기
# 저장되게 만들기
# 만든이 누르면 이름 뜨기