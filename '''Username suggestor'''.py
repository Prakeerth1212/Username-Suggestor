s=input('Enter the name:')
b=int(input('Enter birth year:'))
if len(s)<2:
    print('Enter full name:')
username1=s+str(b)
username2=str(b)+s
print('''Usernames that can be used are:
            ''',username1,'''and
            ''',username2)