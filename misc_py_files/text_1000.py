with open('text_copy.txt', encoding='utf8') as myfile:
    count = 0
    for line in myfile:
        a = line.split(' ')
        len_a = len(a)
        count += len_a
    print(count)
