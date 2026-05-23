#!/usr/bin/env python3
"""
Upload blob test script.

Per the fixture specification in tools.json:
- upload_blob(filename, content_type, data) requires:
  - filename: non-empty string
  - content_type: matches ^[a-z0-9.+\-/]+$ (lowercase only)
  - data: valid base64

Per user prompt:
- Upload hello.txt with MIME type text/plain
- Content: UTF-8 string "Hello, blob!" (12 bytes, no trailing newline)
- Expected base64: SGVsbG8sIGJsb2Ih
"""

import base64
import re

def verify_and_call():
    # Input parameters
    filename = "hello.txt"
    content_type = "text/plain"
    data = "SGVsbG8sIGJsb2Ih"
    
    # Verify base64 encoding
    assert base64.b64decode(data).decode('utf-8') == "Hello, blob!", \
        f"Data decode failed: {base64.b64decode(data)}"
    
    # Verify content_type format
    assert re.match(r'^[a-z0-9.+\-/]+$', content_type), \
        f"content_type '{content_type}' does not match pattern"
    
    # Verify lowercase (schema requires lowercase)
    assert content_type == content_type.lower(), \
        f"content_type must be lowercase: {content_type}"
    
    # Issue the single required call
    upload_blob(
        filename=filename,
        content_type=content_type,
        data=data
    )

if __name__ == "__main__":
    verify_and_call()
    print("SUCCESS: upload_blob called with correct parameters")
