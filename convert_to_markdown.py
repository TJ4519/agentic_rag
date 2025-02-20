# Document to Mar   kdown converter
import os
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat, ExportFormat
from pathlib import Path

def get_pdf_paths(base_dir, pdf_files):
    """
       Prepend the base directory path to each PDF filename
    """
    return [os.path.join(base_dir, pdf) for pdf in pdf_files]


#Instantiate converter class with pdf support
converter = DocumentConverter(
    allowed_formats=[InputFormat.PDF],
    export_format=ExportFormat.MARKDOWN_WITH_IMAGES
)

# Initialize the pipeline for PDF processing
converter.initialize_pipeline(InputFormat.PDF)

# breakpoint()
#List of pdfs to convert
pdfs = [
    "applied-llms_org-llm-tricks.pdf",
    "LLM_ENGINEERS_HANDBOOK.pdf"
]

documents_dir = "documents"
pdf_paths = get_pdf_paths(documents_dir, pdfs)

#Create output directory
output_dir = "markdown_output"
Path(output_dir).mkdir(parents=True, exist_ok=True)

#Convert pdfs to markdown

for pdf_path in pdf_paths:

    conv_result = converter.convert(pdf_path)

    output_filename = os.path.basename(pdf_path).rsplit('.', 1)[0] + '.md'
    output_path = os.path.join(output_dir, output_filename)

    markdown_content = conv_result.document.export_to_markdown()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Successfully converted {pdf_path} to {output_path}")

# def convert_pdf_to_markdown(input_path, output_path):
#     """
#     Convert a PDF file to Markdown format
    
#     Args:
#         input_path (str): Path to the input PDF file
#         output_path (str): Path where the markdown file will be saved
#     """
#     try:
#         # Load the document
#         doc = Document(input_path)
        
#         # Convert to markdown
#         markdown_content = doc.to_markdown()
        
#         # Save the markdown content
#         with open(output_path, 'w', encoding='utf-8') as f:
#             f.write(markdown_content)
            
#         print(f"Successfully converted {input_path} to {output_path}")
        
#     except Exception as e:
#         print(f"Error converting {input_path}: {str(e)}")

# if __name__ == "__main__":
#     # Specific files to convert
#     files_to_convert = [
#         "applied-llms_org-llm-tricks.pdf",
#         "LLM_ENGINEERS_HANDBOOK.pdf"
#     ]
    
#     documents_dir = "documents"
#     output_dir = "markdown_output"
    
#     # Create output directory if it doesn't exist
#     Path(output_dir).mkdir(parents=True, exist_ok=True)
    
#     # Convert only the specified files
#     for filename in files_to_convert:
#         input_path = os.path.join(documents_dir, filename)
#         output_path = os.path.join(output_dir, filename.rsplit('.', 1)[0] + '.md')
#         convert_pdf_to_markdown(input_path, output_path)

# #