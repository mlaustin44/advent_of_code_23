import sys

def parse_engine_map(input):
    engine_map = []
    for l in input:
        # get rid of the newlines
        l = l.rstrip()
        engine_map.append(list(l))
    return engine_map

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
def is_sym(c):
    if (c in digits) or (c == "."):
        return False
    else:
        return True

def is_num(c):
    if c in digits:
        return True
    return False

def solve_part1(engine_map):
    # first come up with a map of where the symbols touch
    # max x dim (rows)
    xm = len(engine_map)
    # max y dim (cols)
    ym = len(engine_map[0])

    # create an array to serve as a map of all the symbol adjacent squares
    sym_map = [[0 for x in range(xm)] for y in range(ym)]

    # find all the symbol adjacent squares
    for i in range(xm):
        for j in range(ym):
            if is_sym(engine_map[i][j]):
                # naive gross solution
                # set the square to the right
                if i < (xm - 1):
                    sym_map[i+1][j] = 1
                # square to the left
                if i > 0:
                    sym_map[i-1][j] = 1
                # square above
                if j < (ym - 1):
                    sym_map[i][j+1] = 1
                # square below
                if j > 0:
                    sym_map[i][j-1] = 1
                # top left
                if (i > 0) and (j < (ym - 1)):
                    sym_map[i-1][j+1] = 1
                # top right
                if (i < (xm - 1)) and (j < (ym - 1)):
                    sym_map[i+1][j+1] = 1
                # bottom left
                if (i > 0) and (j > 0):
                    sym_map[i-1][j-1] = 1
                # bottom right
                if (i < (xm - 1)) and (j > 0):
                    sym_map[i+1][j-1] = 1

    # find the numbers, and if any digit is touching a symbol, count it
    valid_nums = []
    seen = [[0 for x in range(xm)] for y in range(ym)]
    for i in range(xm):
        for j in range(ym):
            if seen[i][j] == 1:
                continue
            if is_num(engine_map[i][j]):
                touching = False
                num = ''
                while True:
                    if not is_num(engine_map[i][j]):
                        if touching:
                            valid_nums.append(int(num))
                        break
                    num += engine_map[i][j]
                    if (not touching) and (sym_map[i][j] == 1):
                        touching = True
                    if j < (ym - 1):
                        j = j + 1
                        seen[i][j] = 1
                    else:
                        if touching:
                            valid_nums.append(int(num))
                        break
    
    # sum the valid numbers
    sum = 0
    for n in valid_nums:
        sum += n
    print(f"Part 1 solution: {sum}")

def solve_part2(engine_map):
    # iterate through, find all the '*' charecters (these are gears), then find adjacent numbers
    # max x dim (rows)
    xm = len(engine_map)
    # max y dim (cols)
    ym = len(engine_map[0])
    
    def is_num_w_bounds(y, x):
        if (x < 0) or (x == xm) or (y < 0) or (y == ym):
            return False
        else:
            return is_num(engine_map[y][x])


    def find_touching_nums(y, x):
        # create a map of already visited squares (to avoid double counting numbers)
        seen = [[0 for x in range(xm)] for y in range(ym)]
        touching_nums = []

        def exhaust_number(y, x):
            xmin = x
            xmax = x
            seen[y][x] = 1
            # to the left
            while True:
                if is_num_w_bounds(y, (xmin - 1)):
                    xmin = xmin - 1
                    seen[y][xmin] = 1
                else:
                    break
            # to the right
            while True:
                if is_num_w_bounds(y, (xmax + 1)):
                    xmax = xmax + 1
                    seen[y][xmax] = 1
                else:
                    break
            # figure out what the number is
            acc = ''
            for i in range(xmin, xmax+1):
                acc += engine_map[y][i]
            return int(acc)

        # to the left
        if (seen[y][x-1] != 1) and (is_num_w_bounds(y, x-1)):
            num = exhaust_number(y, x-1)
            touching_nums.append(num)
        # to the right
        if (seen[y][x+1] != 1) and (is_num_w_bounds(y, x+1)):
            num = exhaust_number(y, x+1)
            touching_nums.append(num)
        # to the down
        if (seen[y-1][x] != 1) and (is_num_w_bounds(y-1, x)):
            num = exhaust_number(y-1, x)
            touching_nums.append(num)
        # to the up
        if (seen[y+1][x] != 1) and (is_num_w_bounds(y+1, x)):
            num = exhaust_number(y+1, x)
            touching_nums.append(num)
        # to the up left
        if (seen[y+1][x-1] != 1) and (is_num_w_bounds(y+1, x-1)):
            num = exhaust_number(y+1, x-1)
            touching_nums.append(num)
        # to the up right
        if (seen[y+1][x+1] != 1) and (is_num_w_bounds(y+1, x+1)):
            num = exhaust_number(y+1, x+1)
            touching_nums.append(num)
        # to the down left
        if (seen[y-1][x-1] != 1) and (is_num_w_bounds(y-1, x-1)):
            num = exhaust_number(y-1, x-1)
            touching_nums.append(num)
        # to the down right
        if (seen[y-1][x+1] != 1) and (is_num_w_bounds(y-1, x+1)):
            num = exhaust_number(y-1, x+1)
            touching_nums.append(num)
        
        return touching_nums
    
    gears = []

    for y in range(ym):
        for x in range(xm):
            if engine_map[x][y] == '*':
                nums = find_touching_nums(x, y)
                if len(nums) == 2:
                    gears.append(nums)

    # now multiple through our gear matches
    total = 0
    for g in gears:
        prod = g[0] * g[1]
        total += prod

    print(f"Part 2 solution: {total}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_file = "input.test"
    else:
        input_file = "input"

    with open(input_file, 'r') as f:
        input = f.readlines()

    engine_map = parse_engine_map(input)
    solve_part1(engine_map)
    solve_part2(engine_map)