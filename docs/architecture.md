# Scratch-mode architecture

Scratch mode allows the agent to choose how to construct the final artifact. The verifier therefore should not assume the gold implementation is the only valid implementation.

Use an explicit output contract where possible: named outputs, required sections, schemas, or machine-readable summaries. Combine this with weighted checks for numerical/content correctness, dependencies/provenance, structure, and presentation.

Recommended validation order:

1. Gold/oracle passes.
2. At least one independently valid alternative passes when layout freedom is allowed.
3. Known wrong human or synthetic controls fail the intended dimensions.
4. Partial-credit behavior is checked at scoring boundaries.
5. Model rollouts begin only after verifier validation.
