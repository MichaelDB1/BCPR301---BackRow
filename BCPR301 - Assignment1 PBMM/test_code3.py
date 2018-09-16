class D:
    pass


class F:
    pass


class E(D):
    def __init__(self, parameter=F()):
        self.attribute = parameter
        self.another = D()


def main():
    print(E(F()).attribute)


if __name__ == "__main__":
    main()
