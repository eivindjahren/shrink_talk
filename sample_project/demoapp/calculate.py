from .super_calculate import SuperCalculate
import pandas as pd

class Calculate(SuperCalculate):
    def calculate(self):
        return pd.DataFrame([self.df[column1] / self.df[column2] for column1, column2 in zip(self.df.columns, self.df.columns)])
