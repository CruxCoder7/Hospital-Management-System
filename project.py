from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import pyglet


def raise_frame(frame, win_title):
    frame.tkraise()
    window.title(win_title)


def user_not_found():
    os.chdir('D:\pyproj\pictures')

    animation = pyglet.image.load_animation('not.gif')
    animSprite = pyglet.sprite.Sprite(animation)

    w = animSprite.width
    h = animSprite.height

    window = pyglet.window.Window(width=w, height=h)

    r, g, b, alpha = 0.5, 0.5, 0.8, 0.5

    pyglet.gl.glClearColor(r, g, b, alpha)

    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()

    pyglet.app.run()


def password_not_recognised():
    os.chdir('D:\pyproj\pictures')

    animation = pyglet.image.load_animation('tenor.gif')
    animSprite = pyglet.sprite.Sprite(animation)

    w = animSprite.width
    h = animSprite.height

    window = pyglet.window.Window(width=w, height=h)

    r, g, b, alpha = 0.5, 0.5, 0.8, 0.5

    pyglet.gl.glClearColor(r, g, b, alpha)

    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()

    pyglet.app.run()


def patpwd_not_found():
    lab1 = Label(pat_login_screen, text="wrong pwd")
    lab1.place(x=200, y=300)


def patuser_not_found():
    lab = Label(pat_login_screen, text="wrong username")
    lab.place(x=200, y=300)


def video():
    os.chdir('D:\pyproj\pictures')
    vidPath = 'corona virus.mp4'
    window = pyglet.window.Window(width=820, height=700)
    player = pyglet.media.Player()
    source = pyglet.media.StreamingSource()
    MediaLoad = pyglet.media.load(vidPath)

    player.queue(MediaLoad)
    player.play()

    @window.event
    def on_draw():
        if player.source and player.source.video_format:
            player.get_texture().blit(50, 0)

    pyglet.app.run()


def pat_register_user():
    os.chdir('D:\pyproj\PatientCredentials')
    pat_username_info = pat_username.get()
    pat_pwd_info = pat_password.get()

    file = open(pat_username_info, "w")
    file.write(pat_username_info+"\n")
    file.write(pat_pwd_info)
    file.close()
    pat_username_entry.delete(0, END)
    pat_password_entry.delete(0, END)
    pat_reglabel = Label(
        pat_regis_screen, text="Registration successful", fg="green", font=("calibri", 11))
    pat_reglabel.place(x=790, y=600, anchor="center")


def login_verify():
    os.chdir('D:\pyproj\AdminCredentials')
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            raise_frame(sess_screen, 'dashboard')
        else:
            password_not_recognised()
    else:
        user_not_found()


def save():
    import mysql.connector as sqltor
    mycon = sqltor.connect(host="localhost", user="root",
                           password="Akash20032006", database="doctors")
    cursor = mycon.cursor()
    filename = raw_filename.get()
    notes = raw_notes.get()
    sno = raw_sno.get()
    spec = raw_spec.get()
    global pat
    pat = raw_pat.get()
    sql = "insert into appointments (s_no,name,specialisation,timings,PatientName) values(%s,%s,%s,%s,%s)"
    val = (sno, filename, spec, notes, pat)
    cursor.execute(sql, val)
    mycon.commit()
    savlab = Label(appt_screen, text="SAVED", fg="green", font=("calibri", 10))
    savlab.place(x=790, y=780)


def patlogin_verify():
    os.chdir('D:\pyproj\PatientCredentials')
    username2 = pat_username_verify.get()
    password2 = pat_password_verify.get()
    username2_entry2.delete(0, END)
    password2_entry2.delete(0, END)
    pat_credentials = os.listdir()
    if username2 in pat_credentials:
        file2 = open(username2, "r")
        verify2 = file2.read().splitlines()
        if password2 in verify2:
            if password2 == raw_pat:
                global show_mb
                raise_frame(side2_screen2, 'dashboard')
                lex = Label(side2_screen2, text="hello")
                lex.place(x=100, y=200)
                show_mb = True
            elif password2 in verify2:
                raise_frame(side2_screen2, 'dashboard')
                if show_mb:
                    messagebox.showwarning('alert', 'pay the bill')
                    show_mb = False
            else:
                password_not_recognised()
        else:
            password_not_recognised()
    else:
        user_not_found()


