from typing import Dict
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrock
import boto3
import os
import argparse
from typing import Optional
from yaspin import yaspin


def setup_bedrock_client() -> ChatBedrock:
    """Initialize and return a Bedrock LLM client.

    Returns:
        ChatBedrock: Configured Bedrock client
    """

    bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        region_name=os.getenv("AWS_REGION", "us-east-2"),
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    )

    return ChatBedrock(
        client=bedrock_client,
        model_id="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
        model_kwargs={
            "max_tokens": int(os.getenv("MAX_TOKENS", "4096")),
            "temperature": float(os.getenv("TEMPERATURE", "0.0")),
        },
    )


def get_llm_response(llm: ChatBedrock, question: str) -> Optional[Dict]:
    """Get response from LLM for a given question.

    Args:
        llm (ChatBedrock): Configured LLM client
        question (str): Question to ask the LLM

    Returns:
        Optional[Dict]: Response from the LLM or None if error occurs
    """
    try:
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a helpful assistant. Answer the user's question."),
                ("user", "{question}"),
            ]
        )

        # LCEL chain using Langchain Expressive Core Language read more [here](https://python.langchain.com/docs/versions/migrating_chains/llm_chain/)
        chain = prompt | llm | StrOutputParser()
        return chain.invoke({"question": question})

    except Exception as e:
        print(f"Error getting LLM response: {str(e)}")
        return None


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments
    """
    parser = argparse.ArgumentParser(
        description="Chat with Claude 3.5 Sonnet via AWS Bedrock"
    )
    parser.add_argument(
        "-q", 
        "--question",
        type=str,
        help="Question to ask the LLM",
        default="What is the capital of Canada?"
    )
    return parser.parse_args()


def main() -> None:
    """Main function to process LLM requests."""
    with yaspin(text="Loading...", spinner=True, color="cyan") as spinner:
        try:
            args = parse_arguments()
            llm = setup_bedrock_client()
            response = get_llm_response(llm, args.question)
            spinner.ok("✅ ")

            if response:
                print(response)
            else:
                spinner.fail("❌ ")
                print("Error getting LLM response")

        except Exception as e:
            spinner.fail("❌ ")
            print(f"Application error: {str(e)}")


if __name__ == "__main__":
    main()
