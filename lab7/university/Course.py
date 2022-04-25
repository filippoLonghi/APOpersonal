class Course:

    def __init__(self, title: str, teacher: str) -> None:
        self.title = title
        self.teacher = teacher

    def get_title(self) -> str:
        return self.title

    def get_teacher(self) -> str:
        return self.teacher