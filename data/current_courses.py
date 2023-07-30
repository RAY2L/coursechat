#!/usr/bin/env python3
import json
from typing import Dict, List


def current_courses(current_courses: Dict) -> List[Dict]:
    courses_set = set()
    courses_list = list()

    for metadata in current_courses.values():
        subject = metadata["Subject"]
        courseId = metadata["CourseId"]

        course_name = f"{subject} {courseId}"
        course_value = { "subject": subject, "courseId": courseId }
        
        if (course_name not in courses_set):
            courses_list.append({ "name": course_name, "value": course_value })
            courses_set.add(course_name)

    return courses_list


def run():
    # Open the JSON file
    with open("cur.json", "r") as file:
        # Load JSON data from file
        courses = json.load(file)

        # print(courses(evals))

    with open("current_courses.json", "w") as file:
        json.dump(current_courses(courses), file)
