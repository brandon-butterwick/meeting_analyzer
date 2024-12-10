"""
Test document processing
"""

from meeting_brain.utils.document_processor import read_pdf, read_pdfs

def test_single_pdf():
    """Test reading a single PDF"""
    try:
        content = read_pdf('meeting_agent/meeting_analyzer_prompt.pdf')
        print("\nSingle PDF test successful!")
        print("Preview:")
        print("=" * 50)
        print(content[:200] + "...")
    except Exception as e:
        print(f"Error reading single PDF: {str(e)}")

def test_multiple_pdfs():
    """Test reading multiple PDFs"""
    try:
        docs = read_pdfs({
            'prompt': 'meeting_agent/meeting_analyzer_prompt.pdf',
            'transcript': 'meeting_agent/meeting_transcript.pdf'
        })
        print("\nMultiple PDFs test successful!")
        for name, content in docs.items():
            print(f"\n{name.upper()} Preview:")
            print("=" * 50)
            print(content[:200] + "...")
    except Exception as e:
        print(f"Error reading multiple PDFs: {str(e)}")

if __name__ == "__main__":
    print("Testing document processing...")
    test_single_pdf()
    test_multiple_pdfs()
