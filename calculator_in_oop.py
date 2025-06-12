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
    def __init__(self):
        self.first_operand = 0.0
        self.second_operand = 0.0
        self.current_operation = None
        self.is_new_input = True

    def set_operation(self, operation_instance):
        self.current_operation = operation_instance

    def calculate_result(self, second_operand):
        if self.current_operation is None:
            return second_operand
        result = self.current_operation.calculate(self.first_operand, second_operand)
        self.clear()
        return result

    def clear(self):
        self.first_operand = 0.0
        self.second_operand = 0.0
        self.current_operation = None
        self.is_new_input = True

class CalculatorApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("OOP Calculator")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
