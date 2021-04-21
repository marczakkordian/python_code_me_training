# Utwórz klasę Pracownik.
# Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
# Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia. Pracownik powinen odprowadzać podatek
# o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
# Pracownik powinien mieć pole typu boolowskiego zawierające status studenta. Jeśli pracownik jest studentem jego składka
# zdrowotna wynosi 0%.
# Wszyscy pracownicy mają wspólną nazwę firmy. Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy.
# Np. Adam Kowalski Love Python Company
# email -> smkwlsk@lovepythoncompany.com

class Employee:
    company_name = 'Love Python Company'

    def __init__(self, position, salary, name, last_name, seniority, tax, med_tax, student_status):
        self.position = position
        self.salary = salary
        self.name = name
        self.last_name = last_name
        self.seniority = seniority
        self.tax = tax
        self.med_tax = med_tax
        self.student_status = student_status
