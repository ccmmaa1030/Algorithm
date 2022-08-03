while True:
    word = input()
    if word == '.':
        break

    pair = []

    for c in word:
        if c == '(' or c == '[':
            pair.append(c)
        
        elif c == ')':
            if len(pair) != 0 and pair[-1] == '(':
                pair.pop()
            else:
                pair.append(')')
                break
        
        elif c == ']':
            if len(pair) != 0 and pair[-1] == '[':
                pair.pop()
            else:
                pair.append(']')
                break

    if len(pair) == 0:
        print('yes')
    else:
        print('no')