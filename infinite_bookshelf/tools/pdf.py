from io import BytesIO
from markdown import markdown
from weasyprint import HTML

def create_pdf_file(content: str) -> BytesIO:
    """Create a PDF from Markdown content."""
    
    html_content = markdown(content, extensions=["extra", "codehilite"])

    styled_html = f"""
    <html>
        <head>
            <style>
                :root {{
                  --text-color: #fff; --bg-color: #000; --title-color: #fbb022; --sub-title-color: #d94f8b;
                  --code-bg: rgba(51,51,51,0.7); --border-color: #444; --input-bg: rgba(34,34,34,0.7); --input-border: #4A90E2;
                }}
                @page {{ size: A4; margin: 1cm; }}
                body {{ margin: 0; padding: 1cm; background: #1a1a1a; color: var(--text-color); font: 12pt Arial; }}
                h1, h2, h3 {{ color: var(--title-color); margin: 1em 0 0.5em; }}
                h4, h5, h6 {{ color: var(--sub-title-color); margin: 1em 0 0.5em; }}
                p {{ margin-bottom: 0.5em; }}
                code {{ background: var(--code-bg); padding: 2px 4px; border-radius: 4px; font: 0.9em 'Courier New'; }}
                pre {{ background: var(--code-bg); padding: 1em; border-radius: 4px; white-space: pre-wrap; overflow-x: auto; }}
                table {{ border-collapse: collapse; width: 100%; margin-bottom: 1em; }}
                th, td {{ border: 1px solid var(--border-color); padding: 8px; }}
                th {{ background: rgba(85,85,85,0.7); font-weight: bold; }}
                input, textarea {{ border: 1px solid var(--input-border); color: var(--text-color); background: var(--input-bg); padding: 8px; border-radius: 4px; }}
                @media print {{ body {{ background: white; color: black; }} h1, h2, h3 {{ color: #fbb022; }} h4, h5, h6 {{ color: #d94f8b; }} }}
            </style>
        </head>
        <body>{html_content}</body>
    </html>
    """

    pdf_buffer = BytesIO()
    HTML(string=styled_html).write_pdf(pdf_buffer)
    pdf_buffer.seek(0)

    return pdf_buffer