"""
Tests for analyze.py

Covers:
  - missing job description
  - missing experience bank
  - missing resume template
  - valid inputs (happy path)
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from analyze import (
    read_job_description,
    read_experience_bank,
    verify_resume_template,
    summarize_inputs,
)


def test_missing_job_description(tmp_path):
    missing_path = tmp_path / "job_description.txt"  # not created
    with pytest.raises(FileNotFoundError):
        read_job_description(missing_path)


def test_missing_experience_bank(tmp_path):
    missing_path = tmp_path / "experience_bank.md"  # not created
    with pytest.raises(FileNotFoundError):
        read_experience_bank(missing_path)


def test_missing_resume_template(tmp_path):
    missing_path = tmp_path / "resume_template.docx"  # not created
    with pytest.raises(FileNotFoundError):
        verify_resume_template(missing_path)


def test_valid_inputs(tmp_path):
    jd_path = tmp_path / "job_description.txt"
    jd_path.write_text("We are hiring a software engineer intern.")

    bank_path = tmp_path / "experience_bank.md"
    bank_path.write_text("# Experience\n\nSome project details.")

    template_path = tmp_path / "resume_template.docx"
    template_path.write_bytes(b"fake docx bytes")  # existence is all that's checked

    job_description = read_job_description(jd_path)
    experience_bank = read_experience_bank(bank_path)
    verify_resume_template(template_path)  # should not raise

    assert "software engineer" in job_description
    assert "project details" in experience_bank

    summary = summarize_inputs(job_description, experience_bank, template_path)
    assert "Job description" in summary
    assert "Experience bank" in summary
    assert "resume_template.docx" in summary
