from google import genai

client = genai.Client(api_key="AIzaSyCp5BwMYEzozwnV7gUOYjHMMr0lGT6Vbjk")
chat = client.chats.create(model='gemini-3-flash-preview')

response1 = chat.send_message('I have a cat named Whiskers.')
print(response1.text)

response2 = chat.send_message('What is the name of my pet?')
print(response2.text)

# To access specific elements in chat history
for message in chat.get_history():
    print(f'role - {message.role}', end=': ')
    print(message.parts[0].text)