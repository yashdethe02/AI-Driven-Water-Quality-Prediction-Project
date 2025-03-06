from transformers import T5ForConditionalGeneration, T5Tokenizer

class WaterQA:
    def __init__(self):
        self.model = T5ForConditionalGeneration.from_pretrained('t5-large')
        self.tokenizer = T5Tokenizer.from_pretrained('t5-large')
        
    def answer_question(self, context, question):
        input_text = f"question: {question} context: {context}"
        inputs = self.tokenizer(input_text, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=200)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)