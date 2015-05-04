keys = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    '0': ' ',
}

T9 = {c: k * (i + 1) for k, v in keys.items() for i, c in enumerate(v)}

for tc in range(int(input())):
    line = input()
    text = ''
    for c in line:
        if text and text[-1] == T9[c][0]:  # add space if same button
            text += ' '
        text += T9[c]
    print('Case #{}: {}'.format(tc + 1, text))
