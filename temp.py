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
    

q = 'Ssgdfgsgsfsdfs1_'

telo_pswd = all([down_in_pswd(q), eng_letters(q), num_in_s(q)]) 

print(telo_pswd)
