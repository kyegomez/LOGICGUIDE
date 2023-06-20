from logic_guide import LogicGuide

logic_guide = LogicGuide(openai_api_key='', openai_api_model='gpt4')

#provide few shot prompt for better results
text = """

Context: Every dog is small. Every feline is a snake. Every animal is not bitter. Sheep are bitter. Cats are
carnivores. Each vertebrate is a mammal. Mammals are felines. Each vertebrate is dull. Snakes are cats.
Cats are not kind. Every snake is not happy. Every sheep is a vertebrate. Each feline is cold. Each dog is a
sheep. Every mammal is not liquid. Every carnivore is a cow. Every carnivore is brown. Alex is a sheep.

Question: True or false: Alex is not bitter.

"""
print(logic_guide.generate(text))

