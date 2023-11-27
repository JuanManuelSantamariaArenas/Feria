class Person:
    def __init__(self, name: str, type_person: str, type_document: str, 
                phone: str, mail: str, address: str) -> None:
        print("Person created...")
        self.name = None
        self.type_person = None
        self.type_document = None
        self.phone = None
        self.mail = None
        self.address = None


class Entrepreneur(Person):
    def __init__(self) -> None:
        super().__init__()
        print("Entrepreneur created...")



class Organizer(Person):
    def __init__(self, business_name: str) -> None:
        super().__init__()
        print("Organizer created...")
        self.business_name = business_name

entrepreneur_one = Entrepreneur()
print(entrepreneur_one.name)