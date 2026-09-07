"""
main.py

Entry point for the tool.

Current goal: JOB DESCRIPTION -> ANALYZE -> TAILORED RESUME (step 1 of 3)

For now this script only handles the "read inputs and verify everything
is in place" step:
  1. Read input/job_description.txt
  2. Read data/experience_bank.md
  3. Verify data/resume_template.docx exists
  4. Print a summary of the inputs
  5. Create output/ if it doesn't exist

AI-powered tailoring is not implemented yet (see tailor.py).
"""

import sys
from pathlib import Path

# Allow running as `python src/main.py` from the project root.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from analyze import read_job_description, read_experience_bank, verify_resume_template, summarize_inputs
from tailor import ensure_output_dir

PROJECT_ROOT = Path(__file__).resolve().parent.parent
JOB_DESCRIPTION_PATH = PROJECT_ROOT / "input" / "job_description.txt"
EXPERIENCE_BANK_PATH = PROJECT_ROOT / "data" / "experience_bank.md"
RESUME_TEMPLATE_PATH = PROJECT_ROOT / "data" / "resume_template.docx"
OUTPUT_DIR = PROJECT_ROOT / "output"


def run(
    job_description_path: Path = JOB_DESCRIPTION_PATH,
    experience_bank_path: Path = EXPERIENCE_BANK_PATH,
    resume_template_path: Path = RESUME_TEMPLATE_PATH,
    output_dir: Path = OUTPUT_DIR,
) -> None:
    job_description = read_job_description(job_description_path)
    experience_bank = read_experience_bank(experience_bank_path)
    verify_resume_template(resume_template_path)

    print(summarize_inputs(job_description, experience_bank, resume_template_path))

    ensure_output_dir(output_dir)
    print(f"\nOutput directory ready: {output_dir}")


if __name__ == "__main__":
    try:
        run()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
