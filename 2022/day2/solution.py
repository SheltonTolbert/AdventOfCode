import sys

match_key = {
        "X": {"L": "C", "R": "B", "modifier": 1}, 
        "Y": {"L": "A", "R": "C", "modifier": 2}, 
        "Z": {"L": "B", "R": "A", "modifier": 3}}

def solve(input):
    score = 0
    for match in input.split("\n"):
        if (match):
            [elf, me] = match.split(" ")
            result = match_key[me]
            if result["L"] == elf:
                score += 6
            elif result["R"] == elf:
                score += 0
            else:
                score += 3
            score += match_key[me]["modifier"]
    return score

if __name__ == "__main__":
    try:
        input_file_path = sys.argv[1]
        file = open(input_file_path)
        input = file.read()
        file.close()
        solution = solve(input)
        print(solution)
    except: 
        print("error: invalid file path arg")
