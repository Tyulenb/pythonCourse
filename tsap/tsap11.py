class MooreMachine:
    def __init__(self):
        self.state = "d0"
        self.vs = {}

    def apply(self):
        match self.state:
            case "U3":
                self.state = "U2"
            case "U2":
                self.state = "U1"

    def show(self):
        match self.state:
            case "U1" if self.vs[n] == 1:
                self.state = "U1"
            case "U1" if self.vs[n] == 0:
                self.state = "U4"
            case "U4":
                self.state = "U0"
            case "U5":
                self.state = "U2"

    def shift(self):
        match self.state:
            case "U0":
                self.state = "U5"
            case "U4" if self.vs[b] == 0:
                self.state = "U5"
            case "U4" if self.vs[b] == 1:
                self.state = "U2"

    def set_var(self, var, val):
        self.vs[var] = val

    def get_output(self):
        match self.state:
            case "d0" | "d2" | "d3":
                return "F1"
            case "d1" | "d4":
                return "F3"
            case "d5":
                return "F2"

    def __getattr__(self, name):
        return lambda: "unknown"
