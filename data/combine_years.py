#!/usr/bin/env python3
import json
from collections import defaultdict
from typing import Dict, List


# Open the JSON file
with open("2022.json", "r") as file1, open("2021.json", "r") as file2:
    # Load JSON data from file
    evals_2022 = json.load(file1)
    evals_2021 = json.load(file2)

    evals = {**evals_2022, **evals_2021}

with open("combine_years.json", "w") as file:
    json.dump(evals, file)