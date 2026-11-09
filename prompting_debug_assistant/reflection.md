# Reflection on AI-Assisted Debugging

## Introduction
I created six buggy snippets in Python, JavaScript and Java, asked an AI assistant to diagnose each one, applied and tested the fixes, and wrote formal bug reports. The goal was to see where AI really helps in debugging and where a human still has to decide. Running every snippet first and giving the AI the real error output made the whole process more reliable.

## AI Strengths
The easiest bug was `bug3.java`. The compiler messages (`';' expected`, `unclosed character literal`) point almost directly at the problem, and the AI correctly explained all five syntax mistakes and the reason for seven errors. `bug1.py` and `bug2.js` were also easy. The stack trace `TypeError: Cannot read properties of undefined (reading 'city')` gave the exact line, and optional chaining was the right fix immediately.

The AI was also very good at reading a bug that had several layers. In `bug4.py`, the first crash was `TypeError: the JSON object must be str, bytes or bytearray, not dict`. The AI found that three more errors were hidden behind it: string addition, `input()` returning text, and a wrong date format. I would likely have found them one by one.

## AI Weaknesses
The hardest bug was `bug5.js`, because the program ran without any error. There was no stack trace, only wrong output (`72 E true`). The AI needed the expected behavior to find the real cause. It also showed that a plausible fix can be incomplete: changing only `>` to `>=` still gave `E, E, E, F`, because the order of conditions was the real problem.

Similarly, the shorter slice `items[-n:]` looked correct for `bug1.py`, but it failed for `n = 0` and returned the whole list. I only found this because I tested it.

## Human Role
Human intuition was needed to define "correct". The AI cannot know that 50 is the minimum passing score or that `"UNKNOWN"` is a good fallback value. I also had to decide whether `age > 18` was a bug or a business rule, so I kept it unchanged. Verification was a human job too. My validation notes at first said `add(10, 5)` returns `15.0`, but the method returns the integer `15`. A reviewer caught this, which shows that even documentation of a fix needs checking. I also had to shorten two test files to meet the 40-line limit.

## Conclusion
My trust level is high for syntax errors and clear stack traces, and medium for logic bugs, where I want to run my own tests before accepting a fix. Overall the AI made diagnosis much faster, but the full process was not much shorter, because testing and documenting took the time that I saved. In real-world debugging, AI works best as a fast, knowledgeable assistant that proposes hypotheses, while a human supplies the requirements, the edge cases and the final verification.
