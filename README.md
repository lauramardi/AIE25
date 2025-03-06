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

## Task:

Load the dataframe “ex1/job_postings.csv” containing some jobs descriptions for different positions and design a prompt to extract the salary range, job title and location for each of them. Return a structured output in JSON format.

NOTE: You can use any LLM that you have a subscription for like OpenAI, o maybe one running on your laptop with OLlama. If you don’t have any of this, you can use Hugging Face Inference Servers (Note that there is a maximun number of times you can call this service). For that, you will need to create an account and an Access token:

1. Go to https://huggingface.co/
2. On the right corner you can find a ‘Sign up’ buttton, clink on it.
3. Provide you email and password. Click ‘Next’ and complete your profile ( with Username and Full name should be enough) and click ‘Create Account’ button.
4. You can generate an avatar, or skip it.
5. Check your email address, you must have receive a confirmation link from Hugging Face. Confirm it.

Create your Access Token:

1. Once you are log into Hugging Face, go to the right corner and click on your avatar ( circle on the top right corner.
2. Go to Access Tokens
3. Click Create new token button.

    a. Select ‘Read’ as Token type.

    b. Add the token name you want like IBM_interview.

    c. Click “Create token”



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
