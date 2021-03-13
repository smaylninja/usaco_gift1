
"""
ID: smaylni1
LANG: PYTHON3
PROB: gift1
"""

with open('gift1.in') as f:
    lines = f.readlines()
f.close()

n = int(lines[0])
persons = {}


for i in range(n):
    person = str(lines[i + 1])
    person = person.replace("\n", "")
    persons[person] = 0


p = n
j = 1

for i in range(n):
    p += 1
    person = str(lines[p])
    person = person.replace("\n", "")
    values = list(map(int, lines[p + 1].split()))

    if int(values[1] > 0):
        persons[person] -= values[0]
        persons[person] += values[0] % values[1]

        for j in range(values[1]):

            person = str(lines[p + j + 2])
            person = person.replace("\n", "")
            persons[person] += values[0] // values[1]
        p += j + 2
    else:
        persons[person] += values[0]
        p += 1

f = open('gift1.out', 'w')
for i in persons.keys():
    f.write(i + ' ')
    f.write(str(persons[i]) + '\n')

f.close()