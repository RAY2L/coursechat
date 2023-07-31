#!/usr/bin/env python3
import json
from typing import List

def run(years: List[str]):
    evals = {}
    for year in years:
        with open(f"{year}.json", "r") as file:
            year_evals = json.load(file)
            evals = {**evals, **year_evals}

    with open("combine_years.json", "w") as file:
        json.dump(evals, file)