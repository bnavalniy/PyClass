my_list = [2,
           4.05,
           'Super',
           5 + 6j,
           [1, 2, 3],
           ["tran", 'zi', 'stor'],
           (2.5, "Do", 'It', [1, 3, 5]),
           {2, 5, 6, 7, 8, 2},
           {'name': 'Dan', 'age': 18, 'isStudent': True},
           dict(name='Radik', age=16, isStudent=False)]
for ind, el in enumerate(my_list):
    if ind == 5:
        for i in el:
            print(i, end='')
    print(f" Element: '{el}', Index:'{ind}', Type {type(el)}")
