import tkinter
import sqlite3

def add_doctor_db(username, firstname, lastname, council, password, visit_price, speciality):

    if username == None or firstname == None or lastname == None or council == None or password == None or visit_price == None or speciality == None:
        return

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT speciality_id FROM Speciality WHERE name = '{speciality}'")
    speciality_id = cursor.fetchone()
    if speciality_id == None:
        return
    speciality_id = speciality_id[0]

    cursor.execute(f"INSERT INTO Doctor (username, first_name, last_name, medical_council_code, password, visit_price, speciality_id) VALUES ('{username}', '{firstname}', '{lastname}', '{council}', '{password}', {visit_price}, {speciality_id});")
    
    connection.commit()
    connection.close()

    return


def edit_doctor_db(username, firstname, lastname, council, password, visit_price, speciality, previous_username, previous_council):

    if username == None or firstname == None or lastname == None or council == None or password == None or visit_price == None or speciality == None:
        return

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT speciality_id FROM Speciality WHERE name = '{speciality}'")
    speciality_id = cursor.fetchone()
    if speciality_id == None:
        return
    speciality_id = speciality_id[0]

    cursor.execute(f"UPDATE Doctor SET username = '{username}', first_name = '{firstname}', last_name = '{lastname}', medical_council_code = '{council}', password = '{password}', visit_price = {visit_price}, speciality_id = {speciality_id} WHERE username = '{previous_username}' AND medical_council_code = '{previous_council}';")
    cursor.execute(f"UPDATE DHH SET username = '{username}', medical_council_code = '{council}' WHERE username = '{previous_username}' AND medical_council_code = '{previous_council}';")
    cursor.execute(f"UPDATE DOH SET username = '{username}', medical_council_code = '{council}' WHERE username = '{previous_username}' AND medical_council_code = '{previous_council}';")
    cursor.execute(f"UPDATE Insurance_Doctor SET username = '{username}', medical_council_code = '{council}' WHERE username = '{previous_username}' AND medical_council_code = '{previous_council}';")
    cursor.execute(f"UPDATE User_Doctor SET username = '{username}', medical_council_code = '{council}' WHERE username = '{previous_username}' AND medical_council_code = '{previous_council}';")
    cursor.execute(f"UPDATE Appointment SET username = '{username}', medical_council_code = '{council}' WHERE username = '{previous_username}' AND medical_council_code = '{previous_council}';")


    connection.commit()
    connection.close()

    return


def add_doctor():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font10 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global add_doctor_page

    add_doctor_page = tkinter.Tk()
    add_doctor_page.attributes('-fullscreen', True)
    add_doctor_page.configure(background="#2d3436")

    back_button = tkinter.Button(add_doctor_page, command=add_doctor_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    add_doctor_frame = tkinter.Frame(add_doctor_page)
    add_doctor_frame.place(relx=0.365, rely=0.144, relheight=0.650, relwidth=0.273)
    add_doctor_frame.configure(relief='flat')
    add_doctor_frame.configure(background="#ffffff")

    username_label = tkinter.Label(add_doctor_frame)
    username_label.place(relx=0.0, rely=0.04, height=54, width=98)
    username_label.configure(background="#ffffff")
    username_label.configure(font=font9)
    username_label.configure(text='''User Name''')

    firstname_label = tkinter.Label(add_doctor_frame)
    firstname_label.place(relx=0.0, rely=0.16, height=54, width=98)
    firstname_label.configure(background="#ffffff")
    firstname_label.configure(font=font9)
    firstname_label.configure(text='''First Name''')

    lastname_label = tkinter.Label(add_doctor_frame)
    lastname_label.place(relx=-0.019, rely=0.27, height=74, width=118)
    lastname_label.configure(activebackground="#f9f9f9")
    lastname_label.configure(background="#ffffff")
    lastname_label.configure(font=font9)
    lastname_label.configure(text='''Last Name''')

    council_label = tkinter.Label(add_doctor_frame)
    council_label.place(relx=0.0, rely=0.40, height=54, width=108)
    council_label.configure(activebackground="#f9f9f9")
    council_label.configure(background="#ffffff")
    council_label.configure(font=font9)
    council_label.configure(text='''Council''')

    password_label = tkinter.Label(add_doctor_frame)
    password_label.place(relx=0.0, rely=0.52, height=54, width=108)
    password_label.configure(activebackground="#f9f9f9")
    password_label.configure(background="#ffffff")
    password_label.configure(font=font9)
    password_label.configure(text='''Password''')

    visit_price_label = tkinter.Label(add_doctor_frame)
    visit_price_label.place(relx=0.0, rely=0.64, height=54, width=108)
    visit_price_label.configure(activebackground="#f9f9f9")
    visit_price_label.configure(background="#ffffff")
    visit_price_label.configure(font=font9)
    visit_price_label.configure(text='''Visit Price''')

    speciality_label = tkinter.Label(add_doctor_frame)
    speciality_label.place(relx=0.0, rely=0.76, height=54, width=108)
    speciality_label.configure(activebackground="#f9f9f9")
    speciality_label.configure(background="#ffffff")
    speciality_label.configure(font=font9)
    speciality_label.configure(text='''Speciality''')

    username_entry = tkinter.Entry(add_doctor_frame)
    username_entry.place(relx=0.21, rely=0.04, height=53, relwidth=0.754)
    username_entry.configure(background="#dfe6e9")
    username_entry.configure(font=font10)
    username_entry.configure(foreground="#ffffff")
    username_entry.configure(justify='center')
    username_entry.configure(relief="flat")

    firstname_entry = tkinter.Entry(add_doctor_frame)
    firstname_entry.place(relx=0.21, rely=0.16, height=53, relwidth=0.754)
    firstname_entry.configure(background="#dfe6e9")
    firstname_entry.configure(font=font10)
    firstname_entry.configure(foreground="#ffffff")
    firstname_entry.configure(justify='center')
    firstname_entry.configure(relief="flat")

    lastname_entry = tkinter.Entry(add_doctor_frame)
    lastname_entry.place(relx=0.21, rely=0.28, height=53, relwidth=0.754)
    lastname_entry.configure(background="#dfe6e9")
    lastname_entry.configure(cursor="fleur")
    lastname_entry.configure(font=font10)
    lastname_entry.configure(foreground="#ffffff")
    lastname_entry.configure(justify='center')
    lastname_entry.configure(relief="flat")
    lastname_entry.configure(selectbackground="#c4c4c4")

    council_entry = tkinter.Entry(add_doctor_frame)
    council_entry.place(relx=0.21, rely=0.40, height=53, relwidth=0.754)
    council_entry.configure(background="#dfe6e9")
    council_entry.configure(font=font10)
    council_entry.configure(foreground="#ffffff")
    council_entry.configure(justify='center')
    council_entry.configure(relief="flat")
    council_entry.configure(selectbackground="#c4c4c4")

    password_entry = tkinter.Entry(add_doctor_frame)
    password_entry.place(relx=0.21, rely=0.52, height=53, relwidth=0.754)
    password_entry.configure(background="#dfe6e9")
    password_entry.configure(font=font10)
    password_entry.configure(justify='center')
    password_entry.configure(relief="flat")
    password_entry.configure(selectbackground="#c4c4c4")
    password_entry.configure(foreground="#ffffff")

    visit_price_entry = tkinter.Entry(add_doctor_frame)
    visit_price_entry.place(relx=0.21, rely=0.64, height=53, relwidth=0.754)
    visit_price_entry.configure(background="#dfe6e9")
    visit_price_entry.configure(font=font10)
    visit_price_entry.configure(justify='center')
    visit_price_entry.configure(relief="flat")
    visit_price_entry.configure(selectbackground="#c4c4c4")
    visit_price_entry.configure(foreground="#ffffff")

    speciality_entry = tkinter.Entry(add_doctor_frame)
    speciality_entry.place(relx=0.21, rely=0.76, height=53, relwidth=0.754)
    speciality_entry.configure(background="#dfe6e9")
    speciality_entry.configure(font=font10)
    speciality_entry.configure(justify='center')
    speciality_entry.configure(relief="flat")
    speciality_entry.configure(selectbackground="#c4c4c4")
    speciality_entry.configure(foreground="#ffffff")

    edit_doctor_submit_button = tkinter.Button(add_doctor_frame, command=lambda: add_doctor_db(username_entry.get(), firstname_entry.get(), lastname_entry.get(), council_entry.get(), password_entry.get(), visit_price_entry.get(), speciality_entry.get()))
    edit_doctor_submit_button.place(relx=0.038, rely=0.89, height=54, width=491)
    edit_doctor_submit_button.configure(activebackground="#dfe6e9")
    edit_doctor_submit_button.configure(background="#2d3436")
    edit_doctor_submit_button.configure(font=font9)
    edit_doctor_submit_button.configure(foreground="#ffffff")
    edit_doctor_submit_button.configure(relief="flat")
    edit_doctor_submit_button.configure(text='''Submit''')

    return


def delete_doctor(council, username):

    if council == None or username == None:
        return

    council = council[3]

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"DELETE FROM Doctor WHERE username = '{username}' AND medical_council_code = '{council}';")
    cursor.execute(f"DELETE FROM Appointment WHERE username = '{username}' AND medical_council_code = '{council}';")
    cursor.execute(f"DELETE FROM DHH WHERE username = '{username}' AND medical_council_code = '{council}';")
    cursor.execute(f"DELETE FROM DOH WHERE username = '{username}' AND medical_council_code = '{council}';")
    cursor.execute(f"DELETE FROM Insurance_Doctor WHERE username = '{username}' AND medical_council_code = '{council}';")
    cursor.execute(f"DELETE FROM User_Doctor WHERE username = '{username}' AND medical_council_code = '{council}';")

    connection.commit()
    connection.close()

    return



