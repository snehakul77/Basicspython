
Birthday = {'Sneha': '10/02/1992',
        'Meera': '01/12/1960',
        'Anagha': '07/18/1992',
        'Tejas': '11/29/1989',
        'Vaishnavi': '03/12/1993'}

print('Welcome to BirthdayCalendar. We know the birthdays of')
for name in Birthday:
    print(name)

print('Who\'s birthday you want to know?')
name = input()

if name in Birthday:
    print('{}\'s birthday is {}'.format(name, Birthday[name]))
else:
    print('Sadly, we don\'t have {}\'s birthday'.format(name))