from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatOpenAI(temperature=0)
    tools = []
    agent_executor = create_react_agent(model, tools)

    print("Welcome to the AI agent. Type 'exit' to quit.")

    while True:
        user_input = input("\nyou: ").strip()

        if user_input == "exit":
            print("Exiting the AI agent. Goodbye!")
            break

        print("\nAI agent:", end=" ")

        for chunk in agent_executor.stream({"messages": [HumanMessage(content=user_input)]}):
            if "agent" in chunk and "message" in chunk["agent"]:
                for message in chunk["agent"]["message"]:
                    print(message.content, end="")
                print()

if __name__ == "__main__":
    main()
