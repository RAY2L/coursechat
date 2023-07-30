#!/usr/bin/env python3
import json

import combine_years
import course_to_evalIDs
import courses
import course_to_coursename

# Add years here
years = ["2021", "2022"]

combine_years.run(years)
course_to_evalIDs.run()
courses.run()
course_to_coursename.run()