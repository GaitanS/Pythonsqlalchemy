from sqlalchemy import Column, Integer, Text, BigInteger, Date, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Departament(Base):
    __tablename__ = 'departament'
    department_id = Column(Integer, primary_key=True, autoincrement=True)
    department_name = Column(Text, nullable=False)

    def __str__(self):
        return f'Departament {self.department_name}'


class Angajat(Base):
    __tablename__ = 'angajati'
    angajat_id = Column(Integer, primary_key=True, autoincrement=True)
    cnp = Column(BigInteger, nullable=False)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    data_angajare = Column(Date, nullable=False)
    departament = Column(Integer, ForeignKey(Departament.department_id), nullable=False)
    salariu = Column(BigInteger, nullable=False)
    manager = Column(Boolean)

    def __str__(self):
        return f'Angajatul:{self.first_name} {self.last_name}'


class Bonus(Base):
    __tablename__ = 'bonus'
    bonus_id = Column(Integer, primary_key=True, autoincrement=True)
    data_acordarii = Column(Date)
    beneficiar = Column(Integer,ForeignKey(Angajat.angajat_id), nullable=False)
    valoare = Column(Integer)

    def __str__(self):
        return f'Bonusul in valoare de {self.valoare} acordat angajatului {self.beneficiar}'
