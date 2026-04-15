from turtleex import turtle

t = turtle.turtle()

# ── READ THIS FIRST ──────────────────────────────────────────────────────────
# Two HOMES have been placed at random spots on the map.
#   Home 1 → red dot
#   Home 2 → blue dot
#
# Your job:
#   1. Visit BOTH homes (move close enough to each one).
#   2. END your journey stopped at ONE of the two homes.
#
# You may ONLY use:
#   t.forward(distance)
#   t.backward(distance)
#   t.left(angle)
#   t.right(angle)
#   t.pos → (x, y)
#
# Check where each home is:
print("Home 1 (red)  is at:", t.home1_pos)   # → (x, y)
print("Home 2 (blue) is at:", t.home2_pos)   # → (x, y)

# ── WRITE YOUR SOLUTION BELOW ─────────────────────────────────────────────────



# ── DO NOT EDIT BELOW THIS LINE ───────────────────────────────────────────────
t.test()
