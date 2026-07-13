# Test Scenarios — SauceDemo QA Suite

Scenarios are organized by flow, covering happy path, edge cases, negative cases, and user-type-specific behavior discovered during exploratory testing.

---

## 1. Login / Logout

- **1.1** — Standard user can log in successfully with valid credentials
- **1.2** — Locked-out user is blocked from logging in and shown an appropriate error message
- **1.3** — Login is rejected with an invalid username
- **1.4** — Login is rejected with an invalid password
- **1.5** — Login is rejected with empty username and/or password fields
- **1.6** — Problem user can log in successfully (login itself is unaffected despite other defects on this account)
- **1.7** — Performance-glitch user can log in successfully, though with a noticeable delay compared to baseline
- **1.8** — Standard user can log out successfully and is returned to the login page
- **1.9** — Logged-out session cannot access authenticated pages directly via URL (session/route protection check)

## 2. Product Listing & Sorting

- **2.1** — Product listing page displays all expected products with name, image, description, and price for standard user
- **2.2** — Default sort (Name A–Z) displays products in correct alphabetical order
- **2.3** — Sort by Name Z–A correctly reverses alphabetical order
- **2.4** — Sort by Price (low to high) correctly orders products ascending by price
- **2.5** — Sort by Price (high to low) correctly orders products descending by price
- **2.6** — _[Problem user]_ All product images render identically instead of showing distinct product images
- **2.7** — _[Problem user]_ Sort options other than the default (Name A–Z) do not correctly reorder products
- **2.8** — _[Performance-glitch user]_ Sorting action completes correctly but with a noticeable delay compared to baseline

## 3. Add to Cart / Remove from Cart

- **3.1** — Standard user can add a single item to the cart, and the cart badge count updates correctly
- **3.2** — Standard user can add multiple items to the cart, and the cart badge count reflects the correct total
- **3.3** — Standard user can remove an item from the cart, and the cart badge count decreases correctly
- **3.4** — Cart contents persist correctly when navigating away from and back to the cart page
- **3.5** — _[Problem user]_ "Add to Cart" is non-functional for specific items (Sauce Labs Bolt T-Shirt, Sauce Labs Fleece Jacket, Test.allTheThings() T-Shirt (Red)) — clicking produces no effect and item is not added
- **3.6** — _[Problem user]_ "Add to Cart" functions correctly for the remaining 3 of 6 catalog items (partial-failure scope check)

## 4. Checkout Flow

- **4.1** — Standard user can complete checkout successfully from cart through order confirmation
- **4.2** — Checkout Step 1 (Your Information) rejects submission when required fields are missing
- **4.3** — Order confirmation/receipt is generated and accurate (matches items and total from cart) for standard user
- **4.4** — Cart empties correctly after successful checkout completion
- **4.5** — User can cancel out of checkout and return to the cart with contents intact
- **4.6** — _[Problem user]_ Last Name field on Checkout Step 1 does not accept input correctly — keystrokes are misdirected into the First Name field, overwriting its contents and preventing valid Last Name entry, which blocks checkout completion entirely for this user

---

## Notes on Scope

- Scenarios tagged _[Problem user]_ or _[Performance-glitch user]_ reflect defects or behaviors discovered during exploratory testing specific to those accounts, documented in full in the exploratory observation log and, where applicable, formal bug reports (see `/docs/bug-reports/`).
- Scenario 1.9 (session/route protection) is included as a security-adjacent edge case that extends beyond the four explicitly listed flows but is a reasonable and common inclusion for a login/logout scenario set.
- Per the take-home instructions, 2–3 scenarios were selected for automation (see `manual-test-cases.md` for the full prioritization rationale): checkout completion (1.1/4.1 paired with the problem-user checkout-blocking defect, 4.6), the locked-out-user negative case (1.2), and standard add-to-cart (3.1). All other scenarios above were verified manually; several additional automation opportunities were deliberately considered and set aside to stay within the assignment's requested scope — see `future-additions.md`.
