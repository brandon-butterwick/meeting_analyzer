"""
Script to run meeting analysis using the Meeting Analyzer agent
"""

import asyncio
import pandas as pd
from pathlib import Path
from agents.meeting_analyzer import MeetingAnalyzer

async def run_analysis():
    # Define our files using a simple dataframe
    files_df = pd.DataFrame({
        'type': ['context', 'context', 'context', 'context', 'meeting', 'meeting'],
        'purpose': ['background', 'teams', 'timeline', 'agent_context', 'transcript', 'agenda'],
        'path': [
            'meeting_agent/project_background.pdf',
            'meeting_agent/teams_at_relex.pdf',
            'meeting_agent/project_timeline.pdf',
            'meeting_agent/meeting_agent_context.pdf',
            'meeting_agent/meeting_transcript.pdf',
            'meeting_agent/meeting_prep_with_agenda.pdf'
        ]
    })
    
    # Quick check if files exist
    files_df['exists'] = files_df.path.apply(Path.exists)
    if not files_df.exists.all():
        missing = files_df[~files_df.exists]
        print("Missing files:")
        print(missing[['purpose', 'path']])
        return
    
    # Organize context files into a dictionary
    context_files = dict(zip(
        files_df[files_df.type == 'context'].purpose,
        files_df[files_df.type == 'context'].path
    ))
    
    # Get meeting files
    transcript = files_df[files_df.purpose == 'transcript'].path.iloc[0]
    agenda = files_df[files_df.purpose == 'agenda'].path.iloc[0]
    
    # Set up output
    output_path = 'meeting_brain/outputs/summaries/meeting_summary.txt'
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Run analysis
    analyzer = MeetingAnalyzer()
    try:
        summary = await analyzer.analyze_meeting(
            context_files=context_files,
            transcript_path=transcript,
            agenda_path=agenda,
            output_path=output_path
        )
        
        print(f"\nAnalysis complete! Summary saved to: {output_path}")
        print("\nSummary Preview:")
        print("=" * 50)
        print(summary[:500] + "..." if len(summary) > 500 else summary)
        
    except Exception as e:
        print(f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    asyncio.run(run_analysis())
