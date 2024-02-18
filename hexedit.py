from tkinter import *
from tkinter import ttk
import ctypes
from tkinter import filedialog as fd


#print(help(Text()))
x = Tk()

width= x.winfo_screenwidth()

height= x.winfo_screenheight()
text = Text(x, width=90, height=95/3.2)
text_bg_color = '#f0f0f0'  # Light gray background
text_fg_color = 'black'

text.config(font=('Courier', 14,"italic"),bg=text_bg_color, fg=text_fg_color)
text.place(x=155, y=42)
x.geometry("%dx%d"%(width,height))
x.title("hex editor")
file_path = ''


def select_files():
    filetypes = (
        ('All files', '*.*'),
        #('All files', '*.*')
    )

    file_path = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)
    return str(file_path[0])


def openfile():
	my_library = ctypes.CDLL('./hexing.dll')
	my_library.hexing.argtypes = [ctypes.c_char_p]
	my_library.get_data.restype = ctypes.c_char_p
	my_library.hexing(select_files().encode())

	get_hex = my_library.get_data()
	
	get_hex_to_str = ctypes.string_at(get_hex).decode('utf-8')
	text.config(state=NORMAL)
	text.delete('1.0','end')

	text.insert(END,get_hex_to_str)

	text.config(state=DISABLED)

	#print(get_hex_to_str)
	#return get_hex_to_str






#---------------

#---------------
style = ttk.Style()
toolbar_frame = Frame(x, bg='#f0f0f0',relief=SOLID, bd=1)
toolbar_frame.pack(side=TOP, fill=X)
#---------------
photo = PhotoImage(file = "open.png")
resimage = photo.subsample(2 ,2)  # Resize by a factor of 2 in both dimensions
#---------------
style = ttk.Style()
style.configure("My.TButton",foreground="#f0f0f0",background="#f0f0f0",width=0, height=0)
#---------------


#---------------
button1 = ttk.Button(toolbar_frame, text="",compound=LEFT,style="My.TButton",image = resimage,command=openfile)
button1.pack(side=LEFT,padx=5)

#button2 = ttk.Button(toolbar_frame, text="",compound=LEFT,style="My.TButton",image = resimage)
#button2.pack(side=LEFT,padx=12)
#---------------




	


text.config(state=DISABLED)


x.mainloop()
