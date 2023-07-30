#!/usr/bin/env python3
import json
from typing import Dict, List


def courses(evals: Dict) -> List[Dict]:
    courses_set = set()
    courses_list = list()

    for data in evals.values():
        for catalog_number in data["Catalog Number"]:
            course_name = f"{catalog_number['Subject']} {catalog_number['CourseId']}"

            course_name_split = course_name.split(" ")
            subject = course_name_split[0]
            courseId = course_name_split[1]

            course_value = { "subject": subject, "courseId": courseId }

            if (course_name not in courses_set):
                courses_list.append({"name": course_name, "value": course_value})
                courses_set.add(course_name)

    return courses_list


# Open the JSON file
with open("2022.json", "r") as file1, open("2021.json", "r") as file2:
    # Load JSON data from file
    evals_2022 = json.load(file1)
    evals_2021 = json.load(file2)

    evals = {**evals_2022, **evals_2021}

    # print(courses(evals))

with open("courses.json", "w") as file:
    json.dump(courses(evals), file)
