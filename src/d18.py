import math
import json
from copy import deepcopy
from itertools import permutations
from os import posix_spawn

def prepare(input):
    return [json.loads(line) for line in input]

class SnailfishNumber:
    def __init__(self, value, parent=None):
        self.parent = parent

        if isinstance(value, list):
            self.left = SnailfishNumber(value[0], self)
            self.right = SnailfishNumber(value[1], self)
            self.value = None
        else:
            self.value = value
            self.left = None
            self.right = None

    def search(self, current, left=True, right=False):
        queue, last, exit_next = [self.right, self.left], None, False
        while len(queue) > 0:
            node = queue.pop()

            if node is None:
                continue

            if left and current is node:
                return last

            if node.is_normal():
                if exit_next:
                    return node
                last = node
        
            if right and current is node:
                exit_next = True

            queue.append(node.right)
            queue.append(node.left)

        return None

    def depth(self):
        depth, ancestor = 0, self.parent
        while ancestor is not None:            
            depth += 1
            ancestor = ancestor.parent
        return depth

    def is_normal(self):
        return self.value is not None

    def is_normal_pair(self):
        return self.left is not None and self.left.is_normal() and \
            self.right is not None and self.right.is_normal()

    def reduce(self):
        exhausted, has_exploded, has_split = False, False, False
        while not exhausted:
            queue, has_exploded = [self.right, self.left], False
            while len(queue) > 0 and not has_exploded:
                node = queue.pop()

                if node is None:
                    continue

                if node.is_normal_pair() and node.depth() >= 4:
                    left = self.search(node.left, True, False)
                    right = self.search(node.right, False, True)
                    if left is not None:
                        left.value += node.left.value
                    if right is not None:
                        right.value += node.right.value
                    node.value = 0
                    node.left = None
                    node.right = None
                    
                    has_exploded = True
                
                queue.append(node.right)
                queue.append(node.left)

            if has_exploded:
                continue
            
            queue, has_split = [self.right, self.left], False
            while len(queue) > 0 and not has_split:
                node = queue.pop()

                if node is None:
                    continue

                if node.is_normal() and node.value >= 10:
                    node.left = SnailfishNumber(math.floor(node.value / 2), node)
                    node.right = SnailfishNumber(math.ceil(node.value / 2), node)
                    node.value = None
                    has_split = True

                queue.append(node.right)
                queue.append(node.left)

            if has_split:
                continue

            exhausted = True

        return self

    def magnitude(self):
        if self.is_normal():
            return self.value
        
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def as_literal(self):
        if self.is_normal():
            return self.value

        return [self.left.as_literal(), self.right.as_literal()]

    def add(self, rhs):
        node = SnailfishNumber([self.as_literal(), rhs])
        self.parent = node
        return node

def part_one(input):
    root = SnailfishNumber(input.pop(0))
    for line in input:
        root = root.add(line)
        root.reduce()
    return root.magnitude()

def part_two(input):
    possible, maximum = list(permutations(input, 2)), 0
    for left, right in possible:
        sum = SnailfishNumber(left).add(right).reduce().magnitude()
        maximum = max(maximum, sum)
    return maximum
    
def test(input):
    input = prepare(input)
    print(part_one(deepcopy(input)))
    assert part_two(input) == 3993

def answer(input):
    input = prepare(input)
    print(part_one(deepcopy(input)))
    print(part_two(input))
