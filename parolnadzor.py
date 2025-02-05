import string

ru_elements = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
errors = []


def down_in_pswd(s: str):
    if '_' in s:
        return True
    else:
        errors.append('В пароле должен быть символ подчёркивания.')
        return False

def eng_letters(s: str):
    flag = True
    for i in s:
        if i not in ru_elements:
            continue
        else:
            errors.append('Пароль должен состоять только из латинских букв')
            flag = False
    return flag

def num_in_s(s: str):
    for i in s:
        if i.isdigit():
            return True
    errors.append('В пароле должна быть цифра')
    return False


def check_title_pswd(s: str):
    if s[0].isupper():
        return True
    else:
        errors.append('Пароль должен начинаться с заглавной буквы.')
        return False


def last_el(s: str):
    if s[-1] in string.ascii_letters + string.digits:
        return True
    else:
        errors.append('Пароль должен заканчиваться только латинской буквой или цифрой')
        return False


def len_str(s):
    if 12 <= len(s) <= 32:
        return True
    else:
        errors.append('Минимальная длина пароля — 12 символов, максимальная — 32 символа')
        return False

pswd = input()

if not pswd:
    print('Пароль обязательное поле')
elif all([check_title_pswd(pswd), down_in_pswd(pswd), eng_letters(pswd), num_in_s(pswd), last_el(pswd), len_str(pswd)]):
    print("Пароль принят!")
    with open('valid_passwords.txt', 'a') as f:
        f.write(pswd + '\n')
else:
    print(f"Пароль не соответствует требованиям!\n\n{'\n'.join(errors)}")

