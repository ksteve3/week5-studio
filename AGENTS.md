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
