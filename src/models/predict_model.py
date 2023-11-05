import sys
import pandas as pd
import numpy as np
import torch

from transformers import BertTokenizer, BertForMaskedLM, pipeline

# saving the argument

if len(sys.argv) < 2:
    print("Usage:\npython predict_model.py [filename_input.txt]")
    exit()

filename = sys.argv[1]

file = open(filename)
input_sent = file.read()
file.close()

if len(input_sent) == 0:
    print("The input file seems to be empty!")
    exit()

# Using a word remover model

from wordremovermodel import WordRemoverModel

def load_toxic_words(path: str) -> set:
    file = open(path)
    toxic_words = set(file.read().strip().split("\n"))
    file.close()

    return toxic_words

toxic_words_path = "data/raw/toxic_words.txt"
toxic_words_set = load_toxic_words(toxic_words_path)

remover = WordRemoverModel(toxic_words_set)
remover_result = remover.detoxify(input_sent)

# Filling a masked word (second approach)

def mask_toxic_words(sentence: str, toxic_set: set):
    mask_token = "[MASK]"

    split = sentence.strip().split()
    masked = []

    masked_counter = 0

    for word in split:
        if word not in toxic_set:
            masked.append(word)
        else:
            masked.append(mask_token)
            masked_counter += 1
    
    return " ".join(masked), masked_counter

model_name = "bert-base-uncased"

bert_tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForMaskedLM.from_pretrained(model_name)

generator = pipeline("fill-mask", model=model, tokenizer=bert_tokenizer)

input_text, counter = mask_toxic_words(input_sent, toxic_words_set)
generated_text = generator(input_text)

bert_results = []

if counter > 1:
    for i in range(counter):
        for sent in generated_text[i]:
            bert_results.append(sent["sequence"])
else:
    for sent in generated_text:
        bert_results.append(sent["sequence"])

# Printing all results
print(f"\n\nInput: {input_sent}")

print(f"\nWord Remover Result:\n{remover_result}\n\n")

print(f"Pre-trained Bert Replace Result:\n")
for sent in bert_results:
    print(sent)
