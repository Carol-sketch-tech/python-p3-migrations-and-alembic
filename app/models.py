# we no longer includign the shebang because this file will not be executed as a script.
# the shebang tells the command line where to find the interpreter for the code in a file.
#  it is only necessary for code that want to execute from the command line wihtout the python keyword.
from datetime import datetime
from sqlalchemy import create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (CheckConstraint, UniqueConstraint, Column, DateTime, Integer, String)

engine= create_engine('sqlite:///migration_test.db')

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (
        UniqueConstraint(
            'email',
            name = 'unique_email'
        ),
        CheckConstraint(
            'grade BETWEEN 1 AND 12', 
            name = 'grade_between_1_and_12'
        )
    )

    id = Column(Integer(), primary_key= True)
    name = Column(String(), index= True)
    email = Column(String(55))
    grade = Column(Integer())
    birthhday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f'Student {self.id}:'\
        + f' {self.name}:'\
        +f'Grade {self.grade}'
    