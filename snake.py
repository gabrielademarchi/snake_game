from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_body_block = Turtle()
        new_body_block.shape('square')
        new_body_block.color('white')
        new_body_block.penup()
        new_body_block.goto(position)
        self.segments.append(new_body_block)

    def extend(self):
        # add segment to where the last segment is
        self.add_segment(self.segments[-1].position())

    def move(self):
        for body_part in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[body_part - 1].xcor()
            new_y = self.segments[body_part - 1].ycor()
            self.segments[body_part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # if is already going up, it cant go back on it self
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
