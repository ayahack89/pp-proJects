import time

username = 'Ayanabha'
password = 'zerotohero'
username_input = input('Enter your Username: ')
password_input = input('Enter a valid Password: ')

if username_input == username and password_input == password:
    print('ACCES GRANDED >>>')
    print('Please wait.....')
    time.sleep(8)
    print('Ok Loading...')
    time.sleep(5)
    print('Fuck yeha.....')
    time.sleep(4)
    print('Ohh , yeha _ Now you are enter in our fucking compiler')
    time.sleep(2)
    print('you are succesfully in.')
elif username_input == username and password_input != password:
    print('ERROR >>> Incorrect Password')
elif username_input != username and password_input == password:
    print('ERROR >>>Inccorect Username')
else:
    print('ERRROR>>>>>  Go fuck your own self....')




