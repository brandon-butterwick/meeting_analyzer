"""
Basic validation tests for Meeting Brain
"""

import pytest
from pathlib import Path
from unittest.mock import Mock, patch, AsyncMock

@pytest.fixture
def mock_agent():
    """Mock base Agent class"""
    with patch('meeting_brain.agents.meeting_analyzer.Agent') as mock:
        mock_instance = Mock()
        mock_instance.run = AsyncMock(return_value=Mock(content="Analysis complete"))
        mock.return_value = mock_instance
        yield mock

class TestMeetingBrain:
    """Basic validation tests"""
    
    @pytest.mark.asyncio
    async def test_meeting_analysis(self, mock_agent):
        """Verify meeting analyzer can process documents and generate analysis"""
        from meeting_brain.agents.meeting_analyzer import MeetingAnalyzer
        
        # Mock file operations
        with patch('pathlib.Path.read_text') as mock_read:
            mock_read.return_value = "Test content"
            
            # Initialize analyzer
            analyzer = MeetingAnalyzer()
            
            # Run analysis
            result = await analyzer.analyze_meeting(
                context_files={'test': 'test.pdf'},
                transcript_path='transcript.pdf',
                agenda_path='agenda.pdf',
                output_path='output.txt'
            )
            
            # Verify basic functionality
            assert result is not None
            assert mock_read.called
            mock_agent.return_value.run.assert_called_once()
