try:
    count = 0
    text = input("Введите строку:")
    result = ""
    for item in text:
        if item not in result:
            result += item
    print(f"{result}")
except ValueError as e:
    print("Произошла ошибка")