# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# max_score = None
# for student_score in student_scores:
#   if max_score == None:
#     max_score = student_score

#   if student_score > max_score:
#     max_score = student_score

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}")


# print(f"The highest score in the class is: {max_score}")