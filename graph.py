import matplotlib.pyplot as plt
import sqlite3
import datetime


def draw_graph(data):
    current_year = datetime.datetime.now().year
    years = {}
    # динамическое создание словаря с годами. От условной даты открытия магазина (2016) до текущего года
    for i in range(2016, current_year + 1):
        years.update(
            {
                str(i): 0
            }
        )
    for i in data:
        years[str(i[4])] += 1
    input_data_structured = [[], []]
    for i in years:
        input_data_structured[0].append(int(i))
        input_data_structured[1].append(years[i])
    print(input_data_structured)
    figure = plt.figure()
    plt.title("Регистрация новых пользователей по годам")
    plt.ylabel('Количество новых клиентов')
    plt.xlabel('Год')
    plt.plot(
        input_data_structured[0][::-1],
        input_data_structured[1][::-1]
    )
    plt.savefig('output/graph.png', dpi=500)

