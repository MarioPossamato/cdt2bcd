# -*- coding: utf-8 -*-
# cdt2bcd, an experimental command line tool to try and convert an SMM1 course (course_data.cdt, course_data_sub.cdt) to work with SMM2 (course_data_000.bcd)

# import modules
import sys

# create buffers
buffer = []
main_area_buffer = []
sub_area_buffer = []

#  check to see if the user input any arguments, print usage if not
try:
    main_area_cdt = sys.argv[1]
    sub_area_cdt = sys.argv[2]
    flag = sys.argv[3]
    output_bcd = sys.argv[4]
    print(main_area_cdt, sub_area_cdt, flag, output_bcd)
except:
    print('usage: python3 cdt2bcd.py <main_area_input> <sub_area_input> <flag> <bcd_output>')
    print('flag -d: does not encrypt the output bcd before it has been written out')
    print('flag -e: encrypts the output bcd before it has been written out')
    print('if <bcd_output> is @default, cdt2bcd will write the output bcd to //default_course_data_000.bcd')
    quit()

# open and read main area cdt
with open(main_area_cdt,'rb') as main_cdt:
    # start y
    main_cdt.seek(283)
    start_y = main_cdt.read(1)
    main_area_buffer.append(bytes.hex(start_y))
    # goal y
    main_cdt.seek(347)
    goal_y = main_cdt.read(1)
    main_area_buffer.append(bytes.hex(goal_y))
    # goal x
    main_cdt.seek(345)
    goal_x = main_cdt.read(2)
    goal_x = bytearray(goal_x)
    goal_x.reverse()
    goal_x = bytes(goal_x)
    main_area_buffer.append(bytes.hex(goal_x))
    # time limit
    main_cdt.seek(112)
    time_limit = main_cdt.read(2)
    time_limit = bytearray(time_limit)
    time_limit.reverse()
    time_limit = bytes(time_limit)
    main_area_buffer.append(bytes.hex(time_limit))
    # clear condition amount
    main_area_buffer.append('0000')
    # last saved year
    main_cdt.seek(16)
    last_saved_year = main_cdt.read(2)
    last_saved_year = bytearray(last_saved_year)
    last_saved_year.reverse()
    last_saved_year = bytes(last_saved_year)
    main_area_buffer.append(bytes.hex(last_saved_year))
    # last saved month, day, hour, and minute
    main_cdt.seek(18)
    last_saved_month_day_hour_minute = main_cdt.read(4)
    main_area_buffer.append(bytes.hex(last_saved_month_day_hour_minute))
    # custom autoscroll speed, clear condition category, clear condition CRC32, Game Version, Management Flags, Number Of Clear Check Tries, Clear Check Time, Creation ID, and Upload ID
    main_area_buffer.append('000000000000110000004100000000000000FFFFFFFF077B56E2000000000000000000000000')
    # padding
    main_area_buffer.append(bytes.hex(bytes(188)))
    # unknown, usually 0xFF
    main_area_buffer.append('FF')
    # game style (M1, M3, MW, WU, 3W)
    main_cdt.seek(106)
    game_style = main_cdt.read(3)
    main_area_buffer.append(bytes.hex(game_style))
    # course name (utf-16)
    main_cdt.seek(41)
    course_name = main_cdt.read(65)
    main_area_buffer.append(bytes.hex(course_name))
    # course decription (utf-16)
    main_area_buffer.append(bytes.hex(bytes(203)))
    # course theme
    main_cdt.seek(109)
    course_theme = main_cdt.read(1)
    main_area_buffer.append(bytes.hex(course_theme))
    # autoscroll type
    main_cdt.seek(114)
    autoscroll_type = main_cdt.read(1)
    main_area_buffer.append(bytes.hex(autoscroll_type))
    # screen boundary flags, area orientation (0=horizontal, 1=vertical), end liquid height,  liquid mode,liquid speed, and start liguid height
    # right boundary, top boundary, left boundary, and bottom boundary
    main_area_buffer.append('000000000000800A0000B0010000000000000000000000000000')
    # object cound
    main_cdt.seek(236)
    object_count = main_cdt.read(4)
    object_count = bytearray(object_count)
    object_count.reverse()
    object_count = bytes(object_count)
    main_area_buffer.append(bytes.hex(object_count))
    # sound effect count, snake block count, clear pipe count, piranha creeper count, ! block count, padding, tile count, track count, icicle count
    main_area_buffer.append(bytes.hex(bytes(24)))
    # object data
    for i in range(2600):
        # x position
        main_cdt.seek(240 + 32 * i)
        x_position = main_cdt.read(4)
        x_position = bytearray(x_position)
        x_position.reverse()
        x_position = bytes.hex(bytes(x_position))
        # y position
        main_cdt.seek(248 + 32 * i)
        y_position = main_cdt.read(2)
        y_position = bytearray(y_position)
        y_position.reverse()
        y_position = bytes.hex(bytes(y_position))
        y_position = y_position+'0000'
        # padding
        padding = '0000'
        # width
        main_cdt.seek(250 + 32 * i)
        width = main_cdt.read(1)
        width = bytes.hex(width)
        # height
        main_cdt.seek(251 + 32 * i)
        height = main_cdt.read(1)
        height = bytes.hex(bytes(height))
        # object flags
        main_cdt.seek(252 + 32 * i)
        object_flags = main_cdt.read(4)
        object_flags = bytearray(object_flags)
        object_flags.reverse()
        object_flags = bytes.hex(bytes(object_flags))
        # child object flags
        main_cdt.seek(256 + 32 * i)
        child_object_flags = main_cdt.read(4)
        child_object_flags = bytearray(child_object_flags)
        child_object_flags.reverse()
        child_object_flags = bytes.hex(bytes(child_object_flags))
        # extended object data
        main_cdt.seek(260 + 32 * i)
        extended_object_data = main_cdt.read(4)
        extended_object_data = bytearray(extended_object_data)
        extended_object_data.reverse()
        extended_object_data = bytes.hex(bytes(extended_object_data))
        # object type
        main_cdt.seek(264 + 32 * i)
        object_type = main_cdt.read(1)
        object_type = bytearray(object_type)
        object_type.reverse()
        object_type = bytes.hex(bytes(object_type))
        # child object type
        main_cdt.seek(265 + 32 * i)
        child_object_type = main_cdt.read(1)
        child_object_type = bytearray(child_object_type)
        child_object_type.reverse()
        child_object_type = bytes.hex(bytes(child_object_type))
        # link id
        main_cdt.seek(266 + 32 * i)
        link_id = main_cdt.read(2)
        link_id = bytearray(link_id)
        link_id.reverse()
        link_id = bytes.hex(bytes(link_id))
        # effect index
        main_cdt.seek(268 + 32 * i)
        effect_index = main_cdt.read(2)
        effect_index = bytearray(effect_index)
        effect_index.reverse()
        effect_index = bytes.hex(bytes(effect_index))
        # unknown
        main_cdt.seek(271 + 32 * i)
        unknown = main_cdt.read(1)
        unknown = bytes.hex(unknown)
        # child object transformation id
        main_cdt.seek(271 + 32 * i)
        child_object_transformation_id = main_cdt.read(1)
        child_object_transformation_id = bytes.hex(child_object_transformation_id)
        object_data_buffer = (x_position+y_position+padding+width+height+object_flags+child_object_flags+extended_object_data+object_type+child_object_type+link_id+effect_index+unknown+child_object_transformation_id)
        main_area_buffer.append(object_data_buffer)
    
    main_area_buffer = ''.join(main_area_buffer)
    with open(output_bcd,'wb') as output_bcd:
        output_bcd.write(bytes.fromhex(main_area_buffer))

def encryptCourse(courseData):
    courseMagic = bytes.hex(b'SCDL') # 0x5353444C
