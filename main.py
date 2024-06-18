import tkinter as tk
from tkinter import filedialog
from tkinter.font import Font


window = tk.Tk()

def open_doc():
    file_path = filedialog.askopenfilename(filetypes=(('Text files', '.txt'),))
    if file_path:
        with open(file_path, 'r') as file:
            ent_text.delete(1.0, tk.END)
            ent_text.insert(index=1.0, chars=file.read())

def save_doc():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    if file_path:
        with open(file_path, 'w') as file:
            file.write(ent_text.get(1.0, tk.END))

def font_down():
    fontSize = ent_text['font']
    fontSize = fontSize.split(' ')[1]
    ent_text['font'] = f'Ariel {int(fontSize) -1}'

    lbl_fontSize['text'] = int(fontSize) - 1

def font_up():
    fontSize = ent_text['font']
    fontSize = fontSize.split(' ')[1]
    ent_text['font'] = f'Ariel {int(fontSize) + 1}'

    lbl_fontSize['text'] = int(fontSize) + 1


window.geometry('1200x1200')
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.title('Text Editor')




# ---- Button frame ----
frm_btn = tk.Frame(master=window, borderwidth=1, relief='sunken')
frm_btn.grid(row=0, column=0, sticky='nsew')
frm_btn.columnconfigure(0, weight=1)

btn_open = tk.Button(master=frm_btn, text='Open', width=10, command=open_doc)
btn_open.grid(row=0, column=0, pady=(20, 10))

btn_save = tk.Button(master=frm_btn, text='Save As', width=10, command=save_doc)
btn_save.grid(row=1, column=0)

# ---- text editor frame ----
frm_textBoxes = tk.Frame(master=window, bg='blue')
frm_textBoxes.grid(row=0, column=1, sticky='nsew')
frm_textBoxes.rowconfigure(1, weight=1)
frm_textBoxes.columnconfigure(0, weight=1)



# ----- font editor frame ------
frm_fontEdit = tk.Frame(master=frm_textBoxes)
frm_fontEdit.grid(row=0, column=0, sticky='nsew')

btn_fontDown = tk.Button(master=frm_fontEdit, text='-A', command=font_down)
btn_fontDown.grid(row=0, column=0)
btn_fontDown.config(font=('', 8))

btn_fontUp = tk.Button(master=frm_fontEdit, text='+A', command=font_up)
btn_fontUp.grid(row=0, column=2)
btn_fontUp.config(font=('', 12))

lbl_fontSize = tk.Label(master=frm_fontEdit, text='22')
lbl_fontSize.grid(row=0, column=1)

# ---- entry -------
ent_text = tk.Text(master=frm_textBoxes, font=('Ariel', 22))
ent_text.grid(row=1, column=0, sticky='nsew')



window.mainloop()