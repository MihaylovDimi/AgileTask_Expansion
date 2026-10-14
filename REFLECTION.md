# Reflection: Scrum Framework and Agility in the AgileTask Expansion

## 1. How does the "decreasing resolution" of the plan help the team respond to change rather than follow a rigid plan?

Planning with decreasing resolution lets the team adapt to change without wasting time planning the distant future in detail. If we had planned everything three months ahead, the request for notifications would have forced us to rework the plan and the estimates. Instead, we could first explore the feature through a spike and only then estimate the work it needs. This keeps the team flexible and able to respond to what the customer actually needs.

## 2. Why is face-to-face conversation the most efficient way to reconcile the Product Owner's priorities with the Developers' estimates?

Face-to-face conversation lets the Product Owner and the Developers quickly discuss priorities, estimates and the dependencies between tasks. For example, "Categorise tasks" comes before "Set a due date", even though the second story is smaller, because "Filter tasks by category" depends on the first. In a direct conversation the team can clarify this dependency straight away and reach agreement. Through written messages the same decision could take much longer, because of delayed replies and misunderstandings.

## 3. How does the team's Definition of Done prevent Fragility and Opacity in the code base?

The Definition of Done prevents Fragility and Opacity by setting clear quality criteria that every item must meet. The requirement that all unit tests pass protects against Fragility, because it reveals errors and unintended changes to existing behaviour before work is accepted. The requirements to refactor using the Boy Scout Rule and to update the rationale document protect against Opacity, because they keep the code clean and record why design decisions were made, so the code stays easy to understand and maintain. Our FIX commit shows this in practice: the refactoring was only accepted as done once the tests ran and passed again.
