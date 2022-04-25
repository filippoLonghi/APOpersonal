from typing import List


class University:

    # R1
    def __init__(self, name: str) -> None:
        self._matricola_studente = 10000
        self._codice_corso = 10
        self.name = name
        self.rector = ""
        self.students = {}       # {codice studente: ["Nome","Cognome"]}
        self.courses = {}          # {codice corso: ["titolo","maestro"]}
        self.attendees = {}       # {"codice_corso1": [codice_studenti], "codice_corso2": [codice_studenti]}
        self.study_plan = {} # {"codice_studente1": [codice_corsi], "codice_studente2": [codice_corsi]}


    def get_name(self) -> str:
        return self.name

    def set_rector(self, name: str, surname: str) -> None:
        self.rector = f'{name} {surname}'

    def get_rector(self) -> str:
        return self.rector

    # R2
    def add_student(self, name: str, surname: str) -> int:
        self.students[self._matricola_studente] = [name, surname] # = Studente(name, surname)
        self._matricola_studente += 1
        return self._matricola_studente - 1

    def get_student_info(self, student_id: int) -> str:
        return f'{student_id} {self.students[student_id][0]} {self.students[student_id][1]}' #self.studenti[student_id].get_name, etc.

    # R3
    def add_course(self, title: str, teacher: str) -> int:
        self.courses[self._codice_corso] = [title, teacher]
        self._codice_corso += 1
        return self._codice_corso - 1

    def get_course_info(self, course_id: int) -> str:
        return f'{course_id},{self.courses[course_id][0]},{self.courses[course_id][1]}'

    # R4
    def register_to_course(self, student_id: int, course_id: int) -> None:
        if course_id not in self.attendees:
            self.attendees[course_id] = []
            self.attendees[course_id].append(student_id)
        else:
            self.attendees[course_id].append(student_id) #ci appendo l'istanza studente
        if student_id not in self.study_plan:
            self.study_plan[student_id] = []
            self.study_plan[student_id].append(course_id)
        else:
            self.study_plan[student_id].append(course_id)

    def get_attendees(self, course_id: int) -> str:
        studenti = ""
        for i in range(len(self.attendees[course_id])):
            if i < len(self.attendees[course_id]) - 1:
                studente = str(self.attendees[course_id][i]) + " " + str(self.students[self.attendees[course_id][i]][0]) + " " + str(self.students[self.attendees[course_id][i]][1]) + "\n"
            else:
                studente = str(self.attendees[course_id][i]) + " " + str(self.students[self.attendees[course_id][i]][0]) + " " + str(self.students[self.attendees[course_id][i]][1])
            studenti += studente
        return studenti

    def get_study_plan(self, student_id: int) -> List[str]:
        corsi = []
        for i in range(len(self.study_plan[student_id])):
            corsi.append(str(self.study_plan[student_id][i])+","+str(self.courses[self.study_plan[student_id][i]][0])+","+str(self.courses[self.study_plan[student_id][i]][1]))
        return corsi