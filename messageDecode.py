def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Sort the lines by the number at the start of each line
    lines.sort(key=lambda line: int(line.split()[0]))

    message_words = []
    counter = 1
    total = 0
    for line in lines:
        num, word = line.split()
        total += 1
        if total == (counter * (counter + 1)) // 2:
            message_words.append(word)
            counter += 1

    return ' '.join(message_words)

decoded_message = decode('coding_qual_input.txt')
print(decoded_message)

