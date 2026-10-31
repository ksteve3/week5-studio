# Mike's Week 5 refactoring proposal

Hi Katie, here's my independent proposal for comparing with yours.
No code has been changed.

## What repeats in search.py

| Job | Repeats | Lines |
| --- | --- | --- |
| Clean the text (strip, lowercase, remove `?` and `.`) | 4 times | 16, 20, 43, 44 |
| Count the 8 vocabulary words | 4 times | 17, 21, 45, 46 |
| Score two count lists (cosine similarity) | 2 times | 22–32, 47–56 |

Cleaning and counting always happen together, in the same order, so I
combine them. That lets two extractions remove all three repeats.

## My two functions

**1. `clean_count(text)`**
- **In:** any text (a question or an FAQ answer).
- **Out:** a list of 8 counts, one per vocabulary word.
  For example, "How do I reset my password?" gives `[1, 0, 0, 0, 0, 0, 0, 0]`.
- **Called from:** `search` (the query, and each FAQ inside the loop) and
  `compare_texts` (both texts). That's 4 uses.

**2. `score(first, second)`**
- **In:** two lists of 8 counts.
- **Out:** one number from 0 to 1. It returns 0.0 if either list is all zeros.
- **Called from:** `search` (once per FAQ inside the loop) and `compare_texts`.
  That's 2 uses. `compare_texts` becomes one line:
  `return score(clean_count(first), clean_count(second))`.

The loop in `search` still builds the list of scores and picks the winner,
so its return shape stays the same.

## Behavior to protect during the refactor

- Keep the math order: `dot / (sqrt(a) * sqrt(b))`, not `sqrt(a * b)`.
  Small rounding differences could fail the baseline check.
- Keep the zero guard. `compare_texts("", "password")` must still return 0.0.
- Keep the tie-break in `search`: the first FAQ wins a tie, so q6 still
  misses (5/6 expected).

## Open for discussion

- **Names.** I'm open to clearer names. My agent independently proposed
  the same two functions as `text_to_vector(text)` and
  `cosine_similarity(first_vector, second_vector)`.
- **Roles.** Who directs extraction 1, and who directs extraction 2?