def edit_doctor(doctor_data, username):

    if doctor_data == None:
        return

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    
    council = doctor_data[3]

    cursor.execute(f"SELECT username, first_name, last_name, medical_council_code, password, visit_price, speciality_id FROM Doctor WHERE username = '{username}' AND medical_council_code = '{doctor_data[3]}';")
    doctor_data = cursor.fetchone()

    cursor.execute(f"SELECT name FROM Speciality WHERE speciality_id = {doctor_data[6]}")
    speciality = cursor.fetchone()
    if speciality != None:
        speciality = speciality[0]

    connection.commit()
    connection.close()

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font10 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global edit_doctor_page

    edit_doctor_page = tkinter.Tk()
    edit_doctor_page.attributes('-fullscreen', True)
    edit_doctor_page.configure(background="#2d3436")

    back_button = tkinter.Button(edit_doctor_page, command=edit_doctor_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    edit_doctor_frame = tkinter.Frame(edit_doctor_page)
    edit_doctor_frame.place(relx=0.365, rely=0.144, relheight=0.650, relwidth=0.273)
    edit_doctor_frame.configure(relief='flat')
    edit_doctor_frame.configure(background="#ffffff")

    username_label = tkinter.Label(edit_doctor_frame)
    username_label.place(relx=0.0, rely=0.04, height=54, width=98)
    username_label.configure(background="#ffffff")
    username_label.configure(font=font9)
    username_label.configure(text='''User Name''')

    firstname_label = tkinter.Label(edit_doctor_frame)
    firstname_label.place(relx=0.0, rely=0.16, height=54, width=98)
    firstname_label.configure(background="#ffffff")
    firstname_label.configure(font=font9)
    firstname_label.configure(text='''First Name''')

    lastname_label = tkinter.Label(edit_doctor_frame)
    lastname_label.place(relx=-0.019, rely=0.28, height=74, width=118)
    lastname_label.configure(activebackground="#f9f9f9")
    lastname_label.configure(background="#ffffff")
    lastname_label.configure(font=font9)
    lastname_label.configure(text='''Last Name''')

    council_label = tkinter.Label(edit_doctor_frame)
    council_label.place(relx=0.0, rely=0.40, height=54, width=108)
    council_label.configure(activebackground="#f9f9f9")
    council_label.configure(background="#ffffff")
    council_label.configure(font=font9)
    council_label.configure(text='''Council''')

    password_label = tkinter.Label(edit_doctor_frame)
    password_label.place(relx=0.0, rely=0.52, height=54, width=108)
    password_label.configure(activebackground="#f9f9f9")
    password_label.configure(background="#ffffff")
    password_label.configure(font=font9)
    password_label.configure(text='''Password''')

    visit_price_label = tkinter.Label(edit_doctor_frame)
    visit_price_label.place(relx=0.0, rely=0.64, height=54, width=108)
    visit_price_label.configure(activebackground="#f9f9f9")
    visit_price_label.configure(background="#ffffff")
    visit_price_label.configure(font=font9)
    visit_price_label.configure(text='''Visit Price''')

    speciality_label = tkinter.Label(edit_doctor_frame)
    speciality_label.place(relx=0.0, rely=0.76, height=54, width=108)
    speciality_label.configure(activebackground="#f9f9f9")
    speciality_label.configure(background="#ffffff")
    speciality_label.configure(font=font9)
    speciality_label.configure(text='''Speciality''')

    username_entry = tkinter.Entry(edit_doctor_frame)
    username_entry.place(relx=0.21, rely=0.04, height=53, relwidth=0.754)
    username_entry.configure(background="#dfe6e9")
    username_entry.configure(font=font10)
    username_entry.configure(foreground="#ffffff")
    username_entry.configure(justify='center')
    username_entry.configure(relief="flat")
    username_entry.insert(0, doctor_data[0])

    firstname_entry = tkinter.Entry(edit_doctor_frame)
    firstname_entry.place(relx=0.21, rely=0.16, height=53, relwidth=0.754)
    firstname_entry.configure(background="#dfe6e9")
    firstname_entry.configure(font=font10)
    firstname_entry.configure(foreground="#ffffff")
    firstname_entry.configure(justify='center')
    firstname_entry.configure(relief="flat")
    firstname_entry.insert(0, doctor_data[1])

    lastname_entry = tkinter.Entry(edit_doctor_frame)
    lastname_entry.place(relx=0.21, rely=0.28, height=53, relwidth=0.754)
    lastname_entry.configure(background="#dfe6e9")
    lastname_entry.configure(cursor="fleur")
    lastname_entry.configure(font=font10)
    lastname_entry.configure(foreground="#ffffff")
    lastname_entry.configure(justify='center')
    lastname_entry.configure(relief="flat")
    lastname_entry.configure(selectbackground="#c4c4c4")
    lastname_entry.insert(0, doctor_data[2])

    council_entry = tkinter.Entry(edit_doctor_frame)
    council_entry.place(relx=0.21, rely=0.40, height=53, relwidth=0.754)
    council_entry.configure(background="#dfe6e9")
    council_entry.configure(font=font10)
    council_entry.configure(foreground="#ffffff")
    council_entry.configure(justify='center')
    council_entry.configure(relief="flat")
    council_entry.configure(selectbackground="#c4c4c4")
    council_entry.insert(0, doctor_data[3])

    password_entry = tkinter.Entry(edit_doctor_frame)
    password_entry.place(relx=0.21, rely=0.52, height=53, relwidth=0.754)
    password_entry.configure(background="#dfe6e9")
    password_entry.configure(font=font10)
    password_entry.configure(justify='center')
    password_entry.configure(relief="flat")
    password_entry.configure(selectbackground="#c4c4c4")
    password_entry.configure(foreground="#ffffff")
    password_entry.insert(0, doctor_data[4])

    visit_price_entry = tkinter.Entry(edit_doctor_frame)
    visit_price_entry.place(relx=0.21, rely=0.64, height=53, relwidth=0.754)
    visit_price_entry.configure(background="#dfe6e9")
    visit_price_entry.configure(font=font10)
    visit_price_entry.configure(justify='center')
    visit_price_entry.configure(relief="flat")
    visit_price_entry.configure(selectbackground="#c4c4c4")
    visit_price_entry.configure(foreground="#ffffff")
    visit_price_entry.insert(0, doctor_data[5])

    speciality_entry = tkinter.Entry(edit_doctor_frame)
    speciality_entry.place(relx=0.21, rely=0.76, height=53, relwidth=0.754)
    speciality_entry.configure(background="#dfe6e9")
    speciality_entry.configure(font=font10)
    speciality_entry.configure(justify='center')
    speciality_entry.configure(relief="flat")
    speciality_entry.configure(selectbackground="#c4c4c4")
    speciality_entry.configure(foreground="#ffffff")
    speciality_entry.insert(0, speciality)

    edit_doctor_submit_button = tkinter.Button(edit_doctor_frame, command=lambda: edit_doctor_db(username_entry.get(), firstname_entry.get(), lastname_entry.get(), council_entry.get(), password_entry.get(), visit_price_entry.get(), speciality_entry.get(), username, doctor_data[3]))
    edit_doctor_submit_button.place(relx=0.038, rely=0.89, height=54, width=491)
    edit_doctor_submit_button.configure(activebackground="#dfe6e9")
    edit_doctor_submit_button.configure(background="#2d3436")
    edit_doctor_submit_button.configure(font=font9)
    edit_doctor_submit_button.configure(foreground="#ffffff")
    edit_doctor_submit_button.configure(relief="flat")
    edit_doctor_submit_button.configure(text='''Submit''')

    return

def doctor_deal_db(insurance, doctor_data, username):

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT insurance_id FROM Insurance WHERE name = '{insurance}'")
    insurance_id = cursor.fetchone()[0]

    cursor.execute(f"INSERT INTO Insurance_Doctor (insurance_id, username, medical_council_code) VALUES ('{insurance_id}', '{username}', {doctor_data[-1]});")
    
    delete = cursor.fetchone()
    connection.commit()
    connection.close()

    return

def doctor_remove_db(insurance, doctor_data, username):

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT insurance_id FROM Insurance WHERE name = '{insurance}'")
    insurance_id = cursor.fetchone()[0]

    cursor.execute(f"DELETE FROM Insurance_Doctor WHERE insurance_id = '{insurance_id}' AND username = '{username}' AND medical_council_code = {doctor_data[-1]};")
    
    delete = cursor.fetchone()
    connection.commit()
    connection.close()

    return

def doctor_deal(doctor_data, username):
    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'

    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global doctor_deal_page

    doctor_deal_page = tkinter.Tk()
    doctor_deal_page.attributes('-fullscreen', True)
    doctor_deal_page.configure(background="#2d3436")

    doctor_deal_frame = tkinter.Frame(doctor_deal_page)
    doctor_deal_frame.place(relx=0.391, rely=0.302, relheight=0.337, relwidth=0.211)
    doctor_deal_frame.configure(relief='flat')
    doctor_deal_frame.configure(borderwidth="2")
    doctor_deal_frame.configure(background="#ffffff")
    doctor_deal_frame.configure(cursor="heart")
    
    doctor_deal_entry = tkinter.Entry(doctor_deal_frame)
    doctor_deal_entry.place(relx=0.101, rely=0.1, height=53, relwidth=0.825)
    doctor_deal_entry.configure(background="#dfe6e9")
    doctor_deal_entry.configure(font=font9)
    doctor_deal_entry.configure(relief="flat")
    doctor_deal_entry.configure(justify="center")
    doctor_deal_entry.configure(foreground="#ffffff")
    doctor_deal_entry.insert(0, 'Insurance Name')

    doctor_deal_button = tkinter.Button(doctor_deal_frame, command=lambda: doctor_deal_db(doctor_deal_entry.get(), doctor_data, username))
    doctor_deal_button.place(relx=0.101, rely=0.5, height=54, width=331)
    doctor_deal_button.configure(activebackground="#dfe6e9")
    doctor_deal_button.configure(background="#2d3436")
    doctor_deal_button.configure(font=font10)
    doctor_deal_button.configure(relief="flat")
    doctor_deal_button.configure(foreground="#ffffff")
    doctor_deal_button.configure(text='''Add Insurance''')

    doctor_deal_button = tkinter.Button(doctor_deal_frame, command=lambda: doctor_remove_db(doctor_deal_entry.get(), doctor_data, username))
    doctor_deal_button.place(relx=0.101, rely=0.7, height=54, width=331)
    doctor_deal_button.configure(activebackground="#dfe6e9")
    doctor_deal_button.configure(background="#2d3436")
    doctor_deal_button.configure(font=font10)
    doctor_deal_button.configure(relief="flat")
    doctor_deal_button.configure(foreground="#ffffff")
    doctor_deal_button.configure(text='''Remove Insurance''')

    return



def doctor_ui():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global doctors_page


    doctors_page = tkinter.Tk()
    doctors_page.title('Add Family')
    doctors_page.attributes('-fullscreen', True)
    doctors_page.configure(background="#2d3436")

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT first_name, last_name, Speciality.name, medical_council_code, username, visit_price FROM Doctor, Speciality WHERE Doctor.speciality_id = Speciality.speciality_id;")
    temp_doctors = cursor.fetchall()


    doctors = []
    usernames = []
    visit_prices = []
    
    for temp_doctor in temp_doctors:
        doctors.append(temp_doctor[:4])
        usernames.append(temp_doctor[4])
        visit_prices.append(temp_doctor[5])
    
    connection.commit()
    connection.close()

    doctors_listbox = tkinter.Listbox(doctors_page)
    doctors_listbox.place(relx=0.208, rely=0.205, relheight=0.416, relwidth=0.585)
    doctors_listbox.configure(background="white")
    doctors_listbox.configure(cursor="dotbox")
    doctors_listbox.configure(font=font9)
    doctors_listbox.configure(highlightbackground="#dfe6e9")
    doctors_listbox.configure(justify='center')
    doctors_listbox.configure(relief="flat")
    doctors_listbox.configure(selectbackground="#dfe6e9")
    doctors_listbox.configure(setgrid="1")

    for i in range(len(doctors)):

        name_text = f'{doctors[i][0]} {doctors[i][1]}'
        speciality_text = f'{doctors[i][2]}'
        council_text = f'{doctors[i][3]}'
        username_text = f'{usernames[i]}'
        visit_prices_text = f'{visit_prices[i]}'


        for i in range(14):
            if i == len(name_text) - 1:
                name_text += ' '
            if i == len(speciality_text) - 1:
                speciality_text += ' '
            if i == len(council_text) - 1:
                council_text += ' '
            if i == len(username_text) - 1:
                username_text += ' '
            if i == len(visit_prices_text) - 1:
                visit_prices_text += ' '

        doctors_listbox.insert(tkinter.END, f'Name: {name_text}| Speciality: {speciality_text}| Medical Council Code: {council_text} | Username: {username_text} | Visit Price: {visit_prices_text}')

    back_button = tkinter.Button(doctors_page, command=doctors_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    doctor_frame = tkinter.Frame(doctors_page)
    doctor_frame.place(relx=0.208, rely=0.644, relheight=0.132, relwidth=0.586)
    doctor_frame.configure(relief='flat')
    doctor_frame.configure(borderwidth="2")

    add_doctor_button = tkinter.Button(doctor_frame, command=add_doctor)
    add_doctor_button.place(relx=0.000, rely=-0.074, height=154, relwidth=0.25)
    add_doctor_button.configure(activebackground="#f9f9f9")
    add_doctor_button.configure(background="#ffffff")
    add_doctor_button.configure(borderwidth="5")
    add_doctor_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    add_doctor_button.configure(text='''Add Doctor''')

    delete_doctor_button = tkinter.Button(doctor_frame, command=lambda: delete_doctor(doctors[doctors_listbox.curselection()[0]], usernames[doctors_listbox.curselection()[0]])) 
    delete_doctor_button.place(relx=0.25, rely=-0.074, height=154, relwidth=0.25)
    delete_doctor_button.configure(activebackground="#f9f9f9")
    delete_doctor_button.configure(background="#ffffff")
    delete_doctor_button.configure(borderwidth="5")
    delete_doctor_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    delete_doctor_button.configure(text='''Delete Doctor''')

    edit_doctor_button = tkinter.Button(doctor_frame, command=lambda : edit_doctor(doctors[doctors_listbox.curselection()[0]], usernames[doctors_listbox.curselection()[0]]))
    edit_doctor_button.place(relx=0.5, rely=-0.074, height=154, relwidth=0.25)
    edit_doctor_button.configure(activebackground="#f9f9f9")
    edit_doctor_button.configure(background="#ffffff")
    edit_doctor_button.configure(borderwidth="5")
    edit_doctor_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    edit_doctor_button.configure(text='''Edit Doctor''')

    doctor_deal_button = tkinter.Button(doctor_frame, command=lambda : doctor_deal(doctors[doctors_listbox.curselection()[0]], usernames[doctors_listbox.curselection()[0]]))
    doctor_deal_button.place(relx=0.75, rely=-0.074, height=154, relwidth=0.25)
    doctor_deal_button.configure(activebackground="#f9f9f9")
    doctor_deal_button.configure(background="#ffffff")
    doctor_deal_button.configure(borderwidth="5")
    doctor_deal_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    doctor_deal_button.configure(text='''Doctor Deal''')

    return


def add_speciality_db(speciality_id, name):

    if speciality_id == None or name == None:
        return

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"INSERT INTO Speciality (speciality_id, name) VALUES ({speciality_id}, '{name}');")
    
    connection.commit()
    connection.close()

    return


def edit_speciality_db(speciality_id, name, previous_id):

    if speciality_id == None or name == None:
        return

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"UPDATE Speciality SET speciality_id = {speciality_id}, name = '{name}' WHERE speciality_id = {previous_id}")
    cursor.execute(f"UPDATE Doctor SET speciality_id = {speciality_id} WHERE speciality_id = {previous_id}")
    
    connection.commit()
    connection.close()

    return


