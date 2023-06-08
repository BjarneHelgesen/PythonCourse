import gradio as gr
import openai


############################### OPEN AI SESSION. NO UI DEPENDENCIES ############################### 

openai.api_key = 'sk-cbnVRSFHkT3YTiwG81pUT3BlbkFJrHPbwRWB732XTHIHkQQca'

CONTEXT = """You are an optimistic science fiction writer who imagines simple, non-realistic solutions to problems. You invent sinple mathematical relationships, 
       that look valid, regardless of whether they are right or wrong. 
       You use LaTex notation for all math formulas and symbols and encapsulate LaTeX expressions in $ signs.
       You expect the reader to have basic engineering knowledge, so you don't explain Ohm's Law, or Newton's second law of motion."""

class OpenAI_Session:
    """This class has an non-traditional, but simple syntax:  It returns the response when a request is added.  
        session = OpenAI_Session("You are rude intellectual who makes jokes about other people's stupidity")
        print(session + "Can you explain relativity") # Prints the response to the question, 
                # E.g. "Yes, I can. It is relatively easy. The question is if you could understand".   
    """
    def __init__(self, context_description, replacements):
        """context_description is a description of which role the ChaptGPT agent should take, such as helpful, conscise, creative, etc. 
        replacements is a dictionary of phrases to replaced in the returned string"""
        self.message_history = [ {"role": "system", "content": context_description} ]
        self.replacements = replacements

    '''
    def __add__(self, message):
        """reply = session + message 
        This is an alias for reply = session.chatCompletion(message) 
        where session is this object. 
        Note that string additons are not supported e.g. reply = session + text1 + text2"""
        return self.chatCompletion(message)
    '''
    def chatCompletion(self, message):
        self.message_history.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.message_history)
        reply = chat.choices[0].message.content
        for old,new in self.replacements.items():
            reply = reply.replace(old, new)
        self.message_history.append({"role": "assistant", "content": reply})
        return reply
 
class WannabeBot:
    def __init__(self, session):
        self.session = session

    def introduce(self, product, design):
        return "The product we want to design is a " + product + ". The planned design is as follows: " + design + \
        ". As always, use LaTeX notation encapsulated by $ signs. The target audience is skilled engineers." 

    def analyse(self, parameters):
        """Convenience function to build the analysis string"""
        return "Please list wild guesses or wishful thinking about the mathematical relationship or proportionality between the following parameters: " + parameters + \
        "Show all mathematical relationships and symbols in LaTeX notation encapsulated by $ signs."

    def design(self, optimize_for):
        """Convenience function to build the design string"""
        return "Please optimize for " + optimize_for + ". What is a a creative that would be useful if it could be realized?. Use LaTeX for equations and symbols and encapsulate with $ signs."

    def constants(self):
        return "Please list material constants and other constant values to be used for the design. Don't list general formulas that don't have values. Use LaTeX for all symbols and encapsulate them by $ signs"
    
    def session_start(self, product, spec, parameters, optimize_for):
        def headline(str):
            return "\n## " + str + "\n"
        yield headline("Introduction")
        yield self.session.chatCompletion(self.introduce(product, spec))
        yield headline("Analysis")
        yield self.session.chatCompletion(self.analyse(parameters)) 
        yield headline("Suggested design")
        yield self.session.chatCompletion(self.design(optimize_for)) 
        yield headline("Constants")
        yield self.session.chatCompletion(self.constants())

def run(product, spec, optimize_for, parameters, replacements):
    session = OpenAI_Session(CONTEXT, replacements)
    bot = WannabeBot(session)
    total_response = ""
    for response in bot.session_start(product, spec, parameters, optimize_for):
        print(response)
        total_response += response
    return total_response


############################### GRADIO UI DEFINITION. SHOULD DEPEND ONLY ON THE run() function  ############################### 
EX_PRODUCT="Subsea Rocket"
EX_SPEC="1 MT cargo, launched from the Mariana Trench"
EX_PARAMETERS="Weight, production cost, number of engines, reliability"
EX_OPTIMIZE_FOR="Low cost, high reliability, simple design"

GRADIO_LATEX_REPLACEMENTS = {"\\implies": "→", #\implies not supported
                             "(R)": "( R )",   # (R) is interpreted as registered trademark. Better to have some extra spaces
                             "\\text": "",     #\text not supoorted
                             "\\space": " "}   #\space not supported

def create_blocks_ui():
    def block_run(el):
        """parameter el: dictinary of element values indexed by element"""
        return run(el[product], el[spec], el[optimize_for], el[parameters], GRADIO_LATEX_REPLACEMENTS)
        
    with gr.Blocks() as ui:
        product = gr.components.Textbox(label="What is the product to evaluate")
        spec = gr.components.Textbox(label="Describe the design and requirements", lines=4)
        optimize_for = gr.components.Textbox(label="Which parameters to optimize for, e.g. low cost, durability")
        parameters = gr.components.Textbox(label="Parameters to evaluate (separated by comma)")
        go = gr.Button("Report")
        examples=gr.Examples([[EX_PRODUCT, EX_SPEC, EX_OPTIMIZE_FOR, EX_PARAMETERS]], [product, spec, optimize_for, parameters])

        analysis = gr.components.Markdown(value=" ", label="Analysis")
        go.click(fn=block_run, inputs={product, spec, optimize_for, parameters}, outputs=analysis),
    return ui


ui = create_blocks_ui()
ui.launch()