def appointments():
    screen13 = Toplevel(window)

    screen13.configure(background="light sky blue")
    import mysql.connector
    my_connect = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Akash20032006",
        database="doctors"
    )
    b11 = Label(screen13, text="S_NO", font=(
        "calibri", 15), bg="light sky blue")
    b11.grid(row=0, column=0)
    b12 = Label(screen13, text="NAME", font=(
        "calibri", 15), bg="light sky blue")
    b12.grid(row=0, column=1)
    b13 = Label(screen13, text="SPECIALISATION",
                font=("calibri", 15), bg="light sky blue")
    b13.grid(row=0, column=2)
    b14 = Label(screen13, text="TIMINGS", font=(
        "calibri", 15), bg="light sky blue")
    b14.grid(row=0, column=3)
    b15 = Label(screen13, text="PATIENTNAME", font=(
        "calibri", 15), bg="light sky blue")
    b15.grid(row=0, column=4)
    my_cursor = my_connect.cursor()
    my_cursor.execute("select * from appointments limit 0,10")
    i = 1
    for student in my_cursor:
        for j in range(len(student)):
            e = Entry(screen13, width=10, font=(
                "calibri", 25), fg='black', bg="powderblue")
            e.grid(row=i, column=j, padx=1)
            e.insert(END, student[j])
        i = i+1

    screen13.mainloop()


def delapp():
    import mysql.connector as sqltor
    mycon = sqltor.connect(host="localhost", user="root",
                           password="Akash20032006", database="doctors")
    cursor = mycon.cursor()
    dext = del_file.get()
    z2.delete(0, END)

    sql = "select name from appointments"
    cursor.execute(sql)
    for name in cursor:
        if dext in name:
            sql = "delete from appointments where name=%s"
            cursor.execute(sql, (dext,))
            mycon.commit()
            crlab = Label(delappt_screen, text="CANCELED")
            crlab.place(x=790, y=180)

        else:
            wrlab = Label(delappt_screen, text="wrong")
            wrlab.place(x=790, y=180)


def delete_pat():
    import mysql.connector as sqltor
    mycon = sqltor.connect(host="localhost", user="root",
                           password="Akash20032006", database="doctors")
    cursor = mycon.cursor()

    delx = del_name.get()
    del_entry.delete(0, END)

    sql = "select PatientName from appointments"
    cursor.execute(sql)
    for patname in cursor:
        if delx in patname:
            sql = "delete from appointments where PatientName=%s"
            cursor.execute(sql, (delx,))
            mycon.commit()
            crlab = Label(del_pat_appt, text="CANCELED")
            crlab.place(x=790, y=180)

        else:
            wrlab = Label(del_pat_appt, text="wrong")
            wrlab.place(x=790, y=180)


def doctors():
    global screen12
    screen12 = Toplevel(window)
    import mysql.connector as sqltor
    mycon = sqltor.connect(host="localhost", user="root",
                           password="Akash20032006", database="doctors")
    screen12.configure(background="misty rose")

    bt11 = Label(screen12, text="S_NO", font=("calibri", 15), bg="misty rose")
    bt11.grid(row=0, column=0)
    bt12 = Label(screen12, text="DOCTORNAME",
                 font=("calibri", 15), bg="misty rose")
    bt12.grid(row=0, column=1)

    cursor = mycon.cursor()
    cursor.execute("SELECT * FROM DOCTORS limit 0,10")

    i = 1
    for student in cursor:
        for j in range(len(student)):
            e = Entry(screen12, width=10, font=("calibri", 25))
            e.grid(row=i, column=j, padx=1)
            e.insert(END, student[j])
        i = i+1
    screen12.mainloop()


def patient_bill1():
    import mysql.connector as sqltor
    mycon = sqltor.connect(host="localhost", user="root",
                           password="Akash20032006", database="doctors")
    cursor = mycon.cursor()

    patient = patient_name.get()
    Doctor = doctor_name.get()
    admission = admission_num.get()
    payment = payment_method.get()
    amount = amount_topay.get()

    sql = "insert into bills (patient_name,doctor_name,admission_num,payment_method,amount) values(%s,%s,%s,%s,%s)"
    val = (patient, Doctor, admission, payment, amount)
    cursor.execute(sql, val)
    mycon.commit()
    paylab = Label(bill_screen, text="Transaction complete",
                   bg="blue", fg="white")
    paylab.place(x=790, y=700)


