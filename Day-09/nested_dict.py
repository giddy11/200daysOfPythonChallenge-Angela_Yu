student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

list = ["andrew", "peter"]

my_dict = {
    1:list,
    2:student_scores,
}

my_dict[2]["Harry"] = 400

print(my_dict)
# print(my_dict[2]["Harry"])
# print(my_dict[1][1])
