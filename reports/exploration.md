# Exploration Report

## References
- [Александр Панченко — Monolingual and Cross-lingual Text Detoxification](https://www.youtube.com/watch?v=PEo3UJKwsN0&t=1219s&ab_channel=%D0%9C%D0%A2%D0%A1Digital)
- [Monolingual and Cross-lingual Text Detoxification [in Russian]](https://www.youtube.com/watch?v=1RsHbmzY2Mg&ab_channel=BayesGroup.ru)
- [Text Detoxification using Large Pre-trained Neural Models](https://arxiv.org/abs/2109.08914)
- [GitHub repository related to the paper right above](https://github.com/s-nlp/detox)

## Approaches

### Dictionary-based Toxic Word Removal/Replacement

This approach seems to be the easiest to implement, but it will also yield sentences that most probably will sound
artificially. It also does not contain any ML, however it can be perceived as a baseline solution.

Steps:
1. Iterate over inputs and identify toxic words using the dictionary.
2. Remove those words or replace them with neutral alternatives.

### Toxic Word Replacement






