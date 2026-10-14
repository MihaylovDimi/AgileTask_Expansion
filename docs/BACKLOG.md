# Product Backlog: AgileTask Expansion

Ordered by priority (Product Owner). Estimated in story points (Developers).

| Priority | Story | Points |
| --- | --- | --- |
| 1 | Categorise tasks | 3 |
| 2 | Set a due date | 2 |
| 3 | Filter tasks by category | 5 |

## 1. Categorise tasks (3 points)

**Story:** As a user, I want to assign a category to each task, so that I can group related work together.

**Acceptance criteria:**
- A task can be created with a category such as "Work" or "Personal".
- A task created without a category is given the category "General".
- The category of an existing task can be changed.

## 2. Set a due date (2 points)

**Story:** As a user, I want to set a due date on a task, so that I know when it must be finished.

**Acceptance criteria:**
- A task can be given a due date.
- A due date in the past is rejected with an error message.
- A task without a due date is still valid.

## 3. Filter tasks by category (5 points)

**Story:** As a user, I want to see only the tasks in one category, so that I can focus on one area of my work at a time.

**Acceptance criteria:**
- Choosing a category shows only tasks in that category.
- Choosing a category with no tasks shows an empty list, not an error.
- Completed and open tasks are both shown, and their status is clearly marked.

## Estimation notes

- **Set a due date (2)** is the smallest: one new field and one validation rule.
- **Categorise tasks (3)** is slightly bigger: a new field, a default value and a way to change it.
- **Filter by category (5)** is the biggest: it depends on story 1 and must handle empty results.
## Technical Spike: Real-time notifications (timeboxed, not estimated)

**Goal:** Find out how to add notifications without changing the `Task` class every time a new channel is needed.

**Outcome:** Introduced a `Notifier` interface. `Task` now accepts any list of notifiers, so email or push notifications can be added as new classes (Open-Closed Principle). The full notification story can now be estimated.