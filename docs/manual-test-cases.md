# Manual Test Cases — SauceDemo QA Suite

**Prioritization approach:** Risk-based, weighted toward financial/business impact first (transaction-blocking > partial functional failure > degraded UX > cosmetic), consistent with the approach applied to automation scope selection. Each case below is labeled with a Priority and a one-line rationale. Cases marked **[Automated]** correspond directly to a test in the automated suite (see `/tests/specs`); all others are manual-only, included because they represent real, verifiable coverage of the in-scope flows or confirmed exploratory findings — not because every scenario needed automating.

## Prioritization Model

Test cases are prioritized using a **risk-based, business-impact-first model**:

- **Highest/High:** Transaction-blocking or catalog-availability defects, and any core flow whose failure directly prevents a purchase or corrupts financial/order data (login gateway, checkout completion, order accuracy, add-to-cart at scale).
- **Medium:** Standard functional and validation coverage that affects usability or data integrity but does not, on its own, block a transaction (individual field validation, cart persistence, sort correctness, cosmetic-but-catalog-relevant defects).
- **Low:** Non-functional observations (performance/timing) noted for completeness and to inform future test strategy, but not treated as functional pass/fail defects in this round of testing.

**Automation scope:** The take-home challenge asks for 2–3 automated test cases, including at least one negative scenario. Three test cases were selected, each answering a distinct, non-overlapping question rather than clustering around a single theme:

1. **TC-4.1 / TC-4.6 (combined, parameterized by user)** — does checkout complete successfully (`standard_user`), and is it correctly, verifiably blocked by the highest-severity defect found during exploratory testing (`problem_user`)? This is the single most business-critical flow in the application and the most severe confirmed defect.
2. **TC-1.2** — is a locked-out account correctly rejected at login? Satisfies the negative-scenario requirement with a clean, unambiguous case distinct from the checkout defect.
3. **TC-3.1** — can a standard user add an item to the cart? Core purchasing functionality, and deliberately kept to a single item/single user to match the manual case's literal scope rather than expanding into full-catalog or multi-user coverage.

Together these three tests cover a blocking defect, a negative-auth case, and core happy-path functionality — three genuinely different kinds of risk, rather than several tests clustered around the same underlying theme. Other confirmed defects (BUG-002, BUG-003, BUG-004) and additional scenarios (TC-3.2, TC-3.5, TC-3.6, TC-2.1, TC-2.6) were deliberately scoped out of automation to stay within the assignment's requested 2–3 test limit; see `future-additions.md` for what was considered and why it was set aside rather than built. Sort (TC-2.7) was also kept manual-only, as a usability-degrading rather than transaction-blocking issue.

**Note on test case numbering:** Test case IDs correspond to scenario numbers from the Test Scenarios document (`test-scenarios.md`, Part 1). Not every scenario was promoted to a full manual test case — see the Prioritization Model above for selection criteria. For example, scenarios 2.3–2.5 (individual non-default sort variants: Name Z-A, Price low-high, Price high-low) were consolidated into TC-2.7, which covers the same underlying defect (non-default sort options are broken) without three redundant, near-identical test cases. Gaps in numbering are therefore intentional consolidations, not omissions.

---

## 1. Login / Logout

### TC-1.1 — Standard user can log in successfully

- **Priority:** High — gateway to every other flow; nothing else is reachable if this fails.
- **Preconditions:** Valid `standard_user` credentials known; browser at SauceDemo login page.
- **Steps:** 1) Enter username `standard_user`. 2) Enter password `secret_sauce`. 3) Click Login.
- **Expected Result:** User is redirected to the product listing (inventory) page.
- **Pass/Fail:** Pass if inventory page loads with products visible; Fail if login is rejected or page does not redirect.

### TC-1.2 — Locked-out user is blocked from logging in **[Automated]**

- **Priority:** High — required negative-path coverage; validates account-restriction logic works correctly.
- **Preconditions:** `locked_out_user` credentials known.
- **Steps:** 1) Enter username `locked_out_user`. 2) Enter password `secret_sauce`. 3) Click Login.
- **Expected Result:** Login is rejected; an error message indicating the account is locked out is displayed.
- **Pass/Fail:** Pass if error message appears and user remains on login page; Fail if login succeeds or no error is shown.

