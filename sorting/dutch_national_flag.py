def dutch_flag_sort(balls):
    red, white, blue = 0, 0, len(balls) - 1

    while white <= blue:
        if balls[white] == "R":
            balls[red], balls[white] = balls[white], balls[red]
            red += 1
            white += 1
        elif balls[white] == "G":
            white += 1
        else:  # balls[white] == "B"
            balls[white], balls[blue] = balls[blue], balls[white]
            blue -= 1

    return balls
     
