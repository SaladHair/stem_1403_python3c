"""
[Homework]
Date: 2021-11-27
Due date: 2021-12-03
Project: A power calculator in OOP
1. Design a calculator class and implement it in OOP
Requirements:
r1. The calculator should support conversion between numbers and words in English or French
Sample: 127
Expected result:  one hundred and twenty seven
r2. The calculator should support conversion among binary, hexadecimal, decimal
r3. The calculator should support arithmetic operation
r4. The calculator should support logical operation
2. Write a client app and use the calculator class
Requirements:
1. Write your own client app and use it.
2. Use another client app written by other programmers
"""


class Calculator:

    def __init__(self, mode="1"):
        self.mode = mode
        self.units = ["", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ",
                      "sextillion ", "septillion ", "octillion ", "nonillion "]
        self.ones = ["", "one ", "two ", "three ", 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ']
        self.tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.teens = ["", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ",
                      "eighteen ", "nineteen "]
        self.available_modes = ["1", "2"]

    def set_mode(self, new_mode):
        if new_mode in self.available_modes:
            self.mode = new_mode
            return f"Set mode to {new_mode}"
        else:
            return f"Tried to set mode to {new_mode} but failed because it isn't recognized as one of the modes: " \
                   f"current mode remains {self.mode} "

    def use_calc(self, term_1, term_1_mode, operation, term_2, term_2_mode):
        if self.mode == "1":
            return self.conversion(term_1_mode, operation, term_1)
        elif self.mode == "2":
            return eval(f"{int(term_1, int(term_1_mode))} {operation} {int(term_2, int(term_2_mode))}")

    def conversion(self, old_mode, new_mode, num_to_convert):
        if new_mode == "Words":
            return self.num_to_words(int(num_to_convert, int(old_mode)))
        elif new_mode == "2":
            return bin(int(num_to_convert, int(old_mode)))
        elif new_mode == "10":
            return int(num_to_convert, int(old_mode))
        elif new_mode == "16":
            return hex(int(num_to_convert, int(old_mode)))

    def num_to_words(self, raw_input_str):
        next_num = ""
        next_word = ""
        output = ""
        input_str = str(int(raw_input_str))
        if input_str == "0":
            return "zero"
        for i in range(len(input_str)):
            if i % 3 == 0:
                if i == len(input_str)-1:
                    output = self.ones[int(input_str[-i - 1])] + self.units[int(i/3)] + output
                    next_word = self.ones[int(input_str[-i - 1])]
                    next_num = input_str[-i - 1]
                else:
                    if input_str[-i-1] != "0" or input_str[-i-2] != "0" or input_str[-i-3] != "0":
                        output = self.units[int(i/3)] + output
                        next_word = self.ones[int(input_str[-i - 1])]
                        next_num = input_str[-i - 1]

            elif i % 3 == 1:
                if input_str[-i-1] == "1":
                    if next_word != "":
                        output = self.teens[int(next_num)] + output
                        next_word = self.teens[int(next_num)]
                    else:
                        output = "ten " + output
                elif input_str[-i-1] == "0":
                    output = self.ones[int(input_str[-i])] + output
                    next_word = ""
                else:
                    if input_str[-i] != "0":
                        output = self.tens[int(input_str[-i-1])] + "-" + self.ones[int(input_str[-i])] + output
                        next_word = self.tens[int(input_str[-i-1])]
                    else:
                        output = self.tens[int(input_str[-i-1])] + " " + output
                        next_word = self.tens[int(input_str[-i-1])]
            else:
                if input_str[-i-1] != "0":
                    if next_word == "" and input_str[-i+1] == "0":
                        output = self.ones[int(input_str[-i-1])] + "hundred " + output
                    else:
                        output = self.ones[int(input_str[-i-1])] + "hundred and " + output
        return output


# main program
calculator_1 = Calculator()
print(calculator_1.set_mode(input("Please input the mode you would like to enter (1 for conversion between writing "
                                  "modes, 2 for arithmetic operations): ")))
print(calculator_1.use_calc(input("Please enter a the first number of the operation: "),
                            input("Please enter the writing mode the number you wrote is in (Write the base, 16 for "
                                  "hex, 10 for dec and so on): "),
                            input("Please enter the operation you wish to perform (For conversion, simply enter the "
                                  "base you wish to convert to, or 'Words' to convert into letters.)"),
                            input("Please enter a the second number of the operation (Press enter if you are "
                                  "converting): "),
                            input("Please enter the writing mode the number you wrote is in (Ignore if you are "
                                  "converting): ")
                            ))
