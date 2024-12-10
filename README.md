# Meeting Brain

A tool that analyzes meeting transcripts and produces structured summaries.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Place your meeting files in the `meeting_agent` folder:
- meeting_transcript.pdf
- project_background.pdf
- teams_at_relex.pdf
- project_timeline.pdf
- meeting_prep_with_agenda.pdf

## Usage

Run the analyzer:
```bash
python meeting_brain/run.py
```

The analysis will be saved to `meeting_brain/outputs/summaries/analysis.txt`

## Structure

- `meeting_brain/run.py` - Main script
- `meeting_brain/agents/meeting_analyzer.py` - Analysis logic
- `meeting_brain/utils/document_processor.py` - PDF handling
- `meeting_brain/config/settings.py` - Configuration

## Output Format

The analysis follows this structure:
1. Notes - Key points from the meeting
2. Decisions Made - Clear decisions and agreements
3. Outstanding Questions - Unresolved items
4. Action Items - Next steps and responsibilities
5. Meeting Summary - Brief overview of outcomes
