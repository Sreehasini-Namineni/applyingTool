"""
analyze.py

Reads and validates the raw inputs the tool needs:
  - the job description
  - the experience bank
  - the resume template

No AI logic lives here yet — just reading files and giving clear
errors when something required is missing.
"""

from pathlib import Path


def read_job_description(path: Path) -> str:
    """Read and return the job description text.

    Raises FileNotFoundError with a clear message if the file is missing.
    """
    if not path.is_file():
        raise FileNotFoundError(
            f"Job description not found at '{path}'. "
            "Add a job_description.txt file to the input/ folder."
        )
    return path.read_text(encoding="utf-8")


def read_experience_bank(path: Path) -> str:
    """Read and return the experience bank text.

    Raises FileNotFoundError with a clear message if the file is missing.
    """
    if not path.is_file():
        raise FileNotFoundError(
            f"Experience bank not found at '{path}'. "
            "Add an experience_bank.md file to the data/ folder."
        )
    return path.read_text(encoding="utf-8")


def verify_resume_template(path: Path) -> None:
    """Verify that the resume template file exists.

    Raises FileNotFoundError with a clear message if it is missing.
    Does not read or parse the .docx contents (that happens later,
    when tailoring is implemented).
    """
    if not path.is_file():
        raise FileNotFoundError(
            f"Resume template not found at '{path}'. "
            "Add a resume_template.docx file to the data/ folder."
        )


def summarize_inputs(job_description: str, experience_bank: str, template_path: Path) -> str:
    """Build a short, human-readable summary of the loaded inputs."""
    jd_words = len(job_description.split())
    bank_words = len(experience_bank.split())
    lines = [
        "Input Summary",
        "-------------",
        f"Job description: {jd_words} words",
        f"Experience bank: {bank_words} words",
        f"Resume template: {template_path.name} (found)",
    ]
    return "\n".join(lines)
