import re

def isStrongPassword(password):
    passRegex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}')
    passwordValidation = passRegex.search(password)
        
    if passwordValidation != None:
        return True

print('Enter password to validate:')
password = input()
test = isStrongPassword(password)
if test == True:
    print('Password is strong!')
else:
    print('Password is not strong.')
