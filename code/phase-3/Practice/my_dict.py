my_dict = {
    "key_one": "Value one",
    "key_two": "Value two",
}

my_dict["key_one"] = "I've changed!"
my_dict.update({"key_one" : "new value one", "key_three" : "value three", 
                "key_four" : "value four"})
my_dict.update(["key_one", "new value one"], ["key_two", "new value two"])

print(my_dict)