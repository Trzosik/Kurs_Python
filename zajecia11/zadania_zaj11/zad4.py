# 6▹ Utwórz klasę Pracownik.
#
#     Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
#
#     Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia.
#     Pracownik powinen odprowadzać podatek o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
#
#     Pracownik powinien mieć pole typu boolowskiego zawierające status studenta. Jeśli pracownik jest studentem jego składka zdrowotna wynosi 0%.
#
#     Wszyscy pracownicy mają wspólną nazwę firmy. Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy. Np.
#
#     Adam Kowalski Love Python Company
#
#     email -> smkwlsk@lovepythoncompany.com

class Worker:
    def __init__(self, position, salary, name, surname, experience, rise, tax, health, student_status, company, mail):
        self.position = position
        self.salary = salary
        self.name = name
        self.surname = surname
        self.experience = experience
        self.rise = rise
        self.tax = tax
        self.health = health
        self.student_status = student_status
        self.company = company
        self.mail = mail

    def yearly_