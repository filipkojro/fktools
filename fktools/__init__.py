try: from pip._internal.operations import freeze
except ImportError: # pip < 10.0
    from pip.operations import freeze

pkgs = freeze.freeze()

with open('autorequirements.txt', 'w') as f:
    for pkg in pkgs:
        f.write(f'{pkg}\n')

import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns