import cohere
from deserializer import csv_to_examples

class CohereWrapper:
    client = None
    examples = []

    def __init__(self, api_key):
        self.client = cohere.Client(api_key)
        self.examples = csv_to_examples()
    
    def analyze_text(self, text):
        res = self.client.classify(  
            inputs=[text],  
            examples=self.examples)

        return res.classifications

if __name__ == "__main__":
    # only for the example
    import os
    from dotenv import load_dotenv

    load_dotenv()
    c = CohereWrapper(os.environ["API_KEY"])

    sample = """I am a computer science student with a passion for software development. I have experience in multiple programming languages including C++, Java and Python. I have completed several projects including building a web-based application using JavaScript and a machine learning model for image classification using Python. I am a quick learner and am always eager to take on new challenges. I am excited about the opportunity to work as a software engineer and to contribute to the development of innovative technology."""
    print(c.analyze_text(sample))