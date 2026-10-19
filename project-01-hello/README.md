# project-01-hello

A simple setup project to check that the AI development environment works: Python 3.13, `uv`, LangChain, and API keys loaded from `.env`.

## Setup

```bash
uv sync
cp .env.example .env   # then add your OPENAI_API_KEY and GOOGLE_API_KEY
```

## Run

```bash
uv run main.py
```

If it runs without errors, the environment is ready.
