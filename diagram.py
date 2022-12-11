import matplotlib.pyplot as plt
import sqlite3


def draw_diagram(data):
    fig = plt.figure()
    plt.title("Соотношение взрослой и детской аудитории")
    age_groups = [0, 0]
    for i in data:
        if int(i[3]) < 18:
            age_groups[0] += 1
        else:
            age_groups[1] += 1

    plt.pie(age_groups, labels=['Несовершеннолетние', 'Совершеннолетние'], autopct='%.2f')
    plt.savefig('output/diagram.png', dpi=500)
