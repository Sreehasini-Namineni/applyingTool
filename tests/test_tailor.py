"""
Tests for tailor.py
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from tailor import ensure_output_dir, tailor_resume


def test_ensure_output_dir_creates_missing_dir(tmp_path):
    output_dir = tmp_path / "output"
    assert not output_dir.exists()

    result = ensure_output_dir(output_dir)

    assert output_dir.exists()
    assert output_dir.is_dir()
    assert result == output_dir


def test_ensure_output_dir_is_idempotent(tmp_path):
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    # Should not raise even though the directory already exists.
    ensure_output_dir(output_dir)

    assert output_dir.exists()


def test_tailor_resume_not_implemented(tmp_path):
    with pytest.raises(NotImplementedError):
        tailor_resume("jd text", "bank text", tmp_path / "template.docx", tmp_path / "output")
