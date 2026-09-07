"""
tailor.py

Handles the output side of the pipeline: making sure output/ exists,
and (eventually) generating the tailored resume itself.

No AI functionality is implemented yet — this module currently only
prepares the output directory.
"""

from pathlib import Path


def ensure_output_dir(path: Path) -> Path:
    """Create the output directory if it doesn't already exist.

    Returns the path for convenience.
    """
    path.mkdir(parents=True, exist_ok=True)
    return path


def tailor_resume(job_description: str, experience_bank: str, template_path: Path, output_dir: Path) -> None:
    """Placeholder for future AI-powered tailoring logic.

    Not implemented yet. When AI tailoring is added, this function will:
      1. Send the job description + experience bank to an AI API
         (using the API key from the AI_API_KEY environment variable)
      2. Use the response to fill in data/resume_template.docx
      3. Save the result to output/
    """
    raise NotImplementedError("AI tailoring is not implemented yet.")
