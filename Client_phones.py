
import psycopg2
from pprint import pprint


def clear_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        DROP TABLE Phone_number;
        DROP TABLE Client;
        """)

def create_db(conn): # создаем структуру БД
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Client(
            id SERIAL PRIMARY KEY,
            First_name VARCHAR(50) NOT NULL,
            Last_name VARCHAR(40) NOT NULL,
            Email VARCHAR(50) UNIQUE
        );
        """)

        cur.execute("""
                CREATE TABLE IF NOT EXISTS Phone_number(
                    id SERIAL PRIMARY KEY,
                    number VARCHAR(20)NOT NULL,
                    Client_Id INTEGER NOT NULL REFERENCES Client(id)
                );
                """)
        conn.commit()  # фиксируем в БД

def add_client(conn, first_name, last_name, email):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO Client(First_name, Last_name, Email) 
        VALUES(%s, %s, %s);
        """, (first_name, last_name, email))
    conn.commit()  # фиксируем в БД

def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO Phone_number(number, Client_Id) 
        VALUES(%s, %s);
        """, (phone, client_id))
    conn.commit()  # фиксируем в БД

def change_client_name(conn, client_id, first_name):
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE Client SET First_name=%s WHERE id=%s;
            """, (first_name, client_id))
        conn.commit()

def change_client_lastname(conn, client_id, last_name):
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE Client SET Last_name=%s WHERE id=%s;
            """, (last_name, client_id))
        conn.commit()

def change_client_email(conn, client_id, email):
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE Client SET Email=%s WHERE id=%s;
            """, (email, client_id))
        conn.commit()

def change_client(conn, client_id, first_name=None, last_name=None, email=None):
    if first_name:
        change_client_name(conn, client_id, first_name)
    if last_name:
        change_client_lastname(conn, client_id, last_name)
    if email:
        change_client_email(conn, client_id, email)



def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
            DELETE FROM Phone_number WHERE Client_Id=%s and Number = %s ;
            """, (client_id, phone))
        conn.commit()

def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""
            DELETE FROM Phone_number WHERE Client_Id=%s;
            """, (client_id, ))
        cur.execute("""
            DELETE FROM Client WHERE id=%s;
            """, (client_id, ))
        conn.commit()

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    base_query = 'SELECT c.id, First_name, Last_name, Email, number FROM Client c LEFT JOIN Phone_number p ON p.Client_Id = c.id WHERE '
    result = ''
    param_query =()

    if first_name == last_name == email == phone == None:
        add_query = 'c.id IS NOT %s;'
        param_query = (None,)
        result = f'{base_query} {add_query}'

    if first_name is not None :
        add_query = 'c.First_name = %s;'
        param_query = (first_name, )
        result = f'{base_query} {add_query}'

    if last_name is not None :
        add_query = 'c.Last_name = %s;'
        param_query = (last_name, )
        result = f'{base_query} {add_query}'

    if email is not None :
        add_query = 'c.Email = %s;'
        param_query = (email, )
        result = f'{base_query} {add_query}'

    if phone is not None :
        add_query = 'p.number = %s;'
        param_query = (phone, )
        result = f'{base_query} {add_query}'

    with conn.cursor() as cur:
        cur.execute(result, param_query)
        pprint(cur.fetchall())

if __name__ == '__main__':
    with psycopg2.connect(database="client_phones", user="postgres", password="zzzzzzzzzz") as conn:
        clear_db(conn)
        create_db(conn)
        add_client(conn, 'Иван', 'Иванов', 'Ivan@yandex.ru')
        add_client(conn,'Петр', 'Петров', 'Peter@yandex.ru')
        add_client(conn, 'Михаил', 'Михайлов', 'Miha@yandex.ru')
        add_phone(conn,1,'+790000000001')
        add_phone(conn, 1, '+790000000011')
        add_phone(conn, 2, '+790000000002')
        add_phone(conn, 2, '+790000000022')
        add_phone(conn, 2, '+790000000222')
        find_client(conn,'Иван')
        find_client(conn, 'Петр')
        find_client(conn, 'Михаил')
        change_client(conn,1, 'Иоан')
        print('Поменяли имя Ивану на Иоан')
        find_client(conn, 'Иоан')
        print('Ищем телефоны Петра')
        find_client(conn, 'Петр')
        print('Удаляем телефон Петра +790000000002')
        delete_phone(conn, 2,'+790000000002')
        print('Ищем телефоны Петра')
        find_client(conn, 'Петр')
        print ('Выводим всех клиентов')
        find_client(conn)
        print('Удаляем Петра из базы')
        delete_client(conn, 2)
        print('Выводим всех клиентов')
        find_client(conn)
    conn.close()