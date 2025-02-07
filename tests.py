from parolnadzor import main

test_case: tuple[str, ...] = (
    "Абвгдекуйерэ",  # False
    "Abcd_4325_fdg124",  # True
    "",  # False
    "abcd_4325_fdg124",  # False
    "Abcd_4325_fdg12_",  # False
)

for item in test_case:
    main(item)
