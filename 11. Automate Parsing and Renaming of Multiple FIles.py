import os


os.chdir('/home/viper/Downloads/')

print(os.getcwd())
for f in os.listdir():
    print(f)
    # to split the format of file eg. .jpg
    print(os.path.splitext(f))  # o/p i n tuple

    f_name, f_ext = os.path.splitext(f) 
    print(f_name, f_ext)
    print(f_name.split('.deb'))

    # f_title = f_title.strip()
    # f_course = f_course.strip()
    # f_num = f_num.strip()[1:].zfill(2)    # .zfill() adds 0 to one digit numbers 

    # f_title, f_num, f_course = f_name.split('-')
    # print((f_course))
    # print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))

    # new_name = '{}-{}-{}{}'.format(f_num, f_title, f_course, f_ext)
    # os.rename(f, new_name)
    # print(new_name)
    # print('{}-{}-{}'.format(f_title, f_course,  f_ext))
