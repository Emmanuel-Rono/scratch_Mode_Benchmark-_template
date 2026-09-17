# Adapting an expert case to Scratch mode

1. Meet with the subject-matter expert and identify the capability being tested.
2. Inventory all source files, hidden gold artifacts, and known correct/incorrect human solves.
3. Define exactly what the agent can see and what it must produce.
4. Copy `task_template/` using `scripts/new_task.py`.
5. Replace placeholder assets in `environment/` and `solution/`.
6. Write the task contract in `instruction.md`.
7. Configure `tests/grading_manifest.json` and, if needed, extend the verifier adapter/check library.
8. Validate gold and negative controls before model rollouts.
9. Record pass rates and trajectories under the buyer's evaluation protocol.
