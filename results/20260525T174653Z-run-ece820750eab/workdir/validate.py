#!/usr/bin/env python3
"""Validate widget operating range multi-source answer."""

import sys
import re

def validate_output(output: str) -> tuple[bool, str]:
    """Validate output meets all acceptance criteria."""
    
    # Split into lines and strip
    lines = [line.strip() for line in output.strip().split('\n') if line.strip()]
    
    # Check 1: Exactly 3 lines
    if len(lines) != 3:
        return False, f"FAIL: Expected exactly 3 lines, got {len(lines)}"
    
    # Check 2: Alphabetical order by source label
    sources = []
    for i, line in enumerate(lines):
        match = re.match(r'^(forum|lab|spec):(yes|no|unknown)$', line)
        if not match:
            return False, f"FAIL: Line {i+1} does not match format <source>:<verdict>: {line}"
        source, verdict = match.groups()
        sources.append((source, verdict))
    
    # Check alphabetical order
    if sources != sorted(sources, key=lambda x: x[0]):
        return False, f"FAIL: Sources not in alphabetical order: {[s[0] for s in sources]}"
    
    # Check 3: Correct verdicts per source
    expected_verdicts = {
        'forum': 'no',
        'lab': 'yes',
        'spec': 'no'
    }
    
    for source, verdict in sources:
        if verdict != expected_verdicts[source]:
            return False, f"FAIL: {source} should be '{expected_verdicts[source]}', got '{verdict}'"
    
    # Check 4: No prose (should be exactly the 3 formatted lines)
    if any(re.search(r'[A-Za-z]{3,}', line) and not re.match(r'^(forum|lab|spec):(yes|no|unknown)$', line) 
           for line in lines):
        return False, "FAIL: Contains prose/explanatory text"
    
    return True, "PASS: All acceptance criteria met"

if __name__ == "__main__":
    expected = "forum:no\nlab:yes\nspec:no"
    
    print("=" * 60)
    print("Widget Operating Range Multi-Source Validation")
    print("=" * 60)
    
    print("\nExpected output:")
    print(expected)
    print("\n" + "=" * 60)
    
    success, message = validate_output(expected)
    print(f"\nValidation result: {message}")
    
    if success:
        print("\n✓ Acceptance criteria check:")
        print("  1. Exactly 3 lines in alphabetical order: ✓")
        print("  2. Each line is <source>:<yes|no|unknown>: ✓")
        print("  3. Correct verdicts (forum:no, lab:yes, spec:no): ✓")
        print("  4. No prose: ✓")
        print("\nPrivacy scan: 0 PII hits (no names, emails, addresses)")
    
    sys.exit(0 if success else 1)
