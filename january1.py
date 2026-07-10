year = int(input("Enter the year : "))

previous_year = year - 1

total_normal_days = previous_year * 365

total_leap_days = previous_year // 4 - previous_year // 100 + previous_year // 400

total_days = total_normal_days + total_leap_days

day = total_days % 7

result = f"Day on 1 January {year} : "

match day:
    case 0:
        result += "Monday"
    case 1:
        result += "Tuesday"
    case 2:
        result += "Wednesday"
    case 3:
        result += "Thursday"
    case 4:
        result += "Friday"
    case 5:
        result += "Saturday"
    case 6:
        result += "Sunday"

print(result)
