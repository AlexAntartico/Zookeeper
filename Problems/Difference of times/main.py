first_hour = int(input())
first_minute = int(input())
first_second = int(input())
second_hour = int(input())
second_minute = int(input())
second_second = int(input())

hour_in_seconds = (second_hour - first_hour) * (60 ** 2)
minutes_in_seconds = (second_minute - first_minute) * 60
seconds = second_second - first_second

print(hour_in_seconds + minutes_in_seconds + seconds)