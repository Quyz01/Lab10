from dataclasses import dataclass

@dataclass
class Paese:
    StateAbb: str
    CCode: int
    StateNme: str

    @property
    def stateAbb(self):
        return self.StateAbb

    @property
    def cCode(self):
        return self.CCode

    @property
    def stateName(self):
        return self.StateNme

    def __hash__(self):
        return self.StateAbb

    def __str__(self):
        return f"Paese: {self.StateNme} ({self.StateAbb})"