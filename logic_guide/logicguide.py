import re

# class LogicGuide:
#     def __init__(self):
#         self.delimiters = ("t1", "t2")  # example delimiters for guiding text extraction

#     def guide_function(self, generated_sequence):
#         """Function to define a set of valid generations based on previously generated sequences."""
#         # Implementation specifics would depend on the underlying logic.
#         return set()  # returns a set of valid next generations

#     def completion_engine(self, input_string):
#         """Completion engine that uses Constrained Semantic Decoding (CSD) algorithm."""
#         t1, t2 = self.delimiters
#         if input_string.endswith(t1):
#             sp = self.extract_text_blocks(input_string, t1, t2)
#             valid_strings = self.guide_function(sp)
#             return self.create_regex(valid_strings, t2)
#         else:
#             return self.create_regex([], t1)  # matches any string not containing t1 and ending in t1

#     @staticmethod
#     def extract_text_blocks(input_string, t1, t2):
#         """Extract blocks of text between two delimiters t1 and t2."""
#         # Implementation would extract and return blocks of text based on input string and delimiters
#         return ""

#     @staticmethod
#     def create_regex(valid_strings, ending):
#         """Create a regular expression matching valid strings ending with a specific character."""
#         # Implementation would return a regex based on valid strings and ending character
#         return ""

#     def logicguide(self, input_string):
#         """The LOGICGUIDE function that utilizes the completion engine and the Peano theorem-proving environment."""
#         # The completion engine is called here to generate valid continuations
#         completion_engine_output = self.completion_engine(input_string)
#         # Integration with the Peano theorem-proving environment would occur here
#         # for now, it will just return the output of the completion engine
#         return completion_engine_output





from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

import os
import openai
import time


import logging 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class OpenAILanguageModel:
    def __init__(self, api_key, api_base="", api_model=""):
        if api_key == "" or api_key == None:
            api_key = os.environ.get("OPENAI_API_KEY", "")
        if api_key != "":
            openai.api_key = api_key
        else:
            raise Exception("Please provide OpenAI API key")

        if api_base == ""or api_base == None:
            api_base = os.environ.get("OPENAI_API_BASE", "")  
        if api_base != "":
            openai.api_base = api_base
            print(f'Using custom api_base {api_base}')
            
        if api_model == "" or api_model == None:
            api_model = os.environ.get("OPENAI_API_MODEL", "")
        if api_model != "":
            self.api_model = api_model
        else:
            self.api_model = "text-davinci-003"
        print(f'Using api_model {self.api_model}')

        self.use_chat_api = 'gpt' in self.api_model

    def openai_api_call_handler(self, prompt, max_tokens, temperature, k=1, stop=None):
        while True:
            try:
                if self.use_chat_api:
                    messages = [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                    response = openai.ChatCompletion.create(
                        model=self.api_model,
                        messages=messages,
                        max_tokens=max_tokens,
                        temperature=temperature,
                    )
                else:
                    response = openai.Completion.create(
                        engine=self.api_model,
                        prompt=prompt,
                        n=k,
                        max_tokens=max_tokens,
                        stop=stop,
                        temperature=temperature,
                    )
                with open("openai.logs", 'a') as log_file:
                    log_file.write("\n" + "-----------" + '\n' +"Prompt : "+ prompt+"\n")
                return response
            except openai.error.RateLimitError as e:
                sleep_duratoin = os.environ.get("OPENAI_RATE_TIMEOUT", 30)
                print(f'{str(e)}, sleep for {sleep_duratoin}s, set it by env OPENAI_RATE_TIMEOUT')
                time.sleep(sleep_duratoin)

    def openai_choice2text_handler(self, choice):
        if self.use_chat_api:
            text = choice['message']['content']
        else:
            text = choice.text.strip()
        return text
    
    def generate_solution(self, initial_prompt):
        try:    
            
            prompt = f"""
            
           @LogicGuide AI

            You are a specialized language model designed to perform intricate tasks. You utilize the capabilities of both the HuggingFace and OpenAI models to deliver efficient results. Here's an overview of how you should structure your tasks:

            Your objective is: {initial_prompt}

            TASK ARCHITECTURE:
            1. Task Decomposition: Break down the problem into smaller, more manageable parts.
            2. Data Gathering: Identify the necessary information and data needed to solve each part.
            3. Algorithm Design: Develop an algorithm to solve each part of the problem.
            4. Implementation: Apply the designed algorithms to solve each part.
            5. Integration: Combine the solutions of each part to solve the whole problem.
            6. Verification: Check if the solution meets the problem's requirements and makes logical sense.


            """

            answer = self.openai_api_call_handler(prompt, 300, 0.5, 1)
            answer_text = self.openai_choice2text_handler(answer.choices[0])
            print(f'Solution: {answer_text}')
            return answer_text
        except Exception as e:
            logger.error(f"Error in generate_solution: {e}")
            return None


class UniversalGuide:
    def __init__(self):
        pass

    def __call__(self, history):
        return history
    

class DigitGuide:
    def __init__(self):
        self.regex = re.compile(r"\d+")
    
    def __call__(self, history):
        if self.regex.match(history):
            return self.regex
        else:
            return None


class GuideFunction:
    def __init__(self, tool):
        self.tool = tool
    
    def __call__(self, model_output):
        return self.tool_check(model_output)


def parity_guide(binary_string):
    count = binary_string.count('1')
    if count % 2 == 0:
        return 1 # belongs to the PARITY language
    else:
        return 0 # does not belong to the PARITY language



class LogicTool:
    def check(self, text):
        #pseudocode use a complex logic system to verify the logical consistency of the text
        #use a sematic analysis and logical inference system
        #use tree
        return True
    
class FactTool:
    def check(self, text):
        #use a complex fact checking system to verify the factural accuracy of the tex
        #implement a system that cross references the text with a reliable database of facts
        #use true
        return True
        
logic_guide = GuideFunction(LogicTool())
fact_guide = GuideFunction(FactTool())

#guides from the paper

class MemoryGuide:
    def __init__(self):
        self.memory = {}

    def __call__(self, history):
        set_trigger = "[[set:"
        get_trigger = "[[get:"
        if set_trigger in history:
            key_value = history.split(set_trigger, 1)[1].split(']]', 1)[0]
            key, value = key_value.split("=")
            self.memory[key] = value
            return history.replace(set_trigger + key_value + ']]', "")
        elif get_trigger in history:
            key_value = history.split(get_trigger, 1)[1].split(']]', 1)[0]
            key = key_value.split("=")[0]
            return history.replace(get_trigger + key_value + ']]', self.memory.get(key, ''))
        return history

import requests
from bs4 import BeautifulSoup

class QuoteGuide:
    def __init__(self, source):
        self.source = source
        self.quotes = self.get_quotes_from_source()

    def get_quotes_from_source(self):
        page = requests.get(self.source)
        soup = BeautifulSoup(page.content, 'html.parser')
        return [p.text for p in soup.find_all('p')]

    def __call__(self, history):
        quote_trigger = "[[quote:]]"
        if quote_trigger in history:
            for quote in self.quotes:
                if quote in history:
                    return history
            return history.replace(quote_trigger, '[[quote:' + self.quotes[0] + ']]')
        return history


import sympy

class AlgebraGuide:
    def __init__(self):
        self.variables = {}

    def __call__(self, history):
        eq_trigger = "[[eq]]"
        solve_trigger = "[[solve:"
        if eq_trigger in history:
            equation = history.split(eq_trigger, 1)[1].split(']]', 1)[0]
            for variable in sympy.symbols(equation).free_symbols:
                self.variables[variable.name] = variable
            return history
        elif solve_trigger in history:
            var_value = history.split(solve_trigger, 1)[1].split(']]', 1)[0]
            var = var_value.split("=")[0]
            if var in self.variables:
                solution = sympy.solve(self.variables[var])[0]
                return history.replace(solve_trigger + var_value + ']]', '[[solve:' + var + '=' + str(solution) + ']]')
        return history

class LogicGuide:
    def __init__(self, model_id, guide_function=None, device="cuda:0", openai_api_key="", openai_api_base="", openai_api_model=""):
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto").to(device)
        self.t1 = "[["  # Guide trigger
        self.t2 = "]]"  # End of trusted generation
        self.device = device

        # Initializing OpenAI model
        self.openai_model = OpenAILanguageModel(api_key=openai_api_key, api_base=openai_api_base, api_model=openai_api_model)

        if guide_function:
            self.guide_function = guide_function
        else:
            self.guide_function = self.default_guide_function

    def default_guide_function(self, S):
        return S

    def get_bnb_config(self):
        return BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16
        )

    def guide(self, S):
        return self.guide_function(S)

    def get_blocks(self, s):
        blocks = []
        split_s = s.split(self.t1)
        for block in split_s[1:]:
            if self.t2 in block:
                blocks.append(block.split(self.t2)[0])
        return blocks

    def generate(self, text, max_new_tokens=20):
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)

        # If guide tool is invoked, invoke guide function
        if self.t1 in text:
            text = self.guide(text)

        outputs = self.model.generate(**inputs, max_new_tokens=max_new_tokens)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage:
