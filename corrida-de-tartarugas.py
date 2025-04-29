import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title('Corrida de Tartarugas!')

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Digite o número de tartarugas (2-10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Tente novamente. Digite um número válido.')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('O número não está entre 2-10')

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Corrida de Tartatugas!')

racers = get_number_of_racers()
init_turtle()

CORES_PORTUGUES = {
    'red': 'vermelho',
    'green': 'verde',
    'blue': 'azul',
    'orange': 'laranja',
    'yellow': 'amarelo',
    'black': 'preto',
    'purple': 'roxo',
    'pink': 'rosa',
    'brown': 'marrom',
    'cyan': 'ciano'
}

random.shuffle(COLORS)
COLORS = COLORS[:racers]
winner = race(COLORS)
print("O vencedor foi a tartaruga com a cor:", CORES_PORTUGUES.get(winner))
time.sleep(5)