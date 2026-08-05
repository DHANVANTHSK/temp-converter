def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
def fahrenheit_to_celsius(f):
    return ((f-32)*5/9)
if __name__ == "__main__":
    c = 25
    f = celsius_to_fahrenheit(c)
    print(f"{c}C is equal to {f}F")
    print(f"{f}F is equal to {c}C")