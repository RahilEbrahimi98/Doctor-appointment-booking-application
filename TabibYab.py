import tkinter
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk

def appointment_family_ui():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global appointment_family_page

    appointment_family_page = tkinter.Tk()
    appointment_family_page.title('Family Appointments Page')
    appointment_family_page.attributes('-fullscreen', True)
    appointment_family_page.configure(background="#2d3436")

    back_button = tkinter.Button(appointment_family_page, command=appointment_family_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    appointment_family_listbox = tkinter.Listbox(appointment_family_page)
    appointment_family_listbox.place(relx=0.050, rely=0.205, relheight=0.552, relwidth=0.9)
    appointment_family_listbox.configure(cursor="spider")
    appointment_family_listbox.configure(font=font9)
    appointment_family_listbox.configure(justify='center')
    appointment_family_listbox.configure(relief="flat")
    appointment_family_listbox.configure(selectbackground="#dfe6e9")
    appointment_family_listbox.configure(setgrid="1")

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT User.first_name, User.last_name, User.phone_number, Doctor.first_name, Doctor.last_name, Appointment.appointment_date FROM Appointment, User, Doctor WHERE User.phone_number = Appointment.phone_number AND Doctor.username = Appointment.username AND Doctor.medical_council_code = Appointment.medical_council_code AND Appointment.phone_number IN (SELECT phone_number_2 FROM USER_USER WHERE phone_number_1 = '{current_phone_number}')")
    family_appointments = cursor.fetchall()

    for family_appointment in family_appointments:
        first_name_text = f'{family_appointment[0]}'
        last_name_text = f'{family_appointment[1]}'
        phone_number_text= f'{family_appointment[2]}'
        appointment_date_text = f'{family_appointment[5]}'
        doctor_firstname_text = f'{family_appointment[3]}'
        doctor_lastname_text = f'{family_appointment[4]}'
    
        for i in range(14):
            if i == len(appointment_date_text) - 1:
                appointment_date_text += ' '
            if i == len(doctor_firstname_text) - 1:
                doctor_firstname_text += ' '
            if i == len(doctor_lastname_text) - 1:
                doctor_lastname_text += ' '
            if i == len(phone_number_text) - 1:
                phone_number_text += ' '
            if i == len(first_name_text) - 1:
                first_name_text += ' '
            if i == len(last_name_text) - 1:
                last_name_text += ' '

        appointment_family_listbox.insert(tkinter.END, f'Appointment Date: {appointment_date_text}| Doctor First Name: {doctor_firstname_text}| Doctor Last Name: {doctor_lastname_text}| Patient Phone Number: {phone_number_text}| Patient First Name: {first_name_text}| Patient Last Name: {last_name_text}')


    connection.commit()
    connection.close()

    return


def my_appointments_by_others_ui():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global appointment_by_others_page

    appointment_by_others_page = tkinter.Tk()
    appointment_by_others_page.title('Appointment by Others Page')
    appointment_by_others_page.attributes('-fullscreen', True)
    appointment_by_others_page.configure(background="#2d3436")

    back_button = tkinter.Button(appointment_by_others_page, command=appointment_by_others_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    appointment_by_others_listbox = tkinter.Listbox(appointment_by_others_page)
    appointment_by_others_listbox.place(relx=0.050, rely=0.205, relheight=0.552, relwidth=0.9)
    appointment_by_others_listbox.configure(cursor="spider")
    appointment_by_others_listbox.configure(font=font9)
    appointment_by_others_listbox.configure(justify='center')
    appointment_by_others_listbox.configure(relief="flat")
    appointment_by_others_listbox.configure(selectbackground="#dfe6e9")
    appointment_by_others_listbox.configure(setgrid="1")

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT Appointment.getter_phone_number, Doctor.first_name, Doctor.last_name, Appointment.appointment_date FROM Appointment, User, Doctor WHERE User.phone_number = Appointment.phone_number AND Doctor.username = Appointment.username AND Doctor.medical_council_code = Appointment.medical_council_code AND Appointment.getter_phone_number IN (SELECT phone_number_1 FROM USER_USER) AND Appointment.getter_phone_number NOT IN ('{current_phone_number}') AND Appointment.phone_number IN ('{current_phone_number}')")
    by_others_appointments = cursor.fetchall()

    if len(by_others_appointments) == 0:
        by_others_appointments = []

    for i in range(len(by_others_appointments)):

        appointment_date_text = f'{by_others_appointments[i][3]}'
        doctor_firstname_text = f'{by_others_appointments[i][1]}'
        doctor_lastname_text = f'{by_others_appointments[i][2]}'
        getter_phone_number_text = f'{by_others_appointments[i][0]}'
        
        getter_phone_number = by_others_appointments[i][0]
        cursor.execute(f"SELECT first_name, last_name FROM User WHERE phone_number = '{getter_phone_number}';")
        getter_data = cursor.fetchone()

        getter_firstname_text = f'{getter_data[0]}'
        getter_lastname_text = f'{getter_data[1]}'

        for i in range(15):
            if i == len(appointment_date_text) - 1:
                appointment_date_text += ' '
            if i == len(doctor_firstname_text) - 1:
                doctor_firstname_text += ' '
            if i == len(doctor_lastname_text) - 1:
                doctor_lastname_text += ' '
            if i == len(getter_phone_number_text) - 1:
                getter_phone_number_text += ' '
            if i == len(getter_firstname_text) - 1:
                getter_firstname_text += ' '
            if i == len(getter_lastname_text) - 1:
                getter_lastname_text += ' '

        appointment_by_others_listbox.insert(tkinter.END, f'Appointment Date: {appointment_date_text}| Doctor First Name: {doctor_firstname_text}| Doctor Last Name: {doctor_lastname_text}| Getter Phone Number: {getter_phone_number_text}| getter First Name: {getter_firstname_text}| getter Last Name: {getter_lastname_text}\n')

    connection.commit()
    connection.close()
    
    return


def edit_profile_db(first_name, last_name, insurance_id, gender, image_path):
    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT insurance_id FROM Insurance WHERE name = '{insurance_id}';")
    insurance_id = cursor.fetchone()[0]

    cursor.execute(f"SELECT gender_id FROM Gender WHERE title = '{gender}';")
    gender_id = cursor.fetchone()
    if gender_id != None:
        gender_id = gender_id[0]
    else:
        gender_id = 0
    
    cursor.execute(f"UPDATE User SET first_name = '{first_name}', last_name = '{last_name}', insurance_id = {insurance_id}, photo = '{image_path}', gender_id = {gender_id} WHERE phone_number = '{current_phone_number}';")

    connection.commit()
    connection.close()

    edit_profile_page.destroy()
    
    return


def edit_profile_ui():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font10 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT first_name, last_name, insurance_id, gender_id, birthday, photo FROM User WHERE phone_number = '{current_phone_number}';")
    temp_user_data = cursor.fetchone()

    user_data = []
    for temp in temp_user_data:
        if temp != None:
            user_data.append(temp)
        else:
            user_data.append('')
    
    cursor.execute(f"SELECT name FROM Insurance WHERE insurance_id = {user_data[2]};")
    insurance_data = cursor.fetchone()

    
    if not (user_data[3] == None or len(str(user_data[3])) == 0):
        cursor.execute(f"SELECT title FROM Gender WHERE gender_id = {user_data[3]};")
        gender_data = cursor.fetchone()
    else:
        gender_data = None

    global edit_profile_page

    edit_profile_page = tkinter.Toplevel()
    edit_profile_page.title('Edit Profile Page')
    edit_profile_page.attributes('-fullscreen', True)
    edit_profile_page.configure(background="#2d3436")

    if not (len(user_data[5]) == 0 or user_data[5] == None):
        image_path = str(user_data[5])
        profile_image = Image.open(image_path)
        profile_image = profile_image.resize((150, 150), Image.ANTIALIAS)
        profile_image = ImageTk.PhotoImage(image=profile_image)
        profile_label = tkinter.Label(edit_profile_page,image=profile_image)
        profile_label.image = profile_image
        profile_label.place(relx=0.4675, rely=0.125)

    back_button = tkinter.Button(edit_profile_page, command=edit_profile_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    Frame1 = tkinter.Frame(edit_profile_page)
    Frame1.place(relx=0.365, rely=0.325, relheight=0.500, relwidth=0.273)
    Frame1.configure(relief='flat')
    Frame1.configure(borderwidth="2")
    Frame1.configure(background="#ffffff")

    firstname_label = tkinter.Label(Frame1)
    firstname_label.place(relx=0.0, rely=0.03, height=54, width=98)
    firstname_label.configure(background="#ffffff")
    firstname_label.configure(font=font9)
    firstname_label.configure(text='''First Name''')

    lastname_label = tkinter.Label(Frame1)
    lastname_label.place(relx=-0.019, rely=0.14, height=74, width=118)
    lastname_label.configure(activebackground="#f9f9f9")
    lastname_label.configure(background="#ffffff")
    lastname_label.configure(font=font9)
    lastname_label.configure(text='''Last Name''')

    insurance_label = tkinter.Label(Frame1)
    insurance_label.place(relx=0.0, rely=0.36, height=54, width=98)
    insurance_label.configure(activebackground="#f9f9f9")
    insurance_label.configure(background="#ffffff")
    insurance_label.configure(font=font9)
    insurance_label.configure(text='''Insurance''')

    phone_number_label = tkinter.Label(Frame1)
    phone_number_label.place(relx=0.0, rely=0.25, height=54, width=108)
    phone_number_label.configure(activebackground="#f9f9f9")
    phone_number_label.configure(background="#ffffff")
    phone_number_label.configure(font=font9)
    phone_number_label.configure(text='''Phone Number''')

    gender_label = tkinter.Label(Frame1)
    gender_label.place(relx=0.0, rely=0.47, height=54, width=108)
    gender_label.configure(activebackground="#f9f9f9")
    gender_label.configure(background="#ffffff")
    gender_label.configure(font=font9)
    gender_label.configure(text='''Gender''')

    birthday_label = tkinter.Label(Frame1)
    birthday_label.place(relx=0.0, rely=0.58, height=54, width=108)
    birthday_label.configure(activebackground="#f9f9f9")
    birthday_label.configure(background="#ffffff")
    birthday_label.configure(font=font9)
    birthday_label.configure(text='''Birthday''')

    image_label = tkinter.Label(Frame1)
    image_label.place(relx=0.0, rely=0.69, height=54, width=108)
    image_label.configure(activebackground="#f9f9f9")
    image_label.configure(background="#ffffff")
    image_label.configure(font=font9)
    image_label.configure(text='''Image Path''')

    firstname_entry = tkinter.Entry(Frame1)
    firstname_entry.place(relx=0.21, rely=0.03, height=53, relwidth=0.754)
    firstname_entry.configure(background="#dfe6e9")
    firstname_entry.configure(font=font10)
    firstname_entry.configure(foreground="#ffffff")
    firstname_entry.configure(justify='center')
    firstname_entry.configure(relief="flat")
    firstname_entry.insert(0, user_data[0])

    lastname_entry = tkinter.Entry(Frame1)
    lastname_entry.place(relx=0.21, rely=0.14, height=53, relwidth=0.754)
    lastname_entry.configure(background="#dfe6e9")
    lastname_entry.configure(cursor="fleur")
    lastname_entry.configure(font=font10)
    lastname_entry.configure(foreground="#ffffff")
    lastname_entry.configure(justify='center')
    lastname_entry.configure(relief="flat")
    lastname_entry.configure(selectbackground="#c4c4c4")
    lastname_entry.insert(0, user_data[1])

    phone_number_entry = tkinter.Entry(Frame1)
    phone_number_entry.place(relx=0.21, rely=0.25, height=53, relwidth=0.754)
    phone_number_entry.configure(background="#dfe6e9")
    phone_number_entry.configure(font=font10)
    phone_number_entry.configure(justify='center')
    phone_number_entry.configure(relief="flat")
    phone_number_entry.configure(selectbackground="#c4c4c4")
    phone_number_entry.insert(0, current_phone_number)
    phone_number_entry.configure(state='readonly')
    phone_number_entry.configure(foreground="#ffffff")

    insurance_entry = tkinter.Entry(Frame1)
    insurance_entry.place(relx=0.21, rely=0.36, height=53, relwidth=0.754)
    insurance_entry.configure(background="#dfe6e9")
    insurance_entry.configure(font=font10)
    insurance_entry.configure(foreground="#ffffff")
    insurance_entry.configure(justify='center')
    insurance_entry.configure(relief="flat")
    insurance_entry.configure(selectbackground="#c4c4c4")
    if insurance_data != None:
        insurance_entry.insert(0, insurance_data[0])

    gender_entry = tkinter.Entry(Frame1)
    gender_entry.place(relx=0.21, rely=0.47, height=53, relwidth=0.754)
    gender_entry.configure(background="#dfe6e9")
    gender_entry.configure(font=font10)
    gender_entry.configure(foreground="#ffffff")
    gender_entry.configure(justify='center')
    gender_entry.configure(relief="flat")
    gender_entry.configure(selectbackground="#c4c4c4")
    if gender_data != None:
        gender_entry.insert(0, gender_data[0])

    birthday_entry = tkinter.Entry(Frame1)
    birthday_entry.place(relx=0.21, rely=0.58, height=53, relwidth=0.754)
    birthday_entry.configure(background="#dfe6e9")
    birthday_entry.configure(font=font10)
    birthday_entry.configure(foreground="#ffffff")
    birthday_entry.configure(justify='center')
    birthday_entry.configure(relief="flat")
    birthday_entry.configure(selectbackground="#c4c4c4")
    if user_data[4] != None:
        birthday_entry.insert(0, user_data[4])

    image_entry = tkinter.Entry(Frame1)
    image_entry.place(relx=0.21, rely=0.69, height=53, relwidth=0.754)
    image_entry.configure(background="#dfe6e9")
    image_entry.configure(font=font10)
    image_entry.configure(foreground="#ffffff")
    image_entry.configure(justify='center')
    image_entry.configure(relief="flat")
    image_entry.configure(selectbackground="#c4c4c4")
    if user_data[5] != None:
        image_entry.insert(0, user_data[5])   

    connection.commit()
    connection.close()

    edit_profile_submit_button = tkinter.Button(Frame1, command=lambda: edit_profile_db(firstname_entry.get(), lastname_entry.get(), insurance_entry.get(), gender_entry.get(), image_entry.get()))
    edit_profile_submit_button.place(relx=0.038, rely=0.84, height=54, width=491)
    edit_profile_submit_button.configure(activebackground="#dfe6e9")
    edit_profile_submit_button.configure(background="#2d3436")
    edit_profile_submit_button.configure(font=font9)
    edit_profile_submit_button.configure(foreground="#ffffff")
    edit_profile_submit_button.configure(relief="flat")
    edit_profile_submit_button.configure(text='''Submit''')

    return

def add_family_db(first_name, last_name, phone_number, insurance_id, password, gender_id, birthday):

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT insurance_id FROM Insurance WHERE name = '{insurance_id}';")
    insurance_id = cursor.fetchone()

    cursor.execute(f"SELECT gender_id FROM Gender WHERE title = '{gender_id}';")
    gender_id = cursor.fetchone()

    cursor.execute(f"INSERT INTO User (phone_number, first_name, last_name, password, insurance_id, gender_id, birthday) VALUES('{phone_number}', '{first_name}', '{last_name}', '{password}', {insurance_id[0]}, {gender_id[0]}, '{birthday}');")

    cursor.execute(f"INSERT INTO User_User VALUES ('{current_phone_number}', '{phone_number}')")

    connection.commit()
    connection.close()

    return

def add_family_inner_ui():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font9 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font10 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global add_family_inner_page

    add_family_inner_page = tkinter.Tk()
    add_family_inner_page.title('Add Family Page')
    add_family_inner_page.attributes('-fullscreen', True)
    add_family_inner_page.configure(background="#2d3436")

    back_button = tkinter.Button(add_family_inner_page, command=add_family_inner_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    Frame1 = tkinter.Frame(add_family_inner_page)
    Frame1.place(relx=0.365, rely=0.250, relheight=0.500, relwidth=0.273)
    Frame1.configure(relief='flat')
    Frame1.configure(borderwidth="2")
    Frame1.configure(background="#ffffff")

    firstname_inner_label = tkinter.Label(Frame1)
    firstname_inner_label.place(relx=0.0, rely=0.03, height=54, width=98)
    firstname_inner_label.configure(background="#ffffff")
    firstname_inner_label.configure(font=font9)
    firstname_inner_label.configure(text='''First Name''')

    lastname_inner_label = tkinter.Label(Frame1)
    lastname_inner_label.place(relx=-0.019, rely=0.15, height=74, width=118)
    lastname_inner_label.configure(activebackground="#f9f9f9")
    lastname_inner_label.configure(background="#ffffff")
    lastname_inner_label.configure(font=font9)
    lastname_inner_label.configure(text='''Last Name''')

    insurance_inner_label = tkinter.Label(Frame1)
    insurance_inner_label.place(relx=0.0, rely=0.39, height=54, width=98)
    insurance_inner_label.configure(activebackground="#f9f9f9")
    insurance_inner_label.configure(background="#ffffff")
    insurance_inner_label.configure(font=font9)
    insurance_inner_label.configure(text='''Insurance''')

    phone_number_inner_label = tkinter.Label(Frame1)
    phone_number_inner_label.place(relx=0.0, rely=0.27, height=54, width=108)
    phone_number_inner_label.configure(activebackground="#f9f9f9")
    phone_number_inner_label.configure(background="#ffffff")
    phone_number_inner_label.configure(font=font9)
    phone_number_inner_label.configure(text='''Phone Number''')

    gender_inner_label = tkinter.Label(Frame1)
    gender_inner_label.place(relx=0.0, rely=0.51, height=54, width=108)
    gender_inner_label.configure(activebackground="#f9f9f9")
    gender_inner_label.configure(background="#ffffff")
    gender_inner_label.configure(font=font9)
    gender_inner_label.configure(text='''Gender''')

    birthday_inner_label = tkinter.Label(Frame1)
    birthday_inner_label.place(relx=0.0, rely=0.63, height=54, width=108)
    birthday_inner_label.configure(activebackground="#f9f9f9")
    birthday_inner_label.configure(background="#ffffff")
    birthday_inner_label.configure(font=font9)
    birthday_inner_label.configure(text='''Birthday''')

    password_inner_label = tkinter.Label(Frame1)
    password_inner_label.place(relx=0.0, rely=0.75, height=54, width=108)
    password_inner_label.configure(activebackground="#f9f9f9")
    password_inner_label.configure(background="#ffffff")
    password_inner_label.configure(font=font9)
    password_inner_label.configure(text='''Password''')

    firstname_inner_entry = tkinter.Entry(Frame1)
    firstname_inner_entry.place(relx=0.21, rely=0.03, height=53, relwidth=0.754)
    firstname_inner_entry.configure(background="#dfe6e9")
    firstname_inner_entry.configure(font=font10)
    firstname_inner_entry.configure(foreground="#ffffff")
    firstname_inner_entry.configure(justify='center')
    firstname_inner_entry.configure(relief="flat")

    lastname_inner_entry = tkinter.Entry(Frame1)
    lastname_inner_entry.place(relx=0.21, rely=0.15, height=53, relwidth=0.754)
    lastname_inner_entry.configure(background="#dfe6e9")
    lastname_inner_entry.configure(cursor="fleur")
    lastname_inner_entry.configure(font=font10)
    lastname_inner_entry.configure(foreground="#ffffff")
    lastname_inner_entry.configure(justify='center')
    lastname_inner_entry.configure(relief="flat")
    lastname_inner_entry.configure(selectbackground="#c4c4c4")


    phone_number_inner_entry = tkinter.Entry(Frame1)
    phone_number_inner_entry.place(relx=0.21, rely=0.27, height=53, relwidth=0.754)
    phone_number_inner_entry.configure(background="#dfe6e9")
    phone_number_inner_entry.configure(font=font10)
    phone_number_inner_entry.configure(justify='center')
    phone_number_inner_entry.configure(relief="flat")
    phone_number_inner_entry.configure(selectbackground="#c4c4c4")
    phone_number_inner_entry.configure(foreground="#ffffff")

    insurance_inner_entry = tkinter.Entry(Frame1)
    insurance_inner_entry.place(relx=0.21, rely=0.39, height=53, relwidth=0.754)
    insurance_inner_entry.configure(background="#dfe6e9")
    insurance_inner_entry.configure(font=font10)
    insurance_inner_entry.configure(foreground="#ffffff")
    insurance_inner_entry.configure(justify='center')
    insurance_inner_entry.configure(relief="flat")
    insurance_inner_entry.configure(selectbackground="#c4c4c4")


    gender_inner_entry = tkinter.Entry(Frame1)
    gender_inner_entry.place(relx=0.21, rely=0.51, height=53, relwidth=0.754)
    gender_inner_entry.configure(background="#dfe6e9")
    gender_inner_entry.configure(font=font10)
    gender_inner_entry.configure(foreground="#ffffff")
    gender_inner_entry.configure(justify='center')
    gender_inner_entry.configure(relief="flat")
    gender_inner_entry.configure(selectbackground="#c4c4c4")


    birthday_inner_entry = tkinter.Entry(Frame1)
    birthday_inner_entry.place(relx=0.21, rely=0.63, height=53, relwidth=0.754)
    birthday_inner_entry.configure(background="#dfe6e9")
    birthday_inner_entry.configure(font=font10)
    birthday_inner_entry.configure(foreground="#ffffff")
    birthday_inner_entry.configure(justify='center')
    birthday_inner_entry.configure(relief="flat")
    birthday_inner_entry.configure(selectbackground="#c4c4c4")

    password_inner_entry = tkinter.Entry(Frame1)
    password_inner_entry.place(relx=0.21, rely=0.75, height=53, relwidth=0.754)
    password_inner_entry.configure(background="#dfe6e9")
    password_inner_entry.configure(font=font10)
    password_inner_entry.configure(foreground="#ffffff")
    password_inner_entry.configure(justify='center')
    password_inner_entry.configure(relief="flat")
    password_inner_entry.configure(selectbackground="#c4c4c4")


    add_family_submit_button = tkinter.Button(Frame1, command=lambda: add_family_db(firstname_inner_entry.get(), lastname_inner_entry.get(), phone_number_inner_entry.get(), insurance_inner_entry.get(), password_inner_entry.get(), gender_inner_entry.get(), birthday_inner_entry.get()))
    add_family_submit_button.place(relx=0.038, rely=0.88, height=54, width=491)
    add_family_submit_button.configure(activebackground="#dfe6e9")
    add_family_submit_button.configure(background="#2d3436")
    add_family_submit_button.configure(font=font9)
    add_family_submit_button.configure(foreground="#ffffff")
    add_family_submit_button.configure(relief="flat")
    add_family_submit_button.configure(text='''Submit''')

    return

def delete_family_db(phone_number):
    if len(phone_number) == 0:
        return
    
    phone_number = phone_number[0][2]

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"DELETE FROM User WHERE phone_number = '{phone_number}';")
    cursor.execute(f"DELETE FROM User_User WHERE phone_number_2 = '{phone_number}';")

    connection.commit()
    connection.close()

    return

def update_family_db(first_name, last_name, insurance_id, phone_number, gender, birthday):
    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT insurance_id FROM Insurance WHERE name = '{insurance_id}';")
    insurance_id = cursor.fetchone()

    cursor.execute(f"SELECT gender_id FROM Gender WHERE title = '{gender}';")
    gender_id = cursor.fetchone()

    cursor.execute(f"UPDATE User SET first_name = '{first_name}', last_name = '{last_name}', insurance_id = {insurance_id[0]}, gender_id = {gender_id[0]}, birthday = '{birthday}' WHERE phone_number = '{phone_number}';")

    connection.commit()
    connection.close()

    update_family_page.destroy()
    
    return


def update_family_ui(phone_number):

    if len(phone_number) == 0:
        return

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font10 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global update_family_page

    update_family_page = tkinter.Toplevel()
    update_family_page.title('Update Member Page')
    update_family_page.attributes('-fullscreen', True)
    update_family_page.configure(background="#2d3436")

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT first_name, last_name, insurance_id, gender_id, birthday, photo FROM User WHERE phone_number = '{phone_number[0][2]}';")
    temp_user_data = cursor.fetchone()

    user_data = []
    for temp in temp_user_data:
        if temp != None:
            user_data.append(temp)
        else:
            user_data.append('')
    
    cursor.execute(f"SELECT name FROM Insurance WHERE insurance_id = {user_data[2]};")
    insurance_data = cursor.fetchone()

    cursor.execute(f"SELECT title FROM Gender WHERE gender_id = {user_data[3]};")
    gender_data = cursor.fetchone()

    back_button = tkinter.Button(update_family_page, command=update_family_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    if not (user_data[5] == None or len(user_data[5]) == 0):
        image_path=user_data[5]
        profile_image = Image.open(image_path)
        profile_image = profile_image.resize((150, 150), Image.ANTIALIAS)
        profile_image = ImageTk.PhotoImage(image=profile_image)
        profile_label = tkinter.Label(update_family_page,image=profile_image)
        profile_label.image = profile_image
        profile_label.place(relx=0.4675, rely=0.125)

    Frame1 = tkinter.Frame(update_family_page)
    Frame1.place(relx=0.365, rely=0.325, relheight=0.500, relwidth=0.273)
    Frame1.configure(relief='flat')
    Frame1.configure(borderwidth="2")
    Frame1.configure(background="#ffffff")

    firstname_label = tkinter.Label(Frame1)
    firstname_label.place(relx=0.0, rely=0.04, height=54, width=98)
    firstname_label.configure(background="#ffffff")
    firstname_label.configure(font=font9)
    firstname_label.configure(text='''First Name''')

    lastname_label = tkinter.Label(Frame1)
    lastname_label.place(relx=-0.019, rely=0.17, height=74, width=118)
    lastname_label.configure(activebackground="#f9f9f9")
    lastname_label.configure(background="#ffffff")
    lastname_label.configure(font=font9)
    lastname_label.configure(text='''Last Name''')

    insurance_label = tkinter.Label(Frame1)
    insurance_label.place(relx=0.0, rely=0.46, height=54, width=98)
    insurance_label.configure(activebackground="#f9f9f9")
    insurance_label.configure(background="#ffffff")
    insurance_label.configure(font=font9)
    insurance_label.configure(text='''Insurance''')

    phone_number_label = tkinter.Label(Frame1)
    phone_number_label.place(relx=0.0, rely=0.32, height=54, width=108)
    phone_number_label.configure(activebackground="#f9f9f9")
    phone_number_label.configure(background="#ffffff")
    phone_number_label.configure(font=font9)
    phone_number_label.configure(text='''Phone Number''')

    gender_label = tkinter.Label(Frame1)
    gender_label.place(relx=0.0, rely=0.6, height=54, width=108)
    gender_label.configure(activebackground="#f9f9f9")
    gender_label.configure(background="#ffffff")
    gender_label.configure(font=font9)
    gender_label.configure(text='''Gender''')

    birthday_label = tkinter.Label(Frame1)
    birthday_label.place(relx=0.0, rely=0.74, height=54, width=108)
    birthday_label.configure(activebackground="#f9f9f9")
    birthday_label.configure(background="#ffffff")
    birthday_label.configure(font=font9)
    birthday_label.configure(text='''Birthday''')

    firstname_entry = tkinter.Entry(Frame1)
    firstname_entry.place(relx=0.21, rely=0.04, height=53, relwidth=0.754)
    firstname_entry.configure(background="#dfe6e9")
    firstname_entry.configure(font=font10)
    firstname_entry.configure(foreground="#ffffff")
    firstname_entry.configure(justify='center')
    firstname_entry.configure(relief="flat")
    firstname_entry.insert(0, user_data[0])

    lastname_entry = tkinter.Entry(Frame1)
    lastname_entry.place(relx=0.21, rely=0.18, height=53, relwidth=0.754)
    lastname_entry.configure(background="#dfe6e9")
    lastname_entry.configure(cursor="fleur")
    lastname_entry.configure(font=font10)
    lastname_entry.configure(foreground="#ffffff")
    lastname_entry.configure(justify='center')
    lastname_entry.configure(relief="flat")
    lastname_entry.configure(selectbackground="#c4c4c4")
    lastname_entry.insert(0, user_data[1])

    phone_number_entry = tkinter.Entry(Frame1)
    phone_number_entry.place(relx=0.21, rely=0.32, height=53, relwidth=0.754)
    phone_number_entry.configure(background="#dfe6e9")
    phone_number_entry.configure(font=font10)
    phone_number_entry.configure(justify='center')
    phone_number_entry.configure(relief="flat")
    phone_number_entry.configure(selectbackground="#c4c4c4")
    phone_number_entry.insert(0, phone_number[0][2])
    phone_number_entry.configure(state='readonly')
    phone_number_entry.configure(foreground="#ffffff")

    insurance_entry = tkinter.Entry(Frame1)
    insurance_entry.place(relx=0.21, rely=0.46, height=53, relwidth=0.754)
    insurance_entry.configure(background="#dfe6e9")
    insurance_entry.configure(font=font10)
    insurance_entry.configure(foreground="#ffffff")
    insurance_entry.configure(justify='center')
    insurance_entry.configure(relief="flat")
    insurance_entry.configure(selectbackground="#c4c4c4")
    if insurance_data != None:
        insurance_entry.insert(0, insurance_data[0])

    gender_entry = tkinter.Entry(Frame1)
    gender_entry.place(relx=0.21, rely=0.6, height=53, relwidth=0.754)
    gender_entry.configure(background="#dfe6e9")
    gender_entry.configure(font=font10)
    gender_entry.configure(foreground="#ffffff")
    gender_entry.configure(justify='center')
    gender_entry.configure(relief="flat")
    gender_entry.configure(selectbackground="#c4c4c4")
    if gender_data != None:
        gender_entry.insert(0, gender_data[0])

    birthday_entry = tkinter.Entry(Frame1)
    birthday_entry.place(relx=0.21, rely=0.74, height=53, relwidth=0.754)
    birthday_entry.configure(background="#dfe6e9")
    birthday_entry.configure(font=font10)
    birthday_entry.configure(foreground="#ffffff")
    birthday_entry.configure(justify='center')
    birthday_entry.configure(relief="flat")
    birthday_entry.configure(selectbackground="#c4c4c4")
    birthday_entry.insert(0, user_data[4])
    

    connection.commit()
    connection.close()

    update_family_submit_button = tkinter.Button(Frame1, command=lambda: update_family_db(firstname_entry.get(), lastname_entry.get(), insurance_entry.get(), phone_number[0][2], gender_entry.get(), birthday_entry.get()))
    update_family_submit_button.place(relx=0.038, rely=0.88, height=54, width=491)
    update_family_submit_button.configure(activebackground="#dfe6e9")
    update_family_submit_button.configure(background="#2d3436")
    update_family_submit_button.configure(font=font9)
    update_family_submit_button.configure(foreground="#ffffff")
    update_family_submit_button.configure(relief="flat")
    update_family_submit_button.configure(text='''Submit''')

    return

def add_family_ui():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global add_family_page

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT first_name, last_name, phone_number, insurance_id, gender_id, birthday FROM USER WHERE phone_number IN (SELECT phone_number_2 FROM User, User_User WHERE User.phone_number = User_User.phone_number_1 AND User.phone_number = '{current_phone_number}')");
    family_members = cursor.fetchall()

    insurance=[]
    for i in range(len(family_members)):
        cursor.execute(f"SELECT name FROM Insurance WHERE insurance_id = '{family_members[i][3]}';");
        insurance.append(cursor.fetchone())

    gender = []
    for i in range(len(family_members)):
        cursor.execute(f"SELECT title FROM Gender WHERE gender_id = '{family_members[i][4]}';");
        gender.append(cursor.fetchone())

    connection.commit()
    connection.close()

    add_family_page = tkinter.Tk()
    add_family_page.title('Add Family')
    add_family_page.attributes('-fullscreen', True)
    add_family_page.configure(background="#2d3436")

    back_button = tkinter.Button(add_family_page, command=add_family_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    Frame1 = tkinter.Frame(add_family_page)
    Frame1.place(relx=0.208, rely=0.644, relheight=0.132, relwidth=0.586)
    Frame1.configure(relief='flat')
    Frame1.configure(borderwidth="2")

    delete_family_button = tkinter.Button(Frame1, command=lambda: delete_family_db([family_members[add_family_listbox.curselection()[0]] for _ in range(1) if 0 != len(add_family_listbox.curselection())]))
    delete_family_button.place(relx=0.249, rely=-0.074, height=154, width=291)
    delete_family_button.configure(activebackground="#f9f9f9")
    delete_family_button.configure(background="#ffffff")
    delete_family_button.configure(borderwidth="5")
    delete_family_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    delete_family_button.configure(text='''Delete Member''')

    update_family_button = tkinter.Button(Frame1, command=lambda: update_family_ui([family_members[add_family_listbox.curselection()[0]] for _ in range(1) if 0 != len(add_family_listbox.curselection())])) 
    update_family_button.place(relx=0.507, rely=-0.074, height=154, width=281)
    update_family_button.configure(activebackground="#f9f9f9")
    update_family_button.configure(background="#ffffff")
    update_family_button.configure(borderwidth="5")
    update_family_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    update_family_button.configure(text='''Update Member''')

    appointment_family_button = tkinter.Button(Frame1, command=appointment_family_ui)
    appointment_family_button.place(relx=0.756, rely=-0.074, height=154, width=281)
    appointment_family_button.configure(activebackground="#f9f9f9")
    appointment_family_button.configure(background="#ffffff")
    appointment_family_button.configure(borderwidth="5")
    appointment_family_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    appointment_family_button.configure(text='''Family Appointments''')

    add_family_button = tkinter.Button(Frame1, command=add_family_inner_ui)
    add_family_button.place(relx=-0.009, rely=-0.074, height=154, width=291)
    add_family_button.configure(activebackground="#f9f9f9")
    add_family_button.configure(background="#ffffff")
    add_family_button.configure(borderwidth="5")
    add_family_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    add_family_button.configure(text='''Add Member''')

    add_family_listbox = tkinter.Listbox(add_family_page)
    add_family_listbox.place(relx=0.208, rely=0.205, relheight=0.416, relwidth=0.585)
    add_family_listbox.configure(background="white")
    add_family_listbox.configure(cursor="dotbox")
    add_family_listbox.configure(font=font9)
    add_family_listbox.configure(highlightbackground="#dfe6e9")
    add_family_listbox.configure(justify='center')
    add_family_listbox.configure(relief="flat")
    add_family_listbox.configure(selectbackground="#dfe6e9")
    add_family_listbox.configure(setgrid="1")

    for i in range(len(family_members)):

        firstname_text = f'{family_members[i][0]}'
        lastname_text = f'{family_members[i][1]}'
        phone_number_text = f'{family_members[i][2]}'
        insurance_text = f'{insurance[i][0]}'
        gender_text = f'{gender[i][0]}'
        birthday_text = f'{family_members[i][5]}'

        for i in range(15):
            if i == len(firstname_text) - 1:
                firstname_text += ' '
            if i == len(lastname_text) - 1:
                lastname_text += ' '
            if i == len(phone_number_text) - 1:
                phone_number_text += ' '
            if i == len(insurance_text) - 1:
                insurance_text += ' '
            if i == len(gender_text) - 1:
                gender_text += ' '
            if i == len(birthday_text) - 1:
                birthday_text += ' '

        add_family_listbox.insert(tkinter.END, f'First Name: {firstname_text}| Last Name: {lastname_text}| Phone Number: {phone_number_text}| Insurance: {insurance_text}| Gender: {gender_text}| Birthday: {birthday_text}')

    return

def my_appointments_ui():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global my_appointments_page

    my_appointments_page = tkinter.Tk()
    my_appointments_page.attributes('-fullscreen', True)
    my_appointments_page.configure(background="#2d3436")

    back_button = tkinter.Button(my_appointments_page, command=my_appointments_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    my_appointments_listbox = tkinter.Listbox(my_appointments_page)
    my_appointments_listbox.place(relx=0.050, rely=0.205, relheight=0.552, relwidth=0.9)
    my_appointments_listbox.configure(cursor="spider")
    my_appointments_listbox.configure(font=font9)
    my_appointments_listbox.configure(justify='center')
    my_appointments_listbox.configure(relief="flat")
    my_appointments_listbox.configure(selectbackground="#dfe6e9")
    my_appointments_listbox.configure(setgrid="1")

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT Appointment.*, first_name, last_name FROM Appointment, User WHERE User.phone_number = Appointment.phone_number AND User.phone_number = '{current_phone_number}';")
    my_appointments_names = cursor.fetchall()

    for my_appointments_name in my_appointments_names:

        appointment_data = []
        doctor_council = my_appointments_name[3]
        doctor_username = my_appointments_name[1]

        cursor.execute(f"SELECT first_name, last_name FROM Doctor WHERE medical_council_code = '{doctor_council}' AND username = '{doctor_username}';")
        doctor_data = cursor.fetchone()


        first_name_text = f'{my_appointments_name[-2]}'
        last_name_text = f'{my_appointments_name[-1]}'
        phone_number_text= f'{current_phone_number}'
        appointment_date_text = f'{my_appointments_name[6]}'
        doctor_firstname_text = f'{doctor_data[0]}'
        doctor_lastname_text = f'{doctor_data[1]}'
    
        for i in range(15):
            if i == len(appointment_date_text) - 1:
                appointment_date_text += ' '
            if i == len(doctor_firstname_text) - 1:
                doctor_firstname_text += ' '
            if i == len(doctor_lastname_text) - 1:
                doctor_lastname_text += ' '
            if i == len(phone_number_text) - 1:
                phone_number_text += ' '
            if i == len(first_name_text) - 1:
                first_name_text += ' '
            if i == len(last_name_text) - 1:
                last_name_text += ' '

        my_appointments_listbox.insert(tkinter.END, f'Appointment Date: {appointment_date_text}| Doctor First Name: {doctor_firstname_text}| Doctor Last Name: {doctor_lastname_text}| Patient Phone Number: {phone_number_text}| Patient First Name: {first_name_text}| Patient Last Name: {last_name_text}')


    connection.commit()
    connection.close()

    return


def find_appointment():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global find_appointment_page

    find_appointment_page = tkinter.Tk()
    find_appointment_page.title('Search an Speciality')
    find_appointment_page.attributes('-fullscreen', True)
    find_appointment_page.configure(background="#2d3436")

    back_button = tkinter.Button(find_appointment_page, command=find_appointment_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    Frame1 = tkinter.Frame(find_appointment_page)
    Frame1.place(relx=0.2, rely=0.585, relheight=0.085, relwidth=0.6)
    Frame1.configure(relief='flat')
    Frame1.configure(borderwidth="2")
    Frame1.configure(background="#ffffff")

    appointment_id_entry = tkinter.Entry(Frame1)
    appointment_id_entry.place(relx=0.05, rely=0.155, height=54, relwidth=0.4)
    appointment_id_entry.configure(background="#dfe6e9")
    appointment_id_entry.configure(font=font9)
    appointment_id_entry.configure(justify='center')
    appointment_id_entry.configure(relief="flat")
    appointment_id_entry.configure(selectbackground="#c4c4c4")
    appointment_id_entry.configure(foreground="#ffffff")
    appointment_id_entry.insert(0, 'Appointment Id')

    find_button = tkinter.Button(Frame1, command=lambda: find_appointment_db(appointment_id_entry.get()))
    find_button.place(relx=0.55, rely=0.155, height=54, relwidth=0.4)
    find_button.configure(activebackground="#dfe6e9")
    find_button.configure(background="#2d3436")
    find_button.configure(font=font10)
    find_button.configure(foreground="#ffffff")
    find_button.configure(relief="flat")
    find_button.configure(text='''Search Doctor''')

    find_appointment_listbox = tkinter.Listbox(find_appointment_page)
    find_appointment_listbox.place(relx=0.2, rely=0.156, relheight=0.377, relwidth=0.6)
    find_appointment_listbox.configure(background="white")
    find_appointment_listbox.configure(font=font9)
    find_appointment_listbox.configure(justify='center')
    find_appointment_listbox.configure(relief="flat")
    find_appointment_listbox.configure(selectbackground="#dfe6e9")
    find_appointment_listbox.configure(setgrid="1")
    
    def find_appointment_db(ap_id):
        
        find_appointment_listbox.delete(0, tkinter.END)

        connection = sqlite3.connect('TabibYab.db')
        cursor = connection.cursor()
        cursor.execute(f"SELECT Distinct Appointment.appointment_id, phone_number, start_time, appointment_date, getter_phone_number FROM DOH, Doctor, Appointment WHERE DOH.username = Appointment.username AND DOH.medical_council_code=Appointment.medical_council_code AND DOH.medical_council_code=Doctor.medical_council_code AND Appointment.phone_number = '{current_phone_number}' AND Appointment.appointment_id = '{ap_id}';  ")
        found = cursor.fetchone()
        
        connection.commit()
        connection.close()

        if found == None:
            find_appointment_listbox.insert(tkinter.END , "Appointment Not Found")

        else:
            appointment_id_text = f'{found[0]}'
            phone_number_text= f'{found[1]}'
            start_time_text = f'{found[2]}'
            appointment_date_text = f'{found[3]}'
            getter_phone_number_text = f'{found[4]}'
        
            for i in range(10):
                if i == len(appointment_id_text) - 1:
                    appointment_id_text += ' '
                if i == len(phone_number_text) - 1:
                    phone_number_text += ' '
                if i == len(start_time_text) - 1:
                    start_time_text += ' '
                if i == len(appointment_date_text) - 1:
                    appointment_date_text += ' '
                if i == len(getter_phone_number_text) - 1:
                    getter_phone_number_text += ' '

            find_appointment_listbox.insert(tkinter.END, f'Appointment Id: {appointment_id_text}| Phone Number: {phone_number_text}| Appointment Date: {appointment_date_text}| Start Time: {start_time_text}| Getter Phone Number: {getter_phone_number_text}')
    return

def profile_ui():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global profile_page

    profile_page = tkinter.Tk()
    profile_page.title('Profile Page')
    profile_page.attributes('-fullscreen', True)
    profile_page.configure(background="#2d3436")

    back_button = tkinter.Button(profile_page, command=profile_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    Frame1 = tkinter.Frame(profile_page)
    Frame1.place(relx=0.193, rely=0.4, relheight=0.132, relwidth=0.586)
    Frame1.configure(relief='flat')
    Frame1.configure(borderwidth="2")

    add_family_button = tkinter.Button(Frame1, command=add_family_ui)
    add_family_button.place(relx=0.2, rely=-0.074, height=164, relwidth=0.2)
    add_family_button.configure(activebackground="#f9f9f9")
    add_family_button.configure(background="#ffffff")
    add_family_button.configure(borderwidth="5")
    add_family_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    add_family_button.configure(text='''View Members''')

    my_appointments_button = tkinter.Button(Frame1, command=my_appointments_ui)
    my_appointments_button.place(relx=0.4, rely=-0.074, height=164, relwidth=0.2)
    my_appointments_button.configure(activebackground="#f9f9f9")
    my_appointments_button.configure(background="#ffffff")
    my_appointments_button.configure(borderwidth="5")
    my_appointments_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    my_appointments_button.configure(text='''My Appointments''')

    my_appointments_by_others_button = tkinter.Button(Frame1, command=my_appointments_by_others_ui)
    my_appointments_by_others_button.place(relx=0.6, rely=-0.074, height=164, relwidth=0.2)
    my_appointments_by_others_button.configure(activebackground="#f9f9f9")
    my_appointments_by_others_button.configure(background="#ffffff")
    my_appointments_by_others_button.configure(borderwidth="5")
    my_appointments_by_others_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    my_appointments_by_others_button.configure(text='''Appointments By Others''')

    edit_profile_button = tkinter.Button(Frame1, command=edit_profile_ui)
    edit_profile_button.place(relx=-0.01, rely=-0.074, height=164, relwidth=0.21)
    edit_profile_button.configure(activebackground="#f9f9f9")
    edit_profile_button.configure(background="#ffffff")
    edit_profile_button.configure(borderwidth="5")
    edit_profile_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    edit_profile_button.configure(text='''Edit Profile''')

    find_appointments_button = tkinter.Button(Frame1, command=find_appointment)
    find_appointments_button.place(relx=0.8, rely=-0.074, height=164, relwidth=0.21)
    find_appointments_button.configure(activebackground="#f9f9f9")
    find_appointments_button.configure(background="#ffffff")
    find_appointments_button.configure(borderwidth="5")
    find_appointments_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    find_appointments_button.configure(text='''Find Appointment''')

    return


def get_appointment(doctor, username, price):

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global appointment_page

    appointment_page = tkinter.Tk()
    appointment_page.title('Set Appointment')
    appointment_page.attributes('-fullscreen', True)
    appointment_page.configure(background="#2d3436")
    
    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT Work_Hour.start_hour, Work_Hour.end_hour,  Work_Hour.w_date, DOH.DOH_id, 0 FROM Work_Hour, DOH, Doctor WHERE Doctor.medical_council_code = DOH.medical_council_code AND Doctor.username = DOH.username AND DOH.DOH_id = Work_Hour.DOH_id AND Doctor.medical_council_code='{doctor[3]}' AND Doctor.username = '{username}';")
    times = cursor.fetchall()

    cursor.execute(f"SELECT Work_Hour.start_hour, Work_Hour.end_hour,  Work_Hour.w_date, 0, DHH.DHH_id FROM Work_Hour, DHH, Doctor WHERE Doctor.medical_council_code = DHH.medical_council_code AND Doctor.username = DHH.username AND DHH.DHH_id = Work_Hour.DHH_id AND Doctor.medical_council_code='{doctor[3]}' AND Doctor.username = '{username}';")
    times += cursor.fetchall()
    
    connection.commit()
    connection.close()
    
    dates = []
    years = []
    months = []
    days = []
    
    for i in range(len(times)):
        dates.append(times[i][2])
        
    for i in range(len(dates)):
        if (dates[i].split("/"))[0] not in years:
            years.append((dates[i].split("/"))[0])

    Frame1_2 = tkinter.Frame(appointment_page)
    Frame1_2.place(relx=0.052, rely=0.215, relheight=0.502, relwidth=0.169)
    Frame1_2.configure(relief='flat')
    Frame1_2.configure(borderwidth="2")
    Frame1_2.configure(background="#ffffff")

    select_years = tkinter.Button(Frame1_2, command=lambda: selected_year(years[all_years_listbox.curselection()[0]] ))
    select_years.place(relx=0.031, rely=0.835, height=74, width=301)
    select_years.configure(activebackground="#dfe6e9")
    select_years.configure(background="#2d3436")
    select_years.configure(font=font10)
    select_years.configure(foreground="#ffffff")
    select_years.configure(relief="flat")
    select_years.configure(text='''Select Year''')

    all_years_listbox = tkinter.Listbox(appointment_page)
    all_years_listbox.place(relx=0.057, rely=0.224, relheight=0.396, relwidth=0.158)
    all_years_listbox.configure(background="white")
    all_years_listbox.configure(font=font9)
    all_years_listbox.configure(justify='center')
    all_years_listbox.configure(relief="flat")
    all_years_listbox.configure(selectbackground="#dfe6e9")
    
    for year in years:
        all_years_listbox.insert(tkinter.END, year)
 
    def selected_year(y):

        for i in range(len(dates)):
            if (dates[i].split("/"))[0] == y and (dates[i].split("/"))[1] not in months:
                months.append((dates[i].split("/"))[1])
    
        Frame1_1 = tkinter.Frame(appointment_page)
        Frame1_1.place(relx=0.234, rely=0.215, relheight=0.502, relwidth=0.169)
        Frame1_1.configure(relief='flat')
        Frame1_1.configure(borderwidth="2")
        Frame1_1.configure(background="#ffffff")

        select_months = tkinter.Button(Frame1_1, command=lambda: selected_month(months[all_months_listbox.curselection()[0]] ))
        select_months.place(relx=0.031, rely=0.835, height=74, width=301)
        select_months.configure(activebackground="#dfe6e9")
        select_months.configure(background="#2d3436")
        select_months.configure(font="-family {ubvazir} -size 10 -weight bold")
        select_months.configure(foreground="#ffffff")
        select_months.configure(relief="flat")
        select_months.configure(text='''Select Month''')

        all_months_listbox = tkinter.Listbox(Frame1_1)
        all_months_listbox.place(relx=0.031, rely=0.019, relheight=0.788, relwidth=0.935)
        all_months_listbox.configure(background="white")
        all_months_listbox.configure(font="-family {DejaVu Sans Mono} -size 10 -weight bold")
        all_months_listbox.configure(justify='center')
        all_months_listbox.configure(relief="flat")
        all_months_listbox.configure(selectbackground="#dfe6e9")

        for month in months:
            all_months_listbox.insert(tkinter.END, month)
        
        def selected_month(m):
            for i in range(len(dates)):
                if (dates[i].split("/"))[0] == y and (dates[i].split("/"))[1] == m and (dates[i].split("/"))[2] not in days:
                    days.append((dates[i].split("/"))[2])
            
            Frame1 = tkinter.Frame(appointment_page)
            Frame1.place(relx=0.417, rely=0.215, relheight=0.502, relwidth=0.169)
            Frame1.configure(relief='flat')
            Frame1.configure(borderwidth="2")
            Frame1.configure(background="#ffffff")

            all_days_listbox = tkinter.Listbox(Frame1)
            all_days_listbox.place(relx=0.031, rely=0.019, relheight=0.788, relwidth=0.935)
            all_days_listbox.configure(background="white")
            all_days_listbox.configure(font="-family {DejaVu Sans Mono} -size 10 -weight bold")
            all_days_listbox.configure(justify='center')
            all_days_listbox.configure(relief="flat")
            all_days_listbox.configure(selectbackground="#dfe6e9")

            select_days = tkinter.Button(Frame1, command=lambda: selected_day(days[all_days_listbox.curselection()[0]] ))
            select_days.place(relx=0.031, rely=0.835, height=74, width=301)
            select_days.configure(activebackground="#dfe6e9")
            select_days.configure(background="#2d3436")
            select_days.configure(font="-family {ubvazir} -size 10 -weight bold")
            select_days.configure(foreground="#ffffff")
            select_days.configure(relief="flat")
            select_days.configure(text='''Select Day''')

            for day in days:
                all_days_listbox.insert(tkinter.END, day)
            
            
            def selected_day(d):
                selected_date = f'{str(y)}/{str(m)}/{str(d)}'
                
                for time in times:
                    if time[2] == selected_date:
                        start = time[0]
                        end = time[1]
                        
                    
                all_times = []
                start_minute = int((start.split(":"))[1])
                end_minute = int((end.split(":"))[1])
                start_time = int((start.split(":"))[0])
                end_time = int((end.split(":"))[0])
                if(end_minute == 30):
                    end_time += 0.5
                if(start_minute == 30):
                    start_time += 0.5
                
                while start_time <= end_time:
                    all_times.append(start_time)
                    start_time += 0.5

                connection = sqlite3.connect('TabibYab.db')
                cursor = connection.cursor()

                cursor.execute(f"SELECT start_time FROM Appointment WHERE medical_council_code = '{doctor[3]}' AND appointment_date = '{selected_date}' AND username = '{username}';")
                not_available_times = cursor.fetchall()
                
                connection.commit()
                connection.close()

                not_available_times_intger = []
                for i in range(len(not_available_times)):
                    hour_not_available = int((not_available_times[i][0].split(":"))[0])
                    minute_not_available = int((not_available_times[i][0].split(":"))[1])
                    if minute_not_available == 30:
                        hour_not_available = hour_not_available + 0.5
                    not_available_times_intger.append(hour_not_available)
                
                available_times = [all_time for all_time in all_times if all_time not in not_available_times_intger]
                
                Frame1_3 = tkinter.Frame(appointment_page)
                Frame1_3.place(relx=0.599, rely=0.215, relheight=0.502, relwidth=0.169)
                Frame1_3.configure(relief='flat')
                Frame1_3.configure(borderwidth="2")
                Frame1_3.configure(background="#ffffff")

                all_times_listbox = tkinter.Listbox(Frame1_3)
                all_times_listbox.place(relx=0.031, rely=0.019, relheight=0.788, relwidth=0.935)
                all_times_listbox.configure(background="white")
                all_times_listbox.configure(font="-family {DejaVu Sans Mono} -size 10 -weight bold")
                all_times_listbox.configure(justify='center')
                all_times_listbox.configure(relief="flat")
                all_times_listbox.configure(selectbackground="#dfe6e9")

                for available_time in available_times:
                    all_times_listbox.insert(tkinter.END, available_time)

                selecet_time = tkinter.Button(Frame1_3, command=lambda: selected_time(available_times[all_times_listbox.curselection()[0]]))
                selecet_time.place(relx=0.031, rely=0.835, height=74, width=301)
                selecet_time.configure(activebackground="#dfe6e9")
                selecet_time.configure(background="#2d3436")
                selecet_time.configure(font="-family {ubvazir} -size 10 -weight bold")
                selecet_time.configure(foreground="#ffffff")
                selecet_time.configure(relief="flat")
                selecet_time.configure(text='''Select Time''')
                
                def selected_time(selected_time):
                    if selected_time % 1 != 0:
                        selected_time = f'{int(selected_time)}:30'
                    else:
                        selected_time = f'{int(selected_time)}:00'
                    
                    for time in times:
                        if time[0] <= selected_time and selected_time <=time[1] and selected_date == time[2]:
                            DOH_id = time[3]
                            DHH_id = time[4]
                        
                    connection = sqlite3.connect('TabibYab.db')
                    cursor = connection.cursor()

                    cursor.execute(f"SELECT first_name, last_name, insurance_id, User_User.phone_number_2 FROM User, User_User WHERE User.phone_number = User_User.phone_number_2 AND User_User.phone_number_1='{current_phone_number}';")
                    family_members = cursor.fetchall() 

                    connection.commit()
                    connection.close()
                    
                    connection = sqlite3.connect('TabibYab.db')
                    cursor = connection.cursor()
                    cursor.execute(f"SELECT first_name, last_name, insurance_id, phone_number FROM User WHERE User.phone_number = '{current_phone_number}';")
                    user_info=cursor.fetchall()
                    
                    connection.commit()
                    connection.close()
                    
                    
                    family_members += user_info

                    Frame1_4 = tkinter.Frame(appointment_page)
                    Frame1_4.place(relx=0.781, rely=0.215, relheight=0.502, relwidth=0.169)
                    Frame1_4.configure(relief='flat')
                    Frame1_4.configure(borderwidth="2")
                    Frame1_4.configure(background="#ffffff")

                    all_people_listbox = tkinter.Listbox(Frame1_4)
                    all_people_listbox.place(relx=0.031, rely=0.019, relheight=0.788, relwidth=0.935)
                    all_people_listbox.configure(background="white")
                    all_people_listbox.configure(font="-family {DejaVu Sans Mono} -size 10 -weight bold")
                    all_people_listbox.configure(justify='center')
                    all_people_listbox.configure(relief="flat")
                    all_people_listbox.configure(selectbackground="#dfe6e9")

                    selecet_people = tkinter.Button(Frame1_4, command=lambda: selected_people(family_members[all_people_listbox.curselection()[0]], DOH_id, DHH_id))
                    selecet_people.place(relx=0.031, rely=0.835, height=74, width=301)
                    selecet_people.configure(activebackground="#dfe6e9")
                    selecet_people.configure(background="#2d3436")
                    selecet_people.configure(cursor="fleur")
                    selecet_people.configure(font="-family {ubvazir} -size 10 -weight bold")
                    selecet_people.configure(foreground="#ffffff")
                    selecet_people.configure(relief="flat")
                    selecet_people.configure(text='''Select Person''')

                    for family_member in family_members:
                        person_name = f'{family_member[0]} {family_member[1]} | {family_member[3]}'
                        all_people_listbox.insert(tkinter.END, person_name)
                    
                    def selected_people(person, DOH_id, DHH_id):
                        
                        connection = sqlite3.connect('TabibYab.db')
                        cursor = connection.cursor()

                        cursor.execute(f"INSERT INTO Payment (cost, payment_code) VALUES ('{price}', '{20}');")
                        payment = cursor.fetchall()

                        connection.commit()
                        connection.close()
                        
                        connection = sqlite3.connect('TabibYab.db')
                        cursor = connection.cursor()

                        cursor.execute(f"SELECT payment_id FROM Payment")
                        payment=cursor.fetchall()

                        connection.commit()
                        connection.close()
                       
                        connection = sqlite3.connect('TabibYab.db')
                        cursor = connection.cursor()

                        if DOH_id != 0:
                            cursor.execute(f"INSERT INTO Appointment (username, phone_number, medical_council_code, payment_id, start_time, appointment_date, getter_phone_number, DOH_id) VALUES ('{username}', '{person[3]}', '{doctor[3]}', '{payment[-1][0]}', '{selected_time}', '{selected_date}', '{current_phone_number}', '{DOH_id}');")
                        elif DHH_id != 0:
                            cursor.execute(f"INSERT INTO Appointment (username, phone_number, medical_council_code, payment_id, start_time, appointment_date, getter_phone_number, DHH_id) VALUES ('{username}', '{person[3]}', '{doctor[3]}', '{payment[-1][0]}', '{selected_time}', '{selected_date}', '{current_phone_number}', {DHH_id});")
                        
                        appointment = cursor.fetchall() 
                        
                        connection.commit()

                        cursor.execute(f"SELECT appointment_id FROM Appointment WHERE username = '{username}' AND phone_number = '{person[3]}' AND medical_council_code = '{doctor[3]}' AND payment_id = '{payment[-1][0]}' AND start_time = '{selected_time}' AND appointment_date = '{selected_date}' AND getter_phone_number = '{current_phone_number}'")

                        messagebox.showinfo('Appointment ID', f"You Appointmet ID is {cursor.fetchone()[0]}")

                        appointment_page.destroy()

                        connection.close()
                    
    return

def doctor_search_db(firstname, lastname, names_found_listbox):
    
    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT first_name, last_name, name, medical_council_code FROM Doctor, Speciality WHERE Doctor.speciality_id = Speciality.speciality_id AND first_name LIKE '%{firstname}%' AND last_name LIKE '%{lastname}%'")
    names_found = cursor.fetchall()
    
    names_found_listbox.delete(0, tkinter.END)

    for i in range(len(names_found)):

        firstname_text = f'{names_found[i][0]}'
        lastname_text = f'{names_found[i][1]}'
        speciality_text = f'{names_found[i][2]}'
        council_text = f'{names_found[i][3]}'

        for i in range(10):
            if i == len(firstname_text) - 1:
                firstname_text += ' '
            if i == len(lastname_text) - 1:
                lastname_text += ' '
            if i == len(speciality_text) - 1:
                speciality_text += ' '
            if i == len(council_text) - 1:
                council_text += ' '

        names_found_listbox.insert(tkinter.END, f'First Name: {firstname_text}| Last Name: {lastname_text}| Speciality: {speciality_text}| Medical Council Code: {council_text}\n')
    
    connection.commit()
    connection.close()

    return

def doctor_search_ui():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global doctor_search_page

    doctor_search_page = tkinter.Tk()
    doctor_search_page.title('Search a Doctor')
    doctor_search_page.attributes('-fullscreen', True)
    doctor_search_page.configure(background="#2d3436")

    back_button = tkinter.Button(doctor_search_page, command=doctor_search_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    names_found_listbox = tkinter.Listbox(doctor_search_page)
    names_found_listbox.place(relx=0.271, rely=0.156, relheight=0.377, relwidth=0.45)
    names_found_listbox.configure(background="white")
    names_found_listbox.configure(font=font9)
    names_found_listbox.configure(justify='center')
    names_found_listbox.configure(relief="flat")
    names_found_listbox.configure(selectbackground="#dfe6e9")
    names_found_listbox.configure(setgrid="1")

    Frame1 = tkinter.Frame(doctor_search_page)
    Frame1.place(relx=0.271, rely=0.585, relheight=0.151, relwidth=0.451)
    Frame1.configure(relief='flat')
    Frame1.configure(borderwidth="2")
    Frame1.configure(background="#ffffff")

    firstname_entry = tkinter.Entry(Frame1)
    firstname_entry.place(relx=0.035, rely=0.129, height=53, relwidth=0.435)
    firstname_entry.configure(background="#dfe6e9")
    firstname_entry.configure(font=font9)
    firstname_entry.configure(justify='center')
    firstname_entry.configure(relief="flat")
    firstname_entry.configure(selectbackground="#c4c4c4")
    firstname_entry.configure(foreground="#ffffff")
    firstname_entry.insert(0, 'First Name')

    set_appointment_button = tkinter.Button(Frame1)
    set_appointment_button.place(relx=0.543, rely=0.516, height=54, width=371)
    set_appointment_button.configure(activebackground="#dfe6e9")
    set_appointment_button.configure(background="#2d3436")
    set_appointment_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    set_appointment_button.configure(foreground="#ffffff")
    set_appointment_button.configure(relief="flat")
    set_appointment_button.configure(text='''Set Appointment''')

    lastname_entry = tkinter.Entry(Frame1)
    lastname_entry.place(relx=0.035, rely=0.516, height=53, relwidth=0.435)
    lastname_entry.configure(background="#dfe6e9")
    lastname_entry.configure(font="-family {DejaVu Sans Mono} -size 10 -weight bold")
    lastname_entry.configure(justify='center')
    lastname_entry.configure(relief="flat")
    lastname_entry.configure(selectbackground="#c4c4c4")
    lastname_entry.configure(foreground="#ffffff")
    lastname_entry.insert(0, 'Last Name')

    search_doctor_button = tkinter.Button(Frame1, command=lambda: doctor_search_db(firstname_entry.get(), lastname_entry.get(), names_found_listbox))
    search_doctor_button.place(relx=0.543, rely=0.129, height=54, width=371)
    search_doctor_button.configure(activebackground="#dfe6e9")
    search_doctor_button.configure(background="#2d3436")
    search_doctor_button.configure(font=font10)
    search_doctor_button.configure(foreground="#ffffff")
    search_doctor_button.configure(relief="flat")
    search_doctor_button.configure(text='''Search Doctor''')

    return

def speciality_search_db(speciality_name, specialities_found_listbox):
    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT first_name, last_name, name, medical_council_code FROM Doctor, Speciality WHERE Doctor.speciality_id = Speciality.speciality_id AND name LIKE '%{speciality_name}%'")
    specialities_found = cursor.fetchall()

    specialities_found_listbox.delete(0, tkinter.END)

    for i in range(len(specialities_found)):

        firstname_text = f'{specialities_found[i][0]}'
        lastname_text = f'{specialities_found[i][1]}'
        speciality_text = f'{specialities_found[i][2]}'
        council_text = f'{specialities_found[i][3]}'

        for i in range(10):
            if i == len(firstname_text) - 1:
                firstname_text += ' '
            if i == len(lastname_text) - 1:
                lastname_text += ' '
            if i == len(speciality_text) - 1:
                speciality_text += ' '
            if i == len(council_text) - 1:
                council_text += ' '

        specialities_found_listbox.insert(tkinter.END, f'First Name: {firstname_text}| Last Name: {lastname_text}| Speciality: {speciality_text}| Medical Council Code: {council_text}\n')

    connection.commit()
    connection.close()

    return

def speciality_search_ui():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global speciality_search_page

    speciality_search_page = tkinter.Tk()
    speciality_search_page.title('Search an Speciality')
    speciality_search_page.attributes('-fullscreen', True)
    speciality_search_page.configure(background="#2d3436")

    back_button = tkinter.Button(speciality_search_page, command=speciality_search_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    specialities_found_listbox = tkinter.Listbox(speciality_search_page)
    specialities_found_listbox.place(relx=0.271, rely=0.156, relheight=0.377, relwidth=0.45)
    specialities_found_listbox.configure(background="white")
    specialities_found_listbox.configure(font=font9)
    specialities_found_listbox.configure(justify='center')
    specialities_found_listbox.configure(relief="flat")
    specialities_found_listbox.configure(selectbackground="#dfe6e9")
    specialities_found_listbox.configure(setgrid="1")

    Frame1 = tkinter.Frame(speciality_search_page)
    Frame1.place(relx=0.271, rely=0.585, relheight=0.151, relwidth=0.451)
    Frame1.configure(relief='flat')
    Frame1.configure(borderwidth="2")
    Frame1.configure(background="#ffffff")

    speciality_entry = tkinter.Entry(Frame1)
    speciality_entry.place(relx=0.035, rely=0.129, height=113, relwidth=0.435)
    speciality_entry.configure(background="#dfe6e9")
    speciality_entry.configure(font=font9)
    speciality_entry.configure(justify='center')
    speciality_entry.configure(relief="flat")
    speciality_entry.configure(selectbackground="#c4c4c4")
    speciality_entry.configure(foreground="#ffffff")
    speciality_entry.insert(0, 'Speciality Name')

    set_appointment_button = tkinter.Button(Frame1)
    set_appointment_button.place(relx=0.543, rely=0.516, height=54, width=371)
    set_appointment_button.configure(activebackground="#dfe6e9")
    set_appointment_button.configure(background="#2d3436")
    set_appointment_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    set_appointment_button.configure(foreground="#ffffff")
    set_appointment_button.configure(relief="flat")
    set_appointment_button.configure(text='''Set Appointment''')

    search_speciality_button = tkinter.Button(Frame1, command=lambda: speciality_search_db(speciality_entry.get(), specialities_found_listbox))
    search_speciality_button.place(relx=0.543, rely=0.129, height=54, width=371)
    search_speciality_button.configure(activebackground="#dfe6e9")
    search_speciality_button.configure(background="#2d3436")
    search_speciality_button.configure(font=font10)
    search_speciality_button.configure(foreground="#ffffff")
    search_speciality_button.configure(relief="flat")
    search_speciality_button.configure(text='''Search Doctor''')

    return

def first_time(council, username):

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT Work_Hour.start_hour, Work_Hour.end_hour, Work_Hour.w_date FROM Work_Hour, DOH, Doctor WHERE  Doctor.medical_council_code = DOH.medical_council_code AND Doctor.username = DOH.username AND DOH.DOH_id = Work_Hour.DOH_id AND Doctor.medical_council_code = '{council}' AND Doctor.username = '{username}';")
    all_times = cursor.fetchall()

    cursor.execute(f"SELECT Work_Hour.start_hour, Work_Hour.end_hour, Work_Hour.w_date FROM Work_Hour, DHH, Doctor WHERE  Doctor.medical_council_code = DHH.medical_council_code AND Doctor.username = DHH.username AND DHH.DHH_id = Work_Hour.DHH_id AND Doctor.medical_council_code = '{council}' AND Doctor.username = '{username}';")
    all_times += cursor.fetchall()

    connection.commit()
    connection.close()

    x = len(all_times)
    
    for i in range(x):

        if len(all_times) == 0:
            return
        
        date = min(all_times, key=lambda tup: tup[2])
        time = ""
        all_work_hour_times = []
        
        start_minute = int((date[0].split(":"))[1])
        end_minute = int((date[1].split(":"))[1])
        start_time = int((date[0].split(":"))[0])
        end_time = int((date[1].split(":"))[0])

        if(end_minute == 30):
            end_time += 0.5
        if(start_minute==30):
            start_time += 0.5
        while start_time <= end_time:
            all_work_hour_times.append(start_time)
            start_time+=0.5
        
        connection = sqlite3.connect('TabibYab.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT start_time FROM Appointment WHERE medical_council_code = '{council}' AND username = '{username}' AND appointment_date = '{date[2]}';")
        not_available_times=cursor.fetchall()

        connection.commit()
        connection.close()
        not_available_times_intger = []
        
        for i in range(len(not_available_times)):

            not_available_time_hour = int((not_available_times[i][0].split(":"))[0])
            not_available_time_minute = int((not_available_times[i][0].split(":"))[1])
            if not_available_time_minute == 30:
                not_available_time_hour = not_available_time_hour+0.5
            not_available_times_intger.append(not_available_time_hour)

        available_times = [i for i in all_work_hour_times if i not in not_available_times_intger] 

        if len(available_times) != 0:

            if min(available_times) % 1 != 0:

                time = f'{int(min(available_times))}:30'
                available_time_and_date = [time, date[2]]
                return available_time_and_date
                
            else:
                time = f'{int(min(available_times))}:00'
                available_time_and_date=[time, date[2]]
                return available_time_and_date

        else:
            all_times.pop(all_times.index(date))
            
    return

def appointment_ui():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global all_doctors_page


    all_doctors_page = tkinter.Tk()
    all_doctors_page.title('Add Family')
    all_doctors_page.attributes('-fullscreen', True)
    all_doctors_page.configure(background="#2d3436")

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT first_name, last_name, Speciality.name, medical_council_code, username, visit_price FROM Doctor, Speciality WHERE Doctor.speciality_id = Speciality.speciality_id ")
    temp_doctors = cursor.fetchall()


    doctors = []
    usernames = []
    price = []
    
    for temp_doctor in temp_doctors:
        doctors.append(temp_doctor[:4])
        usernames.append(temp_doctor[4])
        price.append(temp_doctor[5])
    
    connection.commit()
    connection.close()

    all_doctors_listbox = tkinter.Listbox(all_doctors_page)
    all_doctors_listbox.place(relx=0.208, rely=0.205, relheight=0.416, relwidth=0.585)
    all_doctors_listbox.configure(background="white")
    all_doctors_listbox.configure(cursor="dotbox")
    all_doctors_listbox.configure(font=font9)
    all_doctors_listbox.configure(highlightbackground="#dfe6e9")
    all_doctors_listbox.configure(justify='center')
    all_doctors_listbox.configure(relief="flat")
    all_doctors_listbox.configure(selectbackground="#dfe6e9")
    all_doctors_listbox.configure(setgrid="1")

    for i in range(len(doctors)):

        first_visit_time = first_time(doctors[i][3], usernames[i])

        name_text = f'{doctors[i][0]} {doctors[i][1]}'
        speciality_text = f'{doctors[i][2]}'
        council_text = f'{doctors[i][3]}'
        if first_visit_time != None:
            first_time_text = f'{first_visit_time[0]} - {first_visit_time[1]}'
        else:
            first_time_text = 'Does Not Have'

        for i in range(20):
            if i == len(name_text) - 1:
                name_text += ' '
            if i == len(speciality_text) - 1:
                speciality_text += ' '
            if i == len(council_text) - 1:
                council_text += ' '
            if i == len(first_time_text) - 1:
                first_time_text += ' '

        all_doctors_listbox.insert(tkinter.END, f'Name: {name_text}| Speciality: {speciality_text}| Medical Council Code: {council_text} | First Time: {first_time_text}')

    back_button = tkinter.Button(all_doctors_page, command=all_doctors_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    Frame1 = tkinter.Frame(all_doctors_page)
    Frame1.place(relx=0.208, rely=0.644, relheight=0.132, relwidth=0.586)
    Frame1.configure(relief='flat')
    Frame1.configure(borderwidth="2")


    set_appointment_button = tkinter.Button(Frame1, command=lambda: get_appointment(doctors[all_doctors_listbox.curselection()[0]], usernames[all_doctors_listbox.curselection()[0]], price[all_doctors_listbox.curselection()[0]]))
    set_appointment_button.place(relx=0.249, rely=-0.074, height=154, width=291)
    set_appointment_button.configure(activebackground="#f9f9f9")
    set_appointment_button.configure(background="#ffffff")
    set_appointment_button.configure(borderwidth="5")
    set_appointment_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    set_appointment_button.configure(text='''Set Appointment''')

    search_by_name = tkinter.Button(Frame1, command=doctor_search_ui) 
    search_by_name.place(relx=0.507, rely=-0.074, height=154, width=281)
    search_by_name.configure(activebackground="#f9f9f9")
    search_by_name.configure(background="#ffffff")
    search_by_name.configure(borderwidth="5")
    search_by_name.configure(font="-family {ubvazir} -size 10 -weight bold")
    search_by_name.configure(text='''Search Name''')

    search_by_speciality = tkinter.Button(Frame1, command=speciality_search_ui)
    search_by_speciality.place(relx=0.756, rely=-0.074, height=154, width=281)
    search_by_speciality.configure(activebackground="#f9f9f9")
    search_by_speciality.configure(background="#ffffff")
    search_by_speciality.configure(borderwidth="5")
    search_by_speciality.configure(font="-family {ubvazir} -size 10 -weight bold")
    search_by_speciality.configure(text='''Search Speciality''')

    view_profile_button = tkinter.Button(Frame1, command=lambda:doctor_profile(doctors[all_doctors_listbox.curselection()[0]], usernames[all_doctors_listbox.curselection()[0]]))
    view_profile_button.place(relx=-0.009, rely=-0.074, height=154, width=291)
    view_profile_button.configure(activebackground="#f9f9f9")
    view_profile_button.configure(background="#ffffff")
    view_profile_button.configure(borderwidth="5")
    view_profile_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    view_profile_button.configure(text='''View Profile''')

    return
    
    

def doctor_profile(doctor, username):

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global doctor_page

    doctor_page = tkinter.Toplevel()
    doctor_page.title('Doctor Profile')
    doctor_page.attributes('-fullscreen', True)
    doctor_page.configure(background="#2d3436")

    back_button = tkinter.Button(doctor_page, command=doctor_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    doctor_info_listbox = tkinter.Listbox(doctor_page)
    doctor_info_listbox.place(relx=0.271, rely=0.325, relheight=0.542, relwidth=0.466)
    doctor_info_listbox.configure(background="white")
    doctor_info_listbox.configure(font=font9)
    doctor_info_listbox.configure(justify='left')
    doctor_info_listbox.configure(relief="flat")
    doctor_info_listbox.configure(setgrid="1")

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT DISTINCT first_name, last_name, Speciality.name, Doctor.medical_council_code, photo, visit_price FROM Doctor, DOH, Speciality  WHERE Doctor.speciality_id = Speciality.speciality_id AND Doctor.medical_council_code = DOH.medical_council_code AND Doctor.username = DOH.username  AND Doctor.medical_council_code = '{doctor[3]}' AND Doctor.username = '{username}';");
    doctor_info = cursor.fetchone()
    if doctor_info == None:
        cursor.execute(f"SELECT DISTINCT first_name, last_name, Speciality.name, Doctor.medical_council_code, photo, visit_price FROM Doctor, DHH, Speciality  WHERE Doctor.speciality_id = Speciality.speciality_id AND Doctor.medical_council_code = DHH.medical_council_code AND Doctor.username = DHH.username  AND Doctor.medical_council_code = '{doctor[3]}' AND Doctor.username = '{username}';");
        doctor_info = cursor.fetchone()
    elif doctor_info == None:
        cursor.execute(f"SELECT DISTINCT first_name, last_name, Speciality.name, Doctor.medical_council_code, photo, visit_price FROM Doctor, Speciality  WHERE Doctor.speciality_id = Speciality.speciality_id AND Doctor.medical_council_code = '{doctor[3]}' AND Doctor.username = '{username}';");
        doctor_info = cursor.fetchone()

    cursor.execute(f"SELECT name FROM Insurance WHERE insurance_id IN (SELECT insurance_id FROM Insurance_Doctor WHERE medical_council_code = '{doctor[3]}' AND username = '{username}');")
    insurance_names = cursor.fetchall()

    if doctor_info[4] != None:
        image_path = doctor_info[4]
        profile_image = Image.open(image_path)
        profile_image = profile_image.resize((150, 150), Image.ANTIALIAS)
        profile_image = ImageTk.PhotoImage(image=profile_image)
        profile_label = tkinter.Label(doctor_page,image=profile_image)
        profile_label.image = profile_image
        profile_label.place(relx=0.4675, rely=0.125)

    doctor_info_listbox.insert(tkinter.END, f' ')
    doctor_info_listbox.insert(tkinter.END, f'   First Name: {doctor_info[0]}')
    doctor_info_listbox.insert(tkinter.END, f' ')
    doctor_info_listbox.insert(tkinter.END, f'   Last Name: {doctor_info[1]}')
    doctor_info_listbox.insert(tkinter.END, f' ')
    doctor_info_listbox.insert(tkinter.END, f'   Medical Council Code: {doctor_info[3]}')
    doctor_info_listbox.insert(tkinter.END, f' ')
    doctor_info_listbox.insert(tkinter.END, f'   Speciality: {doctor_info[2]}')
    doctor_info_listbox.insert(tkinter.END, f' ')
    doctor_info_listbox.insert(tkinter.END, f'   Visit Price: {doctor_info[4]}')
    doctor_info_listbox.insert(tkinter.END, f' ')

    connection.commit()
    connection.close()
    
    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT Work_Hour.w_date , Work_Hour.start_hour , Work_Hour.end_hour , Doctor_Office.phone_number, Address.alley, Address.street, Address.plaque FROM Work_Hour,Doctor, DOH, Doctor_Office, Address  WHERE DOH.DOH_id=Work_Hour.DOH_id AND  Doctor.medical_council_code = DOH.medical_council_code AND Doctor.username = DOH.username AND DOH.doctor_office_id=Doctor_Office.doctor_office_id AND Doctor_Office.address_id=Address.address_id AND Doctor.medical_council_code='{doctor[3]}';");
    work_info=cursor.fetchall()

    connection.commit()
    connection.close()
    
    doctor_info_listbox.insert(tkinter.END, "   Offices And Work Hours:")
    doctor_info_listbox.insert(tkinter.END, f' ')
    for work_hours_and_offices in work_info:
        doctor_info_listbox.insert(tkinter.END, f'   Date: {work_hours_and_offices[0]}')
        doctor_info_listbox.insert(tkinter.END, f'   Start Time: {work_hours_and_offices[1]}')
        doctor_info_listbox.insert(tkinter.END, f'   End Time: {work_hours_and_offices[2]}')
        doctor_info_listbox.insert(tkinter.END, f'   Phone Number: {work_hours_and_offices[3]}')
        doctor_info_listbox.insert(tkinter.END, f'   Address: {work_hours_and_offices[4]} - {work_hours_and_offices[5]} - {work_hours_and_offices[6]}')
        doctor_info_listbox.insert(tkinter.END, ' ')

    doctor_info_listbox.insert(tkinter.END, "   Insurances:")
    doctor_info_listbox.insert(tkinter.END, f' ')
    for insurance_name in insurance_names:
        doctor_info_listbox.insert(tkinter.END, f'   Insurance: {insurance_name[0]}')

    return

    

def HCC_doctors_show(index, health_care_centers, HCC_doctors_listbox):

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT first_name, last_name, Speciality.name, Doctor.medical_council_code, HCC.name FROM Doctor, Speciality, HCC, DHH WHERE Doctor.medical_council_code = DHH.medical_council_code AND Doctor.username = DHH.username AND DHH.HCC_id = HCC.HCC_id AND Doctor.speciality_id = Speciality.speciality_id AND HCC.HCC_id = {health_care_centers[index][0]};");
    HCC_doctors = cursor.fetchall()
    
    connection.commit()
    connection.close()

    HCC_doctors_listbox.delete(0, tkinter.END)

    for HCC_doctor in HCC_doctors:

        first_name_text = f'{HCC_doctor[0]}'
        last_name_text = f'{HCC_doctor[1]}'
        speciality_text = f'{HCC_doctor[2]}'
        name_text = f'{HCC_doctor[4]}'

        for i in range(8):
            if i == len(first_name_text) - 1:
                first_name_text += ' '
            if i == len(last_name_text) - 1:
                last_name_text += ' '
            if i == len(speciality_text) - 1:
                speciality_text += ' '
            if i == len(name_text) - 1:
                name_text += ' '

        HCC_doctors_listbox.insert(tkinter.END, f'First Name: {first_name_text}| Last Name: {last_name_text}| Speciality: {speciality_text}| Name: {name_text}')

    return


def health_care_centers_ui():
    
    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global health_care_centers_page

    health_care_centers_page = tkinter.Tk()
    health_care_centers_page.title('Health Care Centers')
    health_care_centers_page.attributes('-fullscreen', True)
    health_care_centers_page.configure(background="#2d3436")

    back_button = tkinter.Button(health_care_centers_page, command=health_care_centers_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    HCC_doctors_listbox = tkinter.Listbox(health_care_centers_page)
    HCC_doctors_listbox.place(relx=0.339, rely=0.185, relheight=0.328, relwidth=0.32)
    HCC_doctors_listbox.configure(background="white")
    HCC_doctors_listbox.configure(cursor="dot")
    HCC_doctors_listbox.configure(font=font9)
    HCC_doctors_listbox.configure(justify='center')
    HCC_doctors_listbox.configure(relief="flat")
    HCC_doctors_listbox.configure(selectforeground="#2d3436")
    HCC_doctors_listbox.configure(setgrid="1")

    health_care_center_doctor_listbox = tkinter.Listbox(health_care_centers_page)
    health_care_center_doctor_listbox.place(relx=0.672, rely=0.185, relheight=0.328, relwidth=0.32)
    health_care_center_doctor_listbox.configure(background="white")
    health_care_center_doctor_listbox.configure(cursor="dot")
    health_care_center_doctor_listbox.configure(font="-family {DejaVu Sans Mono} -size 10 -weight bold")
    health_care_center_doctor_listbox.configure(justify='center')
    health_care_center_doctor_listbox.configure(relief="flat")
    health_care_center_doctor_listbox.configure(selectbackground="#c4c4c4")
    health_care_center_doctor_listbox.configure(selectforeground="#2d3436")
    health_care_center_doctor_listbox.configure(setgrid="1")

    health_care_center_listbox = tkinter.Listbox(health_care_centers_page)
    health_care_center_listbox.place(relx=0.005, rely=0.185, relheight=0.328, relwidth=0.32)
    health_care_center_listbox.configure(background="white")
    health_care_center_listbox.configure(cursor="dot")
    health_care_center_listbox.configure(font="-family {DejaVu Sans Mono} -size 10 -weight bold")
    health_care_center_listbox.configure(justify='center')
    health_care_center_listbox.configure(relief="flat")
    health_care_center_listbox.configure(selectbackground="#c4c4c4")
    health_care_center_listbox.configure(selectforeground="#2d3436")
    health_care_center_listbox.configure(setgrid="1")

    Frame1 = tkinter.Frame(health_care_centers_page)
    Frame1.place(relx=0.005, rely=0.556, relheight=0.132, relwidth=0.987)
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="flat")
    Frame1.configure(background="#ffffff")

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT * FROM HCC")
    health_care_centers = cursor.fetchall()

    for health_care_center in health_care_centers:

        phone_number_text= f'{health_care_center[1]}'
        name_text = f'{health_care_center[2]}'
    
        for i in range(25):
            if i == len(phone_number_text) - 1:
                phone_number_text += ' '
            if i == len(name_text) - 1:
                name_text += ' '
           
        health_care_center_listbox.insert(tkinter.END, f'Phone Number: {phone_number_text}| Name: {name_text}')

    
    cursor.execute(f"SELECT first_name, last_name, Speciality.name, Doctor.medical_council_code, HCC.name FROM Doctor, Speciality, HCC, DHH WHERE Doctor.medical_council_code = DHH.medical_council_code AND Doctor.username = DHH.username AND DHH.HCC_id = HCC.HCC_id AND Doctor.speciality_id = Speciality.speciality_id")
    health_care_center_doctors = cursor.fetchall()

    for health_care_center_doctor in health_care_center_doctors:

        first_name_text = f'{health_care_center_doctor[0]}'
        last_name_text = f'{health_care_center_doctor[1]}'
        speciality_text = f'{health_care_center_doctor[2]}'
        name_text = f'{health_care_center_doctor[4]}'

        for i in range(8):
            if i == len(first_name_text) - 1:
                first_name_text += ' '
            if i == len(last_name_text) - 1:
                last_name_text += ' '
            if i == len(speciality_text) - 1:
                speciality_text += ' '
            if i == len(name_text) - 1:
                name_text += ' '

        health_care_center_doctor_listbox.insert(tkinter.END, f'First Name: {first_name_text}| Last Name: {last_name_text}| Speciality: {speciality_text}| Name: {name_text}')

    HCC_doctors_button = tkinter.Button(Frame1, command=lambda: HCC_doctors_show(health_care_center_listbox.curselection()[0], health_care_centers, HCC_doctors_listbox))
    HCC_doctors_button.place(relx=0.011, rely=0.148, height=94, width=1851)
    HCC_doctors_button.configure(activebackground="#dfe6e9")
    HCC_doctors_button.configure(background="#2d3436")
    HCC_doctors_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    HCC_doctors_button.configure(foreground="#ffffff")
    HCC_doctors_button.configure(relief="flat")
    HCC_doctors_button.configure(text='''Show Doctors''')

    connection.commit()
    connection.close()
    
    return

def home_ui():

    _bgcolor = '#d9d9d9' 
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font9 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global home_page

    home_page = tkinter.Tk()
    home_page.title('Home Page')
    home_page.attributes('-fullscreen', True)
    home_page.configure(background="#2d3436")

    menu_frame = tkinter.Frame(home_page)
    menu_frame.place(relx=0.188, rely=0.4, relheight=0.132, relwidth=0.643)
    menu_frame.configure(relief='flat')
    menu_frame.configure(borderwidth="2")
    menu_frame.configure(background="#ffffff")
    menu_frame.configure(cursor="tcross")

    profile_button = tkinter.Button(menu_frame, command=profile_ui)
    profile_button.place(relx=0.332, rely=-0.074, height=164, width=421)
    profile_button.configure(activebackground="#f9f9f9")
    profile_button.configure(background="#ffffff")
    profile_button.configure(borderwidth="5")
    profile_button.configure(cursor="mouse")
    profile_button.configure(font=font9)
    profile_button.configure(text='''View Profile''')

    appointment_button = tkinter.Button(menu_frame, command=appointment_ui)
    appointment_button.place(relx=-0.008, rely=-0.074, height=164, width=421)
    appointment_button.configure(activebackground="#f9f9f9")
    appointment_button.configure(background="#ffffff")
    appointment_button.configure(borderwidth="5")
    appointment_button.configure(font=font9)
    appointment_button.configure(text='''Visit Doctors''')

    health_care_center_button = tkinter.Button(menu_frame, command=health_care_centers_ui)
    health_care_center_button.place(relx=0.672, rely=-0.074, height=164, width=411)
    health_care_center_button.configure(activebackground="#f9f9f9")
    health_care_center_button.configure(background="#ffffff")
    health_care_center_button.configure(borderwidth="5")
    health_care_center_button.configure(font=font9)
    health_care_center_button.configure(text='''Health Care Centers''')

    return


def login_db(phone_number, password):
    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT password FROM User WHERE phone_number = '{phone_number}';")

    real_password = cursor.fetchone()

    connection.commit()
    connection.close()

    if type(real_password) != type(None):
        real_password = real_password[0]

    if real_password == password:
        global current_phone_number

        current_phone_number = phone_number

        root.destroy()
        login_page.destroy()
        home_ui()

    return

def signup_db(phone_number, password):
    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT phone_number FROM User")
    all_phone_numbers = cursor.fetchall()
    all_phone_numbers = [all_phone_numbers[i][0] for i in range(len(all_phone_numbers))]
    if phone_number not in all_phone_numbers:
        cursor.execute(f"INSERT INTO User (phone_number, password) VALUES ('{phone_number}', '{password}')")
    connection.commit()
    connection.close()

def login_ui():

    global login_page

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'

    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    login_page = tkinter.Tk()
    login_page.configure(background="#2d3436")
    login_page.configure(cursor="arrow")
    login_page.title('Sign Up')
    login_page.attributes('-fullscreen', True)

    back_button = tkinter.Button(login_page, command=login_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    Login = tkinter.Frame(login_page)
    Login.place(relx=0.391, rely=0.302, relheight=0.337, relwidth=0.211)
    Login.configure(relief='flat')
    Login.configure(borderwidth="2")
    Login.configure(background="#ffffff")
    Login.configure(cursor="heart")

    phone_number_entry = tkinter.Entry(Login)
    phone_number_entry.place(relx=0.101, rely=0.131, height=53, relwidth=0.825)
    phone_number_entry.configure(background="#dfe6e9")
    phone_number_entry.configure(font=font9)
    phone_number_entry.configure(relief="flat")
    phone_number_entry.configure(justify="center")
    phone_number_entry.configure(foreground="#ffffff")
    phone_number_entry.insert(0, 'Phone Number')

    password_entry = tkinter.Entry(Login)
    password_entry.place(relx=0.101, rely=0.426,height=53, relwidth=0.825)
    password_entry.configure(background="#dfe6e9")
    password_entry.configure(font=font9)
    password_entry.configure(relief="flat")
    password_entry.configure(justify="center")
    password_entry.configure(foreground="#ffffff")
    password_entry.insert(0, 'Password')

    login = tkinter.Button(Login, command=lambda: login_db(phone_number_entry.get(), password_entry.get()))
    login.place(relx=0.101, rely=0.721, height=54, width=331)
    login.configure(activebackground="#dfe6e9")
    login.configure(background="#2d3436")
    login.configure(font=font10)
    login.configure(relief="flat")
    login.configure(foreground="#ffffff")
    login.configure(text='''Login''')

    return


def signup_ui():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global signup_page


    signup_page = tkinter.Tk()
    signup_page.title('Sign Up')
    signup_page.attributes('-fullscreen', True)
    signup_page.configure(relief="ridge")
    signup_page.configure(background="#2d3436")
    signup_page.configure(cursor="arrow")

    back_button = tkinter.Button(signup_page, command=signup_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    Signup = tkinter.Frame(signup_page)
    Signup.place(relx=0.391, rely=0.302, relheight=0.337, relwidth=0.211)
    Signup.configure(relief='flat')
    Signup.configure(borderwidth="2")
    Signup.configure(background="#ffffff")
    Signup.configure(cursor="heart")

    phone_number_entry = tkinter.Entry(Signup)
    phone_number_entry.place(relx=0.101, rely=0.131, height=53, relwidth=0.825)
    phone_number_entry.configure(background="#dfe6e9")
    phone_number_entry.configure(font=font9)
    phone_number_entry.configure(justify='center')
    phone_number_entry.configure(relief="flat")
    phone_number_entry.configure(foreground="#ffffff")
    phone_number_entry.insert(0, 'Password')

    password_entry = tkinter.Entry(Signup)
    password_entry.place(relx=0.101, rely=0.426, height=53, relwidth=0.825)
    password_entry.configure(background="#dfe6e9")
    password_entry.configure(font=font9)
    password_entry.configure(relief="flat")
    password_entry.configure(justify="center")
    password_entry.configure(foreground="#ffffff")
    password_entry.insert(0, 'Password')

    signup_submit_button = tkinter.Button(Signup, command=lambda: signup_db(phone_number_entry.get(), password_entry.get()))
    signup_submit_button.place(relx=0.101, rely=0.721, height=54, width=331)
    signup_submit_button.configure(activebackground="#dfe6e9")
    signup_submit_button.configure(background="#2d3436")
    signup_submit_button.configure(font=font10)
    signup_submit_button.configure(relief="flat")
    signup_submit_button.configure(text='''Sign Up''')
    signup_submit_button.configure(foreground="#ffffff")

    return


def start():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font9 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global root

    root = tkinter.Tk()
    root.title('TabibYab')
    root.attributes('-fullscreen', True)
    root.configure(background="#2d3436")    

    start_frame = tkinter.Frame(root)
    start_frame.place(relx=0.391, rely=0.302, relheight=0.337, relwidth=0.211)
    start_frame.configure(relief='flat')
    start_frame.configure(borderwidth="2")
    start_frame.configure(background="#ffffff")

    login_button = tkinter.Button(start_frame, command=login_ui)
    login_button.place(relx=0.074, rely=0.261, height=54, width=351)
    login_button.configure(activebackground="#dfe6e9")
    login_button.configure(background="#2d3436")
    login_button.configure(font=font9)
    login_button.configure(relief="flat")
    login_button.configure(foreground="#ffffff")
    login_button.configure(text='''Login''')

    signup_button = tkinter.Button(start_frame, command=signup_ui)
    signup_button.place(relx=0.074, rely=0.696, height=54, width=351)
    signup_button.configure(activebackground="#dfe6e9")
    signup_button.configure(background="#2d3436")
    signup_button.configure(font=font9)
    signup_button.configure(relief="flat")
    signup_button.configure(text='''Sign Up''')
    signup_button.configure(foreground="#ffffff")

    Label1 = tkinter.Label(start_frame)
    Label1.place(relx=0.099, rely=0.145, height=24, width=329)
    Label1.configure(background="#ffffff")
    Label1.configure(font=font9)
    Label1.configure(text='''Already Have An Account?''')

    Label1_3 = tkinter.Label(start_frame)
    Label1_3.place(relx=0.074, rely=0.58, height=24, width=349)
    Label1_3.configure(activebackground="#f9f9f9")
    Label1_3.configure(background="#ffffff")
    Label1_3.configure(font="-family {ubvazir} -size 10 -weight bold")
    Label1_3.configure(text='''Still Does Not Have An Account?''')

    root.mainloop()

    return

start()