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
        if self.state == "C":
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
    m = main()
    assert m.tag() == 0
    assert m.tag() == 2
    assert m.link() == 4
    raises(lambda: m.link(), MealyError)
    assert m.crawl() == 1
    raises(lambda: m.tag(), MealyError)
    assert m.link() == 7
    assert m.tag() == 10
    assert m.tag() == 3
    assert m.link() == 6
    assert m.crawl() == 1
    assert m.link() == 7
    assert m.tag() == 10
    assert m.tag() == 3
    assert m.crawl() == 5
    raises(lambda: m.tag(), MealyError)
    assert m.link() == 7
    assert m.crawl() == 8
    assert m.crawl() == 11
    raises(lambda: m.crawl(), MealyError)
    m.state = "F"
    assert m.link() == 9
