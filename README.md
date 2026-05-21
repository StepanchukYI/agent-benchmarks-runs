# agent-benchmarks-runs

Public results repo for [agent-benchmarks](https://github.com/StepanchukYI/agent-benchmarks). Holds published trajectories + per-pillar scores produced by `ab run`. Consumed by the leaderboard fetcher at https://ab.evgeniy.online.

## Layout

```
results/
└── <utc>-run-<hex>/
    ├── metadata.yaml      # model, effort, tier_hash, dataset_version, runner
    ├── scores.json        # per-pillar scores + total + pass flag
    └── trajectory.jsonl   # append-only event log
```

Each run dir = one task × one model × one effort × one tier execution. Trajectory is the contract; `ab_harness.trajectory.validate` enforces append-only JSONL with strictly monotonic `turn.idx`, single `run_start` + `run_end`, scorer events after the last turn.

Deterministic scorers re-run from the trajectory alone — that's how the leaderboard server awards the `verified` trust tier on third-party submissions.

## Privacy

Three-layer privacy gate enforced before commit:
1. Pre-commit hook (`scripts/privacy_scan.py` in agent-benchmarks)
2. `privacy_check` scorer inside each trajectory
3. `privacy-scan` CI on this repo

Pattern set: [`docs/privacy-patterns.yaml`](https://github.com/StepanchukYI/agent-benchmarks/blob/main/docs/privacy-patterns.yaml). Includes:
- `operator-home-path` — generic `/Users/<any>` and `/home/<any>` (no hardcoded usernames)
- `isolation-honeypot-email` — sentinel `EMAIL` set by `IsolatedEnv`; firing means isolation broke
- Standard credential patterns (AWS, Slack, GitHub tokens, etc.)

## Trust

Fetcher polls every 15 min, validates trajectory schemas, re-runs deterministic scorers, writes a `Submission` row with the trust tier resolved per [`docs/trust-tiers.md`](https://github.com/StepanchukYI/agent-benchmarks/blob/main/docs/trust-tiers.md):

- `self_reported` — published numbers as-is (default)
- `verified` — server's re-score matched within tolerance + every scorer in the chain is replay-capable

## Current contents

| Batch | Model | Suite | Effort | Tier | Runs | Privacy hits |
|---|---|---|---|---|---|---|
| 2026-05-21 | claude-haiku-4-5 | L0_smoke (full 84) | low | T0 | 84 | 0 |

### Aggregate
- Mean total_score: **0.926**
- Median: **0.965**
- Pass rate: **47/84 (56%)** — pass=true requires near-1.0 across all pillars; 53/84 scored ≥0.95 overall
- Real fails (<0.5): **0**

### Isolation
- `AB_CLAUDE_HIDE_USER_CONFIG=1` — `~/.claude/{CLAUDE.md, skills/, agents/}` temp-renamed
- `_isolation.py::_sanitize_path` — `$PATH` stripped of operator-private bin dirs (`~/.local/bin`, `~/.codex/bin`)
- `GIT_CONFIG_GLOBAL=/dev/null` — git can't read operator's `~/.gitconfig`
- `EMAIL=<honeypot sentinel>` — leak detector
