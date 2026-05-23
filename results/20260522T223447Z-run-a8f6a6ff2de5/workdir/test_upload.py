#!/usr/bin/env python3
"""
Test script to call upload_blob with the correct parameters.
"""
import base64
import json
from pathlib import Path

# Load the tools schema
tools_file = Path(__file__).parent / "tools.json"
with open(tools_file) as f:
    tools_spec = json.load(f)

# Extract upload_blob schema
upload_blob_schema = next(t for t in tools_spec["tools"] if t["name"] == "upload_blob")
schema = upload_blob_schema["parameters"]

# Prepare the parameters
filename = "hello.txt"
content_type = "text/plain"
data = base64.b64encode(b"Hello, blob!").decode('ascii')

# Validate against schema
call_params = {
    "filename": filename,
    "content_type": content_type,
    "data": data
}

print("Calling upload_blob with:")
print(f"  filename: {repr(filename)}")
print(f"  content_type: {repr(content_type)}")
print(f"  data: {repr(data)}")
print()

# Validate filename
if not (1 <= len(filename)):
    raise ValueError(f"filename must have minLength 1, got {len(filename)}")

# Validate content_type matches pattern
import re
pattern = schema["properties"]["content_type"]["pattern"]
if not re.match(pattern, content_type):
    raise ValueError(f"content_type {repr(content_type)} does not match pattern {pattern}")

# Validate data
if not (1 <= len(data)):
    raise ValueError(f"data must have minLength 1, got {len(data)}")

# Verify base64 is valid
try:
    decoded = base64.b64decode(data)
    print(f"✓ Valid base64 encoding")
    print(f"✓ Decodes to: {repr(decoded.decode('utf-8'))}")
except Exception as e:
    raise ValueError(f"Invalid base64: {e}")

# Check no additional properties
if set(call_params.keys()) != set(schema["required"]):
    raise ValueError(f"Properties mismatch")

print(f"✓ All schema validations passed")
print()
print("upload_blob call with validated parameters:")
print(f"upload_blob(filename={repr(filename)}, content_type={repr(content_type)}, data={repr(data)})")
