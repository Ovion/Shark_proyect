import pandas as pd
import numpy as np
import re

def clean_last_ws (serie):
    return serie.replace("\s$", "")

