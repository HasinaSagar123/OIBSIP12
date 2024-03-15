from tkinter import *
from tkinter import ttk
from tkinter import messagebox

entries= []

class BMILabel:
    def _init_(self, root, labelText, row):
        self.label = ttk.Label(root, text=labelText, underline=0)
        self.label.grid(row=row, column=0, sticky='E', padx=10, pady=10)

class BMIEntry:
    def _init_(self, root, row):
        self.textVar = StringVar()
        self.entry = ttk.Entry(root, width=30, textvariable=self.textVar)
        self.entry.grid(row=row, column=1)

    def getText(self):
        return self.entry.get().strip()

    def clear(self):
        self.textVar.set("")
        self.entry.delete(0, END)

    def setRO(self):
        self.entry.config(state="readonly")

    def setText(self, text):
        self.clear()
        self.textVar.set(text)

    def focus(self):
        self.entry.focus_force()

    def _format_(self, __format_spec):
        return format(self.getText, __format_spec)


class BMIButton:
    def _init_(self, root, buttonText, sticky, shortCutIndex=0):
        self.button = ttk.Button(root, text=buttonText, padding=5)
        self.button.config(underline=shortCutIndex)
        self.button.grid(row=3, column=1, sticky=sticky, pady=10)

    def bind(self, func):
        self.button.config(command=func)

def addLabels(root):
    BMILabel(root, "Height (cm)", 0)
    BMILabel(root, "Weight (kg)", 1)
    BMILabel(root, "BMI", 2)


def addEntries(root):
    height = BMIEntry(root, 0)
    weight = BMIEntry(root, 1)
    bmi = BMIEntry(root, 2)
    bmi.setRO()
    entries.extend([height, weight, bmi])
    height.focus()


def addButtons(root):
    calculate = BMIButton(root, "Calculate BMI", 'E')
    calculate.bind(calculateBMI)
    clear = BMIButton(root, "Clear", 'W', shortCutIndex=1)
    clear .bind(handleClear)


def addShortCuts(root):
    root.bind("<Alt-h>", lambda _: entries[0].focus())
    root.bind("<Alt-w>", lambda _: entries[1].focus())
    root.bind("<Alt-c>", lambda _: calculateBMI())
    root.bind("<Alt-l>", lambda _: handleClear())  

def handleClear():
    for e in entries:
           e.clear()    


def calculateBMI():
      try:
          heightInCm = float(entries[0].getText())
          weightInKg = float(entries[1].getText())
          if not (0 < weightInKg < 1000):
            raise
          if not (0 < heightInCm < 300):
            raise
      except:
        messagebox.showerror("Invalid Input", "Entered input is invalid")
        return

      bmiValue = (weightInKg/ (heightInCm / 100) ** 2)
      bmi = entries[2]
      bmi.setText(f"{bmiValue:.1f} - {getBMIRange(bmiValue)}")


def getBMIRange(bmiValue):
     if 0.0 < bmiValue < 18.5:
        return "Underweight"
     if 18.5 <= bmiValue < 25.0:
        return "Normal"
     if 25.0 <= bmiValue < 30.0:
        return "Overweight"
     return "Obese"


def main():
     root = Tk()
     root.title("BMI Calculator")
     root.geometry("320x180")
     root.resizable(False, False)

     addLabels(root)
     addEntries(root)
     addButtons(root)
     addShortCuts(root)
    
     root.mainloop()

if __name__=="_main_":
   main()
