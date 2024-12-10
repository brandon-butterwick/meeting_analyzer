"""
Run Meeting Analysis
"""

import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from meeting_brain.agents.meeting_analyzer import MeetingAnalyzer

def analyze_meeting():
    analyzer = MeetingAnalyzer()
    analysis = analyzer.analyze_meeting(
        transcript_path='meeting_agent/meeting_transcript.pdf',
        project_background_path='meeting_agent/project_background.pdf',
        team_roles_path='meeting_agent/teams_at_relex.pdf',
        project_timeline_path='meeting_agent/project_timeline.pdf',
        meeting_prep_path='meeting_agent/meeting_prep_with_agenda.pdf',
        output_path='meeting_brain/outputs/summaries/analysis.txt'
    )
    print(analysis)

if __name__ == "__main__":
    analyze_meeting()
