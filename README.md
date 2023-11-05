# Text Detoxification

## References
- [Александр Панченко — Monolingual and Cross-lingual Text Detoxification](https://www.youtube.com/watch?v=PEo3UJKwsN0&t=1219s&ab_channel=%D0%9C%D0%A2%D0%A1Digital)
- [Monolingual and Cross-lingual Text Detoxification [in Russian]](https://www.youtube.com/watch?v=1RsHbmzY2Mg&ab_channel=BayesGroup.ru)
- [Text Detoxification using Large Pre-trained Neural Models](https://arxiv.org/abs/2109.08914)
- [GitHub repository related to the paper right above](https://github.com/s-nlp/detox)

## Info

Uni Project

Vsevolod Mikulik

v.mikulik@innopolis.university

B20-AI-01

## What's this?

The goal of this project is to explore different approaches to handle text detoxification.

The exploration starts with a baseline model that simply removes toxic words using a dictionary,
and then examines more sophisticated approaches that already exist.

## Usage

### Dataset

First things first: you have to download the dataset. To do that, simply run `src/data/make_dataset.py` **from the root of the
project!**

**Also make sure that you have `wget` and `unzip` on your machine!**

It won't work on Windows :((

If you're on Windows, download the [dataset](https://github.com/skoltech-nlp/detox/releases/download/emnlp2021/filtered_paranmt.zip) manually, unzip it, and put it into `data/raw/`

### Dependencies

Use requirements.txt:

`pip install -r requirements.txt`

### Detoxifying

To see the detoxified versions of inputs, run the following from the root of the project:
```
python src/models/predict_model.py src/models/input.txt
```

**Make sure you have installed all deps**

You can edit `input.txt` or use your own text

Example output:

![figure showing an example output](reports/figures/example_output.png)

## Project Structure

### Reports

`reports/` folder contains two reports describing ideas and exploration process.

### Notebooks

`notebooks/` folder contains all notebooks, which include:
- Data exploration notebook
- Baseline solution notebook
- Solution using a pre-trained Bert
- Attempt at fine-tuning a t5 pre-trained model

### Src

`src/` folder contains `python` scripts that can be executed to conduct training and prediction.
To visualize the outputs, run `src/visualization/visualize.py` 
