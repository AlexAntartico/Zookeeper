group_1 = abs(int(input()))
group_2 = abs(int(input()))
group_3 = abs(int(input()))

group1_chairs = (group_1 // 2) + ((group_1 % 2) > 0)
group2_chairs = (group_2 // 2) + ((group_2 % 2) > 0)
group3_chairs = (group_3 // 2) + ((group_3 % 2) > 0)

group1_chairs //= 2 + %= 2
print((group1_chairs + group2_chairs + group3_chairs))