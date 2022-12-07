from tkinter import *
import random
import os
from tkinter import filedialog
from resizeimage import resizeimage
from PIL import Image, ImageDraw, ImageFont, ImageTk


class Main:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1250x620+135+75')
        self.root.title('Created by Manish')

        title = Label(self.root, text="School Id card Generator", font=(
        "times new roman", 35, "bold"), padx=2, pady=2, bg="#000075", fg="white").place(x=0, y=0, relwidth=1)
    # All Variable=================================#
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_mb = StringVar()
        self.var_bg = StringVar()
        self.var_dob = StringVar()
        self.var_class = StringVar()
        self.var_blood = StringVar()
        self.var_gender = StringVar()
    # =========================================#

        detail_frm = Frame(self.root,  height=500, width=500,
                        bd=2, relief=GROOVE, bg="White")
        detail_frm.place(x=50, y=100)
        detail_lbl = Label(detail_frm, text="Student Details",  font=(
            "times new roman", 20, "bold"), bg="#000075", fg="White").place(x=0, y=0, relwidth=1)
    # Labels ==================#
        name_lbl = Label(detail_frm, text="Name", font=(
            "times new roman", 20), bg="white")
        name_lbl.place(x=20, y=50)

        class_lbl = Label(detail_frm, text="class", font=(
            "times new roman", 20), bg="white")
        class_lbl.place(x=20, y=100)

        dob_lbl = Label(detail_frm, text="DOB", font=(
            "times new roman", 20), bg="white")
        dob_lbl.place(x=300, y=100)

        blood_group_lbl = Label(detail_frm, text="blood group", font=(
            "times new roman", 20), bg="white")
        blood_group_lbl.place(x=20, y=150)

        gender_lbl = Label(detail_frm, text="Gender", font=(
            "times new roman", 20), bg="white")
        gender_lbl.place(x=300, y=148)

        mob_lbl = Label(detail_frm, text="mobile no.",
                        font=("times new roman", 20), bg="white")
        mob_lbl.place(x=20, y=200)

        address_lbl = Label(detail_frm, text="address",
                            font=("times new roman", 20), bg="white")
        address_lbl.place(x=20, y=250)

        self.adress_text = Text(
            detail_frm, height=7, width=35, bg="lightyellow", bd=3, relief=GROOVE)
        self.adress_text.place(x=180, y=250)

        image_lbl = Label(detail_frm, text="Image", font=(
            "times new roman", 20), bg="white")
        image_lbl.place(x=20, y=370)

        upload_img = Button(detail_frm, text="Upload Image", command=self.upload_file, font=(
            "times new roman", 12, "bold"))
        upload_img.place(x=180, y=370)

    # --------------------------------#

    # input's =========================

        name_input = Entry(detail_frm, font=("times new roman", 16),
                            textvariable=self.var_name, bg="lightyellow", width=27, bd=3, relief=GROOVE)
        name_input.place(x=180, y=50)

        class_input = Entry(detail_frm, font=("times new roman", 16),
                            textvariable=self.var_class, bg="lightyellow", width=10, bd=3, relief=GROOVE)
        class_input.place(x=180, y=100)

        dob_input = Entry(detail_frm, font=("times new roman", 16),
                            textvariable=self.var_dob, bg="lightyellow", width=10, bd=3, relief=GROOVE)
        dob_input.place(x=370, y=102)

        blood_input = Entry(detail_frm, font=("times new roman", 16),
                            textvariable=self.var_blood, bg="lightyellow", width=10, bd=3, relief=GROOVE)
        blood_input.place(x=180, y=150)

        gender_input = Entry(detail_frm, font=("times new roman", 16),
                            textvariable=self.var_gender, bg="lightyellow", width=8, bd=3, relief=GROOVE)
        gender_input.place(x=389, y=150)

        mob_input = Entry(detail_frm, font=("times new roman", 16),
                            textvariable=self.var_mb, bg="lightyellow", width=27, bd=3, relief=GROOVE)
        mob_input.place(x=180, y=200)

        id_card_frm = Frame(self.root,  height=500, width=500,
                            bd=2, relief=GROOVE, bg="White")
        id_card_frm.place(x=600, y=100)
        id_card_lbl = Label(id_card_frm, text="ID Card",  font=(
            "times new roman", 20, "bold"), bg="#000075", fg="White").place(x=0, y=0, relwidth=1)
        id_main = Frame(id_card_frm, height=430,
                        width=405, bd=2, relief=GROOVE)
        id_main.place(x=45, y=45)

        self.id_img = Label(id_main, font=("times new roman", 24, "bold"),
                            bg="#000075", text="No preview available", fg="White")
        self.id_img.place(x=0, y=0, width=405, height=430)
        btn = Button(detail_frm, command=self.genrate_id, text="Genrate", font=(
            "times new roman", 20, "bold"), bg="#000075", fg="White", relief=GROOVE, bd=2, borderwidth=0)
        btn.place(x=200, y=430, height=46, width=120)

    def genrate_id(self):
        image = Image.new('RGB', (1000, 900), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype('arial.ttf', size=45)

        (x, y) = (50, 50)
        message = "MANISH ENTERPRICES"
        company = message
        color = 'rgb(25,25,112)'
        font = ImageFont.truetype('arial.ttf', size=80)
        draw.text((x, y), message, fill=color, font=font, bold=True)

        (x, y) = (50, 250)
        message = self.var_name.get()
        name = message
        color = 'rgb(0, 0, 0)'  # black color
        font = ImageFont.truetype('arial.ttf', size=45)
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 350)
        message = self.var_gender.get()
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (250, 350)
        message = self.var_dob.get()
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        # (x, y) = (50, 450)
        # message = input('Enter Your Date Of Birth: ')
        # color = 'rgb(0, 0, 0)' # black color
        # draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 450)
        message = self.var_blood.get()
        color = 'rgb(255, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 550)
        message = self.var_mb.get()
        temp = message
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 650)
        message = self.adress_text.get("1.0", END)
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        image.save("./images/"+str(name)+'.png')

        Id = Image.open("./images/"+name + ".png")
        std_img = Image.open(self.filename)
        std_img = std_img.resize((400, 350), Image.ANTIALIAS)
        logo_img = Image.open("C:/Users/MANISH DAS/Downloads/logo.jpg")
        logo_img = logo_img.resize((1000, 300), Image.ANTIALIAS)
        Id.paste(logo_img, ((0, -80)))
        Id.paste(std_img, (520, 250))
        Id.save("./images/"+str(name)+'.png')
        Id = Id.resize((396, 421), Image.ANTIALIAS)

        self.id_img0 = ImageTk.PhotoImage(Id)
        self.id_img.config(image=self.id_img0, bd=5, bg="white", text="")

    def upload_file(self):
        self.filename = filedialog.askopenfilename(initialdir="", title="Select Image",
                                                filetypes=(("png images", "*.png"), ("jpg images", "*.jpg")))
        print(self.filename)


root = Tk()
obj = Main(root)
root.mainloop()
