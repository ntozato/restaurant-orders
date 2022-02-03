from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        info = {}

        for item in self.orders:
            if item[0] not in info:
                info[item[0]] = [item[1]]
            else:
                info[item[0]].append(item[1])

        result = Counter(info[costumer])
        return result.most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        all_meals = set()
        client_requests = set()

        for item in self.orders:
            if item[1] not in all_meals:
                all_meals.add(item[1])
            if item[0] == costumer:
                client_requests.add(item[1])

        return all_meals.difference(client_requests)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        client_request_days = set()

        for item in self.orders:
            if item[2] not in all_days:
                all_days.add(item[2])
            if item[0] == costumer:
                client_request_days.add(item[2])

        return all_days.difference(client_request_days)

    def get_busiest_day(self):
        days = []

        for item in self.orders:
            days.append(item[2])

        return Counter(days).most_common(1)[0][0]

    def get_least_busy_day(self):
        days = []

        for item in self.orders:
            days.append(item[2])

        return Counter(days).most_common()[-1][0]
