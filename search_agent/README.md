# Your first agent


## Setup the environment

Create an `.env` file:

```bash
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=MY_PROJECT
GOOGLE_CLOUD_LOCATION=MY_REGION
```

## Install the requirements


### 1. Create a virtual environment (.venv)

```bash
uv venv
```

### 2. Activate it

```bash
source .venv/bin/activate
```

### 3. Install your packages safely

```bash
uv pip install requests
```

### 4. Install requirements

```bash
uv pip install -r requirements.txt
```


## Test the agent

Run (from the folder containing the current folder):

```bash
adk web
```

This will start a web application running at `localhost:8000`.

In the interface, select `search_assistant`.

Test the agent with few questions (these are just examples):

* What I can visit in Bucharest? I like ethnic food and traditional art.
* I like art museums and pizza. What I can do in Warsaaw?

