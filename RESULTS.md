# L0_smoke results — 5 models × prompts × effort (post-fix)

Last update: 2026-05-24 · 2830 published trajectories · all isolated (`mode=clean_home`, `real_home_untouched=true`).

## Live board

https://ab.evgeniy.online · pulls this repo and re-scores per the harness rev pinned in [agent-benchmarks](https://github.com/StepanchukYI/agent-benchmarks).

## Methodology

- **Suite**: `L0_smoke` (104 tasks after the quality-fix pass: 84 original + 15 bash-friendly rewrites in place + 20 new tasks across underrepresented categories).
- **Configs**:
  - Anthropic (haiku/sonnet/opus): `vanilla` / `operator-rules` / `karpathy` × `effort=low` / `effort=high` → 6 cells per model.
  - Vendor (GLM-5.1, MiniMax-M2.7) via Anthropic-compat: same 3 prompts, `effort=auto` (vendor's own reasoning).
- **Prompts**:
  - `vanilla` — no custom CLAUDE.md.
  - `operator-rules` — sanitized operator behavior-rules CLAUDE.md (identity-block stripped).
  - `karpathy` — public [karpathy-style behavioral guidelines](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md).
- **Tier**: T0 (vanilla, no operator context injected).
- **Scoring**: `pass` flag = `total_score >= 0.5` OR per-pillar `correctness >= 0.5` (aggregate, not strict-AND). See [B2 fix in main repo](https://github.com/StepanchukYI/agent-benchmarks).
- **Isolation**: per-run clean temp `$HOME`, real `~/.claude` untouched, env-token whitelisted (`ANTHROPIC_API_KEY` / `CLAUDE_CODE_OAUTH_TOKEN` / `ANTHROPIC_AUTH_TOKEN`), macOS keychain on Darwin. 16 deterministic isolation tests + gated live sentinel proof.

## Headline (best cell per model, after fixes)

| # | model | best config | pass-rate |
|---|---|---|---|
| 🥇 | claude-opus-4-7 | vanilla low / karpathy low | **96.2%** |
| 🥈 | claude-sonnet-4-6 | karpathy high | 89.4% |
| 🥉 | claude-haiku-4-5 | karpathy low | 87.5% |
| 4 | GLM-5.1 | vanilla auto | 82.8% |
| 5 | MiniMax-M2.7 | vanilla auto | 72.1% |

## Full matrix (OLD: pre-fix 84-task L0_smoke · POST: combined 104-task post-fix)

| model | prompt | effort | OLD | POST | Δ |
|---|---|---|---|---|---|
| opus | vanilla | low | 78.6% | **96.2%** | +17.6 |
| opus | vanilla | high | 73.8% | 91.3% | +17.5 |
| opus | operator-rules | low | 77.4% | 95.2% | +17.8 |
| opus | operator-rules | high | 75.0% | 93.3% | +18.3 |
| opus | karpathy | low | 78.6% | **96.2%** | +17.6 |
| opus | karpathy | high | 77.4% | 94.2% | +16.8 |
| sonnet | vanilla | low | 57.1% | 77.9% | +20.7 |
| sonnet | vanilla | high | 54.8% | 74.0% | +19.3 |
| sonnet | operator-rules | low | 66.7% | 86.5% | +19.9 |
| sonnet | operator-rules | high | 67.9% | 86.5% | +18.7 |
| sonnet | karpathy | low | 69.0% | 88.5% | +19.4 |
| sonnet | karpathy | high | 70.2% | **89.4%** | +19.2 |
| haiku | vanilla | low | 53.7% | 67.6% | +14.0 |
| haiku | vanilla | high | 44.6% | 61.2% | +16.6 |
| haiku | operator-rules | low | 66.7% | 84.5% | +17.8 |
| haiku | operator-rules | high | 67.5% | 85.4% | +18.0 |
| haiku | karpathy | low | 67.9% | **87.5%** | +19.6 |
| haiku | karpathy | high | 64.3% | 82.7% | +18.4 |
| GLM-5.1 | vanilla | auto | 63.3% | **82.8%** | +19.5 |
| GLM-5.1 | operator-rules | auto | 63.7% | 81.8% | +18.1 |
| GLM-5.1 | karpathy | auto | 66.2% | 82.7% | +16.4 |
| MiniMax-M2.7 | vanilla | auto | 56.0% | **72.1%** | +16.2 |
| MiniMax-M2.7 | operator-rules | auto | 49.4% | 61.2% | +11.8 |
| MiniMax-M2.7 | karpathy | auto | 53.1% | 64.4% | +11.3 |

## What changed between OLD and POST

Three benchmark-quality fixes shipped in [agent-benchmarks](https://github.com/StepanchukYI/agent-benchmarks) commit `4234b17`:

- **B1 — stub-tool MCP exposure** in the claude-code runner. Lets a task YAML declare `expected_tools:` and the runner exposes them as MCP stubs reading from `workdir/tools.json`. Trajectory captures `tool_calls[].name` exactly as the existing `tool_call_validator` scorers read. Without this, 14 L0_30x tasks were universally unsolvable on claude-code (named tools weren't exposed at all).
- **B2 — aggregate-pass rule**. Task `passed` now uses `total_score >= 0.5` (or correctness pillar) instead of strict-AND of every sub-scorer. Many old "fails" had `total_score=0.98` killed by one marginal scorer — those now pass honestly. Individual scorer pass/fail still surfaces in the drill view.
- **B3 — CRLF normalization** in `workdir_file_content_equals` / `preserve_crlf` assertions. LF agent output against CRLF expected file now matches when content is identical.

Plus task-content changes:

- **A.2 — 15 tool-use task rewrites** (L0_301..L0_315): swapped non-existent named tools for bash-friendly equivalents (agent writes typed JSON / text into workdir, scorers assert byte-exact via `file_diff` / `workdir_file_content_equals`). Skill intent preserved.
- **D — 20 new L0 tasks**: 5 reasoning-trap (graduated easy → hard), 5 long-context-niah (multi-needle, decoys, deep-tail, adversarial), 4 schema-fill (nested objects, conditionals), 3 exec (deterministic shell), 3 extract (filter / argmax / nested-key).

## Key observations from the matrix

- **Opus near ceiling.** 4 of 104 fails on its best cell. L0_smoke effectively saturates at Opus-tier — further model differentiation requires harder benchmarks (L1+ memory, L2+ skill-routing).
- **Sonnet shows reasoning-helps-with-guidance.** Unlike haiku (`high` slightly hurts), sonnet's `high` effort > `low` once paired with structured prompts.
- **Haiku gets the biggest prompt boost.** Vanilla low 67.6% → karpathy low 87.5% (+20pp). The Anthropic small model benefits most from explicit behavioral guidance.
- **GLM-5.1 monotonic-with-prompt.** Vanilla / op-rules / karpathy all near each other; auto reasoning enough.
- **MiniMax-M2.7 is anti-prompt.** Vanilla is its best cell; every prompt drops it. Either prompt-instructions confuse the model or its native tuning conflicts with imperative-rule prompts.

## Layout

```
results/
  <UTC>-run-<sha>/
    trajectory.jsonl   # append-only JSONL: run_start, turns, scorer events, run_end
    scores.json        # total_score + per-pillar + per-scorer verdicts
    metadata.yaml      # tier, dataset_version, isolation record, harness build
    workdir/           # the sandbox the agent worked in (post-run state)
RESULTS.md             # this file
```

## How to reproduce / contribute

Clone [agent-benchmarks](https://github.com/StepanchukYI/agent-benchmarks), follow `docs/friend-onboarding.md`. Your published rows appear next to these. Auth options: Claude Max subscription OAuth (`claude setup-token`), `ANTHROPIC_API_KEY`, or vendor key via `--vendor z-ai|minimax`.
