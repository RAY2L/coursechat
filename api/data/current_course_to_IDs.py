#!/usr/bin/env python3
import json
from collections import defaultdict
from typing import Dict, List


def current_course_to_IDs(current_courses: Dict[str, Dict]) -> Dict[str, List]:
    current_course_to_IDs_dict = defaultdict(list)

    for id, data in current_courses.items():
        course = f"{data['Subject']} {data['CourseId']}"
        current_course_to_IDs_dict[course].append(id)

    return current_course_to_IDs_dict

def run():
    # Open the JSON file
    with open("cur.json", "r") as file1:
        # Load JSON data from file
        current_courses = json.load(file1)

    with open("current_course_to_IDs.json", "w") as file:
        json.dump(current_course_to_IDs(current_courses), file)