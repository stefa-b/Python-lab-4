import json
import argparse

# Функция для ввода данных о маршрутах
def add_route(routes, start, end, number):
    route = {
        "start": start,
        "end": end,
        "number": number
    }
    routes.append(route)
    return routes

# Функция для вывода информации о маршруте по номеру
def find_route(routes, number):
    found = False
    for route in routes:
        if route["number"] == number:
            print("Начальный пункт маршрута:", route["start"])
            print("Конечный пункт маршрута:", route["end"])
            found = True
            break
    if not found:
        print("Маршрут с таким номером не найден.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Управление маршрутами')
    parser.add_argument('--add', action='store_true', help='Добавить новый маршрут')
    parser.add_argument('--number', type=str, help='Номер маршрута для поиска')

    args = parser.parse_args()

    try:
        with open("idz.json", "r") as file:
            routes = json.load(file)
    except FileNotFoundError:
        routes = []

    if args.add:
        start = input("Введите начальный пункт маршрута: ")
        end = input("Введите конечный пункт маршрута: ")
        number = input("Введите номер маршрута: ")
        routes = add_route(routes, start, end, number)

    if args.number:
        find_route(routes, args.number)

    # Сохранение данных в файл JSON после ввода информации
    with open("idz.json", "w") as file:
        json.dump(routes, file)