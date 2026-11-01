# My Week 5 Studio work log

## 2026-10-31 - Synchronizing Mike's update

- **Partner directing:** Katie (ksteve3).
- **Agent used:** Codex.
- **What I did:** I asked Codex to check my local changes and remote branches, then safely pull Mike's update. I confirmed that LBXMike pushed the work-log rule and his separate first entry to main. I read the updated shared rules and created my own log. I did not begin refactoring or record an implementation agreement.
- **Files changed:** The pull updated AGENTS.md and added worklog/mike.md. My new local file is worklog/katie.md. I did not edit Mike's log. My existing untracked __pycache__/ folder was left in place.
- **Commit hash:** I synchronized to c3f9fc2a2011210d6c65a6d2df9dae6f9e28e14f. At the end of synchronization, my log entry was uncommitted. I subsequently authorized Codex to commit and push only this log; the recording commit is the commit containing this entry.
- **Checks and actual results:**
  - `git status --short --branch`, `git diff`, and `git diff --cached`: I found no tracked local edits before pulling; only __pycache__/ was untracked.
  - `git ls-remote --heads origin`: I found main, pointing to Mike's update.
  - `git pull --ff-only origin main`: I completed a fast-forward pull.
  - SHA-256 comparisons before and after pulling: I confirmed baseline.json and all six instructor files remained byte-for-byte unchanged.
  - `python -B -c "import evaluate; assert evaluate.search_is_unchanged(); print('PASS: instructor starter fingerprint')"`: I confirmed the instructor starter fingerprint passed.
  - I did not run --baseline or --after, and I did not create after.json.
- **Open questions:** Mike and I still need to compare our independent refactoring proposals and agree on an implementation plan before I authorize changes to search.py.

### Log publication authorization

I authorized Codex to commit and push my log to main after reviewing Git status, unstaged changes, staged changes, and the remote main revision. Only worklog/katie.md is included. I made no code changes, so I did not rerun the evaluator. My implementation plan with Mike is still pending agreement.

## 2026-10-31 - Adding explicit Week 5 rules

- **Partner directing:** Katie (ksteve3).
- **Agent used:** Codex.
- **What I did:** I authorized a Week 5 section in AGENTS.md. I included cards
  1, 2, 3, 4, 5, and 9 and the instructor task limits, while preserving the shared
  general rules, automatic setup rules, and work-log requirements. I left the
  rule selection pending confirmation with Mike and did not claim a joint plan.
- **Files changed:** AGENTS.md and worklog/katie.md. I did not edit Mike's log.
- **Commit hash:** My starting revision was 3c113cbc90a3d48b044e4ef41f146339faf1b284.
  I subsequently authorized committing and pushing this update. The recording commit is the commit containing this entry.
- **Checks and actual results:** I checked Git status and the remote main ref;
  both pointed to my starting revision, with only __pycache__/ untracked before
  editing. SHA-256 comparisons confirmed the baseline, six instructor files,
  Mike's log, and CLAUDE.md were unchanged. I reviewed git diff --check and the
  final diff. I did not run the evaluator because I made no code changes.
- **Open questions:** I still need to confirm the rule selection and agree on an
  implementation plan with Mike. I have not relocated the shared general rules.

## 2026-10-31 - Recording confirmed rules and clarifying commit policy

- **Partner directing:** Katie (ksteve3).
- **Agent used:** Codex.
- **What I did:** I provided Mike's confirmation of cards 1, 2, 3, 4, 5, and 9
  and exclusion of 6, 7, and 8. I updated AGENTS.md to record that confirmation.
  I adopted his proposed policy: I commit work-log and team-note updates
  separately from code changes, immediately after the work they describe.
  I aligned both rule sections and changed Week 5 wording to work for either
  directing partner. I did not record an agreed implementation plan.
- **Files changed:** AGENTS.md and worklog/katie.md.
- **Commit hash:** My starting revision was b282aa50a28ea095618a083ee06748392a1d4bb4.
  I subsequently authorized Codex to commit and push these documentation updates. The recording commit is the commit containing this entry.
