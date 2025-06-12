import tkinter
from abc import ABC, abstractmethod
import math

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
        self.resizable(False, False)

        self.color_light_gray = "#D4D4D2"
        self.color_black = "#1C1C1C"
        self.color_dark_gray = "#505050"
        self.color_orange = "#FF9500"
        self.color_white = "white"

        self.button_values = [
            ["AC", "+/-", "%", "÷"], 
            ["7", "8", "9", "×"], 
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "√", "="]
        ]

        self.current_input = "0"
        self.engine = CalculatorEngine()

        self.frame = tkinter.Frame(self)
        self.label = tkinter.Label(self.frame, text=self.current_input, font=("Arial", 45),
                                   background=self.color_black,
                                   foreground=self.color_white,
                                   anchor="e", width=4)
        self.label.grid(row=0, column=0, columnspan=4, sticky="we")

        for row_index, row in enumerate(self.button_values):
            for column_index, value in enumerate(row):
                button = tkinter.Button(self.frame, text=value, font=("Arial", 30),
                                         width=4, height=1,
                                         command=lambda v=value: self.on_button_click(v))
                if value in ["AC", "+/-", "%"]:
                    button.config(foreground=self.color_black, background=self.color_light_gray)
                elif value in ["÷", "×", "-", "+", "="]:
                    button.config(foreground=self.color_white, background=self.color_orange)
                else:
                    button.config(foreground=self.color_white, background=self.color_dark_gray)

                button.grid(row=row_index+1, column=column_index)

        self.frame.pack()

    def on_button_click(self, button_value):
        if button_value in "0123456789":
            if self.current_input == "0" or self.engine.is_new_input:
                self.current_input = button_value
                self.engine.is_new_input = False
            else:
                self.current_input += button_value
            self.label.config(text=self.current_input)

        elif button_value == ".":
            if "." not in self.current_input:
                self.current_input += "."
                self.label.config(text=self.current_input)

        elif button_value == "AC":
            self.current_input = "0"
            self.engine.clear()
            self.label.config(text=self.current_input)

        elif button_value == "+/-":
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                if self.current_input != "0":
                    self.current_input = "-" + self.current_input
            self.label.config(text=self.current_input)

        elif button_value == "%":
            value = float(self.current_input) / 100
            if value.is_integer():
                self.current_input = str(int(value))
            else:
                self.current_input = str(value)
            self.label.config(text=self.current_input)

        elif button_value in ["+", "-", "×", "÷"]:
            self.engine.first_operand = float(self.current_input)
            self.engine.is_new_input = True

            if button_value == "+":
                self.engine.set_operation(AdditionOperation())
            elif button_value == "-":
                self.engine.set_operation(SubtractionOperation())
            elif button_value == "×":
                self.engine.set_operation(MultiplicationOperation())
            elif button_value == "÷":
                self.engine.set_operation(DivisionOperation())

        elif button_value == "=":
            second_operand = float(self.current_input)
            result = self.engine.calculate_result(second_operand)
            if result.is_integer():
                self.current_input = str(int(result))
            else:
                self.current_input = str(result)
            self.label.config(text=self.current_input)
            self.engine.is_new_input = True

        elif button_value == "√":
            number = float(self.current_input)
            if number < 0:
                self.current_input = "Error"
            else:
                result = math.sqrt(number)
                if result.is_integer():
                    self.current_input = str(int(result))
                else:
                    self.current_input = str(result)
            self.label.config(text=self.current_input)
            self.engine.is_new_input = True

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
