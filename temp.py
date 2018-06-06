student = {
    'name': 'Amilcar Hernandez',
    'grades': [78, 87, 88, 90, 95.5]
}


def fun(a, b, c):
    print '{} {} {}'.format(a, b, c)


def get_numbers():
    i = 0;
    while i < 100:
        yield i
        i += 1


def average(*args):
    '''
    :param args:
    :return:
    '''
    return sum(args) / len(args)


def main():
    g = get_numbers()
    print next(g)
    print next(g)

    obj = range(10)

    print obj

    # exit(0)

    avg1 = average(2, 4, 6)
    # Packing Example
    print avg1
    avg2 = average(10, 15, 20)
    print avg2

    my_list = ['you', 'are', 'good']

    fun(*my_list)

    d = {
        'Name': 'Amilcar Hernandez',
        'Age': 35,
        'Address': '1870 Lamplighter Way'
    }

    p = {
        'Hobby': 'Programming',
        'Language': 'Python'
    }

    for key in d:
        print 'key: {} - value: {}'.format(key, d[key])

    for value in d.itervalues():
        print value

    for key in d.iterkeys():
        print key

    for key, value in d.iteritems():
        print 'key: {} - value: {}'.format(key, value)

    if 'Address' in d:
        del d['Address']

    d.update(p)

    print 'update: {}'.format(d)

    d.clear()

    print d

    list_of_tuples = [('i', 1), ('j', 2), ('k', 3)]
    for k, v in list_of_tuples:
        print k, v

    set1 = {1, 3, 5, 7, 9, 9, 7}
    set2 = {1, 4, 5, 2, 7}
    print set1
    print type(set1)

    set3 = set1 | set2

    print set3

    set3.add(9)

    print set3

    set4 = {x for x in range(10) if x % 2 == 0}

    print set4
    if 10 in set4:
        set4.remove(10)
    print set4

    my_set = set([2, 4, 6, 9])
    print '{} - {}'.format(my_set, type(my_set))


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    def average(self):
        return sum(self.grades) / len(self.grades)

    def __len__(self):
        return len(self.grades)

    def __getitem__(self, item):
        return self.grades[item]

    def __str__(self):
        return 'Student with {} grades'.format(len(self))


class WorkingStudent(Student):

    def __init__(self, name, school, salary):
        super(Student, self).__init__(name, school)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 40


if __name__ == '__main__':
    main()



