import sys

def proc_game(game):
    draws = []
    # first strip the game number and the newline
    stripped_game = game.rstrip().split(": ")[1]
    # split it into multiple draws
    split_draws = stripped_game.split("; ")
    for draw in split_draws:
        draw_outcome = {
            "blue": 0,
            "green": 0,
            "red": 0
        }
        cubes = draw.split(", ")
        for cube in cubes:
            cube_split = cube.split(" ")
            draw_outcome[cube_split[1]] = int(cube_split[0])
        draws.append(draw_outcome)
    return draws

def solve_part1(input):
    red_limit = 12
    green_limit = 13
    blue_limit = 14

    games = []
    for l in input:
        games.append(proc_game(l))

    possibles = []

    for i in range(len(games)):
        possible = True
        for draw in games[i]:
            if (draw["green"] > green_limit) or (draw["red"] > red_limit) or (draw["blue"] > blue_limit):
                possible = False
        possibles.append(possible)

    sum = 0
    for i in range(len(possibles)):
        if possibles[i]:
            sum += (i + 1)

    print(f"Part 1 solution: {sum}")

def solve_part2(input):
    games = []
    for l in input:
        games.append(proc_game(l))

    power_total = 0
    for game in games:
        red_min = 0
        green_min = 0
        blue_min = 0
        for draw in game:
            if draw["blue"] > blue_min:
                blue_min = draw["blue"]
            if draw["green"] > green_min:
                green_min = draw["green"]
            if draw["red"] > red_min:
                red_min = draw["red"]
        power = red_min * blue_min * green_min
        power_total += power
    
    print(f"Part 2 solution: {power_total}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_file = "input.test"
    else:
        input_file = "input"
    with open(input_file, 'r') as f:
        input = f.readlines()
    solve_part1(input)
    solve_part2(input)