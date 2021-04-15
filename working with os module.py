import os
from datetime import datetime
# print(os.getcwd())

# os.chdir('/home/viper/Downloads')
# print(os.getcwd())


# os.mkdir('OS-Demo')   # creates folder
# os.mkdir('OS-Demo/Demo/Sub1')    # creates sub directories

# os.rmdir('/OS-Demo/Demo/Sub1')
# os.removedirs('/OS-Demo')     # remvoes directories

# os.rename('UID.pdf','uid.pdf')

# print(os.stat('uid.pdf').st_mtime)

# Human Readable time
# md_time = os.stat('uid.pdf').st_mtime
# print("\n",datetime.fromtimestamp(md_time))

# print(os.listdir())

#########################To see Entire Directory Tree #################################
# os.walk()   # walk is a generator which yields tuple of 3 values

# print(os.environ.get('HOME'))


# for dirpath, dirnames, filenames in os.walk('/home/viper/Downloads'):
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()

    

################################END####################################################

#### OS.PATH ###########
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))