# AWS LLM Basic

This is a basic example of how to use AWS Bedrock with Langchain.

## Requirements

- Python 3.13
- Langchain 0.3.14
- Langchain AWS 0.2.11
- Boto3 1.36.2

AWS credentials are required to run the application. Follow instructions [here](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html) to set up your credentials.

Read more about [Langchain AWS](https://python.langchain.com/docs/integrations/providers/aws/)

## Installation using [uv](https://docs.astral.sh/uv/) in pip compatible mode

```bash
uv pip install langchain langchain-aws boto3
```

or use `uv sync` to install the dependencies.

```bash
uv sync
```

## Run the application

```bash
uv run main.py
```


