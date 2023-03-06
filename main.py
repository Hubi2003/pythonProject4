import re
def password_strenght(password):
    score = 0
    if len(password) >= 8:
        score += 5
    if re.search(r'[A-Z]', password):
        score += 3
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 2
    if re.search(r'[\W_]', password):
        score += 1
    return score



def is_common_password(password):
     keyword_patterns = ['qwerty', 'password', '1234', '2345', '3456', '4567', '5678', '6789', '0000', '1111', '2222',
                        '3333', '4444', '5555', '6666', '7777', '8888', '9999', '123', 'Qwertyui', 'Hasło','Hasełko''abc']
     for patterns in keyword_patterns:
         if re.search(patterns,password.lower()):
             return True
     return False

while True:
    print('Enter your password to see the truth')
    password = input()
    if len(password) > 5 and len(password) < 15 and any(c for c in password if not c.isalnum()) and any(c.isupper() for c in password) and not is_common_password(password):
        print('hasło zatwierdzone')
        print('real truth')
        print('Kocham siebie  \n Jestem dzieckiem bozym \n wszystko jest i bedzie okej \n Oddałem się Panu Bogu \n mogę wszystko w Chrystusie \n z nim kocham samego siebie \n w Chrystusie nie mam kompleksów \n Let the lion roar \n Mimo popelniania błedów Jezus i tak kocha mnie tak samo mocno')
        break
    elif len(password) <= 5:
        print(f'Trochę króciutkie.Daj cos co ma wiecej liter niz {password}')
    elif len(password) >= 15:
        print(f'Troche za dłuuugie.Poza tym twoje hasło {password} spróbuj ponownie')
    elif is_common_password(password):
        print(f'Twoje hasło nalezy do często używanych hasło "{password}"nie jest dobrym zabezpieczeniem')
    elif not any(c.isupper() for c in password):
        print('Dodaj wielka litere')
    elif not any(c for c in password if not c.isalnum()):
        print('Dodaj jeszcze znak specjalny i bedzie dobrze.')
    elif password_strenght(password) <= 10:
        print(f'Hasło {password} jest za słabe,spróbuj ponownie')




