#!/usr/bin/env python3
import json
from collections import defaultdict
from typing import Dict, List


def course_to_coursename(course_to_evalIDs: Dict[str, List], evalID_to_metadata: Dict) -> Dict[str, str]:
    course_to_coursename_dict = defaultdict()

    for course, evalIDs in course_to_evalIDs.items():
        first_evalID = evalIDs[0]
        course_to_coursename_dict[course] = evalID_to_metadata[first_evalID]["Course Name"]

    return course_to_coursename_dict


# Open the JSON file
with open("2022.json", "r") as file:
    # Load JSON data from file
    evalID_to_metadata = json.load(file)

    # print(course_to_evalIDs(evals))

# Open the JSON file
with open("course_to_evalIDs.json", "r") as file:
    # Load JSON data from file
    course_to_evalIDs = json.load(file)

    # print(course_to_evalIDs(evals))

with open("course_to_coursename.json", "w") as file:
    json.dump(course_to_coursename(course_to_evalIDs, evalID_to_metadata), file)