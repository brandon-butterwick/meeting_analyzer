# Meeting Brain Tests

This directory contains tests for the Meeting Brain analysis pipeline. The tests follow a data science approach, focusing on the core functionality and data processing aspects.

## Test Structure

`test_meeting_brain.py` contains all tests, organized into:

1. Document Processing
   - PDF loading and text extraction
   - File handling

2. Meeting Analysis
   - Integration with 1-shot example
   - OpenAI model interaction
   - Analysis generation

3. Data Organization
   - Pandas DataFrame handling
   - File structure validation

## Running Tests

Install test dependencies:
```bash
pip install pytest pytest-asyncio pandas
```

Run tests:
```bash
pytest meeting_brain/tests/test_meeting_brain.py -v
```

## 1-Shot Example

The system uses a 1-shot example located in `meeting_brain/1_shot_examples/nick_brandon_meeting/analysis.txt` to ensure consistent analysis formatting. The tests verify this example is properly integrated into the analysis pipeline.

## Test Data

Tests use mock data and fixtures to simulate:
- Document content
- OpenAI responses
- File system operations

## Coverage Areas

Tests verify:
1. End-to-end analysis pipeline
2. Document processing functionality
3. Meeting analysis with 1-shot example
4. Data organization using pandas
