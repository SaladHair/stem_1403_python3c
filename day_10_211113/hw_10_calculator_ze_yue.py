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

units = {0: "", 3: "thousand ", 6: "million ", 9: "billion ", 12: "trillion ", 15: "quadrillion ", 18: "quintillion ", 21: "sextillion ", 24: "septillion ", 27: "octillion ", 30: "nonillion "}
ones = ["", "one ", "two ", "three ", 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ']
tens = {0: "", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
teens = {11: "eleven ", 12: "twelve ", 13: "thirteen ", 14: "fourteen ", 15: "fifteen ", 16: "sixteen ", 17: "seventeen ", 18: "eighteen ", 19: "nineteen "}


class Calculator:
    def __init__(self, name):
        self.name = name

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
                    output = ones[int(input_str[-i - 1])] + units[i] + output
                    next_word = ones[int(input_str[-i - 1])]
                    next_num = input_str[-i - 1]
                else:
                    if input_str[-i-1] != "0" or input_str[-i-2] != "0" or input_str[-i-3] != "0":
                        output = units[i] + output
                        next_word = ones[int(input_str[-i - 1])]
                        next_num = input_str[-i - 1]

            elif i % 3 == 1:
                if input_str[-i-1] == "1":
                    if next_word != "":
                        output = teens[int(input_str[-i-1] + next_num)] + output
                        next_word = teens[int(input_str[-i-1] + next_num)]
                    else:
                        output = "ten " + output
                elif input_str[-i-1] == "0":
                    output = ones[int(input_str[-i])] + output
                    next_word = ""
                else:
                    if input_str[-i] != "0":
                        output = tens[int(input_str[-i-1])] + "-" + ones[int(input_str[-i])] + output
                        next_word = tens[int(input_str[-i-1])]
                    else:
                        output = tens[int(input_str[-i-1])] + " " + output
                        next_word = tens[int(input_str[-i-1])]
            else:
                if input_str[-i-1] != "0":
                    if next_word == "" and input_str[-i+1] == "0":
                        output = ones[int(input_str[-i-1])] + "hundred " + output
                    else:
                        output = ones[int(input_str[-i-1])] + "hundred and " + output
        return output


# main program
calculator_1 = Calculator("Albert")
print(calculator_1.num_to_words(input("Please enter a number that will be converted to words: ")))

