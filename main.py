
import tkinter
import customtkinter
from seleniumBot import Bot

class ControllPanel:
    def __init__(self):
        try:
            self.bot = Bot()
            self.root_tk = tkinter.Tk()
            self.root_tk.geometry("500x500")
            self.root_tk.title("Discord bot")
            customtkinter.set_appearance_mode("System")
            self.CountDrivers()
            self.Start()
            self.CreateButtonLogIn()
            self.CreateButtonTryAgain()
            self.CreateButtonOpenBox()
            self.CreateButtonAutoOpen()
            self.root_tk.mainloop()
        finally:
            self.bot.End()

    def _sliderEvent(self, value):
        count = int(1 + value // 0.125)

        self.sliderLabel.configure(text=count)
        self.bot.countDrivers = count
    def CountDrivers(self):
        sliderFrame = customtkinter.CTkFrame(master=self.root_tk,
                                                width=200,
                                                height=70)

        sliderFrame.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        self.sliderLabel = customtkinter.CTkLabel(master=sliderFrame,
                                                text="1")

        self.sliderLabel.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)
        slider = customtkinter.CTkSlider(master=sliderFrame,
                                           width=200,
                                           height=16,
                                           border_width=5.5,
                                           command=self._sliderEvent)
        #Встановлення положення слайдера при ініціалізації
        slider.set(0.125 * (1 - 3))
        slider.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
    def Start(self):
        button = customtkinter.CTkButton(master=self.root_tk,
                                         text="Start",
                                         command=self.bot.CreateDrivers,
                                         width=120,
                                         height=32,
                                         border_width=0,
                                         corner_radius=8)
        button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
    def CreateButtonLogIn(self):
        button = customtkinter.CTkButton(master=self.root_tk,
                                         text="Log in",
                                         command=self.bot.LogIn,
                                         width=120,
                                         height=32,
                                         border_width=0,
                                         corner_radius=8)
        button.place(relx=0.35, rely=0.4, anchor=tkinter.CENTER)

    def CreateButtonTryAgain(self):
        button = customtkinter.CTkButton(master=self.root_tk,
                                         text="Try Again",
                                         command=self.bot.TryAgain,
                                         width=120,
                                         height=32,
                                         border_width=0,
                                         corner_radius=8)
        button.place(relx=0.65, rely=0.4, anchor=tkinter.CENTER)

    def CreateButtonOpenBox(self):
        button = customtkinter.CTkButton(master=self.root_tk,
                                         text="Open Box",
                                         command=self.bot.OpenBox,
                                         width=120,
                                         height=32,
                                         border_width=0,
                                         corner_radius=8)
        button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    def _buttonHanddle(self):
        self.buttonBool = not self.buttonBool
        self.button.configure(fg_color='#53ec53' if self.buttonBool  else  '#ec5353')
        self._buttonPressed()

    def _buttonPressed(self):
        if self.buttonBool:
            self.bot.AutoOpen()
            self.button.after(500, self._buttonPressed)
    def CreateButtonAutoOpen(self):
        self.buttonBool = False
        self.button = customtkinter.CTkButton(master=self.root_tk,
                                         text="Auto open",
                                         command=self._buttonHanddle,
                                         width=120,
                                         height=32,
                                         border_width=0,
                                         fg_color= '#ec5353',
                                         corner_radius=8)
        self.button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

def main():
    ControllPanel()

if __name__ == "__main__":
    main()
