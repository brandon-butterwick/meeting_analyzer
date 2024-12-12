"""
Meeting Analyzer Agent - Processes meeting transcripts and produces structured summaries
"""

from pathlib import Path
from meeting_brain.utils.document_processor import read_pdf, read_pdfs

class MeetingAnalyzer:
    def __init__(self, agent):
        # Load the agent prompt
        prompt_path = Path(__file__).parent.parent.parent / 'meeting_agent/meeting_analyzer_prompt.pdf'
        self.system_prompt = read_pdf(str(prompt_path))
        
        self.agent = agent
        self.agent.system_prompt = self.system_prompt

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
            transcript_path: Path to meeting transcript file
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

Please analyze this meeting following the format specified in the system prompt.
"""
        
        # Get the analysis
        response = self.agent.run(prompt)
        analysis = response.content
        
        # Save the analysis
        if output_path:
            Path(output_path).write_text(analysis, encoding='utf-8')
        
        return analysis
