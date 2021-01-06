duration_days = abs(int(input()))
food_cost = abs(int(input()))
flight = abs(int(input()))
hotel_per_night = abs(int(input()))
food_cost *= duration_days
flight *= 2
hotel_per_night *= (duration_days - 1)
print(food_cost + flight + hotel_per_night)