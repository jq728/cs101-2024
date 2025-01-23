def format_text(words):
    current_line = ""
    formatted_text = []

    for word in words:
        if len(current_line) + len(word) <= 80:
            current_line += word + " "
        else:
            formatted_text.append(current_line.strip())
            current_line = word + " "

    if current_line:
        formatted_text.append(current_line.strip())

    return formatted_text

n = int(input())
words = input().split()
formatted_text = format_text(words)
for line in formatted_text:
    print(line)