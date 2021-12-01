import os

def read_example(day):
    with open(os.path.join(os.getcwd(), "examples", day + ".txt")) as file:
        return file.readlines()

def read_input(day):
    with open(os.path.join(os.getcwd(), "inputs", day + ".txt")) as file:
        return file.readlines()
