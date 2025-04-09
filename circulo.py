class Circulo:
    PI = 3.14159
    def __init__(self, radio):
        self.radio = radio

    def circunferencia(self):
        return 2*self.PI*self.radio

    def area(self):
        return self.PI * self.radio * self.radio


if __name__ == "__main__":
    inst_circulo = Circulo(10)
    print(f"La circunferencia es: {inst_circulo.circunferencia()}")