from typing import Dict
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrock
import boto3
import os
from typing import Optional


def setup_bedrock_client() -> ChatBedrock:
    """Initialize and return a Bedrock LLM client.

    Returns:
        ChatBedrock: Configured Bedrock client
    """
    
    bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        region_name=os.getenv("AWS_REGION", "us-east-2"),
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
    )

    return ChatBedrock(
        client=bedrock_client,
        model_id="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
        model_kwargs={
            "max_tokens": int(os.getenv("MAX_TOKENS", "4096")),
            "temperature": float(os.getenv("TEMPERATURE", "0.9"))
        }
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
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant. Answer the user's question."),
            ("user", "{question}"),
        ])
        
        # LCEL chain using Langchain Expressive Core Language read more [here](https://python.langchain.com/docs/versions/migrating_chains/llm_chain/)
        chain = prompt | llm | StrOutputParser()
        return chain.invoke({"question": question})
    
    except Exception as e:
        print(f"Error getting LLM response: {str(e)}")
        return None


def main() -> None:
    """Main function to process LLM requests."""
    try:
        llm = setup_bedrock_client()
        response = get_llm_response(llm, "What is the capital of Canada?")
        
        if response:
            print(response)
        
    except Exception as e:
        print(f"Application error: {str(e)}")


if __name__ == "__main__":
    main()
