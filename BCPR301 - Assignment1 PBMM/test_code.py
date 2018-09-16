class A:
    pass


class C:
    pass


class B(A):
    def __init__(self, parameter=C()):
        self.attribute = parameter
        self.another = A()


def main():
    print(B(C()).attribute)


if __name__ == "__main__":
    main()
