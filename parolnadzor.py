import string

ALLOWED_CHARS: str = string.ascii_letters + string.digits + '_'

errors: list[str] = []


def has_underscore(password: str) -> bool:
    if '_' not in password:
        errors.append('В пароле должен быть символ подчёркивания.')
        return False
    return True


def contains_only_allowed_chars(password: str) -> bool:
    for char in password:
        if char not in ALLOWED_CHARS:
            errors.append(
                'Пароль должен состоять только из '
                'латинских букв, цифр и символа подчеркивания.'
            )
            return False
    return True


def is_first_char_upper(password: str) -> bool:
    if password[0] not in string.ascii_uppercase:
        errors.append('Пароль должен начинаться с заглавной буквы.')
        return False
    return True


def is_last_char_alpha_num(password: str) -> bool:
    if password[-1] not in (string.ascii_letters + string.digits):
        errors.append(
            'Пароль должен заканчиваться '
            'только латинской буквой или цифрой.'
        )
        return False
    return True


def is_valid_length(password: str) -> bool:
    min_length: int = 12
    max_length: int = 32
    if not (min_length <= len(password) <= max_length):
        # if len(password) not in range(min_length, max_length + 1):
        errors.append(
            f'Минимальная длина пароля — {min_length} '
            f'символов, максимальная — {max_length} символа'
        )
        return False
    return True


def write_to_file(
        filename: str,
        password: str,
        encoding: str = 'UTF-8'
) -> None:
    with open(filename, mode='a', encoding=encoding) as file:
        file.write(password + '\n')


def main(user_password: str) -> None:
    if not user_password:
        print('[Предупреждение] Пароль обязательное поле')
        return None

    lazy_calls: list[bool] = [
        contains_only_allowed_chars(user_password),
        has_underscore(user_password),
        is_first_char_upper(user_password),
        is_last_char_alpha_num(user_password),
        is_valid_length(user_password)
    ]
    if all(lazy_calls):
        print('Пароль принят!')

        filename: str = 'valid_passwords.txt'
        try:
            write_to_file(filename, user_password)
        except FileNotFoundError:
            print(f'[Ошибка] Файл "{filename}" не найден')
        except (PermissionError, IOError) as err_msg:
            print(
                '[Ошибка] При записи файла '
                f'возникла ошибка: {err_msg}'
            )
        except Exception as err_msg:
            print(f'[Ошибка] Что-то пошло не так: {err_msg}')
        else:
            print('[Инфо] Ваш пароль успешно сохранён!')

        return None

    print('[Предупреждение] Пароль не соответствует требованиям!')
    print('\t- ', '\n\t- '.join(errors), sep='')


if __name__ == '__main__':
    main(input())
