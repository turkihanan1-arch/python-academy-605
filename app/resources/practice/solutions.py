# الحلول - لا تفتحه إلا بعد ما تحاول! كل حل مرقم مثل التمرين.

# 1
name = "Sara"
age = 20
print(f"{name} is {age} years old")

# 2
a = 17
b = 5
print(a / b)
print(a // b)
print(a % b)
print(a ** 2)

# 3
text = "python is fun"
print(text.upper())
print(text[0:6])
print(text[-3:])
print(len(text))

# 4
nums = [4, 9, 2, 7]
nums.append(10)
nums.sort()
print(nums)
print(max(nums))
print(sum(nums))

# 5
student = {"name": "Ali", "grade": 80}
student["grade"] = 95
student["city"] = "Tabuk"
for key, value in student.items():
    print(key, "->", value)

# 6
score = 73
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# 7
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# 8
total = 0
num = 1
while total <= 20:
    total += num
    num += 1
print(total, num - 1)   # num زاد بعد الإضافة، لذلك num - 1 هو آخر رقم أضفناه

# 9
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in grid:
    print(sum(row))

# 10
def is_even(n):
    return n % 2 == 0

print(is_even(4))
print(is_even(7))

# 11
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Sara"))
print(greet("Omar", greeting="Hi"))

# 12
def average(*nums):
    return sum(nums) / len(nums)

print(average(2, 4, 6))

# 13
def sum_to(n):
    if n == 0:
        return 0
    return n + sum_to(n - 1)

print(sum_to(4))

# 14
triple = lambda x: x * 3
print(triple(5))
print([triple(x) for x in [1, 2, 3]])

# 15
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    finally:
        print("done")

print(safe_div(10, 2))
print(safe_div(1, 0))

# 16
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print("Error:", e)
