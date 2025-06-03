from datetime import date
import configparser
import sqlalchemy
from sqlalchemy import func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.sql.functions import char_length

from models import create_tables, Publisher, Shop, Book, Stock, Sale

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('settings.ini')
    server = config['Server']['server_name']
    port = config['Server']['port']
    db_name = config['DB']['db_name']
    user = config['User']['user_name']
    password = config['User']['password']

# Создаем DSN
DSN = "postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, server, port, db_name)  # Создаем DSN

# Создаем движок
engine = sqlalchemy.create_engine(DSN)

# Создаем таблицы
create_tables(engine) # Создаем таблицы

Session = sessionmaker(bind = engine) # Создаем класс, который умеет создавать сессии
session = Session()                 # Создаем экземпляр класса

# Заполняем авторов

writer1 = Publisher(name="Пушкин")
writer2 = Publisher(name="Тургенев")
session.add(writer1)
session.add(writer2)
session.commit()

# Заполняем Магазины

sh1 = Shop(name = "Книгомир")
sh2 = Shop(name = "Буквоед")
sh3 = Shop(name="Литрес")
session.add_all([sh1,sh2, sh3])

# Заполняем книги Пушкина

publ1 = session.query(Publisher).filter(Publisher.name=="Пушкин").first()
bk1 = Book(title = "Дубровский", id_publisher=publ1.id)
bk2 = Book(title = "Метель", id_publisher=publ1.id)
bk3 = Book(title = "Пиковая дама", id_publisher=publ1.id)
bk4 = Book(title = "Капитанская дочка", id_publisher=publ1.id)
session.add_all([bk1, bk2, bk3, bk4])

# Заполняем книги Тургенева
publ2 = session.query(Publisher).filter(Publisher.name == "Тургенев").first()
bk1 = Book(title = "Вешние воды", id_publisher=publ2.id)
bk2 = Book(title = "Ася", id_publisher=publ2.id)
bk3 = Book(title = "Первая любовь", id_publisher=publ2.id)
bk4 = Book(title = "Накануне", id_publisher=publ2.id)
bk5 = Book(title = "Отцы и дети", id_publisher=publ2.id)
session.add_all([bk1, bk2, bk3, bk4, bk5])

# Заполняем магазины книгами

shp1 = session.query(Shop).filter(Shop.name == "Книгомир").first()
shp2 = session.query(Shop).filter(Shop.name == "Буквоед").first()
shp3 = session.query(Shop).filter(Shop.name == "Литрес").first()

b1 = session.query(Book).filter(Book.title == "Вешние воды").first()
b2 = session.query(Book).filter(Book.title == "Ася").first()
b3 = session.query(Book).filter(Book.title == "Первая любовь").first()
b4 = session.query(Book).filter(Book.title == "Накануне").first()
b5 = session.query(Book).filter(Book.title == "Отцы и дети").first()

b6 = session.query(Book).filter(Book.title == "Дубровский").first()
b7 = session.query(Book).filter(Book.title == "Метель").first()
b8 = session.query(Book).filter(Book.title == "Пиковая дама").first()
b9 = session.query(Book).filter(Book.title == "Капитанская дочка").first()

st1 = Stock(id_book = b1.id, id_shop = shp1.id, count = 10)
st2 = Stock(id_book = b2.id, id_shop = shp2.id, count = 5)
st3 = Stock(id_book = b3.id, id_shop = shp3.id, count = 6)
st4 = Stock(id_book = b4.id, id_shop = shp1.id, count = 3)
st5 = Stock(id_book = b5.id, id_shop = shp2.id, count = 10)
st6 = Stock(id_book = b6.id, id_shop = shp3.id, count = 10)
st7 = Stock(id_book = b5.id, id_shop = shp3.id, count = 10)
st8 = Stock(id_book = b7.id, id_shop = shp1.id, count = 10)
st9 = Stock(id_book = b8.id, id_shop = shp2.id, count = 7)
st10 = Stock(id_book = b9.id, id_shop = shp3.id, count = 10)
st11 = Stock(id_book = b9.id, id_shop = shp1.id, count = 10)
st12 = Stock(id_book = b9.id, id_shop = shp2.id, count = 10)

session.add_all([st1, st2, st3, st4, st5, st6, st7,st8, st9, st10, st11, st12])

# Совершаем покупки книг

sl1 = Sale(price= 500.00, date_sale=date(2023,1,1), id_stock = 1, count = 1)
sl2 = Sale(price= 350.00, date_sale=date(2024,1,1), id_stock = 2, count = 1)
sl3 = Sale(price= 200.00, date_sale=date(2022,2,2), id_stock = 3, count = 1)
sl4 = Sale(price= 700.00, date_sale=date(2023,3,3), id_stock = 4, count = 1)
sl5 = Sale(price= 400.00, date_sale=date(2023,4,4), id_stock = 5, count = 1)
sl6 = Sale(price= 330.00, date_sale=date(2022,10,10), id_stock = 6, count = 1)
sl7 = Sale(price= 700.00, date_sale=date(2023,5,5), id_stock = 7, count = 1)
sl8 = Sale(price= 100.00, date_sale=date(2023,2,5), id_stock = 8, count = 1)
sl9 = Sale(price= 550.00, date_sale=date(2023,6,7), id_stock = 9, count = 1)
sl10 = Sale(price= 400.00, date_sale=date(2023,8,8), id_stock = 10, count = 1)
sl11 = Sale(price= 300.00, date_sale=date(2023,9,9), id_stock = 11, count = 1)
sl12 = Sale(price= 200.00, date_sale=date(2023,11,11), id_stock = 12, count = 1)
session.add_all([sl1, sl2, sl3, sl4,sl5, sl6, sl7, sl8, sl9, sl10, sl11,sl12])

# Запрос автора
publ = input("Введите имя автора: ")
p = session.query(Publisher).filter(Publisher.name == publ).first()

if p == None:
    print ('Нет такого автора')
else:
    q = session.query(
        Stock.id,
        Stock.id_shop,
        Book.title,
        Shop.name,
        Sale.price,
        Sale.date_sale,
        ).join(Book).join(Shop).join(Sale).filter(Book.id_publisher == p.id)
    len_publ = session.query(func.max(char_length(Book.title))).filter(Book.id_publisher == p.id).scalar()
    len_shop = session.query(func.max(char_length(Shop.name))).scalar()
    # Вывод покупок
    for s in q:
        print(f"{s.title:<{len_publ}} | {s.name:<{len_shop}} | {s.price} | {date.strftime(s.date_sale, '%d.%m.%Y')}")

#Сессии нужно закрывать после использования
session.close()