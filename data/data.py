#!/usr/bin/env python3
import combine_years
import course_to_evalIDs
import courses
import course_to_coursename
import current_courses
import all_courses
import current_course_to_coursename
import all_course_to_coursename
import current_course_to_IDs

# Add years here
years = ["2021", "2022", "current_eval"]

combine_years.run(years)
course_to_evalIDs.run()
courses.run()
current_courses.run()
all_courses.run()
course_to_coursename.run()
current_course_to_coursename.run()
all_course_to_coursename.run()
current_course_to_IDs.run()