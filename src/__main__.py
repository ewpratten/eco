import sys
from random import randint
from time import sleep

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print("ECO c/cpp compiler")
print("Version 1.0")

if len(sys.argv) <= 1:
	print("Please pass in a file path.")
	exit(1)

print("compiling...\n")

# wait random amount of time

sleep(randint(1,10))

#throw random error from list
errors = ["The compiler dislikes your code style"]
random_line = randint(1, file_len(sys.argv[1]))

print("Error on line: " + str(random_line))
print(errors[randint(0, len(errors) - 1)])

# exit code one
exit(1)