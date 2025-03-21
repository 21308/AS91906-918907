from tkinter import *
from functools import partial # To prevent unwanted windows

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
        DisplayHelp(self)



class DisplayHelp:

    def __init__(self, partner):

        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_button.config(state=DISABLED)

        self.help_frame = Frame(self.help_box, width=300,
                            height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                    text="Help / Info",
                                    font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the temperature " \
                    "you wish to convert and then choose to convert " \
                    "to either degrees Celsius (centigrade) or " \
                    "Fahrenheit... \n\n" \
                    " Note that -273 degrees C " \
                    "(-459 F) is absolute zero (the coldest possible " \
                    "temperature). If you try to convert a " \
                    "temperature that is less than -273 degrees C, " \
                    "you will get an error message. \n\n " \
                    "To see your " \
                    "calculation history and export it to a text " \
                    "file, please click the 'History / Export' button."     


        self.help_text_label = Label(self.help_frame,
                                 text=help_text, wraplength=350,
                                 justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                 font=("Arial", "12", "bold"), 
                                 text="Dismiss", bg="#CC6600",
                                 fg="#FFFFFF", 
                                 command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)


        # List and loop to set backgroudn colour on
        # everything except the buttons.
        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]
        
        for item in recolour_list:
            item.config(bg=background)


    def close_help(self, partner):
        partner.to_help_button.config(stae=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()