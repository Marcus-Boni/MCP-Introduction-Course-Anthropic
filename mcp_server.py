from pydantic import Field
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}


@mcp.tool(
    name="read_doc_contents",
    description="Reads the contents of a document given its ID.",
)
def read_doc_contents(
    doc_id: str = Field(description="The ID of the document to read."),
):
    if doc_id not in docs:
        raise ValueError("Document not found.")

    return docs[doc_id]


@mcp.tool(
    name="edit_doc",
    description="Edits the contents of a document given its ID and new content.",
)
def edit_doc(
    doc_id: str = Field(description="The ID of the document to edit."),
    old_content: str = Field(description="The current content of the document."),
    new_content: str = Field(
        description="The new content to replace the current content."
    ),
):
    if doc_id not in docs:
        raise ValueError(f"Document {doc_id} not found.")
    docs[doc_id] = docs[doc_id].replace(old_content, new_content)
    return f"Document {doc_id} updated successfully."


@mcp.resource(
    "docs://documents",
    mime_type="application/json",
)
def list_docs() -> list[str]:
    return list(docs.keys())


@mcp.resource(
    "docs://document/{doc_id}",
    mime_type="text/plain",
)
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Document {doc_id} not found.")

    return docs[doc_id]


@mcp.prompt(
    name="format",
    description="Rewrite the given document content in markdown format.",
)
def format_doc(
    doc_id: str = Field(description="The ID of the document to format."),
) -> list[base.Message]:
    prompt = f"""
    Your goal is to reformat a document into markdown format.
    The document ID is:
    <document_id>{doc_id}</document_id>

    Add in headers, bullet points, tables, and other markdown features as appropriate.
    Feel free to reorganize the content for better clarity.
    Use the 'edit_doc' tool to update the document with the reformatted content.
    After the document is reformatted, respond with 'Done'.
    """

    return [base.UserMessage(prompt)]



if __name__ == "__main__":
    mcp.run(transport="stdio")
