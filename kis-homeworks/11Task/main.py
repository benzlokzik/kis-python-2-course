class MealyError(Exception):
    pass


class MealyMachine:
    def __init__(self):
        self.state = "A"

    def tag(self):
        if self.state == "A":
            self.state = "B"
            return 0
        elif self.state == "B":
            self.state = "C"
            return 2
        elif self.state == "C":
            self.state = "D"
            return 3
        elif self.state == "F":
            self.state = "C"
            return 10
        else:
            raise MealyError("tag")

    def link(self):
        if self.state == "B":
            self.state = "C"
            return 6
        elif self.state == "C":
            self.state = "A"
            return 4
        elif self.state == "D":
            self.state = "A"
            return 6
        elif self.state == "E":
            self.state = "F"
            return 7
        elif self.state == "F":
            self.state = "H"
            return 9
        else:
            raise MealyError("link")

    def crawl(self):
        if self.state == "A":
            self.state = "E"
            return 1
        elif self.state == "D":
            self.state = "E"
            return 5
        elif self.state == "F":
            self.state = "G"
            return 8
        elif self.state == "G":
            self.state = "H"
            return 11
        else:
            raise MealyError("crawl")


def main():
    return MealyMachine()


def raises(function, error):
    output = None
    try:
        output = function()
    except Exception as e:
        assert type(e) is error
    assert output is None


def test():
    o = main()
    assert o.state == "A"
    assert o.tag() == 0  # A -> B
    assert o.state == "B"
    assert o.link() == 6  # B -> C
    assert o.state == "C"
    assert o.link() == 4  # C -> A
    assert o.state == "A"
    assert o.crawl() == 1  # A -> E
    assert o.state == "E"
    raises(lambda: o.crawl(), MealyError)  # E has no 'crawl'
    raises(lambda: o.tag(), MealyError)  # E has no 'tag'
    assert o.link() == 7  # E -> F

    o = main()  # reset
    assert o.tag() == 0  # A -> B
    assert o.state == "B"
    assert o.tag() == 2  # B -> C
    assert o.state == "C"
    assert o.tag() == 3  # C -> D
    assert o.state == "D"
    raises(lambda: o.tag(), MealyError)  # D has no 'tag'
    assert o.link() == 6  # D -> A
    o.state = "D"
    assert o.crawl() == 5  # D -> E
    assert o.state == "E"

    o = main()
    o.crawl()  # A -> E
    o = main()
    o.tag()  # A -> B
    o.tag()  # B -> C
    o.tag()  # C -> D
    assert o.crawl() == 5  # D -> E
    assert o.state == "E"
    raises(lambda: o.tag(), MealyError)  # E has no 'tag'
    raises(lambda: o.crawl(), MealyError)  # E has no 'crawl'

    # Testing transitions involving states F, G, and H
    o = main()
    o.crawl()  # A -> E
    o.state = "F"  # Simulate state F
    assert o.tag() == 10  # F -> C
    assert o.state == "C"
    o.state = "F"  # Simulate state F
    assert o.link() == 9  # F -> H
    assert o.state == "H"
    o.state = "F"  # Simulate state F
    assert o.crawl() == 8  # F -> G
    assert o.state == "G"
    assert o.crawl() == 11  # G -> H
    assert o.state == "H"

    # Testing error transitions
    raises(lambda: o.tag(), MealyError)  # H has no 'tag'
    raises(lambda: o.link(), MealyError)  # H has no 'link'
    raises(lambda: o.crawl(), MealyError)  # H has no 'crawl'

    # Additional test cases to cover all possible transitions
    o = main()
    assert o.crawl() == 1  # A -> E
    assert o.state == "E"
    assert o.link() == 7  # E -> F
    assert o.state == "F"
    assert o.tag() == 10  # F -> C
    assert o.state == "C"
    assert o.tag() == 3  # C -> D
    assert o.state == "D"
    assert o.crawl() == 5  # D -> E
    assert o.state == "E"
    raises(lambda: o.tag(), MealyError)  # E has no 'tag'
    raises(lambda: o.crawl(), MealyError)  # E has no 'crawl'
    assert o.link() == 7  # E -> F
    assert o.state == "F"
    assert o.link() == 9  # F -> H
    assert o.state == "H"
    raises(lambda: o.tag(), MealyError)  # H has no 'tag'
    raises(lambda: o.link(), MealyError)  # H has no 'link'
    raises(lambda: o.crawl(), MealyError)  # H has no 'crawl'


test()

[
    "link",
    "crawl",
    "crawl",
    "link",
    "tag",
    "tag",
    "link",
    "tag",
    "link",
    "tag",
    "link",
    "link",
    "crawl",
    "link",
    "crawl",
    "crawl",
]

a = main()
#
# print(a.link())
# print(a.crawl())
# print(a.crawl())
# print(a.link())
# print(a.tag())
# print(a.tag())
# print(a.link())
# print(a.tag())
# print(a.link())
# print(a.tag())
# print(a.link())
# print(a.link())
# print(a.crawl())
# print(a.link())
# print(a.crawl())
# print(a.crawl())
