from operator import itemgetter

orders = int(input('Введите количество заказов: '))
pizza_orders = dict()

for index in range(orders):
    order = input(f'{index + 1}-й заказ: ').capitalize().split()
    order_name = order[1]
    if order[0] not in pizza_orders:
        pizza_orders[order[0]] = dict()
        pizza_orders[order[0]][order[1]] = int(order[2])
    elif order[0] in pizza_orders and order[1] in pizza_orders[order[0]]:
        pizza_orders[order[0]][order[1]] += int(order[2])
    elif order[0] in pizza_orders and order_name not in pizza_orders[order[0]]:
        pizza_orders[order[0]][order[1]] = int(order[2])


sorted_pizza_orders = dict(sorted(pizza_orders.items(), key= itemgetter(0)))

print('Список покупателей и их заказов: ', sorted_pizza_orders)

