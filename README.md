# LangChain Fundamentals

A structured, hands-on repository for learning the LangChain ecosystem — from basic LLM calls to AI agents.

---

## Repository Structure

```
├── 01 LangChain Model/        # LLMs, Chat Models, and Embeddings
├── 02 LangChain Prompts/      # Prompt Templates, Chatbots, and Message Types
├── 03 LangChain Structured Output/  # TypedDict, Pydantic, JSON Schema, Output Parsers
├── 04 Chains/                 # Sequential, Parallel, and Conditional Chains
├── 05 Runnables/              # RunnableSequence, Parallel, Branch, Lambda, Passthrough
├── 06 Document Loader/        # Text, PDF, Web, CSV, Directory Loaders
├── 07 Text Splitters/         # Length, Structure, Code, Semantic Splitters
├── 08 Vector DB/              # ChromaDB Integration
├── 09 Retrievers/             # Data-source and Search Strategy Retrievers
├── 10 Youtube Chatbot/        # End-to-end RAG project
├── 11 Tools/                  # LangChain Tool Usage
├── 12 Tool Calling/           # Manual Tool Calling and AI Agents
└── 13 AI Agents in Langchain/ # Agent Patterns
```

---

## Modules

### 01 — LangChain Model
Covers the three core model types in LangChain.

- **LLMs** — `OpenAI` with `gpt-3.5-turbo-instruct`
- **Chat Models** — `ChatOpenAI`, `ChatGoogleGenerativeAI` (Gemini), `ChatHuggingFace` (hosted & local)
- **Embeddings** — `OpenAIEmbeddings`, `HuggingFaceEmbeddings`, cosine similarity for document search

### 02 — LangChain Prompts
Building dynamic prompts and multi-turn chatbots.

- `PromptTemplate` and `ChatPromptTemplate`
- Saving/loading prompt templates as JSON (`template.json`)
- `SystemMessage`, `HumanMessage`, `AIMessage`
- `MessagesPlaceholder` for injecting chat history
- A Streamlit-based research tool with selectable paper, style, and length

### 03 — Structured Output
Three approaches to enforce a structured schema on LLM output.

| Approach | File |
|---|---|
| TypedDict + Annotated | `review_structure_output.py` |
| Pydantic BaseModel | `review_pydantic.py` |
| JSON Schema | `review_json.py` |

Also covers output parsers when structure is not provided upfront: `StrOutputParser`, `JsonOutputParser`, `StructuredOutputParser`, `PydanticOutputParser`.

### 04 — Chains
Composing LangChain components using the `|` pipe operator.

- **Sequential** — multi-step summarization pipelines
- **Parallel** — `RunnableParallel` for concurrent sub-chains (notes + quiz generation)
- **Conditional** — `RunnableBranch` for sentiment-based response routing

### 05 — Runnables
Low-level building blocks behind LangChain chains.

- `RunnableSequence` — explicit sequential composition
- `RunnableParallel` — concurrent execution
- `RunnableBranch` — conditional routing (with word-count threshold example)
- `RunnableLambda` — wrapping arbitrary Python functions
- `RunnablePassthrough` — forwarding input unchanged

### 06 — Document Loaders
Loading content from various sources into LangChain `Document` objects.

| Loader | Source |
|---|---|
| `TextLoader` | `.txt` files |
| `PyPDFLoader` | PDF files (with lazy loading) |
| `DirectoryLoader` | Folder of files |
| `WebBaseLoader` | Web pages |
| `CSVLoader` | CSV files |

### 07 — Text Splitters
Chunking documents before embedding.

- **Length-based** — `CharacterTextSplitter`
- **Structure-based** — `RecursiveCharacterTextSplitter`
- **Code/Markdown** — `RecursiveCharacterTextSplitter.from_language()` (Python, Markdown)
- **Semantic** — `SemanticChunker` with OpenAI embeddings and standard deviation breakpoints

### 08 — Vector DB
Persisting and querying embeddings with ChromaDB.

- `Chroma` vector store with `OpenAIEmbeddings`
- `add_documents`, `similarity_search`, `similarity_search_with_score`
- Metadata filtering, document update, and deletion

### 09 — Retrievers
Strategies for retrieving documents from a vector store. See Colab notebooks linked in `concept.txt`.

### 10 — YouTube Chatbot
A complete RAG-based chatbot that answers questions about a YouTube video. Full project in the linked Colab notebook.

### 11 — Tools / 12 — Tool Calling / 13 — AI Agents
- Defining and using LangChain tools
- Manual tool calling loop (currency converter example)
- Agent patterns with `create_react_agent` and similar

---

## Setup

### Prerequisites
- Python 3.10+
- API keys for OpenAI, Google Gemini, and/or HuggingFace (as needed per module)

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd <repo-name>

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies for a specific module
cd "01 LangChain Model"
pip install -r requirements.txt
```
