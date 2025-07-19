import random

number_of_adjective_lists = 8
number_of_adjectives = 3

prev = 0

# list
# 1: quantity or number. only adjective that lead to a plural noun
# 2: Quality or opinion
# 3: Size
# 4: Age
# 5: Shape
# 6: Color
# 7: Origin
# 8: Material
# 9 (todo): Purpose or qualifier
# nouns: plural nouns

expression = []

for i in range(1, number_of_adjectives+1):
  list_number = random.randint(prev+1, number_of_adjective_lists - (number_of_adjectives - i))
  prev = list_number
  with open('lists/' + str(list_number) + '.txt') as f:
    lines = f.readlines() # todo: optimize memory usage
  lines = [x.strip() for x in lines] 
  line_number = random.randint(0, len(lines) - 1)
  expression.append(lines[line_number])

with open('lists/nouns.txt') as f:
  lines = f.readlines() # todo: optimize memory usage
lines = [x.strip() for x in lines] 
line_number = random.randint(0, len(lines) - 1)
expression.append(lines[line_number])

print(' '.join(expression))
