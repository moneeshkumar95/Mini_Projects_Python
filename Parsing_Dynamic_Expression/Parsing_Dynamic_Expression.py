def parse(exp, dic):
    exp_list, result = exp.split(), ''

    for i in range(0, len(exp_list) - 1, 2):
        if '(' in exp_list[i]:
            parantheses = exp_list[i:i + 3]
            parantheses[0], parantheses[2] = parantheses[0][1], parantheses[2][0]

            if parantheses[1] == 'and':
                dic[str(i)] = dic.get(parantheses[0], '') + dic.get(parantheses[2], '')
                exp_list[i:i + 3] = str(i)
            elif parantheses[1] == 'or':
                if dic.get(parantheses[0]):
                    exp_list[i:i + 3] = parantheses[0]
                elif dic.get(parantheses[2]):
                    exp_list[i:i + 3] = parantheses[2]

    exp_length = len(exp_list)
    for i in range(0, exp_length, 2):
        if i != exp_length - 1 and i == 0:
            data = exp_list[i:i + 3]

            if data[1] == 'and':
                result += dic.get(data[0], '') + dic.get(data[2], '')
            elif data[1] == 'or':
                if dic.get(data[0]):
                    result += dic.get(data[0], '')
                elif dic.get(data[2]):
                    result += dic.get(data[2], '')

        elif i != exp_length - 1:
            data = exp_list[i:i + 3]

            if data[1] == 'and':
                result += dic.get(data[2], '')
    return result


expression = 'A and (B or C) and D'
dictionary = {'A': 'Hello', 'C': 'Buddy', 'D': 'Welcome'}
print(parse(expression, dictionary))
