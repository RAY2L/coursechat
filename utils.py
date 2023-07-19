import requests
from requests.exceptions import RequestException
from typing import Dict, List, Optional

from bs4 import BeautifulSoup, Tag


def construct_url(major: str) -> str:
    """
    Constructs the URL based on the major.

    Args:
        major (str): The major.

    Returns:
        str: The URL.
    """
    return f"http://collegecatalog.uchicago.edu/thecollege/{major}/"


def fetch_web_content(url: str) -> Optional[str]:
    """
    Fetches the web content from the URL.

    Args:
        url (str): The URL.

    Returns:
        Optional[str]: The web content if the GET request is successful, None otherwise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise a HTTPError if the response was unsuccessful
        return response.content
    except RequestException as e:
        print(f"Failed to fetch web content from {url} due to {str(e)}")
        return None


def parse_content(content: str) -> List[BeautifulSoup]:
    """
    Parses the content with BeautifulSoup and finds all div elements with class containing 'courseblock main' or 'courseblock subsequence'.

    Args:
        content (str): The content.

    Returns:
        List[BeautifulSoup]: A list of BeautifulSoup objects, each representing a course block.
    """
    soup = BeautifulSoup(content, "html.parser")
    return soup.find_all("div", class_=["courseblock main", "courseblock subsequence"])


def extract_course_information(course_block: Tag) -> Dict[str, Optional[str]]:
    """
    Extracts the course information from a course block.

    Args:
        course_block (Tag): BeautifulSoup Tag object representing a single course block.

    Returns:
        Dict[str, Optional[str]]: A dictionary containing the course title, description, and additional details.
    """
    # Extract course title from the 'courseblocktitle' tag.
    title = (
        course_block.find("p", class_="courseblocktitle")
        .find("strong")
        .get_text(strip=True)
    )

    # Extract course description from the 'courseblockdesc' tag.
    desc = course_block.find("p", class_="courseblockdesc").get_text(strip=True)

    # Extract additional course detail from the 'courseblockdetail' tag if it exists.
    detail = (
        course_block.find("p", class_="courseblockdetail").get_text(strip=True)
        if course_block.find("p", class_="courseblockdetail")
        else None
    )

    # Return the extracted information as a dictionary.
    return {"title": title, "description": desc, "detail": detail}


def generate_course_groups_from_blocks(
    course_blocks: List[BeautifulSoup],
) -> List[List[Dict[str, Optional[str]]]]:
    """
    Generates groups of related courses from a list of course blocks.

    Args:
        course_blocks (List[BeautifulSoup]): A list of BeautifulSoup objects, each representing a course block.

    Returns:
        List[List[Dict[str, Optional[str]]]]: A nested list where each inner list represents a group of related courses.
                                               Each course is represented as a dictionary containing its title, description, and details.
    """
    # Initialize an empty list to hold all course groups.
    course_groups = []

    # Initialize an empty list to hold the current course group.
    current_group = []

    # Iterate over all course blocks.
    for course_block in course_blocks:
        # If the current block is a main course block and there are already courses in the current group,
        # it means we've reached a new course group, so we append the current group to the course groups
        # and start a new group.
        if (
            course_block.has_attr("class")
            and "main" in course_block["class"]
            and "courseblock" in course_block["class"]
            and current_group
        ):
            course_groups.append(current_group)
            current_group = []

        # Extract course information for the current course block and add it to the current group.
        current_group.append(extract_course_information(course_block))

    # Don't forget to add the last group of courses if it exists.
    if current_group:
        course_groups.append(current_group)

    # Return the list of course groups.
    return course_groups


def fetch_courses_for_major(major: str) -> List[List[Dict[str, Optional[str]]]]:
    """
    Fetches courses for a given major.

    Args:
        major (str): The major.

    Returns:
        List[List[Dict]]: A list of course groups, where each course group is a list of dictionaries, each containing the title, description, and detail of a course.
    """
    url = construct_url(major)
    content = fetch_web_content(url)
    if content is None:
        return []

    course_blocks = parse_content(content)
    return generate_course_groups_from_blocks(course_blocks)


def generate_course_blobs(
    course_groups: List[List[Dict[str, Optional[str]]]]
) -> List[str]:
    """
    Transforms a list of course groups into a list of 'blobs' where each blob
    is a string representation of all courses in a single group.

    Args:
        course_groups (List[List[Dict[str, Optional[str]]]]): A list of course groups, where each group is a list
                                                              of dictionaries containing the title, description,
                                                              and detail of each course.

    Returns:
        List[str]: A list of course blobs where each blob represents all the courses in a single group.
    """

    # Initialize an empty list to hold all course blobs
    course_blobs = []

    # Iterate over all course groups
    for group in course_groups:
        # Initialize an empty list to hold the current group's course blobs
        group_blobs = []

        # Iterate over all courses in the current group
        for course in group:
            # Convert the course information into a string and append it to the group blobs
            group_blobs.append(
                f"Title: {course['title']}\nDescription: {course['description']}\nDetails: {course['detail']}"
            )

        # Combine all course blobs in the current group into a single blob and append it to the course blobs
        course_blobs.append("\n\n".join(group_blobs))

    return course_blobs


def generate_major_docs(major: str) -> List[str]:
    """
    Fetches all courses related to a specific major and generates a list of documents,
    where each document is a string representation of all courses in a single course group.

    Args:
        major (str): The major to fetch courses for.

    Returns:
        List[str]: A list of documents where each document represents all the courses in a single group.
    """

    # Fetch the list of course groups for the given major
    course_groups = fetch_courses_for_major(major)
    # Generate a list of Document's for these course_groups
    docs = generate_course_blobs(course_groups)

    return docs
