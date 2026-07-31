import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def generate_email(topic: str, recipient_role: str, tone: str) -> str:
    """
    Generates an email using a LangChain LCEL pipeline.
    LangSmith automatically traces this call because LANGCHAIN_TRACING_V2=true.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a professional communication assistant. Write a clear, {tone} email."),
        ("user", "Write an email about '{topic}' addressed to a {recipient_role}.")
    ])
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    output_parser = StrOutputParser()
    
    # Construct LCEL Chain
    chain = prompt | llm | output_parser
    
    # Run chain
    return chain.invoke({
        "topic": topic,
        "recipient_role": recipient_role,
        "tone": tone
    })
