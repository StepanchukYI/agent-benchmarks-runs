"""
Mock implementation of upload_blob for verification purposes.
The actual fixture would implement the real upload functionality.
"""

def upload_blob(filename, content_type, data):
    """Mock upload_blob function that validates parameters per fixture spec."""
    import base64
    import re
    
    # Validate per tools.json schema
    assert len(filename) >= 1, "filename must be non-empty"
    assert re.match(r'^[a-z0-9.+\-/]+$', content_type), \
        f"content_type '{content_type}' must match pattern ^[a-z0-9.+\-/]+$"
    assert len(data) >= 1, "data must be non-empty"
    
    # Validate base64 decoding
    decoded = base64.b64decode(data)
    print(f"SUCCESS: upload_blob called")
    print(f"  filename: {filename}")
    print(f"  content_type: {content_type}")
    print(f"  data: {data}")
    print(f"  decoded content: {decoded.decode('utf-8')}")
    
    return {"status": "uploaded", "filename": filename}

# Make the required call
upload_blob(filename="hello.txt", content_type="text/plain", data="SGVsbG8sIGJsb2Ih")
