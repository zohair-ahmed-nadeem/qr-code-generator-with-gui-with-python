from tkinter import *
import qrcode


def get_link():
    data =userinput.get()
  
    file_name=userfilename.get()
  
    qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name+".png")


root=Tk()

root.title("My QRCode Generator")
root.geometry("400x500")
root.minsize(400,500)
root.maxsize(400,500)

header=Label(text="QRCode Generator",font="Arial 20 bold",background="gray",pady=5)
header.pack(fill=X)

link_text=Label(text="Enter link or word or number")
link_text.pack(anchor="nw")

user_input=StringVar()
userinput=Entry(textvariable=user_input)
userinput.pack()

filename=Label(text="Enter file name")
filename.pack(anchor="nw")

user_file_name=StringVar()
userfilename=Entry(textvariable=user_file_name)
userfilename.pack()

Button(text="enter",command=get_link).pack()

root.mainloop()
