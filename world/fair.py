class Person:
    def __init__(self) -> None:
        print("Person created...")
        self.name: str = None
        self.type_person: str = None
        self.type_document: str = None
        self.phone: str = None
        self.mail: str = None
        self.address: str = None


class Entrepreneur(Person):
    def __init__(self) -> None:
        super().__init__()
        print("Entrepreneur created...")
    
    def __str__(self) -> str:
        return f"{self.name}, {self.type_person}, {self.type_document}, {self.phone}, {self.mail}, {self.address}"


class Organizer(Person):
    def __init__(self, business_name: str) -> None:
        super().__init__()
        print("Organizer created...")
        self.business_name = business_name

def test(nombre, pito, tipo, celu, mail, dir):
    entrepreneur_one = Entrepreneur()
    entrepreneur_one.name = nombre
    entrepreneur_one.type_person = pito
    entrepreneur_one.type_document = tipo
    entrepreneur_one.phone = celu
    entrepreneur_one.mail = mail
    entrepreneur_one.address = dir
    print(entrepreneur_one)

test("Luis", "Pi","CE", "ra", "pic", "lol")