# Summary

## Approach

I started with a structured exploratory pass across all five SauceDemo user types before writing any test cases, since the prompt hints that different credentials reveal different behaviors. That pass surfaced four real defects of varying severity, which shaped everything downstream: test scenarios, manual test case prioritization, and automation scope.

For prioritization, I used a risk-based, business-impact-first model — transaction-blocking issues first, then partial functional failures, then usability-degrading issues, then cosmetic ones. The same model drove which defects were selected for automation.

The assignment asks for 2–3 automated test cases including at least one negative scenario. I automated exactly three, each answering a distinct question rather than clustering around one theme:

1. **Checkout completion**, parameterized across `standard_user` (succeeds) and `problem_user` (fails on a Last Name field defect that blocks checkout entirely) — the most business-critical flow in the app, and the most severe confirmed defect.
2. **Locked-out login** (`locked_out_user`) — satisfies the negative-scenario requirement with a clean, independent case.
3. **Standard add-to-cart** — core purchasing functionality, kept intentionally simple and matched to the manual test case's literal scope.

Full manual test case documentation (22 cases, prioritized and rationalized) and the complete test scenario list are in `/docs`.

## Framework Choice

I used **Playwright with Python and pytest**. My production automation background is Python-based, and pytest's fixture system and `parametrize` decorator made it straightforward to express "same scenario, different expected outcome by user" cleanly — used throughout, most notably in the checkout test.

Locator strategy was deliberate and consistent: `data-test` attributes where SauceDemo provides static, generic ones (form fields, cart badge), and role-based locators (`get_by_role`) where IDs are dynamic and product-specific (Add to Cart buttons, images) — avoiding the fragility of reconstructing SauceDemo's ID-slugification pattern for every product name.

One implementation detail worth noting: the checkout form fields are filled using `.type()` rather than `.fill()`, specifically because the Last Name defect lives in keystroke-event handling — `.fill()` sets a field's value directly and would likely have missed the bug entirely.

## Bugs Found

Four defects were identified during exploratory testing, all specific to `problem_user`:

| Bug         | Severity        | Description                                                                                   | Automated Evidence                 |
| ----------- | --------------- | --------------------------------------------------------------------------------------------- | ---------------------------------- |
| **BUG-001** | Highest         | Last Name field on checkout misdirects keystrokes into First Name, blocking checkout entirely | Yes — Test 1                       |
| **BUG-002** | High            | "Add to Cart" silently fails for 3 of 6 catalog items                                         | No — documented via manual testing |
| **BUG-003** | Medium          | All non-default sort options fail to reorder products                                         | No — documented via manual testing |
| **BUG-004** | Medium/Cosmetic | All product images render identically                                                         | No — documented via manual testing |

BUG-001 is the headline finding: a full transaction failure for an entire user segment, now protected by a passing regression test that will catch any incomplete fix. BUG-002 through BUG-004 were deliberately left out of the automated scope to stay within the assignment's requested test-case limit — full manual test cases and rationale for each are documented in `/docs/manual-test-cases.md`.

## What I'd Add With More Time

- **Data-driven product listing verification** — I built and verified the underlying support for this (`InventoryPage.get_product_details`, a `products.py` test-data file) but didn't wire it into a fourth automated test, to stay within scope.
- **Automated coverage for BUG-002, BUG-003, and BUG-004** — all three are real, reproducible defects currently protected only by manual test cases.
- **Trace and video capture on failure**, and a broader cross-browser CI matrix as standard rather than an on-demand flag.
- **Formal performance testing** — `performance_glitch_user` shows real, measurable latency on login, sort, and navigation that I only observed qualitatively.

A more complete list of considered-but-deferred work, with reasoning, is in `/docs/future-additions.md`.
