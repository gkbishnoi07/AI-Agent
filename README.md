# AI Agent

## Setup Environment Variables

This project uses environment variables to securely manage your API keys.

### Steps to set up:

1. Copy the example environment file to create your own `.env` file:

    ```bash
    cp .env.example .env
    ```

2. Open the `.env` file in a text editor.

3. Replace the placeholder with your actual OpenAI API key:

    ```env
    OPENAI_API_KEY=your_api_key_here
    ```

    Example:

    ```env
    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ```

4. Save the `.env` file.

---

## Installation & Running

Follow these steps to fork, clone, install dependencies, and run the project:

1. **Fork** this repository on GitHub.

2. **Clone** your fork locally:

    ```bash
    git clone https://github.com/your-username/Ai-agent.git
    cd Ai-agent
    ```

3. **Install** UV (a task runner):

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

4. **Initialize** UV in the project directory:

    ```bash
    uv init .
    ```

5. **Add** required packages:

    ```bash
    uv add langgraph langchain python-dotenv langchain-openai
    ```

6. **Run** the main script:

    ```bash
    uv run main.py
    ```

---

## Usage

- After running, type your messages to interact with the AI agent.
- To exit, type `exit`.

---

**Keep your API key private and never share it publicly.**
