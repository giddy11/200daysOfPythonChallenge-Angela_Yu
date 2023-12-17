from prettytable import *


table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# table.set_style(MSWORD_FRIENDLY)
table.align = "l"

print(table)