def add_speciality():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'

    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global add_speciality_page

    add_speciality_page = tkinter.Tk()
    add_speciality_page.attributes('-fullscreen', True)
    add_speciality_page.config(background='#2d3436')

    back_button = tkinter.Button(add_speciality_page, command=add_speciality_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    add_speciality_frame = tkinter.Frame(add_speciality_page)
    add_speciality_frame.place(relx=0.365, rely=0.302, relheight=0.237, relwidth=0.273)
    add_speciality_frame.configure(relief='flat')
    add_speciality_frame.configure(borderwidth="2")
    add_speciality_frame.configure(background="#ffffff")

    speciality_id_label = tkinter.Label(add_speciality_frame)
    speciality_id_label.place(relx=0.0, rely=0.101, height=54, width=98)
    speciality_id_label.configure(background="#ffffff")
    speciality_id_label.configure(font=font9)
    speciality_id_label.configure(text='''ID''')

    speciality_name_label = tkinter.Label(add_speciality_frame)
    speciality_name_label.place(relx=0.0, rely=0.426, height=54, width=98)
    speciality_name_label.configure(background="#ffffff")
    speciality_name_label.configure(font=font9)
    speciality_name_label.configure(text='''Name''')

    speciality_id_entry = tkinter.Entry(add_speciality_frame)
    speciality_id_entry.place(relx=0.21, rely=0.101, height=53, relwidth=0.755)
    speciality_id_entry.configure(background="#dfe6e9")
    speciality_id_entry.configure(font=font9)
    speciality_id_entry.configure(relief="flat")
    speciality_id_entry.configure(justify="center")
    speciality_id_entry.configure(foreground="#ffffff")

    speciality_name_entry = tkinter.Entry(add_speciality_frame)
    speciality_name_entry.place(relx=0.21, rely=0.426,height=53, relwidth=0.755)
    speciality_name_entry.configure(background="#dfe6e9")
    speciality_name_entry.configure(font=font9)
    speciality_name_entry.configure(relief="flat")
    speciality_name_entry.configure(justify="center")
    speciality_name_entry.configure(foreground="#ffffff")

    add_speciality_submit_button = tkinter.Button(add_speciality_frame, command=lambda: add_speciality_db(speciality_id_entry.get(), speciality_name_entry.get()))
    add_speciality_submit_button.place(relx=0.038, rely=0.721, height=54, width=491)
    add_speciality_submit_button.configure(activebackground="#dfe6e9")
    add_speciality_submit_button.configure(background="#2d3436")
    add_speciality_submit_button.configure(font=font10)
    add_speciality_submit_button.configure(relief="flat")
    add_speciality_submit_button.configure(foreground="#ffffff")
    add_speciality_submit_button.configure(text='''Submit''')

    return



def edit_speciality(speciality):

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'

    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global edit_speciality_page

    edit_speciality_page = tkinter.Tk()
    edit_speciality_page.attributes('-fullscreen', True)
    edit_speciality_page.config(background='#2d3436')

    back_button = tkinter.Button(edit_speciality_page, command=edit_speciality_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    edit_speciality_frame = tkinter.Frame(edit_speciality_page)
    edit_speciality_frame.place(relx=0.365, rely=0.302, relheight=0.237, relwidth=0.273)
    edit_speciality_frame.configure(relief='flat')
    edit_speciality_frame.configure(borderwidth="2")
    edit_speciality_frame.configure(background="#ffffff")

    speciality_id_label = tkinter.Label(edit_speciality_frame)
    speciality_id_label.place(relx=0.0, rely=0.101, height=54, width=98)
    speciality_id_label.configure(background="#ffffff")
    speciality_id_label.configure(font=font9)
    speciality_id_label.configure(text='''ID''')

    speciality_name_label = tkinter.Label(edit_speciality_frame)
    speciality_name_label.place(relx=0.0, rely=0.426, height=54, width=98)
    speciality_name_label.configure(background="#ffffff")
    speciality_name_label.configure(font=font9)
    speciality_name_label.configure(text='''Name''')

    speciality_id_entry = tkinter.Entry(edit_speciality_frame)
    speciality_id_entry.place(relx=0.21, rely=0.101, height=53, relwidth=0.755)
    speciality_id_entry.configure(background="#dfe6e9")
    speciality_id_entry.configure(font=font9)
    speciality_id_entry.configure(relief="flat")
    speciality_id_entry.configure(justify="center")
    speciality_id_entry.configure(foreground="#ffffff")
    speciality_id_entry.insert(0, speciality[0])

    speciality_name_entry = tkinter.Entry(edit_speciality_frame)
    speciality_name_entry.place(relx=0.21, rely=0.426,height=53, relwidth=0.755)
    speciality_name_entry.configure(background="#dfe6e9")
    speciality_name_entry.configure(font=font9)
    speciality_name_entry.configure(relief="flat")
    speciality_name_entry.configure(justify="center")
    speciality_name_entry.configure(foreground="#ffffff")
    speciality_name_entry.insert(0, speciality[1])

    edit_speciality_submit_button = tkinter.Button(edit_speciality_frame, command=lambda: edit_speciality_db(speciality_id_entry.get(), speciality_name_entry.get(), speciality[0]))
    edit_speciality_submit_button.place(relx=0.038, rely=0.721, height=54, width=491)
    edit_speciality_submit_button.configure(activebackground="#dfe6e9")
    edit_speciality_submit_button.configure(background="#2d3436")
    edit_speciality_submit_button.configure(font=font10)
    edit_speciality_submit_button.configure(relief="flat")
    edit_speciality_submit_button.configure(foreground="#ffffff")
    edit_speciality_submit_button.configure(text='''Submit''')

    return

def delete_speciality(speciality_id):
    if speciality_id == None:
        return

    speciality_id = speciality_id[0]

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"DELETE FROM Speciality WHERE speciality_id = '{speciality_id}';")
    cursor.execute(f"DELETE FROM Doctor WHERE speciality_id = '{speciality_id}';")

    connection.commit()
    connection.close()

    return


def speciality_ui():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global specialities_page


    specialities_page = tkinter.Tk()
    specialities_page.title('Add Family')
    specialities_page.attributes('-fullscreen', True)
    specialities_page.configure(background="#2d3436")

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT speciality_id, name FROM Speciality")
    specialities = cursor.fetchall()
    
    connection.commit()
    connection.close()

    speciality_listbox = tkinter.Listbox(specialities_page)
    speciality_listbox.place(relx=0.208, rely=0.205, relheight=0.416, relwidth=0.585)
    speciality_listbox.configure(background="white")
    speciality_listbox.configure(cursor="dotbox")
    speciality_listbox.configure(font=font9)
    speciality_listbox.configure(highlightbackground="#dfe6e9")
    speciality_listbox.configure(justify='center')
    speciality_listbox.configure(relief="flat")
    speciality_listbox.configure(selectbackground="#dfe6e9")
    speciality_listbox.configure(setgrid="1")

    for i in range(len(specialities)):

        id_text = f'{specialities[i][0]}'
        speciality_text = f'{specialities[i][1]}'

        for i in range(50):
            if i == len(id_text) - 1:
                id_text += ' '
            if i == len(speciality_text) - 1:
                speciality_text += ' '

        speciality_listbox.insert(tkinter.END, f'Speciality Id: {id_text}| Speciality Name: {speciality_text}')

    back_button = tkinter.Button(specialities_page, command=specialities_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    speciality_frame = tkinter.Frame(specialities_page)
    speciality_frame.place(relx=0.208, rely=0.644, relheight=0.132, relwidth=0.586)
    speciality_frame.configure(relief='flat')
    speciality_frame.configure(borderwidth="2")

    add_speciality_button = tkinter.Button(speciality_frame, command=add_speciality)
    add_speciality_button.place(relx=0.000, rely=-0.074, height=154, relwidth=0.335)
    add_speciality_button.configure(activebackground="#f9f9f9")
    add_speciality_button.configure(background="#ffffff")
    add_speciality_button.configure(borderwidth="5")
    add_speciality_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    add_speciality_button.configure(text='''Add Speciality''')

    delete_speciality_button = tkinter.Button(speciality_frame, command=lambda: delete_speciality(specialities[speciality_listbox.curselection()[0]])) 
    delete_speciality_button.place(relx=0.335, rely=-0.074, height=154, relwidth=0.334)
    delete_speciality_button.configure(activebackground="#f9f9f9")
    delete_speciality_button.configure(background="#ffffff")
    delete_speciality_button.configure(borderwidth="5")
    delete_speciality_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    delete_speciality_button.configure(text='''Delete Speciality''')

    edit_speciality_button = tkinter.Button(speciality_frame, command=lambda : edit_speciality(specialities[speciality_listbox.curselection()[0]]))
    edit_speciality_button.place(relx=0.669, rely=-0.074, height=154, relwidth=0.334)
    edit_speciality_button.configure(activebackground="#f9f9f9")
    edit_speciality_button.configure(background="#ffffff")
    edit_speciality_button.configure(borderwidth="5")
    edit_speciality_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    edit_speciality_button.configure(text='''Edit Speciality''')

    return


def add_insurance_db(insurance):

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT name FROM Insurance WHERE name = '{insurance}';")
    insurance_name = cursor.fetchone()

    connection.commit()
    connection.close()
    
    if insurance_name == None:
        connection = sqlite3.connect('TabibYab.db')
        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO Insurance (name) VALUES ('{insurance}');")
        
        connection.commit()
        connection.close()
        
    else:
        messagebox.showinfo("Insurance Already Exists")

    return

def add_insurance():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'

    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global add_insurances_page

    add_insurance_page = tkinter.Tk()
    add_insurance_page.attributes('-fullscreen', True)
    add_insurance_page.config(background='#2d3436')
    
    add_insurance_frame = tkinter.Frame(add_insurance_page)
    add_insurance_frame.place(relx=0.391, rely=0.402, relheight=0.200, relwidth=0.211)
    add_insurance_frame.configure(relief='flat')
    add_insurance_frame.configure(borderwidth="2")
    add_insurance_frame.configure(background="#ffffff")
    add_insurance_frame.configure(cursor="heart")
    
    insurance_name_entry = tkinter.Entry(add_insurance_frame)
    insurance_name_entry.place(relx=0.101, rely=0.1, height=53, relwidth=0.825)
    insurance_name_entry.configure(background="#dfe6e9")
    insurance_name_entry.configure(font=font9)
    insurance_name_entry.configure(relief="flat")
    insurance_name_entry.configure(justify="center")
    insurance_name_entry.configure(foreground="#ffffff")
    insurance_name_entry.insert(0, 'Insurance Name')

    insurance = tkinter.Button(add_insurance_frame, command=lambda: add_insurance_db(insurance_name_entry.get()))
    insurance.place(relx=0.101, rely=0.666, height=54, relwidth=0.825)
    insurance.configure(activebackground="#dfe6e9")
    insurance.configure(background="#2d3436")
    insurance.configure(font=font10)
    insurance.configure(relief="flat")
    insurance.configure(foreground="#ffffff")
    insurance.configure(text='''Save Insurance''')

    return


def delete_insurance(insurance):

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"DELETE FROM Disease_Insurance WHERE insurance_id = '{insurance[0]}';")
    cursor.execute(f"DELETE FROM Insurance WHERE insurance_id = '{insurance[0]}';")
    cursor.execute(f"Update User SET insurance_id = 1 WHERE insurance_id = '{insurance[0]}';")
    cursor.execute(f"DELETE FROM Insurance_Doctor WHERE insurance_id = '{insurance[0]}';")

    delete = cursor.fetchone()
    connection.commit()
    connection.close()


def edit_insurance_db(insurance, previous_insurance):
    
    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"UPDATE Insurance SET name = '{insurance}' WHERE name = '{previous_insurance[1]}';")
    
    delete = cursor.fetchone()
    connection.commit()
    connection.close()