- **Checks and actual results:** I checked Git status and the remote main ref;
  both pointed to the starting revision, with only __pycache__/ untracked.
  SHA-256 comparisons passed for baseline.json, the six instructor files,
  Mike's log, and CLAUDE.md. I reviewed the final diff and ran git diff --check.
  I did not run the evaluator because I changed no code.
- **Open questions:** I still need to compare refactoring proposals with my
  partner and agree on an implementation plan. I have not moved the general rules.

## 2026-10-31 - Synchronizing Mike's rule-confirmation log

- **Partner directing:** Katie (ksteve3).
- **Agent used:** Codex.
- **What I did:** I checked origin and my main branch, verified that I had no
  tracked local edits, and pulled Mike's new log entry with a fast-forward-only
  pull. I read the current AGENTS.md and followed the confirmed rule cards,
  separate partner logs, and documentation commit policy. I retained my existing
  log and appended this entry rather than recreating it.
- **Files changed:** The pull updated worklog/mike.md from Mike's commit; I did
  not edit his log. My own local change is this entry in worklog/katie.md.
- **Commit hash:** I synchronized to 5c1d42ee7f5e241f320d603656c42ce6b13321fb.
  This new log entry is uncommitted; I have not authorized a commit or push for it.
- **Checks and actual results:** `git remote -v` confirmed the existing
  https://github.com/ksteve3/week5-studio.git remote; my branch is main.
  `git status --short --branch`, `git diff`, and `git diff --cached` showed
  no tracked edits before pulling, only untracked __pycache__/.
  `git pull --ff-only origin main` succeeded. SHA-256 comparisons confirmed
  baseline.json, all six instructor files, AGENTS.md, and CLAUDE.md were unchanged.
  HEAD matched origin/main after pulling. I did not run the evaluator because
  I changed no code and did not recreate the baseline.
- **Open questions:** I still need to compare independent refactoring proposals
  with my partner and agree on a plan before implementation.

## 2026-10-31 - Checking readiness to compare proposals

- **Partner directing:** Katie (ksteve3).
- **Agent used:** Codex.
- **What I did:** I checked the latest shared rules and assignment status.
  I confirmed that my main branch already matches origin/main, so no pull was
  needed. I preserved my existing uncommitted log entry and appended this review.
  I found no independent refactoring proposal from Mike in the pushed files;
  his latest log still lists proposal comparison as open. TEAM_NOTES.md is blank.
- **Files changed:** Only worklog/katie.md in this session.
- **Commit hash:** HEAD and origin/main are
  5c1d42ee7f5e241f320d603656c42ce6b13321fb. This entry remains uncommitted.
- **Checks and actual results:** `git fetch origin` succeeded;
  `git rev-list --left-right --count HEAD...origin/main` returned 0 0.
  `git ls-remote --heads origin` listed only main. The protected-file diff
  against origin/main was empty. A read-only Python check using -B confirmed
  evaluate.search_is_unchanged() is True, baseline.json exists and records 5/6,
  and after.json is absent. The baseline SHA-256 remains
  2251ba4c22ed79180e870bdb294b00a8600a77e414a9ec2e7aff81ab15aa0ef9.
  I did not run --baseline or --after. I ran git diff --check for this log update.
- **Open questions:** I need Mike's independent proposal and our comparison and
  agreed implementation plan. I also need to complete team notes, paired
  extractions and final verification, add Mike's name to the README, and submit
  the repository link on Canvas. I cannot verify a Canvas submission from Git.

## 2026-10-31 - Saving my completed independent proposal

- **Partner directing:** Katie (ksteve3).
- **Agent used:** Codex.
- **What I did:** I supplied my completed Markdown proposal and asked Codex to
  save it exactly as KATIE_PROPOSAL.md in my Week 5 folder. I confirmed the
  destination did not exist before copying. This is my individual proposal,
  pending discussion with Mike, and does not represent an agreed team plan.
- **Files changed:** KATIE_PROPOSAL.md (new) and worklog/katie.md (this entry).
  I preserved my earlier uncommitted log entries.
