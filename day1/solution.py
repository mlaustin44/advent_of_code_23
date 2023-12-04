
def is_digit(c: str) -> bool:
    ascii = ord(c)
    if (ascii >= 48) and (ascii <= 57):
        return True
    else:
        return False

def find_calibration_values(line: str) -> int:
    first_num = None
    last_num = None
    line_len = len(line)
    for i in range(line_len):
        if is_digit(line[i]):
            first_num = line[i]
            break
    for i in range(line_len - 1, -1, -1):
        if is_digit(line[i]):
            last_num = line[i]
            break
    cal_val_str = f"{first_num}{last_num}"
    return int(cal_val_str)

def solve_part1(input):
    cal_total = 0
    for line in input:
        cal_total += find_calibration_values(line)
    print(f"Part 1 solution: {cal_total}")

def find_calibration_values_p2(line: str) -> int:
    word_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    l_idx = len(line)
    l_val = None
    r_idx = -1
    r_val = None

    # first, find the first and last word based values
    for i, wn in enumerate(word_nums):
        l_found = line.find(wn)
        r_found = line.rfind(wn)
        if (l_found != -1) and (l_found < l_idx):
            l_idx = l_found
            l_val = i + 1
        if (r_found != -1) and (r_found > r_idx):
            r_idx = r_found
            r_val = i + 1
    # then find the first and last number values
    line_len = len(line)
    for i in range(line_len):
        if i > l_idx:
            break
        if is_digit(line[i]):
            l_idx = i
            l_val = int(line[i])
    for i in range(line_len - 1, -1, -1):
        if i < r_idx:
            break
        if is_digit(line[i]):
            r_idx = i
            r_val = int(line[i])

    return(int(f"{l_val}{r_val}"))

def solve_part2(input):
    cal_total = 0
    for line in input:
        cal_total += find_calibration_values_p2(line)
    print(f"Part 2 solution: {cal_total}")

if __name__ == "__main__":
    input_file = "input"
    with open(input_file, 'r') as f:
        input = f.readlines()
    
    solve_part1(input)
    solve_part2(input)