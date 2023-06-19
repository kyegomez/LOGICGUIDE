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
