def user_meta(name, lastname, birth_year, city, email, phone):
    return (f"{name.title()} {lastname.title()}, {birth_year} года рождения, проживает в городе {city.title()},"
            f"email:{email}, телефон {phone}.")


print(user_meta(name=input("Введите имя: "),
                lastname=input("Введите фамилию: "),
                birth_year=input("Введите год рождения: "),
                phone=input("Введите номер телефона: "),
                email=input("Введите адрес электронной почты: "),
                city=input("Введите город проживания: ")))
