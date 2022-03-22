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
        capacity += sum(filter(lambda veh: veh > 0, vehicles))
        max_per_day.append(capacity)
        consumer = -sum(filter(lambda veh: veh < 0, vehicles))
        capacity -= consumer if capacity > consumer else capacity
    return max(max_per_day)


print(transport_hub(['2 -2', '3 3'], 7))
