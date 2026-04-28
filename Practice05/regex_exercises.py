import re

# 1. a followed by zero or more b's
def exercise1(s):
    return re.search(r'ab*', s) is not None

# 2. a followed by 2-3 b's
def exercise2(s):
    return re.search(r'ab{2,3}', s) is not None

# 3. lowercase letters joined with underscore
def exercise3(s):
    return re.findall(r'[a-z]+_[a-z]+', s)

# 4. one uppercase followed by lowercase letters
def exercise4(s):
    return re.findall(r'[A-Z][a-z]+', s)

# 5. a followed by anything, ends with b
def exercise5(s):
    return re.search(r'a.*b$', s) is not None

# 6. replace space, comma, dot with colon
def exercise6(s):
    return re.sub(r'[ ,.]', ':', s)

# 7. snake_case to camelCase
def exercise7(s):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s)

# 8. split string at uppercase letters
def exercise8(s):
    return re.split(r'(?=[A-Z])', s)

# 9. insert space between words starting with capital
def exercise9(s):
    return re.sub(r'([A-Z])', r' \1', s).strip()

# 10. camelCase to snake_case
def exercise10(s):
    return re.sub(r'([A-Z])', r'_\1', s).lower()

# Test examples
if __name__ == "__main__":
    print("Exercise 1:", exercise1("abbb"))
    print("Exercise 2:", exercise2("abbb"))
    print("Exercise 3:", exercise3("hello_world test_case"))
    print("Exercise 4:", exercise4("Hello World"))
    print("Exercise 5:", exercise5("a123b"))
    print("Exercise 6:", exercise6("hello, world. test"))
    print("Exercise 7:", exercise7("hello_world"))
    print("Exercise 8:", exercise8("HelloWorldPython"))
    print("Exercise 9:", exercise9("HelloWorldExample"))
    print("Exercise 10:", exercise10("helloWorldTest"))