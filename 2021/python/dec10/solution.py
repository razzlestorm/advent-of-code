from pathlib import Path

FILE_DIR = Path(__file__).parent

POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

POINTS2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

REV_PAIRS = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}


def find_corrupt(s: str) -> int:
    """returns the points of the index that the corruption occurs in,
    or False if no corruption found
    """
    stack = []
    for ii, char in enumerate(s):
        if char in REV_PAIRS.values():
            stack.append(char)
        else:
            try:
                left = stack.pop()
                if REV_PAIRS[char] != left:
                    # corresponding left character is wrong
                    raise ValueError
            # can no longer pop off meaning no corresponding left char
            except ValueError:
                return POINTS[char]
    return False


def finish_line(s: str) -> int:
    "returns points for line finished"
    stack = []
    for ii, char in enumerate(s):
        if char in REV_PAIRS.values():
            stack.append(char)
        else:
            stack.pop()
    results = []
    for char in stack[::-1]:
        for k, v in REV_PAIRS.items():
            if char == v:
                results.append(k)
    points = 0
    for c in results:
        points *= 5
        points += POINTS2[c]
    return points


if __name__ == "__main__":

    test_data = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]"
    ]

    test_outputs = [x for x in test_data]
    print(sum([find_corrupt(x) for x in test_outputs]))  # 26397
    print(sum([finish_line(x) for x in test_data if not find_corrupt(x)]))  # 2771042

    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [x for x in DATA.split("\n")]
    # sol 1
    print(sum([find_corrupt(x) for x in data]))  # 265527

    # sol 2
    sol2 = [finish_line(x) for x in data if not find_corrupt(x)]
    sol2 = sorted(sol2)
    print(sol2[len(sol2)//2])  # 3969823589
