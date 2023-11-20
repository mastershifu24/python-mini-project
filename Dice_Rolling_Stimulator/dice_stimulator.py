import random

DICE_FACES = [
    [
        "===========",
        "|         |",
        "|    O    |",
        "|         |",
        "==========="
    ],
    [
        "===========",
        "|         |",
        "| O     O |",
        "|         |",
        "==========="
    ],
    [
        "===========",
        "|    O    |",
        "|    O    |",
        "|    O    |",
        "==========="
    ],
    [
        "===========",
        "| O     O |",
        "|         |",
        "| O     O |",
        "==========="
    ],
    [
        "===========",
        "| O     O |",
        "|    O    |",
        "| O     O |",
        "==========="
    ],
    [
        "===========",
        "| O     O |",
        "| O     O |",
        "| O     O |",
        "==========="
    ]
]

def roll_dice():
    number = random.randint(1, 6)
    dice_face = DICE_FACES[number - 1]

    for line in dice_face:
        print(line)

print("This is a dice simulator")
while True:
    roll_dice()
    x = input("Press y to roll again (or any other key to exit): ")
    if x != "y":
        break
