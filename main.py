import graph
import diagram
import bar_chart
import sqlite3
import os

if __name__ == '__main__':
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    data = cursor.fetchall()
    if not os.path.exists('output'):
        os.mkdir('output')
    graph.draw_graph(data)
    diagram.draw_diagram(data)
    bar_chart.draw_bar_chart(data)