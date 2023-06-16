# Harness V 0.1

Harness is a Python-based command-line interface (CLI) for interacting with OpenAI's GPT-3.5 Turbo and GPT-4 models. This tool offers a minimalistic and intuitive interface for generating AI-driven text using the models.

## Setup

You need to have an API key from OpenAI to use this tool. Once you have it, update the `keyLocation` variable at the top of the script to the location of your key file:

```python
keyLocation = '/path/to/your/keyfile'
```

You also need to install the required Python packages. You can do this with pip:

```shell
pip install openai getch termcolor art
``` 

## Usage  

Run the script using Python:
  
```python
python main.py
```  

Upon launching, Harness will clear the terminal and display a welcome message. You will be prompted to choose a GPT model to use (GPT-3.5 Turbo or GPT-4), and a predefined system message.

System messages are initial setup messages for the AI model, such as "You are a helpful assistant." They set the context for the model's responses.

After these initial steps, you will be prompted to input a message for the model. You can either type it directly into the terminal or paste it from a document. The model's response will then be displayed.

The conversation history is saved into a file named convoHistory.txt by default, which is overwritten in each new session.

## Notes  

This tool is intended for developers and enthusiasts who want to experiment with AI text generation in a simple, command-line interface. It is a basic implementation and doesn't handle errors or edge cases robustly. Therefore, it may not be suitable for production or business-critical applications.

Please ensure that you use the AI models responsibly and in accordance with OpenAI's use case policy.