def patient_bill2():
    screen14 = Toplevel(window)

    screen14.configure(background="light sky blue")
    import mysql.connector
    my_connect = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Akash20032006",
        database="doctors"
    )
    a12 = Label(screen14, text="PATIENTNAME", font=(
        "calibri", 15), bg="light sky blue")
    a12.grid(row=0, column=0)
    a13 = Label(screen14, text="DOCTORNAME", font=(
        "calibri", 15), bg="light sky blue")
    a13.grid(row=0, column=1)
    a14 = Label(screen14, text="ADMISSION NUMBER",
                font=("calibri", 15), bg="light sky blue")
    a14.grid(row=0, column=2)
    a15 = Label(screen14, text="PAYMENT METHOD",
                bg="light sky blue", font=("calibri", 15))
    a15.grid(row=0, column=3)
    a16 = Label(screen14, text="AMOUNT",
                bg="light sky blue", font=("calibri", 15))
    a16.grid(row=0, column=4)
    my_cursor = my_connect.cursor()
    my_cursor.execute("SELECT * FROM bills limit 0,10")
    i = 1
    for x in my_cursor:
        for j in range(len(x)):
            e = Entry(screen14, width=10, font=(
                "calibri", 25), fg='red', bg="orange")
            e.grid(row=i, column=j, padx=1)
            e.insert(END, x[j])
        i = i+1

    screen14.mainloop()


def user_buttonC(frame):
    raise_frame(frame, 'welcome screen')


def loginbtnC(frame):
    raise_frame(frame, 'patient login screen')


def log_out_btnC(frame):
    global show_mb
    show_mb = True
    if messagebox.askyesno('alert', 'are u sure u want to log out?', icon="warning") == True:
        raise_frame(frame, 'Main screen')
        show_mb = True


def btt1C(frame):
    raise_frame(frame, 'Main screen')


