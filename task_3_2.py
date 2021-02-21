guests = input("Введите число гостей! - ")
if guests >= 50:
    print("Празднуем в ресторане!")
elif 20<guests<50:
    print("Празднуем в кафе!")
elif guests<20:
    print("Людей маловато, можно и дома отметить!")