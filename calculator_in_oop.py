import tkinter
from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def calculate(self, first_operand, second_operand):
        pass

class AdditionOperation(Operation):
    def calculate(self, first_operand, second_operand):
        return first_operand + second_operand

class SubtractionOperation(Operation):
    def calculate(self, first_operand, second_operand):
        return first_operand - second_operand

class MultiplicationOperation(Operation):
    def calculate(self, first_operand, second_operand):
        return first_operand * second_operand

class DivisionOperation(Operation):
    def calculate(self, first_operand, second_operand):
        if second_operand == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_operand / second_operand

class CalculatorEngine:
    pass

class CalculatorApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("OOP Calculator")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