def edit_insurance(insurance):

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'

    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"


    global edit_insurance_page

    edit_insurance_page = tkinter.Tk()
    edit_insurance_page.attributes('-fullscreen', True)
    edit_insurance_page.config(background='#2d3436')
    
    edit_insurance_frame = tkinter.Frame(edit_insurance_page)
    edit_insurance_frame.place(relx=0.391, rely=0.302, relheight=0.337, relwidth=0.211)
    edit_insurance_frame.configure(relief='flat')
    edit_insurance_frame.configure(borderwidth="2")
    edit_insurance_frame.configure(background="#ffffff")
    edit_insurance_frame.configure(cursor="heart")
    
    edit_insurance_entry = tkinter.Entry(edit_insurance_frame)
    edit_insurance_entry.place(relx=0.101, rely=0.131, height=53, relwidth=0.825)
    edit_insurance_entry.configure(background="#dfe6e9")
    edit_insurance_entry.configure(font=font9)
    edit_insurance_entry.configure(relief="flat")
    edit_insurance_entry.configure(justify="center")
    edit_insurance_entry.configure(foreground="#ffffff")
    edit_insurance_entry.insert(0, insurance[1])

    edit_insurance_button = tkinter.Button(edit_insurance_frame, command=lambda: edit_insurance_db(edit_insurance_entry.get() ,insurance))
    edit_insurance_button.place(relx=0.101, rely=0.721, height=54, width=331)
    edit_insurance_button.configure(activebackground="#dfe6e9")
    edit_insurance_button.configure(background="#2d3436")
    edit_insurance_button.configure(font=font10)
    edit_insurance_button.configure(relief="flat")
    edit_insurance_button.configure(foreground="#ffffff")
    edit_insurance_button.configure(text='''Update Insurance''')

    return


