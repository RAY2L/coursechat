#!/usr/bin/env python3
import json
from collections import defaultdict
from typing import Dict, List


def course_to_evalIDs(evals) -> Dict[str, List]:
    course_to_evalIDs_dict = defaultdict(set)

    for evalID, data in evals.items():
        for catalog_number in data["Catalog Number"]:
            course = f"{catalog_number['Subject']} {catalog_number['CourseId']}"
            course_to_evalIDs_dict[course].add(evalID)

    for key in course_to_evalIDs_dict:
        if isinstance(course_to_evalIDs_dict[key], set):
            course_to_evalIDs_dict[key] = list(course_to_evalIDs_dict[key])

    return course_to_evalIDs_dict


# Open the JSON file
with open("2022.json", "r") as file:
    # Load JSON data from file
    evals = json.load(file)

    # print(course_to_evalIDs(evals))

with open("course_to_evalIDs.json", "w") as file:
    json.dump(course_to_evalIDs(evals), file)