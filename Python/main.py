import pyodbc
import random
import string
import datetime

def main():
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\MSSQLSERVER01;'
                      'Database=Teste2;'
                      'Trusted_Connection=yes;')

    cursor = conn.cursor()
    

    def random_char(number_of_letters):
       return ''.join(random.choice(string.ascii_letters) for x in range(number_of_letters))

    def random_date(start=None, end=None):
        start_date = datetime.date(2003, 1, 1)
        end_date = datetime.date(2022, 2, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return random_date

    def insert_users(cursor=cursor, number_of_usuers=100, data='today'):
        for user in range(number_of_usuers):
            CPF=random.randint(1,99999999)
            NAME=random_char(5)
            USUARIO=random_char(8)
            DATANASC=random_date()
            if data is not 'today':
                DATAREGISTRO=data
            else :
                DATAREGISTRO=random_date()
            EMAIL=random_char(6)+'@'+random_char(4)+'.com'
            SENHA=random_char(10)
            cursor.execute("INSERT INTO dbo.Usuarios (CPF, Nome, Usuario, DataNasc, DataRegistro, Email, Senha) VALUES ({cpf},'{Nome}','{Usuario}','{DataNasc}','{DataRegistro}','{Email}','{Senha}')".format(cpf=CPF, Nome=NAME, Usuario=USUARIO, DataNasc=DATANASC, DataRegistro=DATAREGISTRO, Email=EMAIL, Senha=SENHA))
            cursor.commit()
        return
    insert_users()

    cursor.execute('SELECT * FROM dbo.Usuarios')
 
    for i in cursor:
        print(i)

main()