def insurance_remove_db(disease, insurance):

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT disease_id FROM Disease WHERE title = '{disease}'")
    disease_id = cursor.fetchone()[0]

    cursor.execute(f"DELETE FROM Disease_Insurance WHERE disease_id = '{disease_id}' AND insurance_id = '{insurance[0]}';")
    
    delete = cursor.fetchone()
    connection.commit()
    connection.close()

    return

def insurance_support_db(disease, insurance, discount):
    
    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT disease_id FROM Disease WHERE title = '{disease}'")
    disease_id = cursor.fetchone()[0]

    cursor.execute(f"INSERT INTO Disease_Insurance (insurance_id, disease_id, discount_percent) VALUES ('{insurance[0]}', '{disease_id}', {int(discount)});")
    
    delete = cursor.fetchone()
    connection.commit()
    connection.close()

    return



def insurance_support(insurance):

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'

    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global insurances_support_page

    insurances_support_page = tkinter.Tk()
    insurances_support_page.attributes('-fullscreen', True)
    insurances_support_page.configure(background="#2d3436")

    insurance_support_frame = tkinter.Frame(insurances_support_page)
    insurance_support_frame.place(relx=0.391, rely=0.302, relheight=0.337, relwidth=0.211)
    insurance_support_frame.configure(relief='flat')
    insurance_support_frame.configure(borderwidth="2")
    insurance_support_frame.configure(background="#ffffff")
    insurance_support_frame.configure(cursor="heart")
    
    insurance_support_entry = tkinter.Entry(insurance_support_frame)
    insurance_support_entry.place(relx=0.101, rely=0.1, height=53, relwidth=0.825)
    insurance_support_entry.configure(background="#dfe6e9")
    insurance_support_entry.configure(font=font9)
    insurance_support_entry.configure(relief="flat")
    insurance_support_entry.configure(justify="center")
    insurance_support_entry.configure(foreground="#ffffff")
    insurance_support_entry.insert(0, 'Disease Name')

    insurance_discount_entry = tkinter.Entry(insurance_support_frame)
    insurance_discount_entry.place(relx=0.101, rely=0.3, height=53, relwidth=0.825)
    insurance_discount_entry.configure(background="#dfe6e9")
    insurance_discount_entry.configure(font=font9)
    insurance_discount_entry.configure(relief="flat")
    insurance_discount_entry.configure(justify="center")
    insurance_discount_entry.configure(foreground="#ffffff")
    insurance_discount_entry.insert(0, 'Discount Percent')

    insurance_support_button = tkinter.Button(insurance_support_frame, command=lambda: insurance_support_db(insurance_support_entry.get(), insurance, insurance_discount_entry.get()))
    insurance_support_button.place(relx=0.101, rely=0.5, height=54, width=331)
    insurance_support_button.configure(activebackground="#dfe6e9")
    insurance_support_button.configure(background="#2d3436")
    insurance_support_button.configure(font=font10)
    insurance_support_button.configure(relief="flat")
    insurance_support_button.configure(foreground="#ffffff")
    insurance_support_button.configure(text='''Support Disease''')

    insurance_support_button = tkinter.Button(insurance_support_frame, command=lambda: insurance_remove_db(insurance_support_entry.get(), insurance))
    insurance_support_button.place(relx=0.101, rely=0.7, height=54, width=331)
    insurance_support_button.configure(activebackground="#dfe6e9")
    insurance_support_button.configure(background="#2d3436")
    insurance_support_button.configure(font=font10)
    insurance_support_button.configure(relief="flat")
    insurance_support_button.configure(foreground="#ffffff")
    insurance_support_button.configure(text='''Remove Disease''')

    return




