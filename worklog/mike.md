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

## 2026-10-31 - Reviewing Katie's Week 5 rules

- **Directing:** Mike
- **Agent:** Claude Code
- **What was done:**
  - Pulled Katie's commit b282aa5 (Week 5 section in AGENTS.md) and
    checked it against RULE_CARDS.md and the studio README. It
    includes cards 1, 2, 3, 4, 5 and 9 and all instructor task limits.
  - **Decision:** I confirm rule cards 1, 2, 3, 4, 5 and 9, and
    excluding cards 6, 7 and 8.
  - Sent Katie a reply raising two wording issues, leaving the edits
    to her: (1) her line keeping work-log updates "separate from code
    refactoring" conflicts with the Work log rule to "commit the log
    entry with the work it describes"; (2) "with Mike" and "My saved
    original baseline" read incorrectly when I am directing.
- **Files changed:** worklog/mike.md (this entry only). I did not edit
  AGENTS.md or Katie's log.
- **Commits:** reviewed b282aa5; this entry is in the commit that
  contains it.
- **Tests:** none run; no code changed.
- **Follow-up:** Katie resolved both issues in 4137bc2 (log updates are
  now committed separately from code changes, and the Week 5 wording
  says "my partner"). AGENTS.md now records the confirmed cards.
- **Open questions:** comparing our independent refactor proposals.

## 2026-10-31 - Independent refactoring proposal

- **Directing:** Mike
- **Agent:** Claude Code
- **What was done:**
  - Had Claude Code explain search.py, then identified the repeated
    code myself: cleaning (4x), counting vocabulary words (4x), and
    cosine scoring (2x).
  - Chose to combine cleaning and counting, so two extractions remove
    all three repeats: `clean_count(text)` → list of 8 counts, and
    `score(first, second)` → one number from 0 to 1.
  - Compared with my agent's independent proposal (`text_to_vector`,
    `cosine_similarity`): same plan, different names.
  - Wrote MIKE_PROPOSAL.md as a note for Katie. Wrote it before reading
    KATIE_PROPOSAL.md (97a6b44), which proposes the same two functions
    under the agent's names.
- **Files changed:** MIKE_PROPOSAL.md (new); worklog/mike.md (this entry).
  search.py and TEAM_NOTES.md were not changed.
- **Commits:** the MIKE_PROPOSAL.md commit and this log commit.
- **Tests:** none run; no code changed.
- **Open questions:** agree on function names with Katie, record the
  plan in TEAM_NOTES.md, and decide who directs each extraction.

## 2026-10-31 - Recording the agreed plan

- **Directing:** Mike
- **Agent:** Claude Code
- **What was done:**
  - Katie reviewed my proposal and suggested her function names and the
    roles below. **Decision:** I agreed to use `text_to_vector(text)` and
    `cosine_similarity(first_vector, second_vector)`, with Katie (A)
    directing extraction 1 using Codex while I review, and me (B)
    directing extraction 2 using Claude Code while Katie reviews.
  - Filled in TEAM_NOTES.md with both proposals, the agreed plan and the
    before score (5/6). After score and behavior check left blank.
- **Files changed:** TEAM_NOTES.md; worklog/mike.md (this entry).
  search.py was not changed.
- **Commits:** the TEAM_NOTES.md commit and this log commit.
- **Tests:** none run; no code changed. Before score 5/6 comes from
  baseline.json.
- **Open questions:** none for the plan. Next: Katie directs extraction 1.
