import re

def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]

def capitalizeWords(s):
  return re.sub(r'\w+', lambda m:m.group(0).capitalize(), s)

res = camelCase("hello .sir")
res2 = capitalizeWords("hello gyt")

print(res2)