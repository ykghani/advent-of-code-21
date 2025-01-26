'''Advent of Code 2021 Day 17 - Trick Shot'''

x_dim, y_dim = [206, 250], [-105, -57]
# x_dim = [20, 30]
# y_dim = []

def update_pos(x, y, vx, vy, steps = 1):
    for _ in range(steps): 
        x += vx
        y += vy
        if vx > 0: 
            vx -= 1
        elif vx < 0:
            vx +=1 
        vy -= 1
    return x, y, vx, vy
    
def chart_tragectory(vx, vy, STEPS = 100):
    max_y = 0
    x, y = 0, 0
    hits_target = False
    # while y > y_dim[1] and x < x_dim[1]:
    for _ in range(STEPS):
        x, y, vx, vy = update_pos(x, y, vx, vy)
        max_y = y if y > max_y else max_y
        if x_dim[0] <= x <= x_dim[1] and y_dim[0] <= y <= y_dim[1]:
            hits_target = True
    return max_y if hits_target else None

max_style = 0
for vx in range(1, 500):
    for vy in range(1, 500):
        style = chart_tragectory(vx, vy)
        max_style = style if style is not None else max_style

print(f"Part one: {max_style}")
        