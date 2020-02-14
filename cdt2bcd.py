import tkinter, os, os.path
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()
home = os.path.expanduser("~")
cdt_path = filedialog.askopenfilename(initialdir = home + '/Desktop',title = "Select A Super Mario Maker Course Data Table",filetypes = (("Course Data Table","*.cdt"),("All Files","*.*")))
with open(cdt_path,'rb') as cdt:
    cdt.seek(283)
    start_y = cdt.read(1)
    cdt.seek(347)
    goal_y = cdt.read(1)
    cdt.seek(370)
    goal_x = cdt.read(2)
    goal_x = bytearray(goal_x)
    goal_x.reverse()
    goal_x = bytes(goal_x)
    cdt.seek(112)
    time_limit = cdt.read(2)
    time_limit = bytearray(time_limit)
    time_limit.reverse()
    time_limit = bytes(time_limit)
    cdt.seek(16)
    save_year = cdt.read(2)
    save_year = bytearray(save_year)
    save_year.reverse()
    save_year = bytes(save_year)
    cdt.seek(18)
    save_month = cdt.read(1)
    cdt.seek(19)
    save_day = cdt.read(1)
    cdt.seek(20)
    save_hour = cdt.read(1)
    cdt.seek(21)
    save_minute = cdt.read(1)
    cdt.seek(106)
    course_style = cdt.read(2)
    cdt.seek(41)
    course_name = cdt.read(63)
    cdt.seek(236)
    object_count = cdt.read(4)
    object_count = bytearray(object_count)
    object_count.reverse()
    object_count = bytes(object_count)
    with open(home + '\Desktop\course_data_000.bcd','wb') as bcd:
        b = bytes(2)
        c = bytes(226)
        d = bytes(1)
        e = bytes(233)
        f = bytes(28)
        bcd.write(bytes.fromhex('000000000B000000000000005343444C') + start_y + goal_y + goal_x + time_limit + b + save_year + save_month + save_day + save_hour + save_minute + c + bytes([255]) + course_style + d +course_name + e + object_count + f)
        objs = []
        for i in range(2594):
            with open(cdt_path,'rb') as cdt:
                cdt.seek(432 + 32 * i)
                x_position = cdt.read(4)
                x_position = bytearray(x_position)
                x_position.reverse()
                x_position = bytes(x_position)
                cdt.seek(436 + 32 * i)
                z_position = cdt.read(4)
                z_position = bytearray(z_position)
                z_position.reverse()
                z_position = bytes(z_position)
                cdt.seek(440 + 32 * i)
                y_position = cdt.read(2)
                y_position = bytearray(y_position)
                y_position.reverse()
                y_position = bytes(y_position)
                cdt.seek(442 + 32 * i)
                width = cdt.read(1)
                cdt.seek(433 + 32 * i)
                height = cdt.read(1)
                cdt.seek(444 + 32 * i)
                main_flags = cdt.read(4)
                main_flags = bytearray(main_flags)
                main_flags.reverse()
                main_flags = bytes(main_flags)
                cdt.seek(448 + 32 * i)
                secondary_flags = cdt.read(4)
                secondary_flags = bytearray(secondary_flags)
                secondary_flags.reverse()
                secondary_flags = bytes(secondary_flags)
                cdt.seek(452 + 32 * i)
                extended_obj_data = cdt.read(4)
                extended_obj_data = bytearray(extended_obj_data)
                extended_obj_data.reverse()
                extended_obj_data = bytes(extended_obj_data)
                cdt.seek(456 + 32 * i)
                object_id_data = cdt.read(8)
                object = bytes.hex(x_position + z_position + y_position + width + height + main_flags + secondary_flags + extended_obj_data + object_id_data)
                objs.append(object)
        objs = ''.join(objs)
        with open(home + '\Desktop\course_data_000.bcd','wb') as bcd:
            bcd.seek(584)
            bcd.write(bytes.fromhex(objs))
            bcd.seek(83592)
            bcd.write(bytes(293128) + bytes.fromhex('B1D37F9DF9A2AF2D94C9538F1FA81928F9A2AF2DB1D37F9D1FA8192894C9538F13D88EE8BD403CB0132EE15B655EEE3E'))
            print('Completed!')
