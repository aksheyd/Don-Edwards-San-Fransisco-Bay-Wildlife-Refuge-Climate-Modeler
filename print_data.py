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
print(bs_df[["Common Name", "Scientific Name", "Danger Level"]].head())
print("Max Danger Level for Birds = ", bs_df["Danger Level"].max())
print("Min Danger Level for Birds = ", bs_df["Danger Level"].min())
print("Average Danger Level for Birds = ", bs_df["Danger Level"].mean())
print("Amount of Birds = ", len(bs_df))
os.remove("output_birds.csv")

m_df = pd.read_csv(r'/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/output_mammals.csv')
m_df = m_df[:29] 
print("Mammals: ")
print("======== ")
print()
print(m_df[["Common Name", "Scientific Name", "Danger Level"]].head())
print("Max Danger Level for Mammals = ", m_df["Danger Level"].max())
print("Min Danger Level for Mammals = ", m_df["Danger Level"].min())
print("Average Danger Level for Mammals = ", m_df["Danger Level"].mean())
print("Amount of Mammals = ", len(m_df))
os.remove("output_mammals.csv")
# ADD COLUMNS AND ROW INFO

