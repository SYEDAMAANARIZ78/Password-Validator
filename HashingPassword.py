import bcrypt

password = b"Syed@2003"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

'''entered_password = input('Enter Password to Login:')
entered_password = bytes(entered_password, encoding='utf-8')

if bcrypt.checkpw(entered_password,hashed):
    print('Login successful')
else:
    print('Invalid Password')'''