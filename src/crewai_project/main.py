#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crewai_project.crew import CrewaiProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """

    resume_path = "input/resume.md"
    jd_path = "input/jd.md"

    with open(resume_path, "r", encoding="utf-8") as file:
      resume_content = file.read()


    with open(jd_path, "r", encoding="utf-8") as file:
      jd_content = file.read()

    
    parsed_resume = "output/parsed_resume.md"
    parsed_jd = "output/parsed_jd.md"

    
    inputs = {
        "resume_path": resume_content,
        "jd_path": jd_content ,
        "parsed_resume": parsed_resume,
        "parsed_jd": parsed_jd,
    }
    
    try:
        CrewaiProject().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


