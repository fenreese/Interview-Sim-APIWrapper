import functools
import random
from cohere.classify import Example

csv_file = "sentiments.csv"
labels = ["irrelevant", "positive", "negative"]

def csv_to_examples():
    examples = []

    with open(csv_file) as f:
        for line in f:
            line = line.strip()
            sep = line.rfind(",")
            examples.append((line[:sep], line[sep + 1:]))
    
    random.shuffle(examples)

    # make code absolutely unreadable to everyone 
    return list(map(lambda sample: Example(sample[0], sample[1]), sum([list(filter(lambda x: x[1] == label, examples))[:15] for label in labels], [])))
    
if __name__ == "__main__":
    print(csv_to_examples())