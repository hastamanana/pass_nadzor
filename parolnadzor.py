errors = []
pswd = input()
import string

def down_in_pswd(s: str):
    return '_' in s

def eng_letters(s: str):
    for i in s:
        if i.isalpha():
            return True
    return False

def num_in_s(s: str):
    for i in s:
        if i.isdigit():
            return True
    return False


def check_not_zero_str(s: str):
    if len(s) > 0:
        return True
    else:
        raise 'Пустая строка'


def check_title_pswd(s: str):
    if s[0].isupper():
        return True
    else:
        errors.append('Пароль должен начинаться с заглавной буквы.')
        return False


def last_el(s: str):
    if s[-1].isalnum():
        return True
    else:
        errors.append('Пароль должен заканчиваться только латинской буквой или цифрой')
        return False


def len_str(s):
    if 12 < len(s) < 32:
        return True
    else:
        errors.append('Минимальная длина пароля — 12 символов, максимальная — 32 символа')
        return False

def telo_pswd(s):
    return all([down_in_pswd(pswd), eng_letters(pswd), num_in_s(pswd)]) 
flag = False
if telo_pswd == True:
    flag = True
else:
    errors.append("Пароль должен состоять только из латинских букв, цифр и символа нижнего подчёркивания ('_')")


if all([check_not_zero_str(pswd), check_title_pswd(pswd), telo_pswd(pswd), last_el(pswd), len_str(pswd)]):
    print("Пароль принят!")
    with open('valid_passwords.txt', 'a') as f:
        f.write(pswd + '\n')
else:
    print(f"Пароль не соответствует требованиям!\n\n{'\n'.join(errors)}")

