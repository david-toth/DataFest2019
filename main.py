#!/usr/bin/env python3

from imports import *

# master path to data dir
data_dir = "./data/"

# Data frames
games = pd.read_csv(data_dir + "games.csv")
gps = pd.read_csv(data_dir + "gps.csv")
rpe = pd.read_csv(data_dir + "rpe.csv")
wellness = pd.read_csv(data_dir + "wellness.csv")

print(games.size)
print(gps.size)
print(rpe.size)
print(wellness.size)