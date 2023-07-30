#!/usr/bin/env python3
import json


def run():
    with open("courses.json", "r") as file1:
        courses = json.load(file1)
    
    with open("current_courses.json", "r") as file2:
        current_courses = json.load(file2)

    with open("all_courses.json", "w") as file:
        # combine the two lists
        combined = courses + current_courses

        # create a new dictionary where the keys are the 'name' values
        # and the values are the dictionary from the combined list
        combined_dict = {d["name"]: d for d in combined}

        # get the values from the combined dictionary, which will be unique dictionaries
        unique = list(combined_dict.values())

        # print(unique)
        json.dump(unique, file)
