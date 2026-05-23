"""
Pytest fixtures for the benchmark test.
"""
import base64
import re
import pytest


@pytest.fixture
def upload_blob():
    r"""
    Fixture that simulates uploading a base64-encoded blob.

    Parameters:
    - filename (str): name of the file
    - content_type (str): MIME type, must match pattern ^[a-z0-9.+\-/]+$ (lowercase only)
    - data (str): valid base64-encoded data
    """
    def _upload_blob(filename, content_type, data):
        # Validate filename
        if not isinstance(filename, str) or len(filename) == 0:
            raise ValueError(f"filename must be a non-empty string, got {repr(filename)}")

        # Validate content_type matches pattern (lowercase only)
        pattern = r"^[a-z0-9.+\-/]+$"
        if not re.match(pattern, content_type):
            raise ValueError(
                f"content_type {repr(content_type)} does not match pattern {pattern}. "
                f"Must be lowercase only."
            )

        # Validate data is valid base64
        if not isinstance(data, str) or len(data) == 0:
            raise ValueError(f"data must be a non-empty string, got {repr(data)}")

        try:
            decoded = base64.b64decode(data, validate=True)
        except Exception as e:
            raise ValueError(f"data is not valid base64: {e}")

        # Simulate successful upload
        return {
            "success": True,
            "filename": filename,
            "content_type": content_type,
            "bytes_uploaded": len(decoded),
            "data_encoded": data
        }

    return _upload_blob
