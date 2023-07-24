from langchain import PromptTemplate


course_info_template = """\
The course description for is {course_description}.
"""
course_info_prompt = PromptTemplate.from_template(course_info_template)


course_metadata_template = """\
The course metadata is {course_metadata}.
"""
course_metadata_prompt = PromptTemplate.from_template(course_metadata_template)


eval_text_template = """\
This is a question from the course evaluation: {question}
These are answers to this question:
{answers}
"""
eval_text_prompt = PromptTemplate.from_template(eval_text_template)


eval_stats_template = """\
This is a question from the course evaluation: {question}
These are the statistics from the answers to this question:
{answer}
"""
eval_stats_prompt = PromptTemplate.from_template(eval_stats_template)


def data_to_str_list(data):
    print(data["General Course Information"])
    print(type(data["General Course Information"]))
    course_info = course_info_prompt.format(
        course_description=data["General Course Information"]
    )
    metadata_str = str(data["Evaluation Metadata"])
    course_metadata = course_metadata_prompt.format(course_metadata=metadata_str)

    str_list = [course_info, course_metadata]

    for question, answers in data["Evaluation Text Data"].items():
        eval_text = eval_text_prompt.format(
            question=question, answers="\n".join(answers)
        )

        str_list.append(eval_text)

    for question, answer in data["Evaluation Statistics Data"].items():
        eval_stats = eval_stats_prompt.format(question=question, answer=answer)

        str_list.append(eval_stats)

    return str_list
