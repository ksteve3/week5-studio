# Team notes — short phrases are enough

Partners: A = Katie (ksteve3); B = Mike (LBXMike)

- A's proposed functions (names, inputs → outputs):
  `text_to_vector(text)` → list of VOCAB word counts;
  `cosine_similarity(first_vector, second_vector)` → float score
  (0.0 if either vector is all zeros).
- B's proposed functions (names, inputs → outputs):
  `clean_count(text)` → list of 8 word counts;
  `score(first, second)` → number from 0 to 1. Same two functions as A.
- Our agreed plan (at most two function extractions) and why:
  1. `text_to_vector(text)` → list of word counts. A directs (Codex), B reviews.
  2. `cosine_similarity(first_vector, second_vector)` → float. B directs
     (Claude Code), A reviews.
  Why: cleaning (4x), counting (4x) and scoring (2x) are repeated; two
  extractions remove all three. We use A's names because they say what each
  function returns. Keep the original cleanup order, arithmetic order, zero
  check and strict `>` tie-break so scores match the baseline.
- Before: 5 / 6. After: ___ / 6. Behavior check: ___
