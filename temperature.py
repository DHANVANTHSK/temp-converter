def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
def fahrenheit_to_celsius(f):
    return ((f-32)*5/9)
def kelvin(c):
    return (273-c)
if __name__ == "__main__":
    c = 25
    f = celsius_to_fahrenheit(c)
    k = celsius_to_kelvin(c)
    print(f"{c}C is equal to {f}F")
    print(f"{f}F is equal to {c}C")
    print(f"{c}C is equal to {k}K")
