def pour_coffee(size):
    size_to_ounce_map = {
        "tall": 12,
        "grande":16,
        "venti": 20,
    }
    return size_to_ounce_map.get(size, "Please enter a valid cup size.")

print(pour_coffee("tall"))
print(pour_coffee("grande"))
print(pour_coffee("venti"))
print(pour_coffee("Jumbo"))