def main_screen():
    global window
    window = Tk()
    window.title("Main Screen")
    window.geometry("1920x1080")
    window.state('zoomed')

    # Frames ~ ~ ~
    global side2_screen2_two
    side2_screen2_two = Frame(window)
    side2_screen2_two.place(relwidth=1, relheight=1)

    global bill_screen
    bill_screen = Frame(window)
    bill_screen.place(relwidth=1, relheight=1)

    global delappt_screen
    delappt_screen = Frame(window, bg="red")
    delappt_screen.place(relwidth=1, relheight=1)

    global del_pat_appt
    del_pat_appt = Frame(window, bg="cyan")
    del_pat_appt.place(relwidth=1, relheight=1)

    global appt_screen
    appt_screen = Frame(window)
    appt_screen.place(relwidth=1, relheight=1)

    global sess_screen
    sess_screen = Frame(window)
    sess_screen.place(relwidth=1, relheight=1)
    global screen_2F
    screen_2F = Frame(window)
    screen_2F.place(relwidth=1, relheight=1)

    global side_screen
    side_screen = Frame(window)
    side_screen.place(relwidth=1, relheight=1)

    global side2_screen2
    side2_screen2 = Frame(window)
    side2_screen2.place(relwidth=1, relheight=1)

    global main_screenF
    main_screenF = Frame(window)
    main_screenF.place(relwidth=1, relheight=1)

    global pat_main_screen
    pat_main_screen = Frame(window)
    pat_main_screen.place(relwidth=1, relheight=1)

    global pat_login_screen
    pat_login_screen = Frame(window)
    pat_login_screen.place(relwidth=1, relheight=1)

    global pat_regis_screen
    pat_regis_screen = Frame(window)
    pat_regis_screen.place(relwidth=1, relheight=1)

    global main_screenF1
    main_screenF1 = Frame(window)
    main_screenF1.place(relwidth=1, relheight=1)

    # Frame - main screen
    patscreen_path = r'D:\pyproj\pictures\blue.jpg'
    img_ele = Image.open(patscreen_path)
    img_ele = ImageTk.PhotoImage(img_ele)
    panel_ele = Label(main_screenF1, image=img_ele)
    panel_ele.pack(side="bottom", fill="both", expand="yes")

    path_tee = r'D:\pyproj\pictures\hospital3.png'
    img_tee = Image.open(path_tee)
    img_tee = ImageTk.PhotoImage(img_tee)
    panel_tee = Label(main_screenF1, image=img_tee)
    panel_tee.place(x=680, y=40)

    path_t = r'D:\pyproj\pictures\4.jpg'
    img_t = Image.open(path_t)
    img_t = ImageTk.PhotoImage(img_t)
    panel_t = Label(main_screenF1, image=img_t)
    panel_t.place(x=765, y=625, anchor='center')
    os.chdir('D:\pyproj\pictures')
    admin_pic = PhotoImage(file="button52.png")
    user_pic = PhotoImage(file="button51.png")

    z1 = Button(main_screenF1, text="ADMIN", bg="#ff9737", width=130, image=admin_pic,
                height=30, command=lambda: raise_frame(main_screenF, 'welcome screen'))
    z1.place(x=710, y=268)
    user_button = Button(main_screenF1, text="USER", bg="#ff9737", image=user_pic,
                         width=126, height=30, command=lambda: user_buttonC(pat_main_screen))
    user_button.place(x=710, y=350)

    #Frame - pat_main_screen
    patmainscreen_path = r'D:\pyproj\pictures\blue.jpg'
    img_main = Image.open(patmainscreen_path)
    img_main = ImageTk.PhotoImage(img_main)
    panel_main = Label(pat_main_screen, image=img_main)
    panel_main.pack(side="bottom", fill="both", expand="yes")

    welc_path = r'D:\pyproj\pictures\Capture12.PNG'
    welc_open = Image.open(welc_path)
    welc_open = ImageTk.PhotoImage(welc_open)
    panel_open = Label(pat_main_screen, image=welc_open)
    panel_open.place(x=400, y=10)
    os.chdir('D:\pyproj\pictures')
    login_pic = PhotoImage(file="button11.png")
    register_pic = PhotoImage(file="button12.png")
    back_btn_pic_main = PhotoImage(file="button20.png")

    loginbtn = Button(pat_main_screen, text="LOGIN", bg="#ff9737",
                      width=120, height=40, image=login_pic, command=lambda: loginbtnC(pat_login_screen))
    loginbtn.place(x=785, y=370, anchor='center')

    registerbtn = Button(pat_main_screen, text="REGISTER", bg="#ff9737", width=190,
                         height=40, image=register_pic, command=lambda: raise_frame(pat_regis_screen, 'patient register screen'))
    registerbtn.place(x=785, y=450, anchor='center')

    pat_main_screen_bkbtn = Button(pat_main_screen, text="BACK", bg="#ff9737", image=back_btn_pic_main, height=50, width=125,
                                   command=lambda: raise_frame(main_screenF1, 'Main Screen'))
    pat_main_screen_bkbtn.place(x=1375, y=800, anchor='se')

    #Frame - pat_login_screen
    patscreen_path = r'D:\pyproj\pictures\blue.jpg'
    patscreen_path = r'D:\pyproj\pictures\blue.jpg'
    img_pat = Image.open(patscreen_path)
    img_pat = ImageTk.PhotoImage(img_pat)
    panel_pat = Label(pat_login_screen, image=img_pat)
    panel_pat.pack(side="bottom", fill="both", expand="yes")

    global pat_username_verify
    global pat_password_verify
    pat_username_verify = StringVar()
    pat_password_verify = StringVar()
    global username2_entry2
    global password2_entry2

    details_pic = PhotoImage(file="button24.png")
    enter_user_pic = PhotoImage(file="button22.png")
    enter_password_pic = PhotoImage(file="button23.png")
    login_btn_pic = PhotoImage(file="button14.png")
    back_btn_pic = PhotoImage(file="button20.png")

    pat_login_label = Label(
        pat_login_screen, text="please enter your credentials below", image=details_pic, height=35, width=385, font=("Arial Black", 40))
    pat_login_label.place(x=790, y=25, anchor="center")

    pat_login_us = Label(pat_login_screen, text="Username", image=enter_user_pic,
                         height=40, width=175, bg="#ffef06", font=("Arial Black", 25))
    pat_login_us.place(x=790, y=125, anchor="center")

    username2_entry2 = Entry(
        pat_login_screen, textvariable=pat_username_verify, font=("Calibri", 25))
    username2_entry2.place(x=790, y=225, anchor="center")

    pat_login_pwd = Label(pat_login_screen, text="password", image=enter_password_pic,
                          height=40, width=175, bg="#ffef06", font=("Calibri", 25))
    pat_login_pwd.place(x=790, y=325, anchor="center")

    password2_entry2 = Entry(
        pat_login_screen, textvariable=pat_password_verify, font=("Calibri", 25), show='*')
    password2_entry2.place(x=790, y=425, anchor="center")
    mainloginbtn = Button(pat_login_screen, text="CLICK HERE TO LOGIN",
                          bg="#ff9737", image=login_btn_pic, height=45, width=290, command=patlogin_verify)
    mainloginbtn.place(x=790, y=526, anchor='center')

    pat_login_screen_bkbtn = Button(pat_login_screen, text="BACK", bg="#ff9737", image=back_btn_pic, height=50, width=125,
                                    command=lambda: raise_frame(pat_main_screen, 'welcome screen'))
    pat_login_screen_bkbtn.place(x=1375, y=800, anchor='se')

    # Frame - pat registration screen
    os.chdir('D:\pyproj\pictures')
    pat_regis_screen_path = r'D:\pyproj\pictures\blue.jpg'
    img_pat_regis = Image.open(pat_regis_screen_path)
    img_pat_regis = ImageTk.PhotoImage(img_pat_regis)
    panel_pat_regis = Label(pat_regis_screen, image=img_pat_regis)
    panel_pat_regis.pack(side="bottom", fill="both", expand="yes")

    global pat_username
    global pat_password
    global pat_username_entry
    global pat_password_entry
    pat_username = StringVar()
    pat_password = StringVar()

    enter_det_pic = PhotoImage(file="button21.png")
    username_pic = PhotoImage(file="button22.png")
    password_pic = PhotoImage(file="button23.png")
    register_btn_pic = PhotoImage(file="button13.png")
    back_btn_pic_regis = PhotoImage(file="button20.png")

    enter_det_lab = Label(pat_regis_screen, bg="#3ea0ff", text="Please enter details below",
                          height=35, width=385, image=enter_det_pic, font=("Arial Black", 40))
    enter_det_lab.place(x=790, y=25, anchor='center')

    enter_username_lab = Label(pat_regis_screen, text="Username", height=40,
                               width=175, image=username_pic, bg="#ffef06", font=("Calibri", 25))
    enter_username_lab.place(x=790, y=125, anchor='center')

    pat_username_entry = Entry(pat_regis_screen, font=(
        "Calibri", 25), textvariable=pat_username)
    pat_username_entry.place(x=790, y=225, anchor='center')

    enter_pwd_lab = Label(pat_regis_screen, text="Password", image=password_pic,
                          height=40, width=175, bg="#ffef06", font=("Calibri", 25))
    enter_pwd_lab.place(x=790, y=325, anchor='center')

    pat_password_entry = Entry(
        pat_regis_screen, textvariable=pat_password, show='*', font=("Calibri", 25))
    pat_password_entry.place(x=790, y=425, anchor='center')

    register_button = Button(pat_regis_screen, image=register_btn_pic,
                             width=320, bg="#ff9737", height=45, command=pat_register_user)
    register_button.place(x=790, y=526, anchor='center')

    pat_regis_screen_bkbtn = Button(pat_regis_screen, text="BACK", bg="#ff9737", image=back_btn_pic_regis, height=50, width=125,
                                    command=lambda: raise_frame(pat_main_screen, 'welcome screen'))
    pat_regis_screen_bkbtn.place(x=1375, y=800, anchor='se')

    # Frame - appointment/ bill
    path = r'D:\pyproj\pictures\blue.jpg'
    img_on = Image.open(path)
    img_on = ImageTk.PhotoImage(img_on)
    panel_on = Label(side2_screen2, image=img_on)
    panel_on.pack(side="bottom", fill="both", expand="yes")

    os.chdir('D:\pyproj\pictures')
    photo67 = PhotoImage(file="button15.png")
    photo70 = PhotoImage(file="button20.png")
    photo120 = PhotoImage(file="button42.png")
    log_out_btn_pic = PhotoImage(file="button53.png")
    creat_bill_pic = PhotoImage(file="button33.png")
    remove_appt_pic = PhotoImage(file="button17.png")

    log_out_btn = Button(side2_screen2, image=log_out_btn_pic, height=30, width=135, bg="#ff9737",
                         command=lambda: log_out_btnC(main_screenF1))
    log_out_btn.place(x=1375, y=40, anchor='ne')

    e3 = Button(side2_screen2, image=photo67, width=270, bg="#ff9737", height=50, font=(
        "Calibri", 25), command=lambda: raise_frame(appt_screen, 'sa screen'))
    e3.place(x=790, y=260, anchor='center')

    btt1 = Button(side2_screen2, image=photo70, bg="#ff9737",
                  height=50, width=125, command=lambda: btt1C(main_screenF1))
    btt1.place(x=1375, y=800, anchor='se')

    btt = Button(side2_screen2, image=creat_bill_pic, height="40", bg="#ff9737",
                 width="290", command=lambda: raise_frame(bill_screen, 'billing screen'))
    btt.place(x=790, y=360, anchor='center')

    cancel_apt = Button(side2_screen2, image=remove_appt_pic, height=40, width=290, bg="#ff9737",
                        command=lambda: raise_frame(del_pat_appt, 'delete appointment'))
    cancel_apt.place(x=790, y=460, anchor='center')

    bt3 = Button(side2_screen2, image=photo120, height="40",
                 bg="#ff9737", width="130", command=video)
    bt3.place(x=90, y=800, anchor='sw')

    # Frame - main screen1
    path = r'D:\pyproj\pictures\blue.jpg'
    img = Image.open(path)
    img = ImageTk.PhotoImage(img)
    panel = Label(main_screenF, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")

    path_three = r'D:\pyproj\pictures\hospital3.png'
    img_three = Image.open(path_three)
    img_three = ImageTk.PhotoImage(img_three)
    panel_three = Label(main_screenF, image=img_three)
    panel_three.place(x=780, y=100, anchor='center')

    path_two = r'D:\pyproj\pictures\logo.png'
    img_two = Image.open(path_two)
    img_two = ImageTk.PhotoImage(img_two)
    panel_two = Label(main_screenF, image=img_two)
    panel_two.place(x=530, y=500)

    photo = PhotoImage(file="button11.png")
    photo12 = PhotoImage(file="button42.png")

    b1 = Button(main_screenF, image=photo, height="40", bg="#ff9737",
                width="120", command=lambda: raise_frame(screen_2F, 'lg screen'))
    b1.place(x=720, y=310)

    b3 = Button(main_screenF, text="COVID 19", image=photo12,
                height="40", bg="#ff9737", width="130", command=video)
    b3.place(x=100, y=800, anchor='sw')

    b4 = Button(main_screenF, image=photo70, command=lambda: raise_frame(
        main_screenF1, 'sd screen'), bg="#ff9737", height=50, width=125)
    b4.place(x=1420, y=800, anchor='se')

    # Frame - login screen
    path_four = r'D:\pyproj\pictures\blue.jpg'
    img_four = Image.open(path_four)
    img_four = ImageTk.PhotoImage(img_four)
    panel_four = Label(screen_2F, image=img_four)
    panel_four.pack(side="bottom", fill="both", expand="yes")

    photox = PhotoImage(file="button14.png")
    photo7 = PhotoImage(file="button20.png")
    photo14 = PhotoImage(file="button24.png")
    photo11 = PhotoImage(file="button22.png")
    photoxy = PhotoImage(file="button23.png")

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    lba = Label(screen_2F, bg="#3ea0ff", text="Please enter details below to login",
                height=30, width=385, image=photo14, font=("Arial Black", 40))
    lba.place(x=790, y=25, anchor='center')

    lbx = Label(screen_2F, text="Username", image=photo11,
                height=40, width=175, bg="#ffef06", font=("Calibri", 25))
    lbx.place(x=790, y=125, anchor='center')

    username_entry1 = Entry(
        screen_2F, textvariable=username_verify, font=("Calibri", 25))
    username_entry1.place(x=790, y=225, anchor='center')
    lbz = Label(screen_2F, text="Password", image=photoxy,
                height=40, width=175, bg="#ffef06", font=("Calibri", 25))
    lbz.place(x=790, y=325, anchor='center')

    password_entry1 = Entry(
        screen_2F, textvariable=password_verify, show='*', font=("Calibri", 25))
    password_entry1.place(x=790, y=425, anchor='center')
    bt = Button(screen_2F, image=photox, width=290,
                height=45, bg="#ff9737", command=login_verify)
    bt.place(x=790, y=525, anchor='center')

    bt1 = Button(screen_2F, image=photo7, command=lambda: raise_frame(
        main_screenF, 'main screen'), bg="#ff9737", height=50, width=125)
    bt1.place(x=1240, y=800, anchor='sw')

    # Frame - sessions
    path_six = r'D:\pyproj\pictures\blue.jpg'
    img_six = Image.open(path_six)
    img_six = ImageTk.PhotoImage(img_six)
    panel_six = Label(sess_screen, image=img_six)
    panel_six.pack(side="bottom", fill="both", expand="yes")

    photome1 = PhotoImage(file="button15.png")
    photome2 = PhotoImage(file="button16.png")
    photome3 = PhotoImage(file="button17.png")
    photome4 = PhotoImage(file="button20.png")
    photome5 = PhotoImage(file="button25.png")
    photome6 = PhotoImage(file="button35.png")
    photo111 = PhotoImage(file="button33.png")

    e1 = Label(sess_screen, text="Welcome To Dashboard",
               image=photome5, bg="#3ea0ff", font=("Arial Black", 25))
    e1.place(x=790, y=35, anchor='center')

    e2 = Label(sess_screen, text="")
    e4 = Label(sess_screen, text="")

    e5 = Button(sess_screen, image=photome2, width=305,
                height=40, bg="#ff9737", command=appointments)
    e5.place(x=790, y=200, anchor='center')

    e7 = Button(sess_screen, image=photome3, width=300, height=40, bg="#ff9737",
                command=lambda: raise_frame(delappt_screen, 'cancel screen'))
    e7.place(x=790, y=300, anchor='center')

    bt3 = Button(sess_screen, image=photome4, bg="#ff9737", height=50,
                 width=125, command=lambda: raise_frame(screen_2F, 'lg screen'))
    bt3.place(x=1240, y=750, anchor='sw')
    btt1 = Button(sess_screen, text="view patient's bill", width=250,
                  height=40, image=photome6, bg="#ff9737", command=patient_bill2)
    btt1.place(x=790, y=525, anchor="center")

    # Frame create appointments
    global raw_filename
    raw_filename = StringVar()
    global raw_notes
    raw_notes = StringVar()
    global raw_sno
    raw_sno = StringVar()
    global raw_spec
    raw_spec = StringVar()
    global raw_pat
    raw_pat = StringVar()
    path_seven = r'D:\pyproj\pictures\blue.jpg'
    img_seven = Image.open(path_seven)
    img_seven = ImageTk.PhotoImage(img_seven)
    panel_seven = Label(appt_screen, image=img_seven)
    panel_seven.pack(side="bottom", fill="both", expand="yes")

    photofileone = PhotoImage(file="button18.png")
    photofiletwo = PhotoImage(file="button19.png")
    photofilethree = PhotoImage(file="button20.png")
    photo17 = PhotoImage(file="button25.png")
    photo18 = PhotoImage(file="button26.png")
    photo19 = PhotoImage(file="button27.png")
    photo20 = PhotoImage(file="button28.png")
    photo21 = PhotoImage(file="button29.png")
    photo22 = PhotoImage(file="button30.png")
    c1 = Label(appt_screen, text="Please enter s.no below:", height=40,
               width=375, image=photo18, bg="#ffef06", font=("Calibri", 25))
    c1.place(x=790, y=25, anchor='center')

    c2 = Entry(appt_screen, textvariable=raw_sno, font=("Calibri", 25))
    c2.place(x=790, y=85, anchor='center')

    c3 = Label(appt_screen, text="Please enter the Doctor's name below:",
               image=photo19, height=40, width=450, bg="#ffef06", font=("Calibri", 25))
    c3.place(x=790, y=145, anchor='center')

    c4 = Entry(appt_screen, textvariable=raw_filename, font=("Calibri", 25))
    c4.place(x=790, y=205, anchor='center')

    c5 = Label(appt_screen, text="Please enter specialisation below:",
               height=40, width=450, image=photo20, bg="#ffef06", font=("Calibri", 25))
    c5.place(x=790, y=265, anchor='center')

    c6 = Entry(appt_screen, textvariable=raw_spec, font=("Calibri", 25))
    c6.place(x=790, y=325, anchor='center')

    c7 = Label(appt_screen, text="Please enter the time below:", image=photo21,
               height=40, width=350, bg="#ffef06", font=("Calibri", 25))
    c7.place(x=790, y=385, anchor='center')

    c8 = Entry(appt_screen, textvariable=raw_notes, font=("Calibri", 25))
    c8.place(x=790, y=445, anchor='center')

    c9 = Label(appt_screen, text="Please enter the Patient's name below:",
               image=photo22, height=40, width=450, bg="#ffef06", font=("Calibri", 25))
    c9.place(x=790, y=505, anchor='center')

    c10 = Entry(appt_screen, textvariable=raw_pat, font=("Calibri", 25))
    c10.place(x=790, y=565, anchor='center')

    c11 = Button(appt_screen, image=photofileone, command=save,
                 bg="#ff9737", width=125, height=50, font=("Calibri", 25))
    c11.place(x=790, y=645, anchor='center')

    c12 = Button(appt_screen, image=photofiletwo, bg="#ff9737",
                 font=("Calibri", 50), command=doctors)
    c12.place(x=790, y=735, anchor='center')

    bt4 = Button(appt_screen, image=photofilethree, bg="#ff9737", height=50,
                 width=125, command=lambda: raise_frame(side2_screen2, ' dashboard'))
    bt4.place(x=1240, y=800, anchor='sw')

    # Frame remove appointments
    global del_file
    global z2
    del_file = StringVar()
    photo30 = PhotoImage(file="button31.png")
    photo31 = PhotoImage(file="button32.png")
    photo32 = PhotoImage(file="button20.png")
    z1 = Label(delappt_screen, image=photo30, height=30, width=400)
    z1.place(x=790, y=25, anchor="center")
    z2 = Entry(delappt_screen, font=("calibri", 25), textvariable=del_file)
    z2.place(x=790, y=75, anchor="center")
    z3 = Button(delappt_screen, text="cancel", image=photo31,
                height=40, width=150, command=delapp)
    z3.place(x=790, y=140, anchor="center")
    z4 = Button(delappt_screen, image=photo32, bg="#ff9737", height=50,
                width=125, command=lambda: raise_frame(sess_screen, 'dashboard'))
    z4.place(x=0, y=0)

    # Frame remove appointments from patient's screen
    global del_name
    global del_entry
    del_name = StringVar()
    photo_30 = PhotoImage(file="button30.png")
    photo_31 = PhotoImage(file="button32.png")
    photo_32 = PhotoImage(file="button20.png")

    delabel = Label(del_pat_appt, image=photo_30, height=30, width=450)
    delabel.place(x=790, y=25, anchor="center")

    del_entry = Entry(del_pat_appt, font=(
        "calibri", 25), textvariable=del_name)
    del_entry.place(x=790, y=75, anchor="center")

    delbtn = Button(del_pat_appt, text="cancel", image=photo_31,
                    height=40, width=150, command=delete_pat)
    delbtn.place(x=790, y=140, anchor="center")

    delback = Button(del_pat_appt, image=photo_32, bg="#ff9737", height=50,
                     width=125, command=lambda: raise_frame(side2_screen2, 'dashboard'))
    delback.place(x=0, y=0)

    # Frame create bill
    path_eight = r'D:\pyproj\pictures\blue.jpg'
    img_eight = Image.open(path_eight)
    img_eight = ImageTk.PhotoImage(img_eight)
    panel_eight = Label(bill_screen, image=img_eight)
    panel_eight.pack(side="bottom", fill="both", expand="yes")

    global patient_name
    global admission_num
    global amount_topay
    global doctor_name
    global payment_method
    global patient_name_entry
    global admission_num_entry
    global amount_topay_entry
    global doctor_name_entry
    global payment_method_entry

    photothirty = PhotoImage(file="button34.png")
    photothirtytwo = PhotoImage(file="button36.png")
    photo33 = PhotoImage(file="button37.png")
    photo34 = PhotoImage(file="button38.png")
    photo35 = PhotoImage(file="button39.png")
    photo36 = PhotoImage(file="button40.png")
    photo37 = PhotoImage(file="button41.png")
    photo38 = PhotoImage(file="button20.png")

    patient_name = StringVar()
    admission_num = StringVar()
    amount_topay = StringVar()
    doctor_name = StringVar()
    payment_method = StringVar()

    v1 = Label(bill_screen, bg="#3ea0ff", text="Please enter details below",
               height=30, width=385, image=photo37, font=("Arial Black", 40))
    v1.place(x=790, y=25, anchor='center')

    v2 = Label(bill_screen, text="patient's name", image=photothirtytwo,
               height=40, width=200, bg="#ffef06", font=("Calibri", 25))
    v2.place(x=790, y=100, anchor='center')

    username_entry = Entry(bill_screen, font=(
        "Calibri", 25), textvariable=patient_name)
    username_entry.place(x=790, y=150, anchor='center')

    v3 = Label(bill_screen, text="Doctor's Name", image=photo33,
               height=40, width=220, bg="#ffef06", font=("Calibri", 25))
    v3.place(x=790, y=200, anchor='center')

    password_entry = Entry(
        bill_screen, textvariable=doctor_name, font=("Calibri", 25))
    password_entry.place(x=790, y=250, anchor='center')

    v6 = Label(bill_screen, text="Admission Number", image=photo34,
               height=40, width=230, bg="#ffef06", font=("Calibri", 25))
    v6.place(x=790, y=300, anchor='center')

    admission_num_entry = Entry(bill_screen, font=(
        "Calibri", 25), textvariable=admission_num)
    admission_num_entry.place(x=790, y=350, anchor='center')

    v8 = Label(bill_screen, text="Amount", image=photo35,
               bg="#ffef06", height=40, width=150, font=("Calibri", 25))
    v8.place(x=790, y=400, anchor='center')

    amount_topay_entry = Entry(bill_screen, font=(
        "Calibri", 25), textvariable=amount_topay)
    amount_topay_entry.place(x=790, y=450, anchor='center')

    v7 = Label(bill_screen, text="Payment Method", image=photo36,
               height=40, width=220, bg="#ffef06", font=("Calibri", 25))
    v7.place(x=790, y=500, anchor='center')

    payment_method_entry = OptionMenu(
        bill_screen, payment_method, "Credit Card", "Debit card", "Paytm", "Google Pay")
    payment_method_entry.config(font=("Calibri", 25), bg=("#ffef06"))
    payment_method_entry.place(x=790, y=570, anchor='center')

    v4 = Label(bill_screen, text="", font=("Calibri", 25))
    v5 = Button(bill_screen, text="Pay now", bg="#ff9737", width=135,
                height=40, image=photothirty, command=patient_bill1)
    v5.place(x=790, y=650, anchor='center')
    btt2 = Button(bill_screen, text="Back", image=photo38, height=50, width=125,
                  bg="#ff9737", command=lambda: raise_frame(side2_screen2, 'dashboard'))
    btt2.place(x=1240, y=750, anchor='sw')

    window.mainloop()


main_screen()
