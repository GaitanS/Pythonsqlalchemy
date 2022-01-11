"""
SQL Alchemy este un ORM - OBJECT RELATIONAL MAPPING - o reprezentare a obiecteleor in python sub 0 alta forma
- nu foloseste sintaxa de SQL ci doar de Python
- clasa reprezinta un tabel
- o instanta reprezinta un rand
- atributele instantelor reprezinta coloanele
SQL Alchemy sessionmaker() ce reprezinta comunicarea si manipularea bazei de date, reprezentata de un cursor
pip install sqlalchemy

Tabelele sunt reprezentare de clase, clasele pentru a putea fi luate in considerare trebuie sa mosteneasca declarative_base()
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Student

CONNECTION_STRING = 'mysql+pymysql://{user}:{password}@{host}/{db}'
eng = create_engine(CONNECTION_STRING.format(user='root', password='Frectie!234', host='localhost', db='students_db'))
# acest creat realizeaza o conexiune catre baza de date(students_db)

# creeaza tabelele in baza noastra de date
Base.metadata.create_all(eng)
Session = sessionmaker(bind=eng)  # ne da accesul la sesiune
s = Session()

# s.add_all(
#     [
#         Student(first_name='Gaitan', last_name='Silviu'),
#         Student(first_name='Gaitan', last_name='Mihai'),
#         Student(first_name='Horia', last_name='Cristina')
#     ]
# )
# s.commit()  # la fiecare modificare de db(insert/update/delete)

# SELECT * FROM students
all_students = s.query(Student).all()
for student in all_students:
    print(f'Full name: {student.first_name} {student.last_name}')

# SELECT COUNT(*) FROM students
count_students = s.query(Student).count()
print(f'Total:{count_students}')

# SELECT first_name,last_name FROM students;
all_students = s.query(Student.first_name, Student.last_name).all()
print(f'{all_students}')

# SELECT * FROM students WHERE id>= 2 AND first_name LIKE 'Iu';
results = s.query(Student).filter(Student.student_id >= 1, Student.first_name.like('Ga%')).all()
for result in results:
    print(f'{result}')
