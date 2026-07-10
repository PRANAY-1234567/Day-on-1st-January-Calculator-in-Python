# Day on 1st January Calculator in Python

## 📌 Overview

This project calculates the **day of the week for 1st January** of any given year.
The program uses leap year calculations and the total number of elapsed days from Year 1 to determine the weekday for **January 1**. It then maps the calculated value to the corresponding day using Python's `match-case` statement.

This project is useful for learning date calculations, leap year logic, arithmetic operations, and pattern matching in Python.

---

## 🚀 Features

* Accepts any valid year as input
* Calculates the weekday of **1st January**
* Handles leap years correctly
* Uses Python's `match-case` statement
* Beginner-friendly implementation

---

## 🛠️ Technologies Used

* Python 3.10+

---

## 📂 Project Structure

```text id="qumxzv"
├── january_first_day.py
└── README.md
```

---

## 💻 Source Code

```python id="spnyn7"
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
```

---

## ▶️ How to Run

### Clone the Repository

```bash id="c2o4h7"
git clone https://github.com/your-username/january-first-day-calculator.git
cd january-first-day-calculator
```

### Run the Program

```bash id="2z8v2j"
python january_first_day.py
```

---

## 📋 Sample Output

### Example 1

```text id="6fgwyq"
Enter the year : 2024
Day on 1 January 2024 : Monday
```

### Example 2

```text id="cq1jz7"
Enter the year : 2025
Day on 1 January 2025 : Wednesday
```

### Example 3

```text id="8pim2l"
Enter the year : 2000
Day on 1 January 2000 : Saturday
```

---

## 🧠 Concepts Covered

* User Input
* Arithmetic Operations
* Leap Year Calculation
* Integer Division (`//`)
* Modulus Operator (`%`)
* Pattern Matching (`match-case`)
* Date and Calendar Logic

---

## 🔍 How It Works

1. Read the input year.
2. Calculate the previous year (`year - 1`).
3. Compute the total number of normal days.
4. Calculate the number of leap days using the Gregorian leap year rules.
5. Add both values to obtain the total elapsed days.
6. Find the remainder when divided by 7.
7. Map the remainder to the corresponding weekday using `match-case`.
8. Display the day for **1st January** of the given year.

---

## 🌟 Leap Year Rules

A year is considered a leap year if:

* It is divisible by **4**, **and**
* It is **not divisible by 100**, **unless**
* It is also divisible by **400**.

Examples:

* 2024 ✅ Leap Year
* 1900 ❌ Not a Leap Year
* 2000 ✅ Leap Year

---

## ⏱️ Complexity Analysis

| Operation        | Complexity |
| ---------------- | ---------- |
| Time Complexity  | **O(1)**   |
| Space Complexity | **O(1)**   |

The program performs a fixed number of calculations regardless of the input year.

---

## 🔮 Future Improvements

* Calculate the weekday for any date (day, month, and year)
* Display a full calendar for a given month
* Add input validation for invalid years
* Build a graphical calendar application using Tkinter
* Compare results with Python's `datetime` module

---

## 🎯 Learning Outcomes

After completing this project, you will understand:

* How calendar calculations work
* Leap year determination in the Gregorian calendar
* Using arithmetic to solve date-related problems
* Python's `match-case` statement
* Applying mathematical logic in programming

---

## 👨‍💻 Author

**Pranay Jadhao**

Electronics & Telecommunication Engineer
Aspiring Software Engineer | Python | Java | SQL | Data Analytics

---

## 📄 License

This project is open-source and available for educational and learning purposes.

<img width="869" height="766" alt="image" src="https://github.com/user-attachments/assets/197a3d8b-9701-4000-827f-e24ead409030" />
