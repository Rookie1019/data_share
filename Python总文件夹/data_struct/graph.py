import turtle



def draw_spiral(t, linelen):
    if linelen > 0:
        t.forward(linelen)
        t.right(90)
        draw_spiral(t, linelen-5)

t = turtle.Turtle()

def tree(branch_len):
    if branch_len > 5:
        t




if __name__ == "__main__":
    draw_spiral(t, 500)
    turtle.done