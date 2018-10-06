import sys
from random import randint
from time import sleep

def file_len(fname):
    with open(fname) as f:
        return sum(1 for line in f)

print("ECO c/cpp compiler")
print("Version 1.0")

if len(sys.argv) <= 1:
    print("Compiled Nothing Successfully.")
    print("Please pass in a file path to ensure failure.")
    exit(1)

print("compiling...\n")

# wait random amount of time

sleep(randint(1,10))

#throw random error from list
errors = [
        "The compiler dislikes your code style",
        "File too short",
        "Too many semicolons",
        "Not enough semicolons",
        "Minimum recursion depth not met",
        "418 - I'm a teapot",
        "//TODO: add useful error message",
        "Really? this counts as code to you? Try again.",
        "The compiler wrongfully decided that this line was not needed and removed it",
        "At-least-once delivery has failed to deliver the error message at least once",
        "No overflow detected. Please use larger numbers",
        "Maximum line length of 1 exceeded.",
        "Variable name too descriptive",
        "Too many spaces, You shall use tabs.",
        "Too many tabs, You shall use spaces.",
        "404, File not found."
        ]

random_line = randint(1, file_len(sys.argv[1]))

print("Error on line: " + str(random_line))
print(errors[randint(0, len(errors) - 1)])

# exit code one
exit(1)