def insurance_ui():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'

    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global insurances_page

    insurances_page = tkinter.Tk()
    insurances_page.attributes('-fullscreen', True)
    insurances_page.configure(background="#2d3436")

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT insurance_id, name FROM Insurance")
    insurances = cursor.fetchall()
    
    connection.commit()
    connection.close()

    insurances_listbox = tkinter.Listbox(insurances_page)
    insurances_listbox.place(relx=0.208, rely=0.205, relheight=0.416, relwidth=0.585)
    insurances_listbox.configure(background="white")
    insurances_listbox.configure(cursor="dotbox")
    insurances_listbox.configure(font=font9)
    insurances_listbox.configure(highlightbackground="#dfe6e9")
    insurances_listbox.configure(justify='center')
    insurances_listbox.configure(relief="flat")
    insurances_listbox.configure(selectbackground="#dfe6e9")
    insurances_listbox.configure(setgrid="1")

    for i in range(len(insurances)):

        id_text = f'{insurances[i][0]}'
        insurances_text = f'{insurances[i][1]}'

        for i in range(50):
            if i == len(id_text) - 1:
                id_text += ' '
            if i == len(insurances_text) - 1:
                insurances_text += ' '

        insurances_listbox.insert(tkinter.END, f'Insurance Id: {id_text}| Insurance Name: {insurances_text}')

    back_button = tkinter.Button(insurances_page, command=insurances_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    insurances_frame = tkinter.Frame(insurances_page)
    insurances_frame.place(relx=0.208, rely=0.644, relheight=0.132, relwidth=0.586)
    insurances_frame.configure(relief='flat')
    insurances_frame.configure(borderwidth="2")

    add_insurance_button = tkinter.Button(insurances_frame, command=add_insurance)
    add_insurance_button.place(relx=0.000, rely=-0.074, height=154, relwidth=0.25)
    add_insurance_button.configure(activebackground="#f9f9f9")
    add_insurance_button.configure(background="#ffffff")
    add_insurance_button.configure(borderwidth="5")
    add_insurance_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    add_insurance_button.configure(text='''Add Insurance''')

    delete_insurance_button = tkinter.Button(insurances_frame, command=lambda: delete_insurance(insurances[insurances_listbox.curselection()[0]])) 
    delete_insurance_button.place(relx=0.25, rely=-0.074, height=154, relwidth=0.25)
    delete_insurance_button.configure(activebackground="#f9f9f9")
    delete_insurance_button.configure(background="#ffffff")
    delete_insurance_button.configure(borderwidth="5")
    delete_insurance_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    delete_insurance_button.configure(text='''Delete Insurance''')

    edit_insurance_button = tkinter.Button(insurances_frame, command=lambda : edit_insurance(insurances[insurances_listbox.curselection()[0]]))
    edit_insurance_button.place(relx=0.5, rely=-0.074, height=154, relwidth=0.25)
    edit_insurance_button.configure(activebackground="#f9f9f9")
    edit_insurance_button.configure(background="#ffffff")
    edit_insurance_button.configure(borderwidth="5")
    edit_insurance_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    edit_insurance_button.configure(text='''Edit Insurance''')

    insurance_support_button = tkinter.Button(insurances_frame, command=lambda : insurance_support(insurances[insurances_listbox.curselection()[0]]))
    insurance_support_button.place(relx=0.75, rely=-0.074, height=154, relwidth=0.25)
    insurance_support_button.configure(activebackground="#f9f9f9")
    insurance_support_button.configure(background="#ffffff")
    insurance_support_button.configure(borderwidth="5")
    insurance_support_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    insurance_support_button.configure(text='''Insurance Support''')

    return


def add_disease_db(disease):
    
    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT title FROM Disease WHERE title = '{disease}';")
    disease_name = cursor.fetchone()

    connection.commit()
    connection.close()

    if disease_name == None:

        connection = sqlite3.connect('TabibYab.db')
        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO Disease (title) VALUES ('{disease}');")
        
        connection.commit()
        connection.close()
        
    else:
        messagebox.showinfo("Disease Already Exists")


def add_disease():

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'

    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global add_disease_page

    add_disease_page = tkinter.Tk()
    add_disease_page.attributes('-fullscreen', True)
    add_disease_page.config(background='#2d3436')
    
    add_disease_page_frame = tkinter.Frame(add_disease_page)
    add_disease_page_frame.place(relx=0.391, rely=0.302, relheight=0.337, relwidth=0.211)
    add_disease_page_frame.configure(relief='flat')
    add_disease_page_frame.configure(background="#ffffff")
    add_disease_page_frame.configure(cursor="heart")
    
    add_disease_entry = tkinter.Entry(add_disease_page_frame)
    add_disease_entry.place(relx=0.101, rely=0.131, height=53, relwidth=0.825)
    add_disease_entry.configure(background="#dfe6e9")
    add_disease_entry.configure(font=font9)
    add_disease_entry.configure(relief="flat")
    add_disease_entry.configure(justify="center")
    add_disease_entry.configure(foreground="#ffffff")
    add_disease_entry.insert(0, 'Disease Name')

    add_disease_button = tkinter.Button(add_disease_page_frame, command=lambda: add_disease_db(add_disease_entry.get()))
    add_disease_button.place(relx=0.101, rely=0.721, height=54, width=331)
    add_disease_button.configure(activebackground="#dfe6e9")
    add_disease_button.configure(background="#2d3436")
    add_disease_button.configure(font=font10)
    add_disease_button.configure(relief="flat")
    add_disease_button.configure(foreground="#ffffff")
    add_disease_button.configure(text='''Add Disease''')


def edit_disease_db(disease, previous_disease):
    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"UPDATE Disease SET title = '{disease}' WHERE title = '{previous_disease[1]}';")
    
    delete = cursor.fetchone()
    connection.commit()
    connection.close()


