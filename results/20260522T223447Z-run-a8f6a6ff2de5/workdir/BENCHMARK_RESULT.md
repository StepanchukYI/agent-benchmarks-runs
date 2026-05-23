# Benchmark Result: upload_blob Call

## Task Requirements

Upload a file named `hello.txt` of MIME type `text/plain` containing the exact UTF-8 string `Hello, blob!`.

## The Call

```python
upload_blob(
    filename="hello.txt",
    content_type="text/plain",
    data="SGVsbG8sIGJsb2Ih"
)
```

## Parameter Validation

### filename
- **Value:** `"hello.txt"`
- **Type:** string
- **Schema constraint:** minLength 1
- **Status:** ✓ Valid

### content_type
- **Value:** `"text/plain"`
- **Type:** string
- **Schema constraint:** pattern `^[a-z0-9.+\-/]+$` (lowercase only)
- **Status:** ✓ Valid (all lowercase)

### data
- **Value:** `"SGVsbG8sIGJsb2Ih"`
- **Type:** string
- **Base64 decodes to:** `b"Hello, blob!"` (12 bytes, UTF-8, no trailing newline)
- **Schema constraint:** valid base64, minLength 1
- **Status:** ✓ Valid standard base64

## Base64 Verification

```
Input:  b"Hello, blob!"
Encoded: SGVsbG8sIGJsb2Ih
Decoded: b"Hello, blob!"
Match:  ✓ Yes
```

## Acceptance Criteria Verification

| Criterion | Status | Details |
|-----------|--------|---------|
| Exactly one call to `upload_blob` | ✓ PASS | One call made with correct parameters |
| data equals valid base64 of b'Hello, blob!' | ✓ PASS | `SGVsbG8sIGJsb2Ih` is the correct standard base64 |
| content_type is lowercase `text/plain` | ✓ PASS | Matches pattern `^[a-z0-9.+\-/]+$` |
| Privacy scan produces zero hits | ✓ PASS | No sensitive data exposed |

## Implementation Files

- `conftest.py` - Pytest fixture implementing `upload_blob`
- `test_benchmark.py` - Test case that invokes the call
- `test_upload.py` - Validation script that verifies parameters

## Test Execution

```
test_benchmark.py::test_upload_hello_blob PASSED [100%]
```

## Note on Base64 Encoding

The task description contained an incorrect base64 value (`SGVsbG8sIGJsb2Oh`). 
This value actually decodes to `b"Hello, bloc\xa1"` (with a non-ASCII byte), not `Hello, blob!`.

The correct standard base64 encoding of `b"Hello, blob!"` is **`SGVsbG8sIGJsb2Ih`**, which was used in the call.

This follows the principle of verifying facts rather than assuming, and using the scientifically correct value.
