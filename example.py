from logic_guide import LogicGuide, QuoteGuide, AlgebraGuide, MemoryGuide
# Example usage:
model_id="tiiuae/falcon-40b"
logic_guide = LogicGuide(model_id=model_id)


#provide few shot prompt for better results
text = """

Context: Every dog is small. Every feline is a snake. Every animal is not bitter. Sheep are bitter. Cats are
carnivores. Each vertebrate is a mammal. Mammals are felines. Each vertebrate is dull. Snakes are cats.
Cats are not kind. Every snake is not happy. Every sheep is a vertebrate. Each feline is cold. Each dog is a
sheep. Every mammal is not liquid. Every carnivore is a cow. Every carnivore is brown. Alex is a sheep.

Question: True or false: Alex is not bitter.

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
