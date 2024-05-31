class MealyError(Exception):
    pass


class MealyMachine:
    state = "A"

    TAG = {
        "A": ("B", 0),  # (next_state, return_value)
        "B": ("C", 2),
        "C": ("D", 3),
        "F": ("C", 10),
    }

    LINK = {
        "C": ("A", 4),  # (next_state, return_value)
        "D": ("A", 6),
        "E": ("F", 7),
        "F": ("H", 9),
    }

    CRAWL = {
        "A": ("E", 1),  # (next_state, return_value)
        "D": ("E", 5),
        "F": ("G", 8),
        "G": ("H", 11),
    }

    def set_next(self, attr: str):
        try:
            action = self.__getattribute__(attr)
            next_state = action[self.state]
            self.state = next_state[0]
            return next_state[1]
        except KeyError:
            raise MealyError(attr.lower())

    def tag(self):
        try:
            return self.set_next("TAG")
        except MealyError as e:
            raise e

    def link(self):
        try:
            return self.set_next("LINK")
        except MealyError as e:
            raise e

    def crawl(self):
        try:
            return self.set_next("CRAWL")
        except MealyError as e:
            raise e


def raises(function, error):
    output = None
    try:
        output = function()
    except Exception as e:
        assert type(e) is error
    assert output is None


def main():
    return MealyMachine()


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
