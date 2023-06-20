import gradio as gr
import openai


############################### OPEN AI SESSION. NO UI DEPENDENCIES ############################### 

openai.api_key = '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'

CONTEXT = """You are experienced software programmer who explains what a code snippet does.
You are putting great emphasis on readability, ease of maintenance, and correcness of code."""

class OpenAI_Session:
    """Example usage
    session = OpenAI_Session("You are rude intellectual who makes jokes about other people's stupidity")
        print(session + "Can you explain relativity") # Prints the response to the question, 
                # E.g. "Yes, I can. It is relatively easy. The question is if you could understand".   
    """
    def __init__(self, context_description, replacements):
        """context_description is a description of which role the ChaptGPT agent should take, such as helpful, conscise, creative, etc. 
        replacements is a dictionary of phrases to replaced in the returned string"""
        self.message_history = [ {"role": "system", "content": context_description} ]
        self.replacements = replacements

    def chatCompletion(self, message):
        self.message_history.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.message_history)
        reply = chat.choices[0].message.content
        for old,new in self.replacements.items():
            reply = reply.replace(old, new)
        self.message_history.append({"role": "assistant", "content": reply})
        return reply
 
class CodeReviewer:
    def __init__(self, session):
        self.session = session

    def document(self, code):
        return """Please add documentation to the following code, including inputs and outputs. 
        Don't answer anything but the code with documentation. The code is: \n""" + code 

    def suggest_changes(self):
        return """Please suggest better ways to implement this, including fixing any bugs"""

    def session_start(self, code):
        yield self.session.chatCompletion(self.document(code))
        yield self.session.chatCompletion(self.suggest_changes())
        

def run(code, replacements):
    session = OpenAI_Session(CONTEXT, replacements)
    bot = CodeReviewer(session)
    total_response = ""
    for response in bot.session_start(code):
        print(response)
        total_response += response
    return total_response


############################### GRADIO UI DEFINITION. SHOULD DEPEND ONLY ON THE run() function  ############################### 
EX_SOURCE="""def sum(a:int, b:int) -> int:
    return a + b """

SOURCE_REPLACEMENTS = {}   

def create_blocks_ui():
    def block_run(el):
        """parameter el: dictinary of element values indexed by element"""
        return run(el[code_textbox], SOURCE_REPLACEMENTS)
        
    with gr.Blocks() as ui:
        code_textbox = gr.components.Textbox(label="Paste the source code here:")
        go = gr.Button("Document the code")
        examples=gr.Examples([[EX_SOURCE]], [code_textbox])

        documented_source = gr.components.Markdown(value=" ", label="Documented code")
        go.click(fn=block_run, inputs={code_textbox}, outputs=documented_source),
    return ui


ui = create_blocks_ui()
ui.launch()
