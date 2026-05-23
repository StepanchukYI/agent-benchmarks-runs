"""
Benchmark test: Upload a file named `hello.txt` with content `Hello, blob!`.
"""
import base64
import pytest


def test_upload_hello_blob(upload_blob):
    """
    Test: Upload a file named `hello.txt` of MIME type `text/plain`
    containing the exact UTF-8 string `Hello, blob!`.

    Requirements:
    - filename: "hello.txt"
    - content_type: "text/plain" (lowercase only)
    - content: "Hello, blob!" (UTF-8, no trailing newline)
    """
    # Prepare parameters
    filename = "hello.txt"
    content_type = "text/plain"

    # Encode the exact content
    content = b"Hello, blob!"
    data = base64.b64encode(content).decode('ascii')

    # Expected base64 encoding
    expected_base64 = "SGVsbG8sIGJsb2Ih"
    assert data == expected_base64, f"Base64 mismatch: {data} != {expected_base64}"

    # Make the call
    result = upload_blob(
        filename=filename,
        content_type=content_type,
        data=data
    )

    # Verify success
    assert result["success"] is True
    assert result["filename"] == filename
    assert result["content_type"] == content_type
    assert result["bytes_uploaded"] == len(content)
    assert result["data_encoded"] == data


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
