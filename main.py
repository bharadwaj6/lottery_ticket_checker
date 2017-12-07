def combinations_for_ones(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    non_indices = [i for i in xrange(n) if i not in indices]
    contin = True
    for j in xrange(0, len(non_indices), 2):
        a, b = non_indices[j:j + 2]
        if a + 1 != b:
            contin = False
    if contin:
        yield tuple(pool[i] for i in indices), tuple(pool[i] for i in non_indices), indices
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1

        non_indices = [i for i in xrange(n) if i not in indices]
        contin = True
        for j in xrange(0, len(non_indices), 2):
            a, b = non_indices[j:j + 2]
            if a + 1 != b:
                contin = False

        if contin:
            yield tuple(pool[i] for i in indices), tuple(pool[i] for i in non_indices), indices


def check_all_valid_numbers(alist):
    for num in alist:
        if not (1 <= num < 60):
            return False
    return len(set(alist)) == len(alist)


def get_lottery_format(astring, one_indices):
    combi = []

    flag = False
    for i in xrange(len(astring)):
        if i in one_indices:
            combi.append(astring[i])
            combi.append(' ')
        else:
            combi.append(astring[i])
            if flag:
                combi.append(' ')
            flag = not flag

    return ''.join(combi).strip()


def is_valid_lottery(astring):
    response = {'is_valid': False}
    length = len(astring)
    if length < 7 or length > 14:
        return response
    twos = (length - 7)
    ones = 7 - twos
    is_valid = False
    working_combination = None

    for c in combinations_for_ones(astring, ones):
        one_digit_numbers = [int(i) for i in c[0]]
        two_digit_numbers = [int(''.join(c[1][i:i + 2])) for i in xrange(0, len(c[1]), 2)]
        original_indices = c[2]  # to preserve the order

        all_numbers = one_digit_numbers + two_digit_numbers
        valid_combination = check_all_valid_numbers(all_numbers)

        if valid_combination:
            working_combination = get_lottery_format(astring, original_indices)
            is_valid = True
            break

    response = {
        'is_valid': is_valid,
        'combination': working_combination
    }
    return response


def fetch_valid_strings(strings):
    valid_strings = {}
    for astring in strings:
        response = is_valid_lottery(astring)
        if response['is_valid']:
            valid_strings[astring] = response['combination']
    return valid_strings


if __name__ == "__main__":
    strings = ['569815571556', '4938532894754', '1234567', '472844278465445']
    # strings = ['1234567', '123456789', '123', '1234567892455626262', '123456789', '9438532894754']

    print('input: {}'.format(strings))
    outputs = fetch_valid_strings(strings)
    for input_string, output_string in outputs.iteritems():
        print '{input} => {output}'.format(input=input_string, output=output_string)
