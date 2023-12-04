
my_dict = {
    "bug":"i have a bug",
    "function":"i am a function",
    "loop":"i can loop well",
}

my_dict["fourth"] = "i have been added to the dictionary"
# my_dict.clear()
# my_dict.pop("loop")

# for i in my_dict:
    # print(my_dict[i])
    # print(f'{i}:"my_dict[i]",')


my_dict1 = {
    "bug":21,
    "function":26,
    "loop":2,
}

max_value = max(my_dict.values())
max_key = max(my_dict, key=my_dict.get)