import random
from functools import reduce

names = [
    'Chad Jackson',
    'Julio Wilson',
    'Virginia Freeman',
    'Joanne Hanson',
    'Olga Gonzalez',
    'Cynthia Mitchell',
    'Sarah Webb',
    'Jennifer Garza',
    'Cheryl Wagner',
    'Alex Jones',
    'Maria Austin',
    'Wanda Burke',
    'Patricia Clark',
    'Patricia Young',
    'Charles Guzman',
    'Eva Brown',
    'Kathryn Wallace',
    'Shawn Harrison',
    'Travis Walsh',
    'Lorraine Daniels'
]


def print_list(lst):
    for e in lst:
        print(e)


students = [{"name": name,
             "age": random.randrange(18, 28),
             "grades": [random.randrange(0, 101), random.randrange(0, 101), random.randrange(0, 101),
                        random.randrange(0, 101)]} for name in names]


# --------------------------------------------------------------------------------------
#
# task 1.1
def filter_age(low_age, high_age, data):
    return list(filter(lambda x: low_age <= x["age"] <= high_age, data))


# task 1.1 example
# print_list(filter_age(20, 25, students))


# task 1.2
def average_grades(data):
    return list(map(lambda student: reduce(lambda s, a: s + a, student["grades"]) / len(student["grades"]), data))


def absolute_average(data):
    return reduce(lambda s, a: s + a, average_grades(data)) / len(data)


# task 1.2 example
# print(average_grades(students))
# print(absolute_average(students))


# task 1.3
def max_avg_students(data):
    return list(filter(
        lambda x: reduce(lambda s, a: s + a, x["grades"]) / len(x["grades"]) == reduce(lambda s, a: s if s > a else a,
                                                                                       average_grades(data)), data))


# task 1.3 example
# print_list(max_avg_students(students))
#
# --------------------------------------------------------------------------------------

users = [{"name": name,
          "expenses": [random.randrange(0, 401), random.randrange(0, 401), random.randrange(0, 401),
                       random.randrange(0, 401)]} for name in names]


# task 2
# критерии отбора - ? - пусть будет: каждый расход юзера > N
def calc_sum_expenses(data, n):
    return sum(
        list(map(lambda user: sum(user["expenses"]), list(filter(lambda user: min(user["expenses"]) > n, data)))))


# task 2 example
# print(calc_sum_expenses(users, 50))
# --------------------------------------------------------------------------------------
orders = [{
    "order_id": i,
    "customer_id": random.randrange(1, 6),
    "amount": random.randrange(1, 200)
} for i in range(1, 21)]


# --------------------------------------------------------------------------------------
# task 3.1
def filter_one_user(customer, data):
    return list(filter(lambda x: x["customer_id"] == customer, data))


# task 3.1 example
# print(filter_one_user(2, orders))


# task 3.2
def sum_one_user(customer, data):
    return sum([a["amount"] for a in filter_one_user(customer, data)])


# task 3.2 example
# print(sum_one_user(2, orders))

# task 3.3
def avg_price_one_user(customer, data):
    return sum_one_user(customer, data) / len(filter_one_user(customer, data))

# task 3.3 example
# print(avg_price_one_user(2, orders))
