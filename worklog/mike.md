# Mike's work log

Newest entries at the bottom. Rules for entries are in AGENTS.md
under "Work log".

## 2026-10-31

- **Directing:** Mike
- **Agent:** Claude Code
- **What was done:**
  - Cloned ksteve3/week5-studio locally.
  - Confirmed no baseline.json existed on my machine and that my
    course copy of search.py is the unmodified starter (matches the
    evaluator's fingerprint).
  - Pulled Katie's baseline.json (c12883f) and checked it against my
    starter's output in memory, without writing files: equivalent.
  - Copied the six starter files unchanged from the course repo and
    pushed them.
  - Added the agreed "Work log" rule to AGENTS.md and created this file.
- **Files changed:** search.py, evaluate.py, eval_cases.json,
  README.md, RULE_CARDS.md, TEAM_NOTES.md (added unchanged);
  AGENTS.md (Work log section); worklog/mike.md (new).
- **Commits:** d784636 (starter files); the commit containing this
  entry (Work log rule + this file).
- **Tests:** `evaluate.search_is_unchanged()` → True;
  `evaluate.run()` → 5/6 correct (q6 expected miss);
  `evaluate.equivalent(baseline.json, run())` → True.
  `python evaluate.py --after` was not run, so no after.json exists yet.
- **Open questions:**
  - Which rule cards go into AGENTS.md for Part 1 (Katie suggested
    1–5 and 9).
  - Whether to restore the Week 5 task limits to AGENTS.md.