- **Commit hash:** My starting revision is
  5c1d42ee7f5e241f320d603656c42ce6b13321fb. I subsequently authorized committing and pushing only my proposal and this log with the message "I add my independent Week 5 refactoring proposal". The recording commit is the commit containing this entry.
- **Checks and actual results:** I checked Git status and the remote main ref,
  which still matches my starting revision. A byte-for-byte comparison confirmed
  the saved proposal exactly matches my supplied Downloads file (3,185 bytes).
  SHA-256 checks confirmed search.py, baseline.json, TEAM_NOTES.md, and Mike's log
  were unchanged. I checked final Git status and ran git diff --check on my log.
  I did not run the evaluator because I changed no Python code.
- **Open questions:** I approved the proposed documentation commit and push.
  Mike and I still need to compare proposals and agree
  on an implementation plan before refactoring.

## 2026-10-31 - Extraction 1 prepared; evaluation blocked by checkout line endings

- **Partner directing:** Katie (Student A, ksteve3).
- **Agent used:** Codex. Mike (Student B) is assigned to review; I have not
  claimed his review is complete.
- **What I did:** I pulled Mike's agreed plan through 37c89de and verified the
  unchanged starter before editing. I extracted text_to_vector(text), preserving
  cleanup order and VOCAB counting, and replaced four text-processing sites.
  I left both cosine calculations, data, interfaces, and tie-breaking unchanged.
- **Files changed:** search.py; the evaluator created after.json; I appended
  this entry to worklog/katie.md. I did not edit evaluator, cases, baseline,
  team notes, or Mike's log. __pycache__/ remains untracked.
- **Commit hash:** Starting revision 37c89de; no extraction commit yet.
- **Checks and actual results:** `git pull --ff-only origin main` succeeded.
  The pre-edit instructor fingerprint passed, and protected-file hashes were
  unchanged by the pull. `python evaluate.py --after` returned 5/6 and FAIL.
  I diagnosed only fixture_sha256 differing: baseline expects LF case-file
  bytes, while Git checked out CRLF. LF-normalized hash equals the baseline's
  hash. A read-only in-memory run of HEAD's original starter also fails against
  this baseline; the extraction report exactly matches that starter's report.
  `git diff --check` passed; protected-file Git diff was empty.
- **Open questions:** I need approval to restore eval_cases.json to its exact
  original LF bytes before rerunning the evaluator. I will not change case
  contents or the evaluator or baseline. Mike's diff review and my approval
  remain required before committing, pushing, or starting Extraction 2.

## 2026-10-31 - Running the supplementary Extraction 1 diagnostic

- **Partner directing:** Katie (ksteve3).
- **Agent used:** Codex.
- **What I did:** I supplied eval-1b.py and asked Codex to save an exact copy
  and run it. I preserved the original failed after.json and did not rerun the
  official evaluator. I kept Extraction 1 unchanged while awaiting Mike's review.
- **Files changed:** eval-1b.py (new supplementary diagnostic) and this entry
  in worklog/katie.md. I preserved earlier uncommitted work.
- **Commit hash:** Starting revision 37c89de59a1443c03f6cae72650ed39d0c7fd8d9.
  I have not authorized a commit or push for this diagnostic session.
- **Checks and actual results:** `python eval-1b.py` exited 0:
  DIAGNOSTIC PASS, 5/6 correct, with all behavior matching the baseline after
  verifying the fixture differs only in CRLF/LF endings. The diagnostic adjusts
  the fixture hash only in memory after proving the normalized hash matches;
  it does not change expected answers or saved files. The original official
  `python evaluate.py --after` result remains 5/6 and FAIL, and is not replaced
  by this diagnostic result. SHA-256 checks passed for search.py, evaluate.py,
  eval_cases.json, baseline.json, after.json, TEAM_NOTES.md, and Mike's log.
  The preserved failed after.json hash is dc1302625393713e2ddab0aea4083bbe17ce76ba6d007815cb3ab2f331f924b8.
  I reviewed Git diff and status and ran git diff --check on tracked changes.
