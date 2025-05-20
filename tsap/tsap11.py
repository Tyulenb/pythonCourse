class MooreMachine:
    def __init__(self):
        self.state = "U3"
        self.vs = {}
        self.seen = {"apply": 0, "show": 0, "shift": 0}

    def go(self, op):
        match op:
            case "apply":
                self.seen["apply"] += 1
                return self.apply()
            case "show":
                self.seen["show"] += 1
                return self.show()
            case "shift":
                self.seen["shift"] += 1
                return self.shift()
            case _:
                return "unknown"

    def apply(self):
        match self.state:
            case "U3":
                self.state = "U2"
            case "U2":
                self.state = "U1"
            case _:
                self.seen["apply"] -= 1
                return "unsupported"

    def show(self):
        match self.state:
            case "U1" if self.vs["n"] == 1:
                self.state = "U1"
            case "U1" if self.vs["n"] == 0:
                self.state = "U4"
            case "U4":
                self.state = "U0"
            case "U5":
                self.state = "U2"
            case _:
                self.seen["show"] -= 1
                return "unsupported"

    def shift(self):
        match self.state:
            case "U0":
                self.state = "U5"
            case "U4" if self.vs["b"] == 0:
                self.state = "U5"
            case "U4" if self.vs["b"] == 1:
                self.state = "U2"
            case _:
                self.seen["shift"] -= 1
                return "unsupported"

    def n(self, val):
        self.vs["n"] = val

    def b(self, val):
        self.vs["b"] = val

    def get_output(self):
        match self.state:
            case "U0":
                return "W1"
            case "U2" | "U4" | "U5":
                return "W0"
            case "U3" | "U1":
                return "W2"
            case _:
                return ""

    def seen_method(self, method):
        return self.seen[method]

    def part_of_loop(self):
        if self.state != "U3":
            return True
        else:
            return False


def main():
    moore = MooreMachine()
    return moore


def test():
    obj = main()
    assert obj.get_output() == "W2"
    assert obj.part_of_loop() is False
    assert obj.go("add") == "unknown"
    assert obj.go("shift") == "unsupported"
    assert obj.go("apply") is None
    assert obj.go("apply") is None
    assert obj.n(1) is None
    assert obj.go("show") is None
    assert obj.get_output() == "W2"
    assert obj.n(0) is None
    assert obj.go("show") is None
    assert obj.get_output() == "W0"
    assert obj.go("apply") == "unsupported"
    assert obj.b(1) is None
    assert obj.go("shift") is None
    assert obj.go("show") == "unsupported"
    assert obj.part_of_loop() is True
    assert obj.go("apply") is None
    assert obj.go("show") is None
    assert obj.go("show") is None
    assert obj.get_output() == "W1"
    assert obj.go("shift") is None
    assert obj.go("show") is None
    assert obj.seen_method("apply") == 3
    assert obj.go("apply") is None
    assert obj.go("show") is None
    assert obj.b(0) is None
    assert obj.go("shift") is None
    assert obj.seen_method("shift") == 3
    obj.state = "W1"
    assert obj.get_output() == ""


test()