model_id="tiiuae/falcon-40b"
logic_guide = LogicGuide(model_id=model_id)


#provide few shot prompt for better results
text = """

What is your theory of everything?






"""
print(logic_guide.generate(text))







model_id = "tiiuae/falcon-40b"
device = "cuda:0"  # Change to "cpu" if you don't have a CUDA-compatible GPU.

# Memory Guide
memory_guide = MemoryGuide()
logic_guide = LogicGuide(model_id=model_id, guide_function=memory_guide, device=device)

text = "[[set:name=OpenAI]] What is your name?"
print(logic_guide.generate(text))  # Output: "My name is OpenAI."

text = "[[get:name=]] What is your name?"
print(logic_guide.generate(text))  # Output: "My name is OpenAI."

# Quote Guide (for this example, we're using Project Gutenberg's "The Adventures of Sherlock Holmes")
quote_guide = QuoteGuide(source="https://www.gutenberg.org/files/1661/1661-h/1661-h.htm")
logic_guide = LogicGuide(model_id=model_id, guide_function=quote_guide, device=device)

text = "[[quote:]] What is a quote from Sherlock Holmes?"
print(logic_guide.generate(text))  # Output: A quote from "The Adventures of Sherlock Holmes" (random quote from the source)

# Algebra Guide
algebra_guide = AlgebraGuide()
logic_guide = LogicGuide(model_id=model_id, guide_function=algebra_guide, device=device)

text = "[[eq]] x^2 + 3x + 2 = 0"
print(logic_guide.generate(text))  # Output: "x^2 + 3x + 2 = 0" (and stores the equation for later)

text = "[[solve:x=]] What is the value of x?"
print(logic_guide.generate(text))  # Output: "The value of x is ..." (the solutions of the equation)
