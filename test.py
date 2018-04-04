def main():
    # print('do stuff')
    num_list = [2, 4, 1, 6, 5, 40, -1]
    integers_problem_new(num_list, 30)


def integers_problem(int_list, target_mul):
    factors = []
    found = False
    for num in int_list:
        # print('value: {}'.format(num))
        if target_mul % num == 0:
            # print('factor: {}'.format(num))
            if not factors:
                factors.append(num)
            else:
                for factor in factors:
                    if num * factor == target_mul:
                        print('The two numbers are {} and {}'.format(num, factor))
                        found = True
                        break
                if not found:
                    factors.append(num)
        if found:
            break

    # print factors


def integers_problem_new(int_list, target_mul):
    factors = []
    for num in int_list:
        # print('value: {}'.format(num))
        if target_mul % num == 0:
            comp = target_mul / num
            # print('factor: {}'.format(num))
            if comp in factors:
                print('The two numbers are {} and {}'.format(num, comp))
                break
            factors.append(num)

    # print factors


if __name__ == "__main__":
    main()
else:
    print 'this module is being imported'

