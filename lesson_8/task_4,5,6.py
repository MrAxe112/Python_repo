class QuantError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    reg_num = 0

    def __init__(self, company):
        self.company = company
        self.storage = []

    def arrival(self, equip, quantity):
        try:
            if str(quantity).isdigit():
                Warehouse.reg_num += 1
                location = "warehouse"
                creator = {"Inventory number": Warehouse.reg_num,
                           "Amount": quantity,
                           "Location": location,
                           **equip.get_dict()
                           }
                self.storage.append(creator)
            else:
                raise QuantError(f"`QuantError`: Введенное значение `{quantity}` не может быть принята как количество.")
        except QuantError as err:
            print(err)

    def change_location(self, req_num, new_location):
        self.storage[req_num - 1]['Location'] = new_location

    def __str__(self):
        return f"На складе организации {self.company} находятся следующие позиции товаров: \n{self.storage}"


class OfficeEquipment:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def get_dict(self):
        return self.__dict__


class Printer(OfficeEquipment):
    def __init__(self, printer_name, printing_media_type):
        self.printer_name = printer_name
        self.printer_type = printing_media_type

    def __str__(self):
        return self.name, self.printer_type


class Xerox(OfficeEquipment):
    def __init__(self, xerox_name, colour):
        self.xerox_name = xerox_name
        self.colour = colour

    def __str__(self):
        return self.name, self.colour


class Scanner(OfficeEquipment):
    def __init__(self, scanner_name, resolution):
        self.scanner_name = scanner_name
        self.resolution = resolution

    def __str__(self):
        return self.name, self.resolution


warehouse = Warehouse("ИП Петров")

p1 = Printer("HP 2551", "Laser")
x1 = Xerox("Xerox", "Monochrome")
s1 = Scanner("Dell", "DPI 1200")

warehouse.arrival(p1, "o")
warehouse.arrival(x1, 1)
warehouse.arrival(s1, 2)

warehouse.change_location(1, "office")
warehouse.change_location(2, "garage")
print(warehouse)
