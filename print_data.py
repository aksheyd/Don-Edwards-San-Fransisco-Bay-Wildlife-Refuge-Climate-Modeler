#!/usr/bin/python3

import pandas as pd
import io
import json
import os

bs_df = pd.read_csv (r'/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/output_birds.csv')
bs_df = bs_df[:270] 
print("Birds: ")
print("======")
print()
print(bs_df)
print("Max Danger Level for Birds = ", bs_df["Danger Level"].max())
print("Min Danger Level for Birds = ", bs_df["Danger Level"].min())
print("Average Danger Level for Birds = ", bs_df["Danger Level"].mean())
os.remove("output_birds.csv")


