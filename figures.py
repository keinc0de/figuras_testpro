class Line:
    def __init__(self, simbol:str):
        self.simbol = simbol

    def horizontal(self, num:int) -> str:
        return self.simbol * num
    
    def vertical(self, num:int) -> str:
        return f'{self.simbol}\n' * num
   

class Draw:
    def __init__(self, simbol='*'):
        self.line = Line(simbol=simbol)

