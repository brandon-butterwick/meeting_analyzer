"""
Meeting Analyzer Agent - Processes meeting transcripts and produces structured summaries
"""

import os
from pathlib import Path
from phi.agent import Agent
from meeting_brain.utils.document_processor import read_pdf, read_pdfs

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

class MeetingAnalyzer(Agent):
    def __init__(self):
        # Load the agent prompt
        prompt_path = Path(__file__).parent.parent.parent / 'meeting_agent/meeting_analyzer_prompt.pdf'
        system_prompt = read_pdf(str(prompt_path))
        
        super().__init__(
            name="Meeting Analyzer",
            description="A specialized tool designed to process meeting transcripts and produce actionable outputs",
            system_prompt=system_prompt
        )

    def analyze_meeting(self, 
                     transcript_path: str,
                     project_background_path: str,
                     team_roles_path: str,
                     project_timeline_path: str,
                     meeting_prep_path: str,
                     output_path: str) -> str:
        """
        Analyze meeting transcript with all required context documents
        
        Args:
            transcript_path: Path to meeting transcript
            project_background_path: Path to project background doc
            team_roles_path: Path to team roles doc
            project_timeline_path: Path to project timeline
            meeting_prep_path: Path to meeting prep doc
            output_path: Where to save the analysis
        """
        # Load all documents
        docs = read_pdfs({
            'transcript': transcript_path,
            'background': project_background_path,
            'team_roles': team_roles_path,
            'timeline': project_timeline_path,
            'prep': meeting_prep_path
        })
        
        # Prepare analysis prompt
        prompt = f"""
Please analyze this meeting and format your response exactly like this example:

# Analysis of the Nick & Brandon Meeting

### 1. Notes

- Bullet points of key information
- Each point should be clear and concise

### 2. Decisions Made

- **Decision Title:** Description of the decision
- **Another Decision:** Details about it

### 3. Outstanding Questions

- Clear questions that need answers
- Questions from the meeting that weren't resolved

### 4. Action Items

- **Action Title:** Who needs to do what
- **Next Steps:** Specific actions to take

### 5. Meeting Summary

A few paragraphs that synthesize the key points and outcomes of the meeting.

Now analyze this meeting with the same structure:

Project Background:
{docs['background']}

Team Roles:
{docs['team_roles']}

Project Timeline:
{docs['timeline']}

Meeting Prep:
{docs['prep']}

Meeting Transcript:
{docs['transcript']}
"""
        
        # Get the analysis
        response = self.run(prompt)
        analysis = response.content
        
        # Save the analysis
        if output_path:
            Path(output_path).write_text(analysis, encoding='utf-8')
        
        return analysis
