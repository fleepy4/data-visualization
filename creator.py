import sqlite3
from faker import Faker
import random
from progress.bar import Bar
from datetime import datetime

start_time = datetime.now()
fake = Faker('ru_RU')
connect = sqlite3.connect('clients.db')
cursor = connect.cursor()
cursor.execute("""
CREATE TABLE clients (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name,
    region,
    age,
    register_year
);
""")
with Bar("Создания базы", max=1000000) as bar:
    for i in range(1000000):
        cursor.execute("INSERT INTO clients(full_name, region, age, register_year) VALUES(?,?,?,?)",
                       [
                           fake.name(),
                           random.choice(
                               [
                                   "Витебская",
                                   "Минская",
                                   "Гомельская",
                                   "Брестская",
                                   "Гродненская",
                                   "Могилевская"
                               ]
                           ),
                           random.randint(10, 65),
                           random.randint(2016, 2022)
                       ])
        bar.next()
connect.commit()
end_time = datetime.now() - start_time
print(f'База создана\nВремя исполнения скрипта: {str(end_time)}')