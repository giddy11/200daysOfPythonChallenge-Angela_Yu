# Nested dict in a list
states1 = ["Paris", "Lille", "Dijon"]
states2 = ["Berlin", "Hamburg", "Stuggart"]


# travel_log = {
#     "country": "France", "cities_visited": states1, "total_visits": 12,
#     "country": "Germany", "cities_visited": states2, "total_visits": 5
# }

# travel_log = {
#     "country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12,
#     "country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuggart"], "total_visits": 5
# }

travel_log = {
    {"country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    {"country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuggart"], "total_visits": 5},
}

print(travel_log)















# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# name_list = ["andrew", "peter"]

# my_dict1 = {
#     "bug": "i have a bug",
#     "function": "i am a function",
#     "loop": "i can loop well",
# }

# # Combine dictionaries using update method
# combined_dict = {}
# combined_dict.update({1: name_list})
# combined_dict.update({2: student_scores})
# combined_dict.update({3: my_dict1})

# my_list = [combined_dict]

# print(my_list)

