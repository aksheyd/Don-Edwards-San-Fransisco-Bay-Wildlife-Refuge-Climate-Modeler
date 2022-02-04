#!/usr/bin/python3

import pandas as pd
import io
import json

# Adds command line arguements to take in input for climate
import argparse
parser = argparse.ArgumentParser(description='Analyzer for data')
parser.add_argument("-p", "--print_string", help="Takes in the supplied argument for calculation.", nargs='*')
args = parser.parse_args()
print(args.print_string)

bs_df = pd.read_csv (r'/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/BirdSheet.csv')
bs_df = bs_df[:270] 

#converts Occurrence column into string for if statements in DangerLevel func
bs_df["Occurrence"] = bs_df["Occurrence"].astype(str)
bs_df["Classification"] = bs_df["Classification"].astype(str)
bs_df["Federal"] = bs_df["Federal"].astype(str)
bs_df["State"] = bs_df["State"].astype(str)

def DangerLevel (row1):
    returnVal = 0

    # Locally nested birds have acclimated to the climate better
    if (row1["Occurrence"] == "nests locally"):
        returnVal += 1
    # This is just an estimate between accidental occurring birds and locally nested
    elif (row1["Occurrence"] == "nan"):
        returnVal += 5
    # Accidental birds have no evolutionary acclimation to new climate and are more in danger
    elif (row1["Occurrence"] == "accidental"):
        returnVal += 10

    # Native birds, like locally nested, have better climate acclimation
    if (row1["Classification"] == "native"):
        returnVal += 1
    # Non Native birds are given higher danger because of above 
    elif (row1["Classification"] == "non-native"):
        returnVal += 5

    # Endangered species are close to extinction on a Federal level
    if (row1["Federal"] == "E"):
        returnVal += 50
    # Threatened species are close to becoming endangered
    elif (row1["Federal"] == "T"):
        returnVal += 25
    
    # Every state endangered species is also federally endangered
    if (row1["State"] == "E"):
        returnVal += 0
    # Threatened species are close to becoming endangered
    elif (row1["State"] == "T"):
        returnVal += 25
    # SSC (Species of Special Concern) is a CA specific classification for threatened and declining population species
    elif (row1["State"] == "SSC"):
        returnVal += 50
    # SP means State Protected 
    elif (row1["State"] == "SP"):
        return 0
    
    return returnVal

# Creates Danger Level column
bs_df.insert(len(bs_df.columns), 'Danger Level', 0)

# Iterates through rows to calculate Danger Level
bs_df['Danger Level'] = bs_df.apply(lambda row1: DangerLevel(row1), axis = 1)

bs_df.to_csv("output_birds.csv", index = False)
#print(bs_df)