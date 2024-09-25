try:
    count = 0
    text = input("Введите строку:")
    pattern = ".,;:!?"
    for item in text:
        if item in pattern:
            count += 1
    print(f"Введено {count} знаков пунктуации")
except ValueError as e:
    print("Произошла ошибка")