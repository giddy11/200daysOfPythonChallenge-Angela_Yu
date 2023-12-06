def FormatName(first_name, last_name):
    formatted_f_name = first_name.capitalize()
    formatted_l_name = last_name.capitalize()

    return f"{formatted_f_name} {formatted_l_name}"

res = FormatName("caroline", "gideon")
print(res)