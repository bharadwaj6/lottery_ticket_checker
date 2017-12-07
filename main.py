def are_sequential_indexes(non_indices):
    """Check if the given indices are sequential two digit numbers"""
    continuous = True
    for j in xrange(0, len(non_indices), 2):
        a, b = non_indices[j:j + 2]
        if a + 1 != b:
            continuous = False
    return continuous


def valid_combinations(iterable, r):
    """Generate valid combinations of given string for a given length.

    :param iterable: the input number string
    :param r: number of one digit numbers that would be in the combination
    :return: valid combinations in given format:
        tuple of one digit numbers that will be in the combination
        tuple of two digit numbers that will be in the combination
        list of indices that tell where one digit numbers were in the original string
        (to get back ordering that was lost)
    :rtype: tuple of tuples and list

    .. note:: this is not stable - will destroy the original order of elements while returning combinations.
    """
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    two_digit_indices = [i for i in xrange(n) if i not in indices]
    is_sequential = are_sequential_indexes(two_digit_indices)
    if is_sequential:
        yield tuple(pool[i] for i in indices), tuple(pool[i] for i in two_digit_indices), indices
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1

        two_digit_indices = [i for i in xrange(n) if i not in indices]
        is_sequential = are_sequential_indexes(two_digit_indices)
        if is_sequential:
            yield tuple(pool[i] for i in indices), tuple(pool[i] for i in two_digit_indices), indices


def check_all_valid_numbers(alist):
    """Check if given list of numbers fall within the given range."""
    for num in alist:
        if not (1 <= num < 60):
            return False
    return len(set(alist)) == len(alist)


def get_lottery_format(astring, one_digit_indices):
    """Given a string of numbers and indices where we selected one digit numbers to be,
    generate the lottery ticket in output format.

    :Example:
    "12345678" with one_digit_indices = [0,  1] => "1 2 34 56 78"
    """
    combi = []

    flag = False
    for i in xrange(len(astring)):
        if i in one_digit_indices:
            combi.append(astring[i])
            combi.append(' ')
        else:
            combi.append(astring[i])
            if flag:
                combi.append(' ')
            flag = not flag

    return ''.join(combi).strip()


def is_valid_lottery(input_string):
    """CHeck if a valid lottery is possible for a given input string."""
    response = {'is_valid': False}
    length = len(input_string)
    if length < 7 or length > 14:
        return response

    twos = (length - 7)  # no of two digit numbers that should be there
    ones = 7 - twos  # no of one digit numbers that will be there
    is_valid = False
    working_combination = None

    for combination in valid_combinations(input_string, ones):
        one_digit_numbers = [int(i) for i in combination[0]]
        two_digit_numbers = [int(''.join(combination[1][i:i + 2])) for i in xrange(0, len(combination[1]), 2)]
        original_indices = combination[2]  # to preserve the order

        all_numbers = one_digit_numbers + two_digit_numbers
        valid_combination = check_all_valid_numbers(all_numbers)

        if valid_combination:
            working_combination = get_lottery_format(input_string, original_indices)
            is_valid = True
            break

    response = {
        'is_valid': is_valid,
        'combination': working_combination
    }
    return response


def fetch_valid_strings(strings):
    """Given a list of strings, create a mapping between valid lottery numbers and their lottery format."""
    valid_strings = {}
    for each_string in strings:
        response = is_valid_lottery(each_string)
        if response['is_valid']:
            valid_strings[each_string] = response['combination']
    return valid_strings


if __name__ == "__main__":
    strings = ['569815571556', '4938532894754', '1234567', '472844278465445']
    # strings = ['1234567', '123456789', '123', '1234567892455626262', '123456789', '9438532894754'] #  extra inputs

    print('input: {}'.format(strings))
    outputs = fetch_valid_strings(strings)
    for input_string, output_string in outputs.iteritems():
        print '{input} => {output}'.format(input=input_string, output=output_string)
