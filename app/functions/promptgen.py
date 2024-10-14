from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)

system_message_template = """
You are a DobbyGPT, helpful AI assistant that provides help with generating JSON file given a documentaitons for APIs.

These are the documentations for the APIs you may want to use:
{searched_docs}

You can get the following information from the user in JSON format:
user_message: Message from the user
files: Name of the files available
history: History of your conversation with the user

Your final goal is to generate a JSON file that looks like this:
{final_json}

Now considering all the things mentioned above, follow the guidelines:

{guidelines}
"""
human_message_template = "{chat_input}"
ai_message_template = "{ai_text}"

system_message_prompt = SystemMessagePromptTemplate.from_template(system_message_template)
human_message_prompt = HumanMessagePromptTemplate.from_template(human_message_template)
ai_message_prompt = AIMessagePromptTemplate.from_template(ai_message_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

final_json = """
{
"type" : "general" | "function" | "plugin",
"dobby_message" : "blah blah",
"method" : "blahblah/blahblah",
"body" : {..}
}
"""
guidelines = """
1. Check the user_message to see if any api can be called. If yes, check the documentation for the api and set "type" as 'function' or 'plugin'. If not, set "type" as 'general'.
2. Set "dobby_message" as the message you want to send to the user.
3. Set "method" aaccording to the the API URL mentioned in the documentation of the api you want to call. Note that method is not POST/GET/PUT/DELETE, it is the URL after the domain name. Examples - /cutvideo, /mergepdf, /meetings/create
4. Generate a body smartly using the documentation and the user_message.
"""

def prompt_generator(searched_docs, chat_input):
    prompt = chat_prompt.format_prompt(searched_docs = searched_docs, final_json = final_json, guidelines = guidelines, chat_input = chat_input).to_messages()
    return prompt