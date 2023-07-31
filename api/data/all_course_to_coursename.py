#!/usr/bin/env python3
import json
from collections import defaultdict
from typing import Dict, List


def run():
    with open("course_to_coursename.json", "r") as file1:
        course_to_metadata = json.load(file1)
        
    with open("current_course_to_coursename.json", "r") as file2:
        current_course_to_metadata = json.load(file2)
        
    with open("all_course_to_coursename.json", "w") as file:
        json.dump({ **course_to_metadata, **current_course_to_metadata }, file)