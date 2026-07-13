# What I'd Add With More Time

This document exists for two purposes: it's genuine content for the final summary deliverable, and — just as importantly — it's a deliberate parking lot for good ideas that don't belong in the required 2-3 automated tests. The take-home explicitly asks for 2-3 automated test cases including one negative scenario. Anything below this line is _documented and considered_, not built, so the actual test suite stays tightly scoped, explainable, and true to what was asked.

**Standing rule for the rest of this build:** if an idea for additional test coverage comes up, it goes here first. It does not go into the test suite unless we explicitly, deliberately decide to spend one of the 2-3 (or the one optional 3rd) slots on it, with a clear reason why it's more important than what it would replace.

---

## Additional Test Coverage Considered

**Data-driven, parameterized product listing verification** (across `standard_user` and `problem_user`, checking name/description/price/image integrity via an external test-data fixture). This would demonstrate data-driven test design and catch the duplicate-image bug (BUG-004) with automated evidence. Deliberately not included in the required 2-3 tests to keep the automated suite tightly scoped to the assignment's actual ask; the underlying page object support (`InventoryPage.get_product_details`) was still built and verified manually, so this could be added quickly if desired.

**Full-catalog add-to-cart verification** (looping all 6 products for both users, rather than a single targeted item). More thorough than the manual test cases (TC-3.1, TC-3.2, TC-3.5, TC-3.6) strictly require, but expands one test's scope well beyond "2-3 tests total" if treated as its own dedicated test. The single, narrowly-scoped version (one known-broken item, `problem_user`) was chosen instead to stay within the assignment's requested scope.

**Sort functionality testing** (TC-2.7, confirmed defect — non-default sort options broken). Medium priority per the risk-based model in the manual test cases (degrades usability, doesn't block a transaction) — deliberately kept manual-only rather than automated, consistent with prioritizing the two highest-severity, transaction-blocking/catalog-availability defects for the limited automation budget.

**Cart persistence and removal flows** (TC-3.3, TC-3.4). Verified manually and confirmed working correctly; not automated, as they weren't identified as high-risk findings requiring regression protection.

## Infrastructure/Engineering Additions Considered

**Cross-browser execution** (Chromium, Firefox, WebKit) — Playwright supports this with minimal config; not yet added, worth doing if time allows as a low-cost way to demonstrate broader tooling awareness without expanding the _number_ of test cases.

**CI integration** (GitHub Actions or equivalent) — running the suite automatically on push/PR, with report artifacts uploaded. High-value, low-cost addition; doesn't add test cases, just execution infrastructure around the existing ones.

**Trace/video/screenshot capture on failure** — Playwright's built-in `trace`/`video`/`screenshot` config options, providing rich debugging evidence for any test failure without adding new tests.

**Performance testing** — noted from exploratory testing (`performance_glitch_user` shows real, measurable delays on login/sort/navigation). Not functionally tested here since it's a non-functional concern; would use a dedicated tool (e.g., Playwright's own timing APIs, or a proper load-testing tool) in a fuller engagement.

## Why These Were Deliberately Excluded, Not Forgotten

The assignment scope is 2-3 automated test cases. Every item above is a legitimate, considered piece of engineering judgment — deliberately not built, so the delivered suite stays small, explainable, and squarely matched to what was actually asked, rather than expanding because it was _possible_ to expand it. This document is the evidence that the scope discipline was a choice, not an oversight.
