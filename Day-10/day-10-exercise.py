def FormatName(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You did'nt provide valid inputs."
    
    formatted_f_name = first_name.capitalize()
    formatted_l_name = last_name.capitalize()

    return f"{formatted_f_name} {formatted_l_name}"

res = FormatName("", "gideon")
print(res)