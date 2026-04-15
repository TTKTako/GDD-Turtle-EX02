import turtle as tt
import random
import math


class turtle:
    def __init__(self):
        self._screen = tt.Screen()
        self._screen.title("Turtle Likes To Travel!")
        self._screen.setup(600, 600)
        self._screen.bgcolor("lightyellow")

        # Spawn Home 1 at a random position
        self._home1_x = float(random.randint(-220, 220))
        self._home1_y = float(random.randint(-220, 220))

        # Spawn Home 2 far enough from Home 1
        while True:
            self._home2_x = float(random.randint(-220, 220))
            self._home2_y = float(random.randint(-220, 220))
            dist = math.sqrt((self._home2_x - self._home1_x) ** 2 +
                             (self._home2_y - self._home1_y) ** 2)
            if dist >= 120:
                break

        self._home1_color = "red"
        self._home2_color = "blue"

        # Track which homes have been visited
        self._visited1 = False
        self._visited2 = False

        # Draw both home markers instantly (no animation)
        self._screen.tracer(0)
        self._draw_homes()
        self._screen.update()
        self._screen.tracer(1)

        # Player turtle
        self._t = tt.Turtle()
        self._t.shape("turtle")
        self._t.color("green")
        self._t.speed(5)

    # ------------------------------------------------------------------ #
    def _draw_homes(self):
        for hx, hy, color, label in [
            (self._home1_x, self._home1_y, self._home1_color, "HOME 1"),
            (self._home2_x, self._home2_y, self._home2_color, "HOME 2"),
        ]:
            m = tt.Turtle()
            m.hideturtle()
            m.penup()
            m.goto(hx, hy)
            m.dot(28, color)
            m.goto(hx, hy + 14)
            m.color("white")
            m.write(label, align="center", font=("Arial", 10, "bold"))

    # ------------------------------------------------------------------ #
    def _check_visit(self):
        """Mark a home as visited if the turtle is close enough."""
        cx, cy = self._t.xcor(), self._t.ycor()
        visit_tolerance = 20.0
        if not self._visited1:
            d = math.sqrt((cx - self._home1_x) ** 2 + (cy - self._home1_y) ** 2)
            if d <= visit_tolerance:
                self._visited1 = True
        if not self._visited2:
            d = math.sqrt((cx - self._home2_x) ** 2 + (cy - self._home2_y) ** 2)
            if d <= visit_tolerance:
                self._visited2 = True

    # ------------------------------------------------------------------ #
    # Allowed movement commands
    def left(self, angle):
        self._t.left(angle)
        self._check_visit()

    def right(self, angle):
        self._t.right(angle)
        self._check_visit()

    def forward(self, distance):
        self._t.forward(distance)
        self._check_visit()

    def backward(self, distance):
        self._t.backward(distance)
        self._check_visit()

    # ------------------------------------------------------------------ #
    @property
    def pos(self):
        """Current turtle position as (x, y)."""
        return (round(self._t.xcor(), 4), round(self._t.ycor(), 4))

    @property
    def home1_pos(self):
        """Home 1 (red) position as (x, y)."""
        return (self._home1_x, self._home1_y)

    @property
    def home2_pos(self):
        """Home 2 (blue) position as (x, y)."""
        return (self._home2_x, self._home2_y)

    # ------------------------------------------------------------------ #
    @staticmethod
    def turtle():
        return turtle()

    # ------------------------------------------------------------------ #
    def test(self):
        """Check whether the turtle visited both homes and ended at one."""
        self._check_visit()  # capture the final resting position
        cx, cy = self._t.xcor(), self._t.ycor()
        final_tolerance = 15.0

        d1 = math.sqrt((cx - self._home1_x) ** 2 + (cy - self._home1_y) ** 2)
        d2 = math.sqrt((cx - self._home2_x) ** 2 + (cy - self._home2_y) ** 2)
        ended_at_home = (d1 <= final_tolerance) or (d2 <= final_tolerance)
        passed_both   = self._visited1 and self._visited2

        self._screen.tracer(0)
        self._t.penup()

        if passed_both and ended_at_home:
            print("=" * 52)
            print("  SUCCESS!  Visited both homes and stopped at one!")
            print(f"  Home 1 (red)  : ({self._home1_x:.1f}, {self._home1_y:.1f})  visited={self._visited1}")
            print(f"  Home 2 (blue) : ({self._home2_x:.1f}, {self._home2_y:.1f})  visited={self._visited2}")
            print(f"  Turtle ended  : ({cx:.1f}, {cy:.1f})")
            print("=" * 52)
            self._t.color("lime green")
        else:
            print("=" * 52)
            print("  FAIL!")
            v1 = "OK" if self._visited1 else "NOT visited"
            v2 = "OK" if self._visited2 else "NOT visited"
            print(f"  Home 1 (red)  : ({self._home1_x:.1f}, {self._home1_y:.1f})  {v1}")
            print(f"  Home 2 (blue) : ({self._home2_x:.1f}, {self._home2_y:.1f})  {v2}")
            if not ended_at_home:
                print(f"  Turtle ended at ({cx:.1f}, {cy:.1f})  — not at either home")
            print("=" * 52)
            self._t.color("orange")

        self._screen.update()
        self._screen.mainloop()  # keep the window open until closed

