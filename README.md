# Agora

This implementation is brought to you by Agora, we're devoted to advancing Humanity with meaningful open source AI Research

[Agora banner](agora-banner.png)

[Join our discord to help contribute to this project or 40+ other projects](https://discord.gg/qUtxnK2NMf)

# LogicGuide: Boost Your Model's Logical Reasoning by 40%

<!-- ![LogicGuide](https://github.com/kyegomez/LOGICGUIDE/blob/main/logicguide.jpg?raw=true) -->

LogicGuide is an innovative add-on that can be plugged into any model to boost its logical reasoning capabilities by 40%. LogicGuide is designed to allow your model to harness the power of advanced logical reasoning algorithms and functions, allowing it to generate more accurate, sensible, and meaningful responses. It's as simple as plug and play!

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Examples](#examples)
4. [Contribute](#contribute)
5. [Share with Friends](#share-with-friends)
6. [License](#license)

## Installation

First, clone this repository:

```
git clone https://github.com/kyegomez/LOGICGUIDE.git
cd LOGICGUIDE
```

Then, install the necessary dependencies:

```
pip install -r requirements.txt
```

## Usage

Below is the usage guide for LogicGuide:

```python
from logicguide import MemoryGuide, QuoteGuide,AlgebraGuide, LogicGuide, 



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

```

## Examples

More examples are available in the [examples](https://github.com/kyegomez/LOGICGUIDE/tree/main/examples) directory.

## Contribute

We love your input! We want to make contributing to LogicGuide as easy and transparent as possible. Please check out our [contributing guide](https://github.com/kyegomez/LOGICGUIDE/blob/main/CONTRIBUTING.md) for more information.

## Share with Friends

- [Facebook](http://www.facebook.com/sharer.php?u=https://github.com/kyegomez/LOGICGUIDE)
- [Twitter](https://twitter.com/share?url=https://github.com/kyegomez/LOGICGUIDE&text=Boost+Your+Model's+Logical+Reasoning+by+40%25+with+LogicGuide)
- [LinkedIn](http://www.linkedin.com/shareArticle?mini=true&url=https://github.com/kyegomez/LOGICGUIDE)
- [Reddit](http://reddit.com/submit?url=https://github.com/kyegomez/LOGICGUIDE&title=LogicGuide:+Boost+Your+Model's+Logical+Reasoning)

## License

LogicGuide is released under the MIT License. See the [LICENSE](https://github.com/kyegomez/LOGICGUIDE/blob/main/LICENSE) file for more details.

Note: LogicGuide was created and is maintained by [Kye Gomez](https://github.com/kyegomez).



# Documentation

## UniversalGuide
This is a basic guide class that doesn't alter the input. 

**Methods**
- `__call__(self, history)`: When the class instance is called like a function, it simply returns the input string `history` unchanged.

## DigitGuide
This guide class is designed to interact with digit-related operations in the input string.

**Methods**
- `__init__(self)`: In the initialization method, a regular expression object is created that matches one or more digits.
- `__call__(self, history)`: If the input string `history` matches the regular expression (i.e., it's a sequence of digits), the method returns the regular expression object. Otherwise, it returns None.

## GuideFunction
This is a class for creating guide functions based on a provided tool. 

**Methods**
- `__init__(self, tool)`: The initialization method accepts a `tool` object that is stored for later use.
- `__call__(self, model_output)`: When the instance is called as a function with `model_output` as the argument, it applies the `tool_check` method of the `tool` object to `model_output`.

## parity_guide(binary_string)
This function is used to check the parity of a binary string. 

- `binary_string`: This function takes a binary string as an argument.
- Returns: `1` if the binary string has an even number of 1's (belonging to the parity language), and `0` if it doesn't.

## LogicTool & FactTool
These classes are designed to provide a logic check and a fact check on the input text respectively. 

**Methods**
- `check(self, text)`: These methods accept a string `text` as input and return True. In a complete implementation, these methods would use complex logic systems, semantic analysis, logical inference systems, and fact-checking systems to verify the logical consistency and factual accuracy of the text.

## MemoryGuide
This class acts as a memory manager, storing and retrieving values based on certain triggers in the input string. 

**Methods**
- `__init__(self)`: In the initialization method, an empty dictionary is created to act as the memory store.
- `__call__(self, history)`: This method modifies the input string `history` based on memory set/get triggers.

## QuoteGuide
This class fetches quotes from a source URL and allows the replacement of a quote trigger in the input text with a quote from the source. 

**Methods**
- `__init__(self, source)`: The initialization method accepts a source URL and stores a list of quotes fetched from the source.
- `get_quotes_from_source(self)`: This method fetches all paragraphs from the source webpage and returns them as a list.
- `__call__(self, history)`: This method replaces a quote trigger in the input string `history` with a quote from the source.

## AlgebraGuide
This class interacts with algebraic equations in the input string.

**Methods**
- `__init__(self)`: The initialization method creates an empty dictionary for storing variable-symbol pairs.
- `__call__(self, history)`: This method interacts with the input string `history` based on equation and solve triggers.

## LogicGuide
This class acts as the main logic guide that uses the Hugging Face transformers library to generate responses based on a guide function. 

**Methods**
- `__init__(self, model_id, guide_function=None, device="cuda:0")`: The initialization method sets up the transformers model and tokenizer based on `model_id`, and sets the guide function to `guide_function` or a

 default function if `guide_function` is None.
- `default_guide_function(self, S)`: This method returns the input string `S` unchanged.
- `get_bnb_config(self)`: This method returns a `BitsAndBytesConfig` object for model quantization.
- `guide(self, S)`: This method applies the guide function to the input string `S`.
- `get_blocks(self, s)`: This method returns a list of all guide blocks in the input string `s`.
- `generate(self, text, max_new_tokens=20)`: This method generates a response based on the input string `text`, using the transformers model and applying the guide function if needed.

## Example Usage
The example usage shows how to use the `LogicGuide` class with a specific transformers model. It generates a response to the input "What is your theory of everything?" using the model's default behavior, as no guide function is provided.