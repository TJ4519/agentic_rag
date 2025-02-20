from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.pipeline.standard_pdf_pipeline import StandardPdfPipeline
from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend
from pathlib import Path
import os
from tqdm import tqdm  # For progress bar

def get_pdf_paths(base_dir, pdf_files):
    """Prepend the base directory path to each PDF filename"""
    return [os.path.join(base_dir, pdf) for pdf in pdf_files]

# Instantiate converter with multimodal support
converter = DocumentConverter(
    allowed_formats=[InputFormat.PDF],
    format_options={
        InputFormat.PDF: PdfFormatOption(
            pipeline_cls=StandardPdfPipeline,
            backend=PyPdfiumDocumentBackend
        )
    }
)

# Initialize pipeline
converter.initialize_pipeline(InputFormat.PDF)

# List of PDFs to convert
pdfs = [
    "applied-llms_org-llm-tricks.pdf",
    "LLM_ENGINEERS_HANDBOOK.pdf"
]

documents_dir = "documents"
pdf_paths = get_pdf_paths(documents_dir, pdfs)

# Create output directory
output_dir = "markdown_output"
Path(output_dir).mkdir(parents=True, exist_ok=True)

# Convert PDFs to markdown with progress bar
for pdf_path in tqdm(pdf_paths, desc="Converting PDFs"):
    try:
        # Convert without the invalid parameter
        conv_result = converter.convert(pdf_path)
        
        output_filename = os.path.basename(pdf_path).rsplit('.', 1)[0] + '.md'
        output_path = os.path.join(output_dir, output_filename)
        
        # Export to markdown
        markdown_content = conv_result.document.export_to_markdown()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
            
        print(f"\nSuccessfully converted {pdf_path} to {output_path}")
        
    except Exception as e:
        print(f"\nError converting {pdf_path}: {str(e)}")

print("\nConversion complete!")