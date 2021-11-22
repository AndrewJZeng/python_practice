apple = {
    'color': 'red',
    'Size': 20
    }

banana = {
    'color': 'yellow',
    'size': 10
    }

fruit = [ apple, banana ]

print(fruit)

print(fruit[0])

print(fruit[-1])

print(fruit[0]['color'])

print(fruit[1]['size'])


apple = {
    'color': ['red', 'yellow'],
    'size': [10, 20, 30]
    }

print(apple)

print(apple['color'])

print(apple['color'][1])
