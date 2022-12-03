import sys

moves = ["A", "B", "C"]
results = ["X", "Y", "Z"]

def solve(input):
    score = 0
    for match in input.split("\n"):
        if (match):
            [elf, me] = match.split(" ")

            move_offset = results.index(me) - 1
            my_move = moves[(moves.index(elf) + move_offset) % len(moves)]

            result_score = moves.index(my_move) + 1
            move_score = results.index(me) * 3

            score += result_score + move_score
    return score

if __name__ == "__main__":
    input_file_path = sys.argv[1]
    file = open(input_file_path)
    input = file.read()
    file.close()
    solution = solve(input)
    print(solution)
