# AIE25

# Introduction

Before You Begin:
- You'll have 1 hour to work on these questions.
- Please use your personal laptop with Python and a code editor of your choice.
- Feel free to approach this at your own pace - it's completely fine if you don't finish everything.

Guidelines:
- Use any online resources or documentation you find helpful.
- We're interested in your approach and thought process as much as the final solution.
- If you get stuck on a particular question, feel free to move on to the next one.
- You're welcome to skip parts of questions that you find challenging.

Sharing Your Work:
- If possible, please create a GitHub repository for your code.
- If GitHub isn't convenient for you, any method of sharing your code works fine (email, file sharing, etc.).

What Happens Next:
- During the interview, we'll discuss your solutions and thought process.
- We're not looking for perfect solutions - we want to understand how you approach problems.

Remember, this assessment is designed to be a conversation starter for our technical discussion, not a high-pressure exam. Good luck, and we look forward to discussing your approach!


# Exercise 1: Model Prompting

**Objective:** Use an LLM for data processing.


# Exercise 2: Vector Embeddings & Semantic Search

**Objective:** Build a semantic search pipeline for text data.

## Task:

1. Generate embeddings using an existing model for each document/paragraph in `/ex2`
2. Use a vector DB to index these embeddings.
3. Demonstrate a simple search: retrieve the top-5 most similar passages given a query.
4. Discuss scaling approaches for larger datasets.

**Hint:** For simplicity, you can use an in-memory vector database such as:
- [ChromaDB](https://docs.trychroma.com)
- [Milvus Lite](https://milvus.io/docs)
- Any vector DB of your choice.


# Exercise 3: LLM-based Evaluation

**Objective:** Use LLM-based metrics.

## Task:

Compare the summarized output from `/ex3` and calculate precision (e.g., BLEU or other metrics) using provided summaries:
- Reference summary (`summary-1-flan-ul2--article1`)
- Candidate summary (`summary-2-flan-ul2--article1`)


# Exercise 4: FastAPI

**Objective:** Create an AI application via API.

## Task:

1. Build a RESTful API exposing functionality from a previous exercise solution.
2. Demonstrate API usage with a sample request (curl, Postman, Python requests).

**Hint:** Use frameworks like FastAPI or Flask for building HTTP-based services locally (e.g., localhost:8000).
