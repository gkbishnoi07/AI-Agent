# AI Agent

## Setup Environment Variables

This project uses environment variables to securely manage your API keys.

### Steps to set up:

1. Copy the example environment file to create your own `.env` file:

```bash
cp .env.example .env


Open the .env file in a text editor.

Replace the placeholder with your actual OpenAI API key:

ini
Copy
Edit
OPENAI_API_KEY=your_api_key_here
Example:

ini
Copy
Edit
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Save the .env file.

Installation & Running
Follow these steps to fork, clone, install dependencies, and run the project:

Fork this repository on GitHub.

Clone your fork locally:

bash
Copy
Edit
git clone https://github.com/your-username/Ai-agent.git
cd Ai-agent
Install UV (a task runner):

bash
Copy
Edit
curl -LsSf https://astral.sh/uv/install.sh | sh
Initialize UV in the project directory:

bash
Copy
Edit
uv init .
Add required packages:

bash
Copy
Edit
uv add langgraph langchain python-dotenv langchain-openai
Run the main script:

bash
Copy
Edit
uv run main.py