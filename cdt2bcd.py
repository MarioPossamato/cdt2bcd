import tkinter, os, os.path, binascii
from tkinter import filedialog

buffer = []

root = tkinter.Tk()
root.withdraw()
home = os.path.expanduser("~")
cdt_path = filedialog.askopenfilename(initialdir = home + '/Desktop',title = "Select A Main Super Mario Maker Course Data Table",filetypes = (("Course Data Table","*.cdt"),("All Files","*.*")))
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
        f = bytes(40)
        buffer.append(bytes.hex(bytes.fromhex('000000000B000000000000005343444C') + start_y + goal_y + goal_x + time_limit + b + save_year + save_month + save_day + save_hour + save_minute + c + bytes([255]) + course_style + d +course_name + e + object_count + f))
        objs = []
        with open(cdt_path,'rb') as cdt:
            for i in range(2594):
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
            buffer.append(bytes.hex(bytes.fromhex(objs) + bytes(105076)))
            print('Main File Data Conversion Completed!')

cdt_path = filedialog.askopenfilename(initialdir = home + '/Desktop',title = "Select A Sub Super Mario Maker Course Data Table",filetypes = (("Course Data Table","*.cdt"),("All Files","*.*")))
with open(cdt_path,'rb') as cdt:
    cdt.seek(236)
    object_count = cdt.read(4)
    object_count = bytearray(object_count)
    object_count.reverse()
    object_count = bytes(object_count)
    objs = []
    with open(cdt_path,'rb') as cdt:
            for i in range(2594):
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
                buffer.append(bytes.hex(object_count + bytes(40) + bytes.fromhex(objs) + bytes(104856) + bytes.fromhex('B1D37F9DF9A2AF2D94C9538F1FA81928F9A2AF2DB1D37F9D1FA8192894C9538F13D88EE8BD403CB0132EE15B655EEE3E')))
                bcd.seek(0)
                buffer = ''.join(buffer)
                buffer = bytes.fromhex(buffer)
                bcd.write(buffer)
                print('Sub File Data Conversion Completed!')

# fixes CRC32 Checksum
def fixLevel(data):
    crc = binascii.crc32(data[16:]) & 0xFFFFFFFF
    data = bytearray(data)
    data[8] = crc >> 24
    data[9] = (crc >> 16) & 0xFF
    data[10] = (crc >> 8) & 0xFF
    data[11] = crc & 0xFF
    return bytes(data)

def main():
    with open(home + '\Desktop\course_data_000.bcd', 'rb') as f:
        data = f.read()
    with open(home + '\Desktop\course_data_000.bcd', 'wb') as f:
        f.write(fixLevel(data))
        print('CRC32 Corrected Successfully!')

main()
