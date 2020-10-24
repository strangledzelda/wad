# создадим класс "Книга" с полями:
# ID книги, название, автор, жанр, кол-во страниц, год первого издания, ID магазина
class Book:
    def __init__(self, id, title, author, genre, pages, year, shop_id):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.year = year
        self.shop_id = shop_id


# создадим класс "Книжный магазин" с полями: ID магазина, название, адрес
class Shop:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address


# создадим класс для реализации связи М-М
class BookShop:
    def __init__(self, shop_id, book_id):
        self.shop_id = shop_id
        self.book_id = book_id


# данные по книгам
books = [
    Book(1, "Грозовой перевал", "Эмили Бронте", "готический роман", 384, 1847, 3),
    Book(2, "Щегол", "Донна Тартт", "роман", 832, 2013, 1),
    Book(3, "Большие надежды", "Чарльз Диккенс", "роман", 544, 1861, 2),
    Book(4, "Мы", "Евгений Замятин", "роман-антиутопия", 224, 1920, 2),
    Book(5, "Дракула", "Брэм Стокер", "готический роман", 412, 1897, 5),
    Book(6, "Рассказ служанки", "Маргарет Этвуд", "роман-антиутопия", 311, 1985, 1),
    Book(7, "Дети капитана Гранта", "Жюль Верн", "приключенческий роман", 558, 1868, 4)
]

# данные по книжным магазинам
shops = [
    Shop(1, "Читай-город", "Москва, пр-т Мира, 182/2"),
    Shop(2, "Москва", "Москва, ул. Тверская, 8"),
    Shop(4, "Республика", "Москва, ул. Большая Ордынка, 21с2"),
    Shop(3, "Читай-город", "Москва, ул. Снежная, 27"),
    Shop(5, "Молодая Гвардия", "Москва, ул. Сущёвская, 19с5"),
]

bookshops = [
    BookShop(1, 2),
    BookShop(2, 3),
    BookShop(2, 4),
    BookShop(3, 1),
    BookShop(5, 5),
    BookShop(1, 6),
    BookShop(4, 7)
]

one_to_many_list = list((book, shop)
                        for book in books
                        for shop in shops
                        if (book.shop_id == shop.id))

many_to_many_list = list((shop.name, book.id)
                         for shop in shops
                         for book in books
                         for bk, sh in list((item.book_id, item.shop_id) for item in bookshops)
                         if shop.id == sh and book.id == bk)


# Задание 1: Вывести адреса всех книжных с наличием книги,
# в названии жанра которых есть "антиутопия"
print("Задание 1")
for i in one_to_many_list:
    if "антиутопия" in i[0].genre:
        print(i[1].address)

# Задание 2: Вывести среднее количество страниц указанных книг в каждом магазине
print("\nЗадание 2")
pageAvgList = list()
for s in shops:
    bookList = list(filter(lambda x: x[0].shop_id == s.id, one_to_many_list))
    pageAvg = 0
    for item in bookList:
        book = item[0]
        pageAvg += book.pages
    pageAvg = round(pageAvg/len(bookList), 2)
    pageAvgList.append((s.name, pageAvg))
for item in sorted(pageAvgList, key=lambda x: x[0]):
    print("Среднее число страниц в магазине",item[0], "составляет", item[1])



# Задание 3: Вывести названия всех книжных магазинов,
# в которых продаются книги, чьё первое издание пришлось на 19 век
print("\nЗадание 3")
for book in books:
    if book.year < 1800 or book.year > 1899:
        continue
    shopList = list(filter(lambda x: book.id == x[1], many_to_many_list))
    for item in shopList:
        print(item[0])