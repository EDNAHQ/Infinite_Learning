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
                @page {{
                    margin: 1cm;  /* Set margins for print to 1cm */
                }}
                body {{
                    margin: 0;                      /* Remove default margins */
                    background-color: black;        /* Set background to black */
                    color: white;                   /* Set default text color to white */
                    font-family: 'Poppins', sans-serif; 
                    line-height: 1.6; 
                    font-size: 12pt; 
                }}
                h1, h2, h3, h4, h5, h6 {{
                    color: gold;                   /* Set header color to gold */
                    margin-top: 1em;              
                    margin-bottom: 0.5em;         
                }}
                p {{
                    margin-bottom: 0.5em;         
                }}
                code {{
                    background-color: #333;       
                    padding: 2px 4px;             
                    border-radius: 4px;           
                    font-family: monospace;       
                    font-size: 0.9em;             
                }}
                pre {{
                    background-color: #333;       
                    padding: 1em;                 
                    border-radius: 4px;           
                    white-space: pre-wrap;        
                    word-wrap: break-word;        
                }}
                blockquote {{
                    border-left: 4px solid #777;   
                    padding-left: 1em;            
                    margin-left: 0;               
                    font-style: italic;            
                }}
                table {{
                    border-collapse: collapse;     
                    width: 100%;                  
                    margin-bottom: 1em;           
                    color: white;                 
                }}
                th, td {{
                    border: 1px solid #444;       
                    padding: 8px;                 
                    text-align: left;             
                }}
                th {{
                    background-color: #555;       
                }}
                input, textarea {{
                    border-color: #4A90E2 !important; 
                    color: white;                  /* Change text color in inputs and textareas */
                    background-color: #222;        /* Set a dark background for inputs */
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
