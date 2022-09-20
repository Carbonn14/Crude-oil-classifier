API=float(input(f'Enter the API of crude: '))
S=float(input(f'Enter sulfur content in percent: '))
if API > 31.5:
    print(f'Light crude oil')
elif 31.5 > API > 22.3:
    print(f'Medium crude oil')
elif 22.3 > API > 10.0:
    print(f'Heavy crude oil')
elif API < 10.0:
    print(f'Extra-heavy crude oil')
else:
    print(f'Invalid data')
if S > 1.0:
    print(f'Sour crude')
elif 0 <= S <= 1.0:
    print(f'Sweet crude')
else:
    print(f'Wrong input')


