import matplotlib.pyplot as plt
import sqlite3


def draw_bar_chart(data):
    plt.figure(figsize=(9, 3))
    regions = {
        "Витебская": 0,
        "Минская": 0,
        "Гомельская": 0,
        "Брестская": 0,
        "Гродненская": 0,
        "Могилевская": 0
    }

    for i in data:
        regions[i[2]] += 1

    input_data = [[], []]
    for i in regions:
        input_data[0].append(i)
        input_data[1].append(regions[i])

    plt.barh(input_data[0], input_data[1])
    plt.savefig('output/bar_chart.png', dpi=500)
