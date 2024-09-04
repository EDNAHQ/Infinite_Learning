"""
Functions to manage pdf content
"""

from io import BytesIO
from markdown import markdown
from weasyprint import HTML, CSS


def create_pdf_file(content: str) -> BytesIO:
    """
    Create a PDF file from the provided Markdown content.
    Converts Markdown to styled HTML, then HTML to PDF.
    """

    html_content = markdown(content, extensions=["extra", "codehilite"])

    styled_html = f"""
    <html>
        <head>
            <style>
                /* Global Variables */
                :root {{
                  --text-color: #ffffff;
                  --main-title-color: #fbb022;
                  --sub-title-color: #d94f8b;
                  --code-background: rgba(51, 51, 51, 0.7);
                  --border-color: #444;
                  --input-background: rgba(34, 34, 34, 0.7);
                  --input-border-color: #4A90E2;
                }}
                
                /* Print Settings */
                @page {{
                  size: A4;
                  margin: 2cm;
                }}
                
                /* Base Styles */
                body {{
                  margin: 0;
                  padding: 2cm;
                  background-color: #1a1a1a;
                  color: var(--text-color);
                  font-family: Arial, sans-serif;
                  line-height: 1.6;
                  font-size: 12pt;
                }}
                
                /* Typography */
                h1, h2, h3 {{
                  color: var(--main-title-color);
                  margin: 1em 0 0.5em;
                }}
                
                h4, h5, h6 {{
                  color: var(--sub-title-color);
                  margin: 1em 0 0.5em;
                }}
                
                p {{
                  margin-bottom: 0.5em;
                }}
                
                /* Code Blocks */
                code {{
                  background-color: var(--code-background);
                  padding: 2px 4px;
                  border-radius: 4px;
                  font-family: 'Courier New', monospace;
                  font-size: 0.9em;
                }}
                
                pre {{
                  background-color: var(--code-background);
                  padding: 1em;
                  border-radius: 4px;
                  white-space: pre-wrap;
                  word-wrap: break-word;
                  overflow-x: auto;
                }}
                
                /* Tables */
                table {{
                  border-collapse: collapse;
                  width: 100%;
                  margin-bottom: 1em;
                }}
                
                th, td {{
                  border: 1px solid var(--border-color);
                  padding: 8px;
                  text-align: left;
                }}
                
                th {{
                  background-color: rgba(85, 85, 85, 0.7);
                  font-weight: bold;
                }}
                
                /* Form Elements */
                input, textarea {{
                  border: 1px solid var(--input-border-color);
                  color: var(--text-color);
                  background-color: var(--input-background);
                  padding: 8px;
                  border-radius: 4px;
                }}
                
                /* Print Styles */
                @media print {{
                  body {{
                    background-color: white;
                    color: black;
                  }}
                  
                  h1, h2, h3 {{
                    color: #fbb022;
                  }}
                  
                  h4, h5, h6 {{
                    color: #d94f8b;
                  }}
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
    </html>
    """

    pdf_buffer = BytesIO()
    HTML(string=styled_html).write_pdf(pdf_buffer)
    pdf_buffer.seek(0)

    return pdf_buffer
