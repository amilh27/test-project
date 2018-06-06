class Animal:
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


class RevStr(str):
    def __str__(self):
        return self[::-1]


class NewAnimal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meaow'

    def type(self, t=None):
        if t:
            self._type = t
        return self._type

    def name(self, n=None):
        if n:
            self._name = n
        return self._name

    def sound(self, s=None):
        if s:
            self._sound = s
        return self._sound

    def __str__(self):
        return 'The {} is named {} and says {}'.format(self.type(), self.name(), self.sound())


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def name(self):
        return self._name

    def salary(self):
        return self._salary


def print_animal(animal):
    if not isinstance(animal, Animal):
        raise TypeError('The animal parameter is not of type Animal: Type: {}'.format(type(animal)))
    print('The {} is named {} and says {}'.format(animal.type(), animal.name(), animal.sound()))


def main():
    a1 = Animal('kitten', 'fluffy', 'meaow')
    a2 = Animal('donald', 'duck', 'quack')
    print_animal(a1)
    print_animal(a2)
    print_animal(Animal('dinosaur', 'denver', 'roarr'))
    # print_animal(Employee('Amil', 80000))
    na = NewAnimal(sound='Cluck', type='Chicken', name='Hanna')
    print(na)
    # print('Type: {} Name: {} Sound: {}'.format(na.type(), na.name(), na.sound()))
    hello = RevStr('hello world.')
    print(hello)


if __name__ == '__main__':
    try:
        main()
    except TypeError:
        print('Error'.format())


