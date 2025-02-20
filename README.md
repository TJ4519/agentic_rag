# Agentic RAG (Retrieval Augmented Generation)
<!-- This is a system for enhancing AI interactions with document-based knowledge -->

## Instructions for Using Script

### Convert to Markdown
<!-- This is Step 1 of the document processing pipeline -->

To organise documents by section, we first convert them to markdown.
<!-- Markdown format allows for better parsing and section identification -->

The `convert_to_markdown.py` script processes files in the `docs` folder and converts them to Markdown format. It only supports `.pdf` files as input for now (later, we will use an LLM to convert other file types to md). The converted files are saved in the `docs/output` directory.
<!-- Note: PDF support likely uses a PDF parsing library like PyPDF2 or pdfminer -->

1. Place your input files in the `docs` directory.
2. Run the script:
   ```bash
   uv run convert_to_markdown.py
   <!-- 'uv' is an alternative to pip/venv, offering faster package operations -->
   ```
3. Check the `docs/output` directory for the converted Markdown files.

Next, we generate a table of contents for each Markdown file.
<!-- Step 2: TOC generation helps with document navigation and structure -->

The `generate_toc.py` script generates a table of contents for each Markdown file in the `docs/output` directory.
<!-- This likely uses markdown parsing to identify headers and create links -->

1. Ensure your Markdown files are in the `docs/output` directory.
<!-- The pipeline expects files to flow from docs → docs/output --> 