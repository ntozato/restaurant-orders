import csv
from collections import Counter


def read_file(path):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        data = list(reader)
    return data


# https://pt.stackoverflow.com/questions/216970/como-pegar-as-10-palavras-mais-frequentes-de-em-array/216976
def most_requested(data, client):
    info = {}

    for item in data:
        if item[0] not in info:
            info[item[0]] = [item[1]]
        else:
            info[item[0]].append(item[1])

    result = Counter(info[client])
    return result.most_common(1)[0][0]


def how_many_times_requested(data, client, food):
    count = 0

    for item in data:
        if item[0] == client and item[1] == food:
            count += 1

    return count


def meals_never_requested(data, client):
    all_meals = set()
    client_requests = set()

    for item in data:
        if item[1] not in all_meals:
            all_meals.add(item[1])
        if item[0] == client:
            client_requests.add(item[1])

    return all_meals.difference(client_requests)


def days_off(data, client):
    all_days = set()
    client_request_days = set()

    for item in data:
        if item[2] not in all_days:
            all_days.add(item[2])
        if item[0] == client:
            client_request_days.add(item[2])

    return all_days.difference(client_request_days)


def save_in_mkt_file(data):

    with open('data/mkt_campaign.txt', 'w') as file:
        for row in data:
            file.write('{}\n'.format(row))


def analyze_log(path_to_file):
    data = read_file(path_to_file)
    maria_most_requested = most_requested(data, 'maria')
    arnaldo_times = how_many_times_requested(data, 'arnaldo', 'hamburguer')
    joao_never_requested = meals_never_requested(data, 'joao')
    joao_days_off = days_off(data, 'joao')

    result = [
        maria_most_requested,
        arnaldo_times,
        joao_never_requested,
        joao_days_off
    ]

    save_in_mkt_file(result)


# data = read_file('data/orders_1.csv')
# print(most_requested(data, 'maria'))
# print(how_many_times_requested(data, 'arnaldo', 'hamburguer'))
# print(meals_never_requested(data, 'joao'))
# print(days_off(data, 'joao'))
# print(analyze_log('data/orders_1.csv'))
