# applyingTool

A simple local tool for tailoring a resume to a job description.

**Current goal:** JOB DESCRIPTION → ANALYZE → TAILORED RESUME

This is step 1: reading and validating inputs. AI-powered tailoring is not
implemented yet.

## Project structure

```
applyingTool/
├── data/
│   ├── experience_bank.md      # your raw experience, projects, skills
│   └── resume_template.docx    # the resume template to fill in later
├── input/
│   └── job_description.txt     # the job description you're applying to
├── output/                     # generated resumes will go here
├── src/
│   ├── main.py                 # entry point
│   ├── analyze.py              # reads & validates inputs
│   └── tailor.py                # output dir handling + future AI tailoring
├── tests/
├── requirements.txt
├── .env.example
└── README.md
```

## Setup

```bash
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env       # fill in AI_API_KEY when tailoring is implemented
```

## Usage

1. Replace `input/job_description.txt` with the job description you're applying to.
2. Fill in `data/experience_bank.md` with your real experience, projects, and skills.
3. Replace `data/resume_template.docx` with your actual resume template.
4. Run:

```bash
python src/main.py
```

This will read the job description and experience bank, verify the resume
template exists, print a short summary, and create the `output/` folder if
it doesn't already exist. It does not generate a tailored resume yet.

## Running tests

```bash
pytest tests/
```

Tests cover:
- missing job description
- missing experience bank
- missing resume template
- valid inputs (happy path)

## Roadmap

- [x] Read and validate inputs
- [ ] Analyze job description (extract keywords, requirements)
- [ ] AI-powered tailoring using `AI_API_KEY`
- [ ] Generate tailored `.docx` resume into `output/`
