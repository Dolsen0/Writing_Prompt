import openai
from apiKey import apiPass

openai.api_key = apiPass

setting = input("what kind of setting would you like? Fantasy, futuristic, cyberpunk, etc")

response = openai.Completion.create(
    model = "text-davinci-001",
    prompt = f"create a writing prompt based on a {setting} setting",
    temperature = .30,
    max_tokens = 64,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0,

)

writing_prompt = response["choices"][0]["text"]

print(writing_prompt)