- **Open questions:** I still need Mike's review and an instructor-compatible
  resolution of the fixture line endings before an official PASS. I need approval
  before committing or pushing. I have not started Extraction 2.

## 2026-10-31 - Restoring the original fixture bytes and official verification

- **Partner directing:** Katie (Student A, ksteve3).
- **Agent used:** Codex.
- **What I did:** I authorized restoration of only eval_cases.json directly
  from origin/main using Git blob bytes. I backed up the local CRLF fixture
  and original failed after.json outside the repository at C:\Users\krste\projects\week5-studio-backup-20261031-163006.
  I verified the GitHub blob exactly matches the baseline fixture hash before
  writing it. I changed no questions or expected answers.
- **Files changed:** eval_cases.json now has its exact original LF bytes;
  the official evaluator updated after.json; I appended this work-log entry.
  My existing Extraction 1 remains unchanged and awaits Mike's review.
- **Commit hash:** Starting revision 37c89de59a1443c03f6cae72650ed39d0c7fd8d9.
  I have not authorized staging, committing, or pushing this session.
- **Checks and actual results:** I checked status, branch main, and the existing
  shared remote, then ran git fetch origin. The restored fixture SHA-256 is
  595290132310ec7eb0da1d2d2798dbd724b61238de3afb1138e01f0512686dbc, matching baseline.json.
  `python evaluate.py --after` exited 0: 5/6 correct AND PASS;
  results and scores match baseline. I did not run eval-1b.py.
  SHA-256 checks confirmed search.py, evaluate.py, baseline.json, TEAM_NOTES.md,
  Mike's log, and eval-1b.py unchanged. I reviewed Git diffs and status and ran
  git diff --check. I preserved failed evidence in the outside backup.
- **Open questions:** I still need Mike's Extraction 1 review and approval
  before committing or pushing. Extraction 2 has not begun.

## 2026-10-31 - Publishing Extraction 1 for Mike's review

- **Partner directing:** Katie (Student A, ksteve3).
- **Agent used:** Codex.
- **What I did:** I authorized pushing Extraction 1 for Mike's review. I reviewed
  the search.py diff and staged only that file for the code commit. I have not
  claimed Mike's review is complete and have not begun Extraction 2.
- **Files changed:** search.py was committed separately. This documentation
  commit includes worklog/katie.md and the official passing after.json report.
  I left eval-1b.py and __pycache__/ untracked and excluded eval_cases.json.
- **Commit hash:** I committed and pushed Extraction 1 as
  12aca650f159f7a0e6c5e67329372f4375d36bb5, with the message
  "I extract text_to_vector for Week 5 studio". This entry is recorded in the
  following documentation commit.
- **Checks and actual results:** I reviewed unstaged and staged changes and
  checked the remote main ref before committing. The staged diff check passed.
  The code push succeeded. My previous official evaluation returned 5/6 AND
  PASS; I verified after.json records behavior_preserved=true and correct=5.
  I rechecked that the restored fixture hash matches baseline.json. I made no
  additional code edits and did not rerun the supplementary diagnostic.
- **Open questions:** I await Mike's review before he directs Extraction 2.
  The earlier failed evaluation evidence remains in the outside backup.

## 2026-10-31 - Reviewing Mike's Extraction 2

- **Partner directing:** Katie (Student A, ksteve3), reviewing Mike's work.
- **Agent used:** Codex.
- **What I did:** I pulled through 77ef11e and reviewed Mike's Extraction 2
  commit 584a1c984b5b53a5a756a3784f852a87c3c5abd7 against its previous version.
  I verified first_vector and second_vector receive matching VOCAB count lists,
  the helper returns a float, zero handling is unchanged, and the dot product,
  squared norms, square roots, and division retain their original order.
  I verified search calls cosine_similarity(qv, v), and compare_texts returns
  cosine_similarity(av, bv). I found no change to data, interfaces, return
  structures, text_to_vector, or strict-greater-than tie-breaking.
- **Files changed:** The pull brought Mike's search.py and log updates. My only
  authored change is this log entry. The evaluator rewrote after.json with
  equivalent content. I did not edit instructor files or TEAM_NOTES.md.
