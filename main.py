import qrcode
import tkinter as QRcodeGenrator


root=QRcodeGenrator.Tk()
root.title("AJAY-BANIYAL")




canvas1 =QRcodeGenrator.Canvas(root, width = 400, height = 300,  relief = 'raised' , background="black")
canvas1.pack()

label1 = QRcodeGenrator.Label(root, text='Generate QRCode ',foreground="white", background="black",font=('helvetica',20))
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = QRcodeGenrator.Label(root, text='Enter URL:',foreground="white", background="black",font=('helvetica', 20))
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = QRcodeGenrator.Entry (root)
canvas1.create_window(200, 140, window=entry1)

def getQR ():

    x1 = entry1.get()

    label3 = QRcodeGenrator.Label(root, text= 'The QR CODE for ' + x1 + ' is:',font=('helvetica', 10),foreground="white", background="black")
    canvas1.create_window(200, 210, window=label3)


    img = qrcode.make(x1)

    label4 = QRcodeGenrator.Label(root, text= img,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)
    save=img.save('images/output.png')
    savedimg=img.show('images/output.png')
    label5=QRcodeGenrator.Label(root,image=savedimg)


button1 = QRcodeGenrator.Button(text='click here to generate QRcode', command=getQR, bg='Green', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)



root.mainloop()
