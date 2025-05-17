def test_uno() -> str:
    return 'resultado uno (1)'

def escribe(text:str):
    with open ('salida_test.txt', 'w') as file:
        file.write(text)

if __name__ == '__main__':
    escribe(test_uno())
