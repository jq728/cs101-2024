def correct_message(shift, message):
    keyboard = [
        "qwertyuiop",
        "asdfghjkl;",
        "zxcvbnm,./"
    ]

    if shift == 'L':
        shift_value = 1
    elif shift == 'R':
        shift_value = -1
    else:
        return "Invalid shift direction"

    corrected_message = []
    for char in message:
        for row in keyboard:
            if char in row:
                index = row.index(char)
                new_index = (index + shift_value) % len(row)
                corrected_message.append(row[new_index])
                break
    return ''.join(corrected_message)

shift = input()
message = input()
print(correct_message(shift, message))