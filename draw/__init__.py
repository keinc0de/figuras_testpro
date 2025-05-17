class Line:
    def __init__(self, simbol='*'):
        self.simbol = simbol

    def horizontal(self, num:int) -> str:
        return self.simbol * num
    
