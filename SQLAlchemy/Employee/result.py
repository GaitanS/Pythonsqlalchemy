import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Departament, Bonus, Angajat

CONNECTION_STRING = 'mysql+pymysql://{user}:{password}@{host}/{db}'
eng = create_engine(CONNECTION_STRING.format(user='root', password='Frectie!234', host='localhost', db='employee_db'))
# acest creat realizeaza o conexiune catre baza de date(students_db)

# creeaza tabelele in baza noastra de date
Base.metadata.create_all(eng)
Session = sessionmaker(bind=eng)  # ne da accesul la sesiune
s = Session()

# s.add_all(
#     [
#         Departament(department_name='Marketing'),
#         Departament(department_name='Contabilitate'),
#         Departament(department_name='IT'),
#         Departament(department_name='Resurse Umane')
#
#     ]
# )
# s.commit()
# s.add_all(
#     [
#         Angajat(cnp='123456798', first_name='Silviu', last_name='Gaitan', data_angajare=datetime.date(2020, 4, 15),
#                 departament=1, salariu=4000, manager=True),
#         Angajat(cnp='123456798', first_name='Silvia', last_name='Gaitan', data_angajare=datetime.date(2020, 4, 11),
#                 departament=2, salariu=6000, manager=False),
#         Angajat(cnp='123456698', first_name='Silva', last_name='Gaitan', data_angajare=datetime.date(2020, 4, 12),
#                 departament=3, salariu=7000, manager=False),
#         Angajat(cnp='123456748', first_name='Sinia', last_name='Gaitan', data_angajare=datetime.date(2020, 4, 10),
#                 departament=3, salariu=6000, manager=True)
#
#     ]
# )
# s.commit()
# s.add_all(
#     [
#         Bonus(data_acordarii=datetime.date(2020, 4, 15), beneficiar=1, valoare=4000),
#         Bonus(data_acordarii=datetime.date(2020, 4, 14), beneficiar=2, valoare=4000),
#         Bonus(data_acordarii=datetime.date(2020, 4, 20), beneficiar=3, valoare=4000)
#
#     ]
# )
# s.commit()

result = s.query(Angajat).filter(Angajat.salariu).order_by(Angajat.salariu.desc()).first()
print(result)


def adauga_angajat_nou():
    cnp = input('CNP:')
    first_name = input('Numele:')
    last_name = input('Prenumele:')
    data_angajare = datetime.datetime.now().date()
    departament = input('Departament ID:')
    salariu = input('Salariu:')
    manager = bool(input('Manager? 1 =Yes or 0= No : '))
    s.add(
        Angajat(cnp=cnp, first_name=first_name, last_name=last_name, data_angajare=data_angajare,
                departament=departament, salariu=salariu, manager=manager)
    )
    s.commit()


def update():
    nume = str(input('Cauta un angajat dupa ID:'))
    x = s.query(Angajat).get(nume)
    print("Name: ", x.first_name, "Last:", x.last_name, 'Departament:', x.departament, 'Manager:', x.manager)
    dep = input('ID nou:')
    x.departament = dep
    s.commit()
    man = bool(input('Devine si manager? 1 = Da sau 0 = Nu:'))
    x.manager = man
    s.commit()
    print("Name: ", x.first_name, "Last:", x.last_name, 'Departament:', x.departament, 'Manager:', x.manager)


update()