- **Commit hash:** Review target 584a1c984b5b53a5a756a3784f852a87c3c5abd7;
  synchronized HEAD 77ef11e. My log entry is uncommitted.
- **Checks and actual results:** `python evaluate.py --after` returned 5/6 AND
  PASS, exit 0. I compared every baseline field: fixture_sha256, FAQ data,
  vocabulary, correct count, results (selections and all similarity scores),
  and comparison_probes all match; behavior_preserved is true. Spot checks with
  the first vector zero, second zero, and both zero returned 0.0. Protected-file
  SHA-256 checks passed across synchronization and evaluation. The LF fixture
  remained untouched. I ran git diff --check for the log update.
- **Line endings:** core.autocrlf is true; eval_cases.json is LF in the index
  and working file, but has no explicit attributes. I recommend the minimal
  root .gitattributes line `eval_cases.json text eol=lf`. I have not created or
  changed that file; I need approval first.
- **Open questions:** My review supports approval of Extraction 2. I prepared
  a message for Mike; I have not sent it. Mike still needs to perform the final
  Part 3 verification before I record final PASS in TEAM_NOTES.md. No commit
  or push is authorized for this session.

## 2026-10-31 - Approving Extraction 2 and preventing fixture conversion

- **Partner directing:** Katie (Student A, ksteve3).
- **Agent used:** Codex.
- **What I did:** I approved Mike's Extraction 2 based on my review and official
  passing evaluation. I authorized adding root .gitattributes containing only
  `eval_cases.json text eol=lf` to prevent Windows checkout conversion for that
  fixture. I did not modify case contents or expected answers.
- **Files changed:** .gitattributes (new) and worklog/katie.md. The official
  evaluator reran and wrote equivalent after.json content. I preserved earlier
  uncommitted review notes and did not change code or TEAM_NOTES.md.
- **Commit hash:** Starting revision 77ef11e760aab8c94b10337d7d7ea85d24a7bbd2.
  These changes are uncommitted and await my approval before commit or push.
- **Checks and actual results:** The fixture SHA-256 remains
  595290132310ec7eb0da1d2d2798dbd724b61238de3afb1138e01f0512686dbc,
  exactly matching baseline.json. `python evaluate.py --after` returned
  5/6 correct AND PASS, exit 0. SHA-256 checks confirmed search.py, evaluate.py,
  baseline.json, eval_cases.json, TEAM_NOTES.md, and Mike's log unchanged.
  I reviewed Git diff and ran git diff --check. I checked the effective fixture
  attributes and line endings. I did not stage, commit, or push.
- **Open questions:** Mike still needs to run the required final Part 3 check.
  I prepared an approval message, but have not sent it or recorded final results
  in TEAM_NOTES.md. Proposed commits: the LF attribute rule first, then my
  separate review and verification log.

## 2026-10-31 - Publishing my review and LF fixture rule

- **Partner directing:** Katie (ksteve3).
- **Agent used:** Codex.
- **What I did:** I reported that Mike completed his final Part 3 verification:
  5/6 correct AND PASS, exit 0, behavior_preserved=true. This is Mike's reported
  result, not a new test run by me. I authorized the two specified commits and
  their push. I left TEAM_NOTES.md and README.md to Mike.
- **Files changed:** .gitattributes in the first commit; only worklog/katie.md
  in the second. I preserved the earlier review and evaluation entries above.
- **Commit hash:** LF rule commit eb3ce54fde6776fb431783dc12d6af55f92dd98b.
  This entry and my pending review are recorded in the following log commit.
- **Checks and actual results:** I fetched origin and ran
  `git pull --ff-only origin main`: already up to date at 77ef11e. I reviewed
  staged diffs and file lists for each commit and excluded unrelated files.
  I verified the fixture still matches the baseline hash. My previous official
  evaluation was 5/6 AND PASS; I did not rerun it for this documentation-only
  publication. I did not change the instructor evaluation files, code, team
  notes, README, or Mike's log. My supplementary script and cache stay untracked.
- **Open questions:** Mike is handling the final shared documentation updates.
