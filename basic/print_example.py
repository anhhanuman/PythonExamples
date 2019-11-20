bicycles = ['rado', 'bidan', 'xena', 'yellow bicycle']
print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[2].title())  # xena becomes Xena which is capitalized
print(bicycles[2].capitalize())  # xena becomes Xena which is capitalized
print(bicycles[-1])

message = f"My first bicycles was {bicycles[0].title()}"
# f string to create a message based on a value from the list

print(message)

bicycles[0] = 'Radiomen'
message = f'My first bicycle\'s was {bicycles[0].title()}'
print(message)
print(bicycles)

# appending element to the list

bicycles.append('New added bicycle')
print(bicycles)


def hello():
    print('tester')


def sayHello(team):
    print('hello' + team)


sayHello('team')
