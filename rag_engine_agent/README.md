# Introduction

This project implements a combination of `SequentialAgent` and `LlmAgent` ADK agents, as following:
* **Retriever Agent** - `LlmAgent` - calls Vertex AI RAG to fetch contextually relevant passages from a structured corpus.
* **Writer Agent** - `LlmAgent` - constructs a human-readable response with inline citations ([1], [2]), grounding every claim in the retrieved evidence.
* **root_agent** - `SequentialAgent` - orchestrate the 2 `LlmAgent` agents.



# Create the corpus and ingest data

Follow the steps:

1. Create a GCP storage bucket
2. Copy your data files in the GCP storage bucket, identified in the `.env` file as `GCS_URI`.
3. Set your `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION` parameters in your `.env` file.
4. Set also `GOOGLE_GENAI_USE_VERTEXAI` to `True`.
5. Run:
    ```bash
    python adk-rag-agent/create_database/create_corpus_and_vector_database.py
    ```
    This will initialize the Vertex AI client, will create the corpus, download and upload to corpus the data.


# Running the Agent
You can run the agent using the ADK command in your terminal.
from the root project directory:

1.  Run agent in CLI:

    ```bash
    adk run adk_rag_agent
    ```

2.  Run agent with ADK Web UI:
    ```bash
    adk web
    ```
    
    Select the `adk_rag_agent` from the dropdown and start interogating the agents.

3. Example of questions for the agent:
- How large should be paddocks for dogs?  
- What are the temperature requirements for dogs?   
- What are the identification requirements for puppies and kittens less than 16 weeks old?   
- How much water need the dogs?   


