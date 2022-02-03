#!/usr/bin/python3

import pandas as pd
import io
import json

bs_df = pd.read_csv (r'/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/BirdSheet.csv')
bs_df = bs_df[:270] 

#converts Occurrence column into string for if statements in DangerLevel func
bs_df["Occurrence"] = bs_df["Occurrence"].astype(str)

def DangerLevel (row1):
    try:
        returnVal = 0

        # Checks danger vals based on if the bird nests locally or accidentally came
        if (row1["Occurrence"] == "nests locally"):
            returnVal += 1
        elif (row1["Occurrence"] == "nan"):
            returnVal += 0
        elif (row1["Occurrence"] == "accidental"):
            returnVal += 2

        
        return returnVal
    except: 
        return 100

# Creates Danger Level column
bs_df.insert(len(bs_df.columns), 'Danger Level', 0)

# Iterates through rows to calculate Danger Level
bs_df['Danger Level'] = bs_df.apply(lambda row1: DangerLevel(row1), axis = 1)

print(bs_df)