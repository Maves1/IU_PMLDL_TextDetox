# Final Report

Text detoxification seems to be a complex and challenging task.
Many techniques can be applied to tackle it.

## What I've Tried

### Baseline

I decided to start with implementing a baseline approach.

Steps:

1. Each input sentence is tokenized using Bert tokenizer
2. Each token is checked against a set of known toxic words
3. Toxic words are removed

While it may seem too basic, there are many cases when this
algorithm shows itself well.

Example:

```
Input: Don't fucking say that shit!

Word Remover Result:
don ' t say that!
```

### Toxic Word Replacement with Bert

This approach is slightly more advanced. Instead of simply removing toxic words, I use
a pre-trained Bert model to replace those words.

Steps:

1. Tokenize each input sentence using Bert tokenizer
1. Iterate over inputs and identify toxic words using the dictionary.
2. Mask the words
3. Use a pre-trained Bert model to replace the words.

Example of different replacements:

```
Input: Don't fucking say that shit !

Pre-trained Bert Replace Result:

[CLS] don't ever say that [MASK]! [SEP]
[CLS] don't even say that [MASK]! [SEP]
[CLS] don't you say that [MASK]! [SEP]
[CLS] don't fucking say that [MASK]! [SEP]
[CLS] don't just say that [MASK]! [SEP]
[CLS] don't [MASK] say that again! [SEP]
[CLS] don't [MASK] say that shit! [SEP]
[CLS] don't [MASK] say that word! [SEP]
[CLS] don't [MASK] say that!! [SEP]
[CLS] don't [MASK] say that now! [SEP]
```

### Pre-trained T5

I also wanted to fine-tune T5 using the dataset given in this assignment. However,
I didn't quite manage to do that. There is an attempt in `notebooks/4.0-t5-pretrained-finetune.ipynb`

## Results and Conclusion

As it was already mentioned, text detoxification can be approached in different ways.

This work shows some approaches to tackling this problem, however, it must be noted
that additional research is required in order to enhance the current outcomes.
