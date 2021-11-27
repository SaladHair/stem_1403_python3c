"""
[Homework]
Date: 2021-11-13
Due date: 2021-11-19
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
        self.available_modes = ["1"]

    def set_mode(self, new_mode=input("Please input the mode you would like to enter (1 for number to word "
                                      "conversion): ")):
        if new_mode in self.available_modes:
            self.mode = new_mode
        else:
            print(f"Tried to set mode to {new_mode} but failed because it isn't recognized as one of the modes: "
                  f"current mode remains {self.mode}")

    def use_calc(self, term_1, operation=None, term_2=None):
        if self.mode == "1":
            self.num_to_words(term_1)

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
calculator_1.set_mode()
print(calculator_1.use_calc(input("Please enter a number that will be converted to words: ")))

