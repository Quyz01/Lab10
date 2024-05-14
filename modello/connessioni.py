from dataclasses import dataclass

@dataclass
class Connessioni:
    state1no: int
    state1ab: str
    state2no: int
    state2ab: str
    year: int
    conttype: int

    @property
    def stateAbb1(self):
        return self.state1ab

    @property
    def stateAbb2(self):
        return self.state2ab

    @property
    def stateCod1(self):
        return self.state1no

    @property
    def stateCod2(self):
        return self.state2no

    @property
    def year(self):
        return self.year

    @property
    def conttype(self):
        return self.conttype

    def __hash__(self):
        return self.state1no, self.state2no