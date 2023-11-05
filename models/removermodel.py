from transformers import BertTokenizer

class RemoverModel:
    def __init__(self, toxic_words: set) -> None:
        self.toxic_words = toxic_words
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    
    def detoxify(self, input: str):
        tokenized = self.tokenizer.tokenize(input)

        output_list = []
        for token in tokenized:
            if token not in self.toxic_words:
                output_list.append(token)
        
        return " ".join(output_list)
