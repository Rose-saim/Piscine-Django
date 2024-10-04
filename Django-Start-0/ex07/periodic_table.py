# periodic_table.py
import sys

def create_periodic_table():
    with open('periodic_table.txt', 'r') as file:
        elements = file.readlines()

    with open('periodic_table.html', 'w') as html_file:
        html_file.write("<table>\n")
        for element in elements:
            name, number, symbol, weight = element.strip().split(',')
            html_file.write(f"<td style='border: 1px solid black;'>\n")
            html_file.write(f"<h4>{name}</h4>\n")
            html_file.write("<ul>\n")
            html_file.write(f"<li>No {number}</li>\n")
            html_file.write(f"<li>{symbol}</li>\n")
            html_file.write(f"<li>{weight}</li>\n")
            html_file.write("</ul>\n")
            html_file.write("</td>\n")
        html_file.write("</table>")

if __name__ == '__main__':
    create_periodic_table()
