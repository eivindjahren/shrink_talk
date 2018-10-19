import numpy as np
class SuperCalculate:
    def __init__(self, df):
        np.seterr(all='raise')
        self.df = df.copy()
        if 'greenhouse' in self.df.columns and self.df.index.any():
            self.df['greenhouse'].iloc[-1] = 0
