#!/usr/bin/python3

import pandas as pd
import io
import json
import math


# Adds command line arguements to take in input for climate
import argparse
parser = argparse.ArgumentParser(description='Analyzer for data')
parser.add_argument("-p", "--print_string", help="Takes in the supplied argument for calculation.", nargs='*')
args = parser.parse_args()
new_temp = int(args.print_string[0])
avg_temp_dfsb = 60
diff = avg_temp_dfsb - new_temp

# Calculates changes to danger level (see readme for explanation on how this works! - IN PROGRESS)
if (diff <= 11):
    changeVal = math.ceil(pow(1.2, diff) - 1)
if (diff > 11):
    changeVal = math.ceil(0.0032 * pow(diff - 35, 3) + 50)

#changeVal = math.ceil(pow(1.07977616, diff) - 1)
#changeVal = (5/3) * diff

# Birds CSV
bs_df = pd.read_csv (r'/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/BirdSheet.csv')
bs_df = bs_df[:270] 

# Mammals CSV
m_df = pd.read_csv (r'/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/MammalsSheet.csv')
m_df = m_df[:30] 

# Amphibians/Reptiles CSV
ar_df = pd.read_csv (r'/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/AmphibianReptilesSheet.csv')
ar_df = ar_df[:14] 

# Reptiles CSV
f_df = pd.read_csv (r'/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/FishsSheet.csv')
f_df = f_df[:58] 

#converts Occurrence column into string for if statements in DangerLevel func
bs_df["Occurrence"] = bs_df["Occurrence"].astype(str)
bs_df["Classification"] = bs_df["Classification"].astype(str)
bs_df["Federal"] = bs_df["Federal"].astype(str)
bs_df["State"] = bs_df["State"].astype(str)

m_df["Occurrence"] = m_df["Occurrence"].astype(str)
m_df["Classification"] = m_df["Classification"].astype(str)
m_df["Federal"] = m_df["Federal"].astype(str)
m_df["State"] = m_df["State"].astype(str)

ar_df["Occurrence"] = ar_df["Occurrence"].astype(str)
ar_df["Classification"] = ar_df["Classification"].astype(str)
ar_df["Federal"] = ar_df["Federal"].astype(str)
ar_df["State"] = ar_df["State"].astype(str)

f_df["Occurrence"] = f_df["Occurrence"].astype(str)
f_df["Classification"] = f_df["Classification"].astype(str)
f_df["Federal"] = f_df["Federal"].astype(str)
f_df["State"] = f_df["State"].astype(str)

# Creates Danger Level column
bs_df.insert(len(bs_df.columns), 'Danger Level', 0)
m_df.insert(len(m_df.columns), 'Danger Level', 0)
ar_df.insert(len(ar_df.columns), 'Danger Level', 0)
f_df.insert(len(f_df.columns), 'Danger Level', 0)

def DangerLevel (row1):
    returnVal = changeVal

    # Locally nested birds have acclimated to the climate better
    if (row1["Occurrence"] == "nests locally"):
        returnVal += 1 
    # This is just an estimate between accidental occurring birds and locally nested
    elif (row1["Occurrence"] == "nan"):
        returnVal += 5
    # Accidental birds have no evolutionary acclimation to new climate and are more in danger
    elif (row1["Occurrence"] == "accidental"):
        returnVal += 10


    # Solo habitat lowers survival chance (LOOK INTO CHANGING CLIMATE BASED ON HABTIAT)
    if ((row1["Occurrence"] == "upland") or (row1["Occurrence"] == "marsh") or (row1["Occurrence"] == "tidal sloughs")):
        returnVal += 10
    # Multiple habitats means greater survival in more areas
    elif ((row1["Occurrence"] == "all habitats")):
        returnVal += 5


    # Solo habitat lower survival chance (LOOK INTO CHANGING CLIMATE BASED ON HABTIAT))
    if (row1["Occurrence"] == "present in tidal waters"):
        returnVal += 10
    # More habitats -> greater survival
    elif (row1["Occurrence"] == "present in tidal waters and ponds"):
        returnVal += 5
    # Rare occurence means lower population and lower survival
    elif (row1["Occurrence"] == "rare in tidal waters"):
        returnVal += 20


    # Native species, like locally nested, have better climate acclimation
    if (row1["Classification"] == "native"):
        returnVal += 1
    # Non Native species are given higher danger because of above 
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
    # SSC/SC (Species of Special Concern) is a CA specific classification for threatened and declining population species
    elif (row1["State"] == "SSC") or (row1["State"] == "SC"):
        returnVal += 50
    # SP means State Protected 
    elif ((row1["State"] == "SP") or (row1["State"] == "FP")):
        return 0

    return returnVal

if (new_temp == avg_temp_dfsb):
    changeVal = 0

    # Iterates through rows to calculate Danger Level
    bs_df['Danger Level'] = bs_df.apply(lambda row1: DangerLevel(row1), axis = 1)
    m_df['Danger Level'] = m_df.apply(lambda row1: DangerLevel(row1), axis = 1)
    ar_df['Danger Level'] = ar_df.apply(lambda row1: DangerLevel(row1), axis = 1)
    f_df['Danger Level'] = f_df.apply(lambda row1: DangerLevel(row1), axis = 1)

    # Turns all datasets into csv files
    bs_df.to_csv("output_birds.csv", index = False)
    m_df.to_csv("output_mammals.csv", index = False)
    ar_df.to_csv("output_amphibianreptiles.csv", index = False)
    f_df.to_csv("output_fishs.csv", index = False)
else:
    # Iterates through rows to calculate Danger Level
    bs_df['Danger Level'] = bs_df.apply(lambda row1: DangerLevel(row1), axis = 1)
    m_df['Danger Level'] = m_df.apply(lambda row1: DangerLevel(row1), axis = 1)
    ar_df['Danger Level'] = ar_df.apply(lambda row1: DangerLevel(row1), axis = 1)
    f_df['Danger Level'] = f_df.apply(lambda row1: DangerLevel(row1), axis = 1)

    # Turns all datasets into csv files
    bs_df.to_csv("output_birds.csv", index = False)
    m_df.to_csv("output_mammals.csv", index = False)
    ar_df.to_csv("output_amphibianreptiles.csv", index = False)
    f_df.to_csv("output_fishs.csv", index = False)
