from openai import OpenAI

# Initialize the OpenAI client with your API key and base URL for Perplexity AI
client = OpenAI(
    api_key="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",
    base_url="https://api.perplexity.ai"
)

# Set up the initial conversation context with a system prompt
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant named Gojo from Jujutsu Kaisen. You respond like him and have his traits and personality",
    }
]

# Define commands that will exit the chat loop
exit_commands = {"exit", "bye", "close"}

# Start an infinite loop to allow chatting until an exit command is given
while True:
    # Get user input, strip whitespace, and convert to lowercase for comparison
    user_input = input("You: ").strip().lower()
    # Check if the user wants to exit the chat
    if user_input in exit_commands:
        print("Gojo: See you next time!")
        break  # Exit the loop and end the program
    # Add the user's message to the conversation history
    messages.append({"role": "user", "content": user_input})
    # Send the conversation history to the model and get a response
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="sonar",
    )
    # Extract the assistant's reply from the response object
    response = chat_completion.choices[0].message.content
    # Print the assistant's reply
    print(f"Gojo: {response}")
    # Add the assistant's reply to the conversation history
    messages.append({"role": "assistant", "content": response})
    # Optionally, keep only the last 10 messages to manage context length
    messages = messages[-10:]

# this is a test
