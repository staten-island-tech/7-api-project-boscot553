import tkinter as tk
import random

# Window setup
WIDTH = 500
HEIGHT = 500
SPEED = 100  # lower = faster
SPACE = 20   # size of each square
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BG_COLOR = "black"


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(root, bg=BG_COLOR, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.direction = "Right"

        self.snake = [(100, 100), (80, 100), (60, 100)]  # starting body
        self.food = None

        self.draw_snake()
        self.spawn_food()

        self.root.bind("<KeyPress>", self.change_direction)
        self.move_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + SPACE, y + SPACE, fill=SNAKE_COLOR, tag="snake")

    def spawn_food(self):
        x = random.randint(0, (WIDTH - SPACE) // SPACE) * SPACE
        y = random.randint(0, (HEIGHT - SPACE) // SPACE) * SPACE
        self.food = (x, y)
        self.canvas.delete("food")
        self.canvas.create_oval(x, y, x + SPACE, y + SPACE, fill=FOOD_COLOR, tag="food")

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= SPACE
        elif self.direction == "Down":
            head_y += SPACE
        elif self.direction == "Left":
            head_x -= SPACE
        elif self.direction == "Right":
            head_x += SPACE

        new_head = (head_x, head_y)

        # Check collisions with walls
        if (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in self.snake
        ):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        # Check if food eaten
        if new_head == self.food:
            self.spawn_food()
        else:
            self.snake.pop()

        self.draw_snake()
        self.root.after(SPEED, self.move_snake)

    def game_over(self):
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2,
            text="GAME OVER",
            fill="white",
            font=("Arial", 30)
        )

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()