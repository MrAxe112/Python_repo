
sec = int(input("введите время в секундах "))

sec = sec % (24 * 60 * 60)

hour = sec // (60 * 60)
sec %= (60 * 60)

minute = sec // 60
sec %= 60

print(f"{hour:02d}:{minute:02d}:{sec:02d}")
