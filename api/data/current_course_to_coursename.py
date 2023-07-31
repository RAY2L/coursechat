#!/usr/bin/env python3
import json
from collections import defaultdict
from typing import Dict


def current_course_to_coursename(current_course_to_metadata: Dict[str, Dict]) -> Dict[str, str]:
    current_course_to_coursename_dict = defaultdict()

    for metadata in current_course_to_metadata.values():
        course = f"{metadata['Subject']} {metadata['CourseId']}"
        current_course_to_coursename_dict[course] = metadata["Course Name"]

    return current_course_to_coursename_dict

def run():
    with open("cur.json", "r") as file1:
        current_course_to_metadata = json.load(file1)
        
    with open("current_course_to_coursename.json", "w") as file:
        json.dump(current_course_to_coursename(current_course_to_metadata), file)