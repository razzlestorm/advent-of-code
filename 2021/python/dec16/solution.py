from collections import defaultdict, Counter
from pathlib import Path
from typing import List

FILE_DIR = Path(__file__).parent

# Packets with type ID 4 represent a literal value. Literal value packets encode a single binary number. 
# To do this, the binary number is padded with leading zeroes until its length is a multiple of four bits,
# and then it is broken into groups of four bits. Each group is prefixed by a 1 bit except the last group, which is prefixed by a 0 bit.

BINARY = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111",
}

def translate_hex(data: str) -> str:
    return "".join(BINARY[c] for c in data)

def parse_header(s: str) -> tuple[int]:
    """ Takes in 6 bits and returns version and type_id """
    version = int(s[:3], 2)
    type_id = int(s[3:], 2)
    return version, type_id

def get_literal(s: str) -> tuple[int]:
    """ Returns literal number and how many extra 0s are at the end of the bitstring """
    num = ""
    i = 0 
    final = False
    while not final:
        if s[i] == "1":
            num += s[i+1:i+5]
            i += 5
        else:
            num += s[i+1:i+5]
            i += 5
            final = True
    # What to do about the extra zeroes?
    return int(num, 2), len(s[i:])

print(get_literal("00001"))

def check_length_type(s: str) -> int:
    if s == "0":
        return True
    return False

def parse_operator(s: str, length: bool=True) -> str:
    pass

def solve_one(data: str) -> int:
    i = 0
    count = 0
    while len(data) > 6:
        # we will take in a packet, parse header
        version, type_id = data[i:i+6]
        count += version
        data = data[i+6:]
        # check if literal or operator
        if type_id != 4:
            if check_length_type(data[i]):
                # check 15 bits
                pass

            else:
                pass
                # check 11 bits
        else:
            # get_literal 
            pass
            
        # parse packet accordingly
        # then subtract corresponding number from data
        # repeat until done

def solve_two(data: List[str]) -> int:
    pass


if __name__ == "__main__":

    test_data = [
        translate_hex("8A004A801A8002F478"),
        translate_hex("620080001611562C8802118E34"),
        translate_hex("C0015000016115A2E0802F182340"),
        translate_hex("A0016C880162017C3686B18A3D4780")
    ]
    test_one = test_data[0]
    test_two = test_data[1]
    test_three = test_data[2]
    test_four = test_data[3]
    # Pt 1 Tests
    #assert solve_one(test_one) == 16
    #assert solve_one(test_two) == 12
    #assert solve_one(test_three) == 23
    #assert solve_one(test_four) == 31
    print("Test2: ", solve_two(test_data))  

    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [x for x in DATA.split("\n")][0]
    data = translate_hex(data)
    # print(data)

    #print("Sol1:", solve_one(data))
    #print("Sol2:", solve_two(data)) 
