from tkinter import *
from functions.functions import *
class Page(Tk):

    def __init__(self):
        super().__init__()
        # self.frame = Frame(self)


        self.temperature = IntVar()

        self.result = StringVar()

        self.input_field = Entry(self, font=('Times New Roman', 15, 'bold'), justify=CENTER,
                                 textvariable=self.temperature)

        # vcmd = (self.register(self.__valid_data), '%P')
        # self.input_field.config(validate='focusout', validatecommand=vcmd)

        self.to_celsius_button = Button(self, text="Fahrenheit to Celsius", command=self.__convert_to_celsius)
        self.to_farenheit_button = Button(self, text="Celsius to Fahrenheit", command=self.__convert_to_fahrenheit)
        self.result_label = Label(self, textvariable=self.result)

        self.__display_form()

    def __display_form(self):

        self.input_field.pack(ipadx=20, ipady=20,fill=BOTH, expand=True)
        self.to_celsius_button.pack(ipadx=20, ipady=20,fill=BOTH, expand=True)
        self.to_farenheit_button.pack(ipadx=20, ipady=20,fill=BOTH, expand=True)
        self.result_label.pack(ipadx=20, ipady=20,fill=BOTH, expand=True)

    def __convert_to_celsius(self):
        value = self.temperature.get()
        self.temperature.set(value)
        celsius = round((value - 32) * (5/9))
        self.result.set(str(celsius))

    def __convert_to_fahrenheit(self):
        value = self.temperature.get()
        self.temperature.set(value)
        fahrenheit =round((value * 9/5) + 32)
        self.result.set(str(fahrenheit))

    # def __in_valid_data(self):
    #     print("invalid data")
    # def __valid_data(self,value):
    #     print("valid data")
    #     if format_number(value)==0:
    #         self.temperature.set(0)
    #         return False
    #     return True