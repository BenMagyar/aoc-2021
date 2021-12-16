from math import prod

def prepare(input):
    return ''.join([bin(int(char, 16))[2:].zfill(4) for char in input])

class Reader:
    def __init__(self, input):
        self.input = input
        self.pointer = 0
        self.versions = 0
    
    def read(self, bits):
        value = self.input[self.pointer:self.pointer + bits]
        self.pointer += bits
        return value

    def number(self, bits):
        return int(self.read(bits), 2)

    def literal(self):
        has_next_packet, value = True, ''
        while has_next_packet:
            has_next_packet = bool(self.number(1))
            value += self.read(4)
        return int(value, 2)

    def operator(self, id):
        length_id = self.number(1)
        
        if length_id == 0:
            length, start, values = self.number(15), self.pointer, []
            while self.pointer < start + length:
                values.append(self.next())
        else:
            subpackets = self.number(11)
            values = [self.next() for _ in range(subpackets)]

        if id == 0:
            value = sum(values)
        elif id == 1:
            value = prod(values)
        elif id == 2:
            value = min(values)
        elif id == 3:
            value = max(values)
        elif id == 5:
            value = int(values[0] > values[1])
        elif id == 6:
            value = int(values[0] < values[1])
        elif id == 7:
            value = int(values[0] == values[1])
    
        return value
    
    def next(self):
        if str.strip(self.input[self.pointer:], '0') == '':
            return False

        version = self.number(3)
        id = self.number(3)
        self.versions += version

        value = self.literal() if id == 4 else self.operator(id)
        
        return value

def part_one(input):
    reader = Reader(input)
    reader.next()
    return reader.versions

def part_two(input):
    reader = Reader(input)
    return reader.next()
    
def test(input):
    input = prepare(input)
    assert part_one(prepare('A0016C880162017C3686B18A3D4780')) == 31
    assert part_two(prepare('04005AC33890')) == 54

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
