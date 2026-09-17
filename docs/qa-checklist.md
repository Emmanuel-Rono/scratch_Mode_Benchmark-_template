# QA checklist

- [ ] Task is human-authored and domain-expert approved.
- [ ] Agent-visible inputs are complete but do not leak the gold answer.
- [ ] `instruction.md` defines output location, units/schema, constraints, and tolerances.
- [ ] Gold/oracle solution passes the verifier.
- [ ] Known incorrect solutions fail for the intended reason.
- [ ] Legitimate alternative solutions pass where allowed.
- [ ] Verifier outputs an auditable check-by-check score.
- [ ] Task runs from a clean environment with no hidden local dependency.
- [ ] Buyer-specific Harbor schema fields have been validated against the canonical sample.
- [ ] Model rollouts and trajectories are preserved for difficulty reporting.
