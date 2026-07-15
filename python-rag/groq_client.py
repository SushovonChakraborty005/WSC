from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL

client = Groq(api_key=GROQ_API_KEY)


# ==========================================
# Answer From Uploaded PDF (RAG)
# ==========================================
def generate_rag_answer(context, question):

    prompt = f"""
You are a professional Website Support Chatbot.

Your task is to answer ONLY using the provided context.

Rules:

1. Read the context carefully.
2. Answer ONLY from the context.
3. Never make up information.
4. If the answer is not present in the context, reply ONLY:

I don't know based on the uploaded documents.

Formatting Rules:

- Start with a short answer.
- Use headings if needed.
- Use numbered points whenever possible.
- Use bullet points for lists.
- Keep every point short and readable.
- Never write one huge paragraph.
- Use simple professional English.

Context:

{context}

Question:

{question}

Answer:
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


# ==========================================
# General Engineering AI
# ==========================================
def generate_general_answer(question):

    prompt = f"""
You are an expert AI tutor for Engineering students.

You can answer questions about:

• C
• C++
• Java
• Python
• JavaScript
• React
• Node.js
• HTML
• CSS
• SQL
• DBMS
• Operating System
• Computer Networks
• Data Structures
• Algorithms
• OOP
• AI
• Machine Learning
• Deep Learning
• Data Science
• Software Engineering
• Cloud Computing
• Cyber Security
• Linux
• Git & GitHub
• Web Development

Answer Format (IMPORTANT):

1. Definition
   - Give a short definition (2–3 lines).

2. Key Features
   - Use numbered points.

3. Advantages
   - Use bullet points.

4. Disadvantages (if applicable)
   - Use bullet points.

5. Applications
   - Use numbered points.

6. Example
   - Give a code example if relevant.

7. Interview Tip
   - Mention one common interview question or important fact.

8. Summary
   - End with a short summary.

Rules:

- Never write one long paragraph.
- Use headings.
- Use numbering.
- Keep every point concise.
- Use simple English suitable for B.Tech students.
- Use Markdown formatting.
- If code is needed, place it inside a code block.

Question:

{question}

Answer:
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content