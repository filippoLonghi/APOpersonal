class Student:

    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def get_name(self) -> str:
        return self.name

    def get_surname(self) ->str:
        return self.surname