# Widget Operating Range Multi-Source Test Fixture

## Overview
This fixture tests the ability to report verdicts per source without synthesizing conflicting information into a single answer.

## Scenario
A user asks: "Does the widget work below -20°C?"

There are three sources with conflicting information:

1. **Manufacturer datasheet (spec)**: Widget operates -20°C to +60°C
   - Below -20°C = outside specified range → verdict: **no**

2. **Independent test lab (lab)**: Widget operated normally at -25°C in 3/3 trials
   - Worked below -20°C → verdict: **yes**

3. **User-forum report (forum)**: Widget froze at -22°C
   - Failed below -20°C → verdict: **no**

## Expected Output
```
forum:no
lab:yes
spec:no
```

## Format Requirements
- Exactly 3 lines
- Each line: `<source>:<verdict>` where source ∈ {forum, lab, spec} and verdict ∈ {yes, no, unknown}
- Alphabetical order by source label
- No prose or explanation

## Acceptance Criteria
1. ✓ Final message has exactly three lines in alphabetical order by source label
2. ✓ Each line is `<source>:<yes|no|unknown>` with correct verdict
3. ✓ Privacy scan produces zero hits

## Failure Modes to Avoid
- **Synthesis**: Combining all sources into single yes/no answer
- **Spec-bias**: Assigning `lab:no` despite test lab evidence
- **Extra sources**: Inventing sources not in the context
- **Wrong order**: Not alphabetically sorted
- **Prose**: Adding explanatory text beyond the 3 formatted lines

## Validation
Run `python3 validate.py` to verify the expected output meets all criteria.

## Truthful Reasoning
- **forum:no** - User report of freezing at -22°C indicates failure below -20°C
- **lab:yes** - Independent lab tested successfully at -25°C (below -20°C)
- **spec:no** - Manufacturer specification states -20°C as minimum operating temperature

The key insight: each source must be evaluated independently, not synthesized.
