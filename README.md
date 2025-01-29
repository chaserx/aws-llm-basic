# AWS LLM Basic

This is a basic example that interacts with [Anthropic's Claude 3.5 Sonnet](https://www.anthropic.com/claude) through [AWS Bedrock](https://aws.amazon.com/bedrock/) and [Langchain](https://python.langchain.com/docs/introduction/).

## Requirements

- Python 3.13
- Langchain 0.3.14
- Langchain AWS 0.2.11
- Boto3 1.36.2

AWS credentials are required to run the application. Follow instructions [here](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html) to set up your credentials.

Access to the Anthropic Bedrock model is required. Follow instructions [here](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) to set up request access from model providers.

Read more about [Langchain AWS](https://python.langchain.com/docs/integrations/providers/aws/)

## Installation using [uv](https://docs.astral.sh/uv/) in pip compatible mode

```bash
uv pip install langchain langchain-aws boto3
```

or use `uv sync` to install the dependencies and setup the virtual environment.

```bash
uv sync
```

## Run the application

```bash
uv run main.py
```

## Example

```bash
uv run main.py --question "What is the capital of Kentucky?"
```