def edit_disease(disease):

    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global edit_disease_page

    edit_disease_page = tkinter.Tk()
    edit_disease_page.attributes('-fullscreen', True)
    edit_disease_page.config(background='#2d3436')
    
    edit_disease_frame = tkinter.Frame(edit_disease_page)
    edit_disease_frame.place(relx=0.391, rely=0.302, relheight=0.337, relwidth=0.211)
    edit_disease_frame.configure(relief='flat')
    edit_disease_frame.configure(borderwidth="2")
    edit_disease_frame.configure(background="#ffffff")
    edit_disease_frame.configure(cursor="heart")
    
    edit_disease_entry = tkinter.Entry(edit_disease_frame)
    edit_disease_entry.place(relx=0.101, rely=0.131, height=53, relwidth=0.825)
    edit_disease_entry.configure(background="#dfe6e9")
    edit_disease_entry.configure(font=font9)
    edit_disease_entry.configure(relief="flat")
    edit_disease_entry.configure(justify="center")
    edit_disease_entry.configure(foreground="#ffffff")
    edit_disease_entry.insert(0, 'Disease Name')

    edit_disease_button = tkinter.Button(edit_disease_frame, command=lambda: edit_disease_db(edit_disease_entry.get(), disease))
    edit_disease_button.place(relx=0.101, rely=0.721, height=54, width=331)
    edit_disease_button.configure(activebackground="#dfe6e9")
    edit_disease_button.configure(background="#2d3436")
    edit_disease_button.configure(font=font10)
    edit_disease_button.configure(relief="flat")
    edit_disease_button.configure(foreground="#ffffff")
    edit_disease_button.configure(text='''Edit Name''')


def delete_disease(disease):

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()

    cursor.execute(f"DELETE FROM Disease_Insurance WHERE disease_id = '{disease[0]}';")
    cursor.execute(f"DELETE FROM Disease WHERE disease_id = '{disease[0]}';")
    
    connection.commit()
    connection.close()

    return

