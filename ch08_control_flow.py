# Control flow: Practical Task 1
def transport_hub(schedule, days):
    capacity = 0
    max_per_day = []
    for day in range(1, days + 1):
        vehicles = []
        for vehicle in schedule:
            per, cap = vehicle.split(' ')
            if day % int(per) == 0:
                vehicles.append(int(cap))
        producer, consumer = 0, 0
        for vehicle in vehicles:
            if vehicle > 0:
                producer += vehicle
            else:
                consumer -= vehicle
        capacity += producer
        max_per_day.append(capacity)
        capacity -= consumer if capacity > consumer else capacity
    return max(max_per_day)


print(transport_hub(['2 -2', '3 3'], 7))
