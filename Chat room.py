def can_say_hello(s):
    target = "hello"
    pointer = 0

    for char in s:
        if char == target[pointer]:
            pointer += 1
            if pointer == len(target):
                return "YES"
    return "NO"
s = input().strip()
print(can_say_hello(s))