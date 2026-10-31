# My Independent Refactoring Proposal — Week 5 Studio

**Student:** Katie (`ksteve3`)  
**Status:** Independent proposal; pending discussion with Mike (`LBXMike`)

## My understanding of the program

I reviewed the original `search.py` with my coding agent. I understand it as a small FAQ search program that compares a question against three FAQ entries: password reset, travel expenses, and vacation leave. It cleans the text, counts the occurrences of words in the fixed `VOCAB` list, and uses cosine similarity to select the highest-scoring FAQ. The `search(query)` function returns the selected FAQ ID, its score, and all candidate scores. The separate `compare_texts(first, second)` function calculates a similarity score between two supplied strings.

The vectors contain word counts, not learned semantic embeddings. The program therefore does not recognize synonyms that are missing from its vocabulary.

## Repetition I identified

I found that the same cleanup and vocabulary-counting operations appear when processing the query, each FAQ, and both arguments to `compare_texts`. I also found that the dot-product, vector-magnitude, and cosine-similarity calculations are repeated in `search` and `compare_texts`.

## My proposed function extractions

| Function | Parameters | Return value | Where I would call it |
| --- | --- | --- | --- |
| `text_to_vector(text)` | One text string | A list of integer word counts in the existing `VOCAB` order | For the query and each FAQ in `search`, and for both inputs in `compare_texts` |
| `cosine_similarity(first_vector, second_vector)` | Two word-count vectors | A floating-point cosine similarity score, or `0.0` if either vector has zero magnitude | For each query–FAQ comparison in `search`, and for the two vectors in `compare_texts` |

I would have `text_to_vector` use the original cleanup steps, in the original order: `strip()`, `lower()`, removal of `?`, and removal of `.`. It would then count vocabulary words just as the starter code does.

I would have `cosine_similarity` reuse the original arithmetic loop and zero-vector check without changing the sequence of operations.

## How I would preserve behavior

I would keep the original `FAQS` data, `VOCAB` ordering, public function signatures, and return structures. I would preserve the existing FAQ selection loop, including its strict `>` comparison so tied scores still select the earliest matching FAQ. I would not add dependencies, new features, or semantic matching.

My original baseline was **5/6 correct**, which is the expected starting result. I would leave the known sixth-case limitation unchanged and preserve `baseline.json`. After Mike and I agree on a plan and implement each extraction together, I would run `python evaluate.py --after` after each change. The expected result is **5/6 correct AND PASS**, including matching scores and comparison probes—not just matching total accuracy.

## Collaboration status

This is my independent proposal. I have not yet compared it with Mike's proposal, and I am not claiming that we have agreed on these functions. I have not refactored `search.py` or updated `TEAM_NOTES.md` with a team decision.
