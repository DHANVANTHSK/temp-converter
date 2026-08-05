def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
if __name__ == "__main__":
    c = 25
    f = celsius_to_fahrenheit(c)
    print(f"{c}C is equal to {f}F")
