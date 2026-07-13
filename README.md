# SauceDemo QA Suite

Take-home QA submission for the Amp QA Engineer role — Python, pytest, and Playwright.

# Overview

- Test scenarios: `docs/test-scenarios.md`
- Manual test cases & prioritization rationale: `docs/manual-test-cases.md`
- Summary (approach, framework justification, bugs found, future work): `docs/summary.md`
- Pre-generated test report: `report.html` (open directly in any browser)

# Setup Instructions

```
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

## Troubleshooting

**macOS users:** if `venv` creation or `pip install` behaves unexpectedly, confirm you're using a standard Python 3.11+ install (e.g., from python.org or Homebrew) rather than macOS's bundled system Python or Xcode's Python, which can cause silent installation issues. Verify with `python3 --version` before proceeding.

## Running Tests

Standard (Chromium only):

```
pytest tests/specs/ -v
```

Cross-browser (Chromium, Firefox, WebKit):

```
pytest tests/specs/ -v --browser chromium --browser firefox --browser webkit
```

Generate an HTML report:

```
pytest tests/specs/ -v --html=report.html --self-contained-html
```

# Project Structure

```
tests/
  pages/        # Page Object Model classes
  specs/        # 3 automated test cases
  test_data/    # Product catalog data
  conftest.py   # Shared fixtures
docs/           # Scenarios, manual test cases, summary, future additions
.github/workflows/  # CI: runs suite cross-browser on every push
```

# Framework Choice & Justification

Python, pytest, and Playwright. Full rationale, including locator strategy, is in `docs/summary.md`.

# Bugs Discovered

Four defects found during exploratory testing; the highest-severity one is automated as a regression test. Full detail in `docs/summary.md` and `docs/manual-test-cases.md`.

# Additional Test Coverage

Additional coverage was considered but deliberately not automated, to stay within the assignment's requested 2–3 test scope. See `docs/future-additions.md` for what was considered and why.
