Michigan EcoData: Don Edwards San Fransisco Bay Wildlife Refuge Climate Modeler
===============================================================================
By Akshey Deokule <aksheyd@umich.edu>

# Introduction
This project is a Climate Modeler for the DESFB, a wildlife refuge 5 minutes away from my home in Fremont, CA which I frequent, using US Wildlife & Refuge data on the park's numerous species. I used C++ for the user environment and Python (Pandas) for the data analysis, sorting, and calculations of the danger level of species depending on the climate variables given.

The calculations are (for now) based on a single variable called DangerValue which is changed depending on classifications of the species given and when it hits a 100 depending on what is changed in the climate modeler, that species is considered extinct in the model. There are many variables which truly affect a ecosystem, and so this is a very simple attempt to try and replicate that. I intend to add more variables in the future.

# Get Started
###### Disclaimer: This project is *NOT* intended to be heavily scientific. The calculations done on the ecosystem's survivability are loosely based on scientific articles and journals (even some Wikipedia). The source for the dataset of the flora and fauna can be found at https://fws.gov/refuge/Don_Edwards_San_Francisco_Bay/ 
###### *Requires Python 3 and C++*

```console 
$ make main.exe
$ ./main.exe
```

# Explanation of Danger Level Calculations
<img src="/danger_level_regression.png" alt="regression"/>


