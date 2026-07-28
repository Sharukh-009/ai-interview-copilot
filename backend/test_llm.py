from app.services.llm import llm

print("Before invoke")

response = llm.invoke("Reply with only the word Hello")

print(response.content)

print("Done")