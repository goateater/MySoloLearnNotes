print("This is a sentence.".endswith("sentence."))
print("This is a sentence.".startswith("This"))

print("spam, eggs, ham".split("a"))


nums = [55, 44, 30, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")
else:
    print("One or more is less than 5")


for v in enumerate(nums, 1):
    print(v)


def decor(func):
    def wrap():
        print("~~~~~~~~~~~~~")
        func()
        print("~~~~~~~~~~~~~~")
    return wrap

def print_text():
    print("SUP SUP SUP")

decorated = decor(print_text)
decorated()