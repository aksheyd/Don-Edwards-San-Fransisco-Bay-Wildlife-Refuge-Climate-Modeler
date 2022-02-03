#!/usr/bin/python3

import pandas as pd
import io
import json

bs_df = pd.read_csv (r'/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/BirdSheet.csv')
bs_df = bs_df[:270]
print(bs_df)