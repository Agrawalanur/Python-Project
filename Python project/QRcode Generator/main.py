from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class QRcode_Generator:
    def __init__(self,root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QRcode Generator")
        self.root.resizable(False,False)
        self.link_details=StringVar()
        title=Label(self.root,text="QR Code Generator",font=("Times New Roman",40),bg="blue",background="pink").place(x=0,y=0,relwidth=1)
        '''QR code frame'''
        qr_Frame = Frame(self.root,bd=3,relief=RIDGE,bg="White")
        qr_Frame.place(x=100,y=80,width=700,height=400)
        qr_title=Label(qr_Frame,text="QR Code Deatils",font=("Times New Roman",20),bg="blue",background="pink").place(x=0,y=0,relwidth=1)
        qr_link=Label(qr_Frame,text="Link Deatils",font=("Times New Roman",15,'bold'),bg="White").place(x=50,y=60)
        qr_txt=Entry(qr_Frame,font=("Times New Roman",15),textvariable=self.link_details,bg="lightyellow").place(x=200,y=60,width=180,height=20)
        qr_but=Button(qr_Frame,text="QR genrator",command=self.genrate,font=("times new roman",15),bg='white').place(x=30,y=250,width=150,height=20)
        clear_but=Button(qr_Frame,text="Clear",command=self.clear,font=("times new roman",15),bg='white').place(x=250,y=250,width=120,height=20)
        self.msg=''
        self.lbl_msg=Label(qr_Frame,text=self.msg,font=("times new roman",15),bg='white',fg="green")
        self.lbl_msg.place(x=0,y=300,relwidth=1)
        self.qrcode=Label(qr_Frame,text="Qr code Not\navaible",font=("time new roman",15),bg="blue",fg="white",bd=1)
        self.qrcode.place(x=450,y=70,width=200,height=200)

    def clear(self):
        self.link_details.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qrcode.config(image='')
    def genrate(self):
        if self.link_details.get() =='':
            self.msg="Please provide a Link"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Link details: {self.link_details.get()}")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[190,190])
            #print(qr_code)
            qr_code.save("QR code/Emp_"+str(self.link_details.get())+'.png')
            self.img=ImageTk.PhotoImage(file="QR code/Emp_"+str(self.link_details.get())+'.png')
            self.qrcode.config(image=self.img)
            self.msg="QR genrated Succusfully"
            self.lbl_msg.config(text=self.msg,fg='green')
                     
root = Tk()
obj = QRcode_Generator(root)
root.mainloop()