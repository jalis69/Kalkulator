"""Empty """
class Calculator:
    """Kalkulator dwóch liczb."""
 
    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2
 
    def sum(self) -> float:
        """Dodawanie."""
        return self.op1 + self.op2
 
    def sub(self) -> float:
        """Odejmowanie."""
        return self.op1 - self.op2
 
    def mul(self) -> float:
        """Mnożenie."""
        return self.op1 * self.op2
 
    def div(self) -> float:
        """Dzielenie z kontrolą dzielenia przez zero."""
        if self.op2 == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero.")
        return self.op1 / self.op2
 
 
if __name__ == "__main__":
    calc = Calculator(5, 2)
    print("Dodawanie:", calc.sum())
    print("Odejmowanie:", calc.sub())
    print("Dzielenie:", calc.div())
    print("Mnozenie:", calc.mul())
 
    # Przykład bezpiecznej obsługi dzielenia przez zero
    try:
        print("Dzielenie przez zero:", Calculator(5, 0).div())
    except ZeroDivisionError as error:
        print("Błąd:", error)