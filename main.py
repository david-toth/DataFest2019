#!/usr/bin/env python3

from imports import *

# master path to data dir
data_dir = "./data/"

# Data frames
games = pd.read_csv("games.csv")
gps = pd.read_csv("gps.csv")
rpe = pd.read_csv("rpe.csv")
wellness = pd.read_csv("wellness.csv")