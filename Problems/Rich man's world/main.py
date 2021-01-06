limit = 700_000
interest_rate = .071
initial_deposit = float(input())
years = 0

while initial_deposit < limit:
    initial_deposit += (initial_deposit * interest_rate)
    years += 1
print(years)
