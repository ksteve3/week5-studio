# Shared TECHIN 509 AI coding instructions

## Scope

I use this file as the master instruction file for Codex and Claude Code.
I use these rules for TECHIN 509 assignments and future MSTI projects.
My collaborator, when an assignment involves joint work, is Mike (LBXMike).

In these instructions, "I", "me", and "my" mean the person currently
directing the agent. Do not assume which partner completed an action.

## Writing and accuracy

- Write explanations, documentation, reflections, README updates, and
  submission text on my behalf in first person.
- Use I/me/my for my individual work.
- Use we/us/our only for work Mike and I actually completed together.
- Never invent contributions, discussions, agreements, results, or test
  outcomes. Ask when attribution is unclear.

## Reading, planning, and permission

- Read the relevant code, assignment README, and instructor instructions
  before suggesting edits.
- Explain proposed changes and their reasoning.
- Ask for my explicit permission before major alterations, including
  substantial rewrites, deletions, file renaming, architecture changes,
  new dependencies, or changes to shared deliverables.
- Identify the affected files before requesting approval, and wait for
  approval before making those changes.
- Preserve existing behavior unless my requested change explicitly
  requires otherwise.
- Follow assignment-specific instructions when they impose additional
  restrictions. General permission does not waive assignment boundaries.

## Code, verification, and existing work

- Follow PEP 8 for modified Python code.
- Run applicable tests and report the commands and actual results.
  Clearly state when a test was not run.
- Never change instructor-supplied tests or expected answers merely to
  make evaluations pass.
- Protect existing work. Inspect Git status and review the relevant
  working-tree and staged diffs before committing.
- Commit only the intended files. Do not include unrelated changes.
- Do not overwrite Mike's work or my work without explicit permission.

## Work log

- After each work session that changes files or makes a decision,
  add an entry to the directing partner's file in worklog/
  (worklog/mike.md or worklog/katie.md). Create the file if it does
  not exist. Never edit the other partner's log file.
- Each entry: date, partner directing, agent used (Codex or
  Claude Code), what was done, files changed, commit hash, test
  commands and their actual results, and any open questions.
- Commit the log entry with the work it describes.
- Record only what actually happened. Do not invent results,
  agreements, or contributions.

## Automatic setup for future projects

- When I ask an agent to create or set up a TECHIN 509 or MSTI project,
  automatically include these shared rules in AGENTS.md at the new
  project's root and create CLAUDE.md containing only @AGENTS.md.
- My request to create or set up the project includes permission to add
  these two instruction files when they do not already exist; do not ask
  me to copy them manually or request separate approval for that setup.
- Use the latest general rules from the main branch of
  https://github.com/ksteve3/week5-studio as the shared source, including
  this automatic setup section. If that source is unavailable, use the
  loaded copy and clearly report that its freshness could not be verified.
- Read existing project and instructor instructions first. If instruction
  files already exist, preserve their content and assignment constraints;
  explain the proposed merge and obtain my approval before replacing or
  changing shared instructions. Do not overwrite another person's work.
- Confirm which instruction files were created and that CLAUDE.md imports
  the adjacent AGENTS.md. Follow those rules for the new project.
- This setup permission does not authorize publishing a new repository,
  changing access, committing, or pushing unless I have requested those
  actions. Do not copy assignment-specific restrictions to other projects.

## Week 5 studio - assignment-specific rules

I apply this section only to Week 5 Studio; I do not copy it into other projects.
I am including rule cards 1, 2, 3, 4, 5, and 9. I still need to confirm the
selection with Mike; this update does not record a joint implementation agreement.

- Card 1: I require the agent to read relevant code before proposing changes.
- Card 2: I require a plan and agreement from Mike and me before code edits.
- Card 3: I require existing behavior to be preserved during refactoring.
- Card 4: I require the supplied evaluation before and after changes. My saved
  original baseline already records the before result; I must not recreate it.
- Card 5: I require an explanation of each extracted function's parameters,
  return value, and call sites.
- Card 9: I require PEP 8 for code written or changed in search.py, without
  reformatting untouched code or adding formatting tools.

I preserve these instructor task limits regardless of rule selection:

- I limit refactoring edits to search.py, preserving search(query) and
  compare_texts(first, second), their interfaces, and their return shapes.
- I leave FAQ data, vocabulary, evaluate.py, eval_cases.json, and baseline.json
  unchanged. I never overwrite, delete, or recreate the saved baseline.
- I add no dependencies, live model calls, or features. I do not change expected
  answers or fix the known sixth-case limitation during this refactoring.
- I compare independent proposals with Mike and record the agreed plan in
  TEAM_NOTES.md before implementation, with at most two small function extractions.
- I use one shared working copy with the original baseline. I follow the
  instructor's directing/reviewing role swap with Mike between extractions.
- I run python evaluate.py --after after each extraction and for final verification.
  I expect 5/6 correct AND PASS, including matching selections and candidate scores.
- I keep required work-log and team-note updates separate from code refactoring.
