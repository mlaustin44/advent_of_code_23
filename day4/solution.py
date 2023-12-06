import sys

# returns an array of arrays, where for each array [0] is the winning #s and [1] is our numbers
def parse_input(input):
    cards = []
    for card in input:
        # remove the 'Card N: ' preamble and then split into the winning #s and our #s
        card = card.split(': ')[1].rstrip().split(' | ')
        # split the lists of numbers and convert them to ints
        # need the conditional because some numbers have two spaces between them,
        #    causing ghost entries
        card[0] = [int(x) for x in card[0].split(' ') if x != '']
        card[1] = [int(x) for x in card[1].split(' ') if x != '']
        cards.append(card)

    return cards

def solve_part1(cards):
    total_pts = 0
    for card in cards:
        win_nos = []
        for n in card[1]:
            if n in card[0]:
                win_nos.append(n)
        if len(win_nos) >= 1:
            pts = 2 ** (len(win_nos) - 1)
            total_pts += pts
    
    print(f"Part 1 solution: {total_pts}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_file = "input.test"
    else:
        input_file = "input"

    with open(input_file, 'r') as f:
        input = f.readlines()

    cards = parse_input(input)
    solve_part1(cards)
