# Scratch-Mode Benchmark Template

A reusable benchmark template for evaluating AI agents that create a complete artifact from provided inputs and instructions. It supports domain-agnostic tasks where valid outputs may differ in structure but must satisfy defined correctness, dependency, structure, and presentation requirements.

## Run with Docker

Start Docker Engine (or Docker Desktop using Linux containers), then build and run the repository checks:

```sh
docker build -t benchmark-template .
docker run --rm benchmark-template
docker run --rm benchmark-template python scripts/validate_task.py task_template
docker run --rm benchmark-template python scripts/validate_task.py example
```

The image includes Python 3.11, the package dependencies, and the template and example. Its default command runs the self-test and exits.

For local development, Compose mounts this repository at `/workspace`, so code edits and generated tasks persist on your host:

```sh
docker compose run --rm --build benchmark
docker compose run --rm benchmark python scripts/new_task.py --id my_task
docker compose run --rm benchmark python scripts/validate_task.py tasks/my_task
```

Rebuild after changing dependencies in `pyproject.toml`. On Linux, add `--user "$(id -u):$(id -g)"` to `docker compose run` when generating tasks to keep files owned by your user.

The root image is for authoring and verification and includes tests and reference solutions. Agent environments use the separate `environment/Dockerfile` in each task; build those with the task's `environment/` directory as the context so solutions and grading data stay outside the agent image.

## Repository Structure

```text
.
├── task_template/
│   ├── instruction.md
│   ├── task.toml
│   ├── environment/
│   │   ├── Dockerfile
│   │   └── inputs/
│   ├── solution/
│   │   └── reference/
│   └── tests/
│       ├── verifier.py
│       └── test.sh
├── benchmark_core/
│   └── verification/
├── example/
│   └── scratch_task/
├── scripts/
│   ├── new_task.py
│   ├── validate_task.py
│   └── self_test.py
└── docs/
```
