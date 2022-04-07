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
        if start is not None and end is not None:
            start=start.split(',')
            end=end.split(',')
            start_date=datetime.date(year=int(start[0]), day=int(start[1]), month=int(start[2]))
            end_date=datetime.date(year=int(end[0]),day=int(end[1]),month=int(end[2]))
        else:
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

    def insert_buys(cursor=cursor, number_of_buys=20, date_start=None, date_end=None):
        for buy in range(number_of_buys):
            if date_start != None and date_end != None:
                date=random_date(date_start, date_end)
            else:
                raise Exception
            CODPRODUTO=random.randint(1,20)
            QTD=random.randint(1,5)
            METODO=['Pay Pal', 'Pix', 'Boleto bancario', 'Cartao de credito']
            METODO_RANDOM=random.randint(0,3)
            ARRAY_OF_CPF=cursor.execute("SELECT CPF FROM dbo.Usuarios").fetchall()
            FINAL_ARRAY=["None"]
            for INDEX in range(len(ARRAY_OF_CPF)):
                NEW_ARRAY_OF_CPF=ARRAY_OF_CPF[INDEX]
                FINAL_ARRAY.append(NEW_ARRAY_OF_CPF[0])
            FINAL_ARRAY.remove("None")
            CPF_RANDOM=random.randint(0, len(FINAL_ARRAY))
            cursor.execute("INSERT INTO dbo.Compras (CodProduto, Qtd, CPF, Metodo, DataCompra) VALUES ({CodProduto},{Qtd},{CPF},'{Metodo}','{DataCompra}')".format(CodProduto=CODPRODUTO, Qtd=QTD, CPF=FINAL_ARRAY[CPF_RANDOM], Metodo=METODO[METODO_RANDOM], DataCompra=date))
            cursor.commit()
        return

    insert_buys(date_start='2021,1,01', date_end='2021,28,05')
    #insert_users()

    cursor.execute('SELECT * FROM dbo.Compras')
 
    for i in cursor:
        print(i)

main()

