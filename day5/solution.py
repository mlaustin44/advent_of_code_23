import sys
import json

# parse the strange ranged map format to a dict with individual values
def parseMap(m):
    res = {}
    v = m.split(' ')
    dest = int(v[0])
    src = int(v[1])
    rlen = int(v[2])

    return {
        'dest': dest,
        'src': src,
        'len': rlen
    }

# using a set of ranges and a value, get the mapped value
def getMappedVal(ranges, val):
    for range in ranges:
        if (val >= range['src']) and (val <= (range['src'] + range['len'])):
            return (val - range['src']) + range['dest']
    # if the value isn't in any of the ranges, set it to the original value
    return val

def parseInput(input):
    # seeds first
    seeds = [int(x) for x in input[0][7:].split(' ')]
    print(seeds)

    #seed-to-soil map will always start line 4
    i = 3
    seed_to_soil = []
    while (input[i] != ''):
        r = parseMap(input[i])
        seed_to_soil.append(r)
        i += 1
    # jump ahead one line
    print(i)
    i += 2
    soil_to_fert = []
    while (input[i] != ''):
        r = parseMap(input[i])
        soil_to_fert.append(r)
        i += 1
    i += 2
    fert_to_water = []
    while (input[i] != ''):
        r = parseMap(input[i])
        fert_to_water.append(r)
        i += 1
    i += 2
    water_to_light = []
    while (input[i] != ''):
        r = parseMap(input[i])
        water_to_light.append(r)
        i += 1
    i += 2
    light_to_temp = []
    while (input[i] != ''):
        r = parseMap(input[i])
        light_to_temp.append(r)
        i += 1
    i += 2
    temp_to_humd = []
    while (input[i] != ''):
        r = parseMap(input[i])
        temp_to_humd.append(r)
        i += 1
    i += 2
    humd_to_loc = []
    while (i < len(input)) and (input[i] != ''):
        r = parseMap(input[i])
        humd_to_loc.append(r)
        i += 1
    return {
        "seeds": seeds,
        "seed_to_soil": seed_to_soil,
        "soil_to_fert": soil_to_fert,
        "fert_to_water": fert_to_water,
        "water_to_light": water_to_light,
        "light_to_temp": light_to_temp,
        "temp_to_humd": temp_to_humd,
        "humd_to_loc": humd_to_loc
    }

def solve_part1(data):
    lowest_loc = 2**32
    for seed in data['seeds']:
        soil = getMappedVal(data['seed_to_soil'], seed)
        fert = getMappedVal(data['soil_to_fert'], soil)
        water = getMappedVal(data['fert_to_water'], fert)
        light = getMappedVal(data['water_to_light'], water)
        temp = getMappedVal(data['light_to_temp'], light)
        humd = getMappedVal(data['temp_to_humd'], temp)
        loc = getMappedVal(data['humd_to_loc'], humd)

        if loc < lowest_loc:
            lowest_loc = loc
    print(f"Part 1 solution: {lowest_loc}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_file = "input.test"
    else:
        input_file = "input"

    with open(input_file, 'r') as f:
        input = f.readlines()
        input = [i.rstrip() for i in input]
    data = parseInput(input)
    solve_part1(data)
