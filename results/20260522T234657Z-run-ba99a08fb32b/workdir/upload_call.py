#!/usr/bin/env python3
"""
Upload blob function call - benchmark submission

Uploads a file named hello.txt with MIME type text/plain
containing the exact UTF-8 string 'Hello, blob!' (no trailing newline)
"""

# The exact call required by the task
upload_blob(
    filename="hello.txt",
    content_type="text/plain",
    data="SGVsbG8sIGJsb2Ih"
)
