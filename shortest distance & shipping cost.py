nodes = ('Boston', 'New York', 'Wash DC', 'Chicago', 'Miami', 'Minneapolis', 'Dallas', 'Denver', 'Las Vegas', 'Los Angeles', 'San Francisco', 'Seattle')
distances = {'Boston': {'New York': 338, 'Chicago': 1613, 'Wash DC': 725},
             'New York': {'Boston': 338, 'Wash DC': 383, 'Miami': 2145},
             'Wash DC': {'Boston': 725, 'New York': 383, 'Chicago': 1145, 'Miami': 1709, 'Dallas': 2113},
             'Chicago': {'Boston': 1613, 'Wash DC': 1145, 'Minneapolis': 661},
             'Miami': {'New York': 2145, 'Wash DC': 1709, 'Dallas': 2161},
             'Minneapolis': {'Chicago': 661, 'Dallas': 1532, 'Denver': 1483, 'Seattle': 2661},
             'Dallas': {'Wash DC': 2113, 'Miami': 2161, 'Minneapolis': 1532, 'Denver': 1258, 'Las Vegas': 1983},
             'Denver': {'Minneapolis': 1483, 'Dallas': 1258, 'Las Vegas': 1225, 'Seattle': 2161},
             'Las Vegas': {'Dallas': 1983, 'Denver': 1225, 'Los Angeles': 435, 'San Francisco': 919},
             'Los Angeles': {'Las Vegas': 435, 'San Francisco': 629},
             'San Francisco': {'Las Vegas': 919, 'Los Angeles': 629, 'Seattle': 1306},
             'Seattle': {'Minneapolis': 2661, 'Denver': 2161, 'San Francisco': 1306},
             }
# Compute shortest distance
start = input('Distance Start Point: ')
unvisited = {node: None for node in nodes}
visited = {}
current = start
current_distance = 0
unvisited[current] = current_distance

while True:
    for neighbor, distance in distances[current].items():
        if neighbor not in unvisited:
            continue
        new_distance = current_distance + distance
        if unvisited[neighbor] is None or unvisited[neighbor] > new_distance:
            unvisited[neighbor] = new_distance
    visited[current] = current_distance
    del unvisited[current]
    if not unvisited:
        break
    candidates = [node for node in unvisited.items() if node[1]]
    current, current_distance = sorted(candidates, key = lambda x: x[1])[0]

print('Shortest Distance: ' + str(visited))

# Compute lowest cost
start_pay = input('Cost Start Point: ')
unpaid = {node: None for node in nodes}
paid = {}
current_pay = start_pay
current_cost = 0
unpaid[current_pay] = current_cost

while True:
    for neighbor, distance in distances[current_pay].items():
        if neighbor not in unpaid:
            continue
        if distance <= 500:
            cost = 0.005 * distance
        elif 500 < distance <= 1000:
            cost = 0.004 * (distance-500) + 0.005*500
        elif 1000 < distance <= 2000:
            cost = 0.003 * (distance-1000) + 0.004*500 + 0.005*500
        elif distance > 2000:
            cost = 0.002 * (distance-2000) + 0.003*1000 + 0.004*500 + 0.005*500
        new_cost = current_cost + cost
        if unpaid[neighbor] is None or unpaid[neighbor] > new_cost:
            unpaid[neighbor] = new_cost
    paid[current_pay] = current_cost
    del unpaid[current_pay]
    if not unpaid:
        break
    candidates = [node for node in unpaid.items() if node[1]]
    current_pay, current_cost = sorted(candidates, key = lambda x: x[1])[0]

print('Least Cost: ' + str(paid))