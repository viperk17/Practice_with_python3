# # print(__name__)
#
#
# def main():
#     print("First Module's Name: {}".format(__name__))
#
#
# if __name__=='__main__':
#     main()

# if __name__=='__main__':
#     print('Runs Directly')
# else:
#     print('Run from import')

print('THis will always be run')

def main():
    print("First Module's Main Method")

if __name__=='__main__':
    main()