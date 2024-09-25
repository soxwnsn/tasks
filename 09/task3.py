try:
    s = input("Введите строку:").replace('','')
    if s.isalnum():
        print(len(s))
    else:
        print('NO')
except ValueError as e:
    print("Некорректный ввод")