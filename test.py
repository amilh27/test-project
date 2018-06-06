def main():
    # # print('do stuff')
    num_list = [2, 4, 1, 6, 5, 40, -1]
    # excercise_udemy()
    find_primes()
    exit(1)
    # integers_problem_new(num_list, 30)
    str_sequence = 'UUUAAAAAABCDDBBBEACCFFEHIJJAUUUUUHHHHFFFFCCCCCEEEEAAASSSDFGHJKLLUUTGGFRRRDSSAAQQQQQQQQSSEDRFFGUABBHHHHIKKLM'
    longest_consecutive_character(str_sequence)

    # my_list = list(str_sequence)
    # sub_list = my_list[2:]
    # # print sub_list


def longest_consecutive_character(str_sequence):

    my_dict = {}
    # my_dict = {'A': 1, 'B': 2, 'C': 3}

    str_list = list(str_sequence)

    for index in range(len(str_list)):
        current_char = str_list[index]

        # # print '{} => {}'.format(index, current_char)
        if index == len(str_list) - 1:
            break

        next_char = str_list[index + 1]

        # print 'current: {} - next: {}'.format(current_char, next_char)

        if current_char == next_char:

            count = 2
            # print 'count set: {}'.format(count)

            for char in str_list[index + 2:]:
                # print 'evaluating char: {} - current: {}'.format(char, current_char)
                if char == current_char:
                    count += 1
                    # print 'count increased'
                else:
                    # print 'breaking'
                    break

            if current_char in my_dict:
                # print 'key exists - count: {} - key: {} - value: {}'\
                    #.format(count, current_char, my_dict[current_char])

                if my_dict[current_char] < count:
                    # # print 'popping'
                    # my_dict.pop(current_char)
                    my_dict[current_char] = count
                    # print 'added key: {} - value: {}'.format(current_char, count)
            else:
                my_dict[current_char] = count
                # print 'added key: {} - value: {}'.format(current_char, count)

            # my_dict[current_char] = 1
    # print '{}\n{}'.format(my_dict, max(my_dict, key=lambda key: my_dict[key]))
    key = max(my_dict, key=lambda key: my_dict[key])
    print 'The longest consecutive character is {} with {} repetitions'.format(key, my_dict[key])


def integers_problem(int_list, target_mul):
    factors = []
    found = False
    for num in int_list:
        # # print('value: {}'.format(num))
        if target_mul % num == 0:
            # # print('factor: {}'.format(num))
            if not factors:
                factors.append(num)
            else:
                for factor in factors:
                    if num * factor == target_mul:
                        # print('The two numbers are {} and {}'.format(num, factor))
                        found = True
                        break
                if not found:
                    factors.append(num)
        if found:
            break

    # # print factors


def integers_problem_new(int_list, target_mul):
    factors = []
    for num in int_list:
        # # print('value: {}'.format(num))
        if target_mul % num == 0:
            comp = target_mul / num
            # # print('factor: {}'.format(num))
            if comp in factors:
                # print('The two numbers are {} and {}'.format(num, comp))
                break
            factors.append(num)

    # # print factors


def excercise_udemy():

    my_tuple = ('hello',)
    other_tuple = 'hello',

    print '{} - {}'.format(my_tuple, type(my_tuple))
    print '{} - {}'.format(other_tuple, type(other_tuple))


def find_primes():
    for i in range(2, 10):
        for j in range(2, i):
            if i % j == 0:
                print '{} equals {} X {}'.format(i, j, i//j)
                break
        else:
            print '{} is a prime number'.format(i) 


if __name__ == "__main__":
    main()
else:
    print 'this module is being imported'

