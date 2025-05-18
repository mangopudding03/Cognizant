import turtle

choice = input("Choose one of the following: \n"
               "1. Calculate the factorial of a number\n"
               "2. Find the nth Fibonacci number\n"
               "3. Draw a recursive fractal pattern (bonus)\n"
               "4. Exit\n> ")

# Factorial Function
def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a - 1)

# Fibonacci Function
def fibonacci(a):
    if a <= 0:
        return 0
    elif a == 1:
        return 1
    return fibonacci(a - 1) + fibonacci(a - 2)

def fractal():
    # screen requirements
    SPEED = 5
    BG_COLOR = "blue"
    PEN_COLOR = "lightgreen"
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    DRAWING_WIDTH = 700
    DRAWING_HEIGHT = 700
    PEN_WIDTH = 5
    TITLE = "H-Tree Fractal with Python Turtle Graphics"
    FRACTAL_DEPTH = 3 # depth of the drawings

    # turtle draws a line from one point to another
    def draw_line(tur, pos1, pos2):
        tur.penup()
        tur.goto(pos1[0], pos1[1])
        tur.pendown()
        tur.goto(pos2[0], pos2[1])


    def recursive_draw(tur, x, y, width, height, count): #recursively draws
        draw_line(
            tur,
            [x + width * 0.25, height // 2 + y],
            [x + width * 0.75, height // 2 + y],
        )
        draw_line(
            tur,
            [x + width * 0.25, (height * 0.5) // 2 + y],
            [x + width * 0.25, (height * 1.5) // 2 + y],
        )
        draw_line(
            tur,
            [x + width * 0.75, (height * 0.5) // 2 + y],
            [x + width * 0.75, (height * 1.5) // 2 + y],
        )

        if count <= 0:  # The base case
            return
        else: # four quadrants for each area
            count -= 1
            # Top left
            recursive_draw(tur, x, y, width // 2, height // 2, count)
            # Top right
            recursive_draw(tur, x + width // 2, y, width // 2, height // 2, count)
            # Bottom left
            recursive_draw(tur, x, y + width // 2, width // 2, height // 2, count)
            # Bottom right
            recursive_draw(tur, x + width // 2, y + width // 2, width // 2, height // 2, count)


    if __name__ == "__main__":
        # Screen setup
        screen = turtle.Screen()
        screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        screen.title(TITLE)
        screen.bgcolor(BG_COLOR)

        # Turtle setup
        artist = turtle.Turtle()
        artist.hideturtle()
        artist.pensize(PEN_WIDTH)
        artist.color(PEN_COLOR)
        artist.speed(SPEED)

        # Recursive draw function
        recursive_draw(artist, - DRAWING_WIDTH / 2, - DRAWING_HEIGHT / 2, DRAWING_WIDTH, DRAWING_HEIGHT, FRACTAL_DEPTH)
        turtle.done()

if choice == "1":
    a = int(input("Enter a number for factorial: "))
    print(f"The factorial of {a} is {factorial(a)}.")

elif choice == "2":
    a = int(input("Enter a number for Fibonacci: "))
    print(f"The {a}th Fibonacci number is {fibonacci(a)}.")

elif choice == "3":
    print("Fractal drawing on another screen")
    fractal()

elif choice == "4":
    print("Byeee!")

else:
    print("Invalid choice. Please only select 1, 2, 3, or 4.")
