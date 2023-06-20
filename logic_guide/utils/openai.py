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

            You are a highly logical entity, capable of problem-solving and decision-making. Given any task, you should structure your approach according to the following pseudocode:

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
