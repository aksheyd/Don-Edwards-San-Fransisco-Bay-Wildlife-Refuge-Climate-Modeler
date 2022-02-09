#!/usr/bin/python3

import pandas as pd
import io
import json
import os

bs_df = pd.read_csv (r'/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/output_birds.csv')
bs_df = bs_df[:270] 
print("Birds: ")
print("======")
print(bs_df[["Common Name", "Scientific Name", "Danger Level"]].head())
print("Max Danger Level for Birds = ", bs_df["Danger Level"].max())
print("Min Danger Level for Birds = ", bs_df["Danger Level"].min())
print("Average Danger Level for Birds = ", "{:.2f}".format(bs_df["Danger Level"].mean()))
print("Amount of Birds = ", len(bs_df))
os.remove("output_birds.csv")
print()

m_df = pd.read_csv(r'/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/output_mammals.csv')
m_df = m_df[:29] 
print("Mammals: ")
print("======== ")
print(m_df[["Common Name", "Scientific Name", "Danger Level"]].head())
print("Max Danger Level for Mammals = ", m_df["Danger Level"].max())
print("Min Danger Level for Mammals = ", m_df["Danger Level"].min())
print("Average Danger Level for Mammals = ", "{:.2f}".format(m_df["Danger Level"].mean()))
print("Amount of Mammals = ", len(m_df))
os.remove("output_mammals.csv")
print()

ar_df = pd.read_csv(r'/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/output_amphibianreptiles.csv')
ar_df = ar_df[:14] 
print("Amphibians/Reptiles: ")
print("==================== ")
print(ar_df[["Common Name", "Scientific Name", "Danger Level"]].head())
print("Max Danger Level for A/R = ", m_df["Danger Level"].max())
print("Min Danger Level for A/R = ", m_df["Danger Level"].min())
print("Average Danger Level for A/R = ", "{:.2f}".format(ar_df["Danger Level"].mean()))
print("Amount of A/R = ", len(ar_df))
os.remove("output_amphibianreptiles.csv")
print()

f_df = pd.read_csv(r'/Users/aksheydeokule/Documents/EcoData S2/Climate Modeler/output_fishs.csv')
f_df = f_df[:58] 
print("Fish: ")
print("===== ")
print(f_df[["Common Name", "Scientific Name", "Danger Level"]].head())
print("Max Danger Level for Fish = ", f_df["Danger Level"].max())
print("Min Danger Level for Fish = ", f_df["Danger Level"].min())
print("Average Danger Level for Fish = ", "{:.2f}".format(f_df["Danger Level"].mean()))
print("Amount of Fish = ", len(f_df))
os.remove("output_fishs.csv")
print() 