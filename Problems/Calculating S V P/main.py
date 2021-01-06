a = abs(int(input()))
b = abs(int(input()))
c = abs(int(input()))

sum_length_edges = 4 * (a + b + c)
surface_area = 2 * ((a * b) + (b * c) + (a * c))
volume = a * b * c

print(f"{sum_length_edges}\n{surface_area}\n{volume}")