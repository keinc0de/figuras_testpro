class Line:
    def __init__(self, simbol:str):
        self.simbol = simbol

    def horizontal(self, num:int) -> str:
        return self.simbol * num
   

class Draw:
    def __init__(self, simbol='*'):
        self.line = Line(simbol=simbol)

