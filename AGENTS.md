# Shared AI coding instructions

## Scope and current status

I use this file as the master instruction file for Codex and Claude Code.
The project partners are ksteve3 and Mike (LBXMike).

In these instructions, "I", "me", and "my" mean the person currently
directing the agent. Do not assume which partner completed an action.

The Week 5 rules and refactoring plan remain pending partner agreement.
Publishing this file does not establish Mike's agreement or authorize
refactoring.

## Writing and accuracy

- Write explanations, documentation, reflections, README updates, and
  submission text on my behalf in first person.
- Use I/me/my for my individual work.
- Use we/us/our only for work Mike and I actually completed together.
- Never invent contributions, discussions, agreements, results, or test
  outcomes. Ask when attribution is unclear.

## Reading, planning, and permission

- Read the relevant code and instructions before suggesting edits.
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

## Week 5 studio: required boundaries

Read README.md and RULE_CARDS.md before proposing Week 5 changes.

I currently recommend instructor cards 1, 2, 3, 4, 5, and 9:
1. Read the relevant code before proposing changes.
2. Propose a plan and wait for Mike and me to agree before editing.
3. Preserve existing behavior during refactoring.
4. Run the supplied evaluation before and after changes.
5. Explain each extracted function's parameters and return value.
9. Follow PEP 8 for code written or changed in search.py. Do not reformat
   untouched code or add formatting tools.

I recommend excluding cards 6, 7, and 8 because whole-program rewrites,
new packages, and changing expected answers conflict with this studio.

### Protected files and behavior

- During refactoring, edit only search.py.
- Do not modify evaluate.py, eval_cases.json, or baseline.json.
- Never overwrite, delete, or recreate baseline.json. It has already
  been saved from the verified original starter. Do not run --baseline.
- Preserve the FAQ data and vocabulary.
- Preserve search(query) and compare_texts(first, second), including
  their public interfaces and return structures.
- Add no dependencies, formatting tools, live model calls, or features.
- Preserve the known sixth-case limitation and expected 5/6 result.
  Do not change expected answers to make checks pass.

### Proposal and partner approval

- Do not start refactoring until I explicitly request that stage.
- Propose at most two small function extractions.
- For each proposed function, explain its name, inputs, return value,
  call sites, and why the extraction helps.
- Wait until Mike and I have compared our independently developed
  proposals and approved one refactoring plan.
- Record only an actually agreed plan in TEAM_NOTES.md, with permission
  to update that shared deliverable.
- Use one working copy with the original baseline for the shared
  submission. Do not merge two independently refactored versions.
- Follow the assignment's driver/reviewer role swap for the extractions.
  Do not claim either partner performed a role without evidence.

### Verification

- Before approved refactoring, after each agreed extraction, and at the
  final check, run: python evaluate.py --after
- This command writes after.json; never substitute --baseline.
- Success requires 5/6 correct AND PASS, with individual FAQ selections,
  candidate scores, and comparison probes matching the saved baseline
  within the evaluator's tolerance. An unchanged total is insufficient.
- If verification fails, inspect the code with my partner and propose
  a small correction. Do not alter the checks.
- Report actual results. Passing these supplied examples is bounded
  evidence, not proof of equivalence for every possible input.
