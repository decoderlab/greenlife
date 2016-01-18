from sqlalchemy import *
from datetime import datetime, timedelta
from flask import Response,make_response

db = create_engine('sqlite:///database.db')

 # Try changing this to True and see what happens
metadata = MetaData(db)

class PostTable():
    def __init__(self):
        pass

    def posttable(self,tablename):
        table = Table(tablename, metadata,
                    Column('id', Integer, primary_key=True),
                    Column('description', String(10000)),
                    Column('date_time', DateTime,default=datetime.now(),nullable=false)
                      )
        #like = Table(tablename+'like'),metadata,
         #           Column('id',)

        return table


class User():
    def __init__(self):
        self.tablename = 'users'


    def usertable(self):
        table = Table(self.tablename, metadata,
                    Column('id', Integer, primary_key=True),
                    Column('uname', String(20), nullable=False),
                    Column('password', String(500), nullable=False),
                    Column('fname', String(20), nullable=False),
                    Column('lname', String(20), nullable=True),
                    Column('email', String(30), nullable=False),
                    Column('gender', String(10), nullable=False),
                    Column('address', String(1000), nullable=False),
                    Column('dob', String(30), nullable=False),
                      )

        return table

class Like():
    def __init__(self):
        self.tablename = 'like'


    def liketable(self):
        table = Table(self.tablename, metadata,
                    Column('id', Integer, primary_key=True),
                    Column('post_id', String(50), nullable=False),
                    Column('user_id', String(20), nullable=False),
                      )

        return table


    #def insert_post_table(self):


#
#table = Table('test', metadata, autoload=True)
#i = table.insert().execute({'description': 'i\'m here'})
#i.execute(name='Mary', age=30, password='secret')
         # {'title': '2nd post', 'description': 'hello again'})