def disease_ui():
    
    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'

    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    global disease_page

    disease_page = tkinter.Tk()
    disease_page.title('disease')
    disease_page.attributes('-fullscreen', True)
    disease_page.configure(background="#2d3436")

    connection = sqlite3.connect('TabibYab.db')
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT disease_id, title FROM Disease")
    diseases = cursor.fetchall()
    
    connection.commit()
    connection.close()

    disease_listbox = tkinter.Listbox(disease_page)
    disease_listbox.place(relx=0.208, rely=0.205, relheight=0.416, relwidth=0.585)
    disease_listbox.configure(background="white")
    disease_listbox.configure(cursor="dotbox")
    disease_listbox.configure(font=font9)
    disease_listbox.configure(highlightbackground="#dfe6e9")
    disease_listbox.configure(justify='center')
    disease_listbox.configure(relief="flat")
    disease_listbox.configure(selectbackground="#dfe6e9")
    disease_listbox.configure(setgrid="1")

    for i in range(len(diseases)):

        id_text = f'{diseases[i][0]}'
        diseases_text = f'{diseases[i][1]}'

        for i in range(50):
            if i == len(id_text) - 1:
                id_text += ' '
            if i == len(diseases_text) - 1:
                diseases_text += ' '

        disease_listbox.insert(tkinter.END, f'Disease Id: {id_text}| Disease Name: {diseases_text}')

    back_button = tkinter.Button(disease_page, command=disease_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''Back''')

    disease_frame = tkinter.Frame(disease_page)
    disease_frame.place(relx=0.208, rely=0.644, relheight=0.132, relwidth=0.586)
    disease_frame.configure(relief='flat')
    
    add_disease_button = tkinter.Button(disease_frame, command=add_disease)
    add_disease_button.place(relx=0.000, rely=-0.074, height=154, relwidth=0.334)
    add_disease_button.configure(activebackground="#f9f9f9")
    add_disease_button.configure(background="#ffffff")
    add_disease_button.configure(borderwidth="5")
    add_disease_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    add_disease_button.configure(text='''Add Disease''')

    delete_disease_button = tkinter.Button(disease_frame, command=lambda: delete_disease(diseases[disease_listbox.curselection()[0]])) 
    delete_disease_button.place(relx=0.334, rely=-0.074, height=154, relwidth=0.335)
    delete_disease_button.configure(activebackground="#f9f9f9")
    delete_disease_button.configure(background="#ffffff")
    delete_disease_button.configure(borderwidth="5")
    delete_disease_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    delete_disease_button.configure(text='''Delete Disease''')

    edit_disease_button = tkinter.Button(disease_frame, command=lambda : edit_disease(diseases[disease_listbox.curselection()[0]]))
    edit_disease_button.place(relx=0.669, rely=-0.074, height=154, relwidth=0.333)
    edit_disease_button.configure(activebackground="#f9f9f9")
    edit_disease_button.configure(background="#ffffff")
    edit_disease_button.configure(borderwidth="5")
    edit_disease_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    edit_disease_button.configure(text='''Edit Disease''')

    return



def home_ui():
    
    global home_page

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'

    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    home_page = tkinter.Tk()
    home_page.attributes('-fullscreen', True)
    home_page.config(background='#2d3436')

    back_button = tkinter.Button(home_page, command=home_page.destroy)
    back_button.place(relx=0.016, rely=0.02, height=54, width=71)
    back_button.configure(activeforeground="#2d3436")
    back_button.configure(background="#2d3436")
    back_button.configure(font=font9)
    back_button.configure(foreground="#ffffff")
    back_button.configure(relief="flat")
    back_button.configure(text='''EXIT''')

    doctor_frame = tkinter.Frame(home_page)
    doctor_frame.place(relx=0.193, rely=0.4, relheight=0.132, relwidth=0.586)
    doctor_frame.configure(relief='flat')
    doctor_frame.configure(borderwidth="0")

    doctor_button = tkinter.Button(doctor_frame, command=doctor_ui)
    doctor_button.place(relx=0, rely=-0.074, height=164, relwidth=0.25)
    doctor_button.configure(activebackground="#f9f9f9")
    doctor_button.configure(background="#ffffff")
    doctor_button.configure(borderwidth="5")
    doctor_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    doctor_button.configure(text='''Doctors''')

    speciality_button = tkinter.Button(doctor_frame, command=speciality_ui)
    speciality_button.place(relx=0.25, rely=-0.074, height=164, relwidth=0.25)
    speciality_button.configure(activebackground="#f9f9f9")
    speciality_button.configure(background="#ffffff")
    speciality_button.configure(borderwidth="5")
    speciality_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    speciality_button.configure(text='''Specialities''')

    insurance_button = tkinter.Button(doctor_frame, command=insurance_ui)
    insurance_button.place(relx=0.500, rely=-0.074, height=164, relwidth=0.25)
    insurance_button.configure(activebackground="#f9f9f9")
    insurance_button.configure(background="#ffffff")
    insurance_button.configure(borderwidth="5")
    insurance_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    insurance_button.configure(text='''Insurances''')

    disease_button = tkinter.Button(doctor_frame, command=disease_ui)
    disease_button.place(relx=0.750, rely=-0.074, height=164, relwidth=0.251)
    disease_button.configure(activebackground="#f9f9f9")
    disease_button.configure(background="#ffffff")
    disease_button.configure(borderwidth="5")
    disease_button.configure(font="-family {ubvazir} -size 10 -weight bold")
    disease_button.configure(text='''Diseases''')

    root.destroy()

    return


def login_check(username, password):

    if username == 'Admin' and password == 'password':
        home_ui()
    else:
        print('You Are not Admin')
    
    return



def start():

    global root

    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'

    font10 = "-family ubvazir -size 10 -weight bold -slant roman -underline 0 -overstrike 0"
    font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

    root = tkinter.Tk()
    root.attributes('-fullscreen', True)
    root.config(background='#2d3436')

    Login = tkinter.Frame(root)
    Login.place(relx=0.391, rely=0.302, relheight=0.337, relwidth=0.211)
    Login.configure(relief='flat')
    Login.configure(borderwidth="2")
    Login.configure(background="#ffffff")
    Login.configure(cursor="heart")

    username_entry = tkinter.Entry(Login)
    username_entry.place(relx=0.101, rely=0.131, height=53, relwidth=0.825)
    username_entry.configure(background="#dfe6e9")
    username_entry.configure(font=font9)
    username_entry.configure(relief="flat")
    username_entry.configure(justify="center")
    username_entry.configure(foreground="#ffffff")
    username_entry.insert(0, 'Username')

    password_entry = tkinter.Entry(Login)
    password_entry.place(relx=0.101, rely=0.426,height=53, relwidth=0.825)
    password_entry.configure(background="#dfe6e9")
    password_entry.configure(font=font9)
    password_entry.configure(relief="flat")
    password_entry.configure(justify="center")
    password_entry.configure(foreground="#ffffff")
    password_entry.insert(0, 'Password')

    login = tkinter.Button(Login, command=lambda: login_check(username_entry.get(), password_entry.get()))
    login.place(relx=0.101, rely=0.721, height=54, width=331)
    login.configure(activebackground="#dfe6e9")
    login.configure(background="#2d3436")
    login.configure(font=font10)
    login.configure(relief="flat")
    login.configure(foreground="#ffffff")
    login.configure(text='''Login''')

    root.mainloop()

    return

start()