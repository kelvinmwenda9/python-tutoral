try:
    with open('sampe/newfile.txt', mode='a') as file:
        # file.write('This is a new file created')
        # writelines [,]
        file.writelines(['\nThis is a new line', '\nthis is a second line'])
        # write on top of file without overwriting
        # mode a
except FileNotFoundError as e:
    print('Error', e)