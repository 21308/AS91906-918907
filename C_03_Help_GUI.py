from tkinter import *


class Converter:
    """"
    Temperature conversion tool
    """

    def __init__(self):




        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_help_button = Button(self.temp_frame,
                                 text="Help / Info",
                                 bg="#CC6600",
                                 fg="#FFFFFF",
                                 font=("Arial", "14", "bold"), width=12,
                                 command=self.to_help)
        self.to_help_button.grid(row=1, padx=5, pady=5)

    def to_help(self):
        print("You pushed the help button")





   # main routine
    if __name__ == "__main__":
     root = Tk()
     root.title("Temperature Converter")
     Converter()
     root.mainloop()