### TC-1.3 — Login rejected with invalid username

- **Priority:** Medium — standard input-validation coverage.
- **Preconditions:** Browser at login page.
- **Steps:** 1) Enter an unrecognized username. 2) Enter any password. 3) Click Login.
- **Expected Result:** Login is rejected with an appropriate error message; no session is created.
- **Pass/Fail:** Pass if error shown and user stays on login page; Fail if login succeeds.

### TC-1.4 — Login rejected with invalid password

- **Priority:** Medium — standard input-validation coverage.
- **Preconditions:** Browser at login page; valid username known.
- **Steps:** 1) Enter a valid username. 2) Enter an incorrect password. 3) Click Login.
- **Expected Result:** Login is rejected with an appropriate error message.
- **Pass/Fail:** Pass if error shown; Fail if login succeeds.

### TC-1.5 — Login rejected with empty fields

- **Priority:** Medium — basic required-field validation.
- **Preconditions:** Browser at login page.
- **Steps:** 1) Leave username and password blank. 2) Click Login.
- **Expected Result:** Login is rejected; validation message indicates required fields.
- **Pass/Fail:** Pass if error shown and no session created; Fail if login proceeds.

### TC-1.6 — Problem user can log in successfully

- **Priority:** Medium — precondition check confirming the account itself is accessible before testing its downstream defects.
- **Preconditions:** `problem_user` credentials known.
- **Steps:** 1) Enter username `problem_user`. 2) Enter password `secret_sauce`. 3) Click Login.
- **Expected Result:** User is redirected to the inventory page successfully (login itself is unaffected by this account's other defects).
- **Pass/Fail:** Pass if inventory page loads; Fail if login is blocked.

### TC-1.7 — Performance-glitch user login completes (with delay)

- **Priority:** Low — non-functional observation, not a correctness defect.
- **Preconditions:** `performance_glitch_user` credentials known.
- **Steps:** 1) Enter username `performance_glitch_user`. 2) Enter password `secret_sauce`. 3) Click Login.
- **Expected Result:** Login eventually succeeds; response time is noticeably slower than `standard_user` baseline.
- **Pass/Fail:** Pass if login completes correctly regardless of delay (delay is noted, not a failure condition, per functional test scope); flagged separately as a performance observation.

### TC-1.8 — Standard user can log out successfully

- **Priority:** High — session termination is a basic security/functional expectation.
- **Preconditions:** Logged in as `standard_user`.
- **Steps:** 1) Open menu. 2) Click Logout.
- **Expected Result:** User is returned to the login page; session is terminated.
- **Pass/Fail:** Pass if login page is shown and authenticated pages are no longer accessible; Fail otherwise.

---

## 2. Product Listing & Sorting

### TC-2.1 — Product listing displays complete, correct item details

- **Priority:** High — core catalog integrity; directly affects purchasing confidence.
- **Preconditions:** Logged in as `standard_user`.
- **Steps:** 1) Load inventory page. 2) Verify all expected products are present. 3) Verify each has name, description, price, and image.
- **Expected Result:** All 6 products visible with complete, correct details; each product has a distinct image.
- **Pass/Fail:** Pass if all fields present and images are unique per product; Fail if any product is missing details or shares an image with another. _(Verified manually; supporting page object method (`InventoryPage.get_product_details`) and test data file were built and verified but not wired into an automated test — see `future-additions.md`.)_

### TC-2.2 — Default sort (Name A–Z) displays correct order

- **Priority:** Medium — default state correctness, high visibility (first thing every user sees).
- **Preconditions:** Logged in as `standard_user`.
- **Steps:** 1) Load inventory page. 2) Observe default sort order.
- **Expected Result:** Products are listed in ascending alphabetical order by name.
- **Pass/Fail:** Pass if order is correctly alphabetical; Fail otherwise.

### TC-2.6 — Problem user: product images are duplicated/incorrect

- **Priority:** Medium — cosmetic but catalog-integrity-relevant.
- **Preconditions:** Logged in as `problem_user`.
- **Steps:** 1) Load inventory page. 2) Compare images across all 6 products.
- **Expected Result (per spec):** Each product should display a distinct, correct image.
- **Actual Result (known defect):** All products display an identical placeholder image.
- **Pass/Fail:** Fail (documented defect — see BUG-004). _(Manual finding; not automated — see `future-additions.md`.)_

### TC-2.7 — Problem user: non-default sort options do not function

- **Priority:** Medium — degrades usability but does not block purchasing; deliberately excluded from automation scope in favor of higher-risk defects (see rationale below).
- **Preconditions:** Logged in as `problem_user`.
- **Steps:** 1) Load inventory page. 2) Select each non-default sort option (Name Z–A, Price low–high, Price high–low) in turn. 3) Observe resulting order.
- **Expected Result:** Products reorder correctly per the selected sort option.
- **Actual Result (known defect):** Only the default (Name A–Z) sort functions; all other options fail to reorder products.
- **Pass/Fail:** Fail (documented defect — see BUG-003).

### TC-2.8 — Performance-glitch user: sort completes (with delay)

- **Priority:** Low — non-functional observation.
- **Preconditions:** Logged in as `performance_glitch_user`.
- **Steps:** 1) Select any sort option. 2) Observe response time.
- **Expected Result:** Sort completes correctly with a noticeably longer response time than baseline.
- **Pass/Fail:** Pass if sort eventually completes correctly; delay noted separately as a performance observation.

---

## 3. Add to Cart / Remove from Cart

### TC-3.1 — Standard user can add an item to the cart **[Automated]**

- **Priority:** High — core purchasing functionality; the most fundamental purchase action in the application.
- **Preconditions:** Logged in as `standard_user`, on inventory page.
- **Steps:** 1) Click "Add to Cart" on any product. 2) Observe cart icon badge.
- **Expected Result:** Item is added; cart badge count increases to 1.
- **Pass/Fail:** Pass if badge updates correctly and item appears in cart; Fail otherwise.

### TC-3.2 — Standard user can add multiple items to the cart

- **Priority:** High — core purchasing functionality at realistic scale.
- **Preconditions:** Logged in as `standard_user`.
- **Steps:** 1) Click "Add to Cart" on 3 different products. 2) Observe cart badge.
- **Expected Result:** Cart badge reflects a count of 3; all 3 items appear in cart.
- **Pass/Fail:** Pass if count and contents are correct; Fail otherwise. _(Verified manually; single-item add automated in TC-3.1 — see `future-additions.md`.)_

### TC-3.3 — Standard user can remove an item from the cart

- **Priority:** Medium — standard cart management functionality.
- **Preconditions:** At least one item in cart.
- **Steps:** 1) Navigate to cart. 2) Click "Remove" on an item.
- **Expected Result:** Item is removed; cart badge count decreases accordingly.
- **Pass/Fail:** Pass if item is removed and count updates; Fail otherwise.

### TC-3.4 — Cart contents persist across navigation

- **Priority:** Medium — user experience/data integrity; prevents accidental cart loss.
- **Preconditions:** At least one item in cart.
- **Steps:** 1) Add item to cart. 2) Navigate away from cart page (e.g., to a product detail page or back to listing). 3) Return to cart.
- **Expected Result:** Cart contents remain unchanged.
- **Pass/Fail:** Pass if item(s) still present; Fail if cart is emptied or altered. _(Confirmed working as expected during exploratory testing.)_

### TC-3.5 — Problem user: "Add to Cart" fails for specific items

- **Priority:** High — direct, partial catalog unavailability; real lost-sale impact.
- **Preconditions:** Logged in as `problem_user`.
- **Steps:** 1) Attempt to add "Sauce Labs Bolt T-Shirt" to cart. 2) Attempt to add "Sauce Labs Fleece Jacket" to cart. 3) Attempt to add "Test.allTheThings() T-Shirt (Red)" to cart. 4) Observe cart badge after each attempt.
- **Expected Result:** Each item is added successfully; cart badge increments accordingly.
- **Actual Result (known defect):** None of the 3 items are added; cart badge does not update; no error is shown to the user.
- **Pass/Fail:** Fail (documented defect — see BUG-002). _(Manual finding; not automated — see `future-additions.md`.)_

### TC-3.6 — Problem user: "Add to Cart" functions correctly for unaffected items

- **Priority:** Medium — confirms partial (not total) failure scope; important for accurately characterizing BUG-002's severity and impact.
- **Preconditions:** Logged in as `problem_user`.
- **Steps:** 1) Attempt to add each of the remaining 3 catalog items (not in the known-broken list) to cart. 2) Observe cart badge after each.
- **Expected Result:** Each item is added successfully.
- **Pass/Fail:** Pass if all 3 unaffected items add correctly, confirming the defect is isolated to the specific items identified in TC-3.5. _(Verified manually; not automated — see `future-additions.md`.)_

---

## 4. Checkout Flow

### TC-4.1 — Standard user can complete checkout successfully **[Automated]**

- **Priority:** High — core revenue-generating flow; highest business criticality in the application.
- **Preconditions:** Logged in as `standard_user`; at least one item in cart.
- **Steps:** 1) Navigate to cart. 2) Click Checkout. 3) Enter valid First Name, Last Name, Zip/Postal Code. 4) Click Continue. 5) Review order. 6) Click Finish.
- **Expected Result:** Order completes successfully; confirmation page is displayed.
- **Pass/Fail:** Pass if confirmation is reached; Fail if any step is blocked or errors. _(Automated together with TC-4.6 as a single parameterized test, varying by user.)_

### TC-4.2 — Checkout rejects submission with missing required fields

- **Priority:** Medium — standard input validation on a critical form.
- **Preconditions:** Logged in as `standard_user`; item in cart; on Checkout Step 1.
- **Steps:** 1) Leave one or more required fields blank. 2) Click Continue.
- **Expected Result:** Submission is rejected; validation error is displayed indicating the missing field.
- **Pass/Fail:** Pass if error shown and user remains on Step 1; Fail if submission proceeds.

### TC-4.3 — Order confirmation is accurate

- **Priority:** High — financial/data accuracy; incorrect order confirmation is a serious trust and billing concern.
- **Preconditions:** Standard checkout in progress with known cart contents.
- **Steps:** 1) Complete checkout through to confirmation. 2) Compare confirmation details (items, total) against original cart contents.
- **Expected Result:** Confirmation accurately reflects the items and total from the cart.
- **Pass/Fail:** Pass if details match exactly; Fail if any discrepancy is found.

### TC-4.4 — Cart empties after successful checkout

- **Priority:** Medium — data integrity; prevents duplicate/accidental reorder confusion.
- **Preconditions:** Checkout completed successfully.
- **Steps:** 1) Complete checkout. 2) Navigate back to cart.
- **Expected Result:** Cart is empty.
- **Pass/Fail:** Pass if cart shows 0 items; Fail if prior items remain.

### TC-4.5 — User can cancel checkout and retain cart contents

- **Priority:** Low-Medium — usability/recovery path, not revenue-blocking on its own.
- **Preconditions:** In checkout flow with items in cart.
- **Steps:** 1) Begin checkout. 2) Click Cancel. 3) Navigate to cart.
- **Expected Result:** User is returned to cart; cart contents remain unchanged.
- **Pass/Fail:** Pass if cart is intact; Fail if items are lost.

### TC-4.6 — Problem user: checkout blocked by non-functional Last Name field **[Automated]**

- **Priority:** Highest — total transaction failure for an entire user segment; single most severe defect identified.
- **Preconditions:** Logged in as `problem_user`; item in cart; on Checkout Step 1.
- **Steps:** 1) Enter valid First Name. 2) Click into Last Name field and type a valid last name. 3) Observe both fields.
- **Expected Result:** Last Name field accepts and displays the typed input; First Name field remains unchanged.
- **Actual Result (known defect):** Last Name field does not accept input; each keystroke instead overwrites First Name's contents with a single character. Last Name remains empty, blocking valid form submission and preventing checkout completion.
- **Pass/Fail:** Fail (documented defect — see BUG-001; highest-severity finding). _(Automated together with TC-4.1 as a single parameterized test, varying by user — this is the project's headline automated defect.)_
