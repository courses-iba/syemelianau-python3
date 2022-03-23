# Control flow: Practical Task 1
def transport_hub(schedule, days):
    result = 0
    capacity = 0
    sch = [tuple(map(int, veh.split(' '))) for veh in schedule]
    for day in range(1, days + 1):
        vehicles = [cap for per, cap in sch if day % per == 0]
        producer = sum([vehicle for vehicle in vehicles if vehicle > 0])
        consumer = sum([vehicle for vehicle in vehicles if vehicle < 0])
        capacity += producer
        if result < capacity:
            result = capacity
        capacity = capacity + consumer if capacity > -consumer else 0
    return result


print(transport_hub(['2 -2', '3 3'], 7))
