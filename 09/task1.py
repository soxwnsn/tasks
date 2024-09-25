try:
    text = input("Введите строку:")
    result = ""
    for item in text:
        if item.isdigit() and result.count(item) == 0:
            result += item
            if result:
                print(f"{result}")
        else:
            print("NO")
except ValueError as e:
    print("Произошла ошибка")