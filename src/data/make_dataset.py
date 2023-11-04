import subprocess, os

dataset_url = "https://github.com/skoltech-nlp/detox/releases/download/emnlp2021/filtered_paranmt.zip"
dataset_dest = "data/raw/"
dataset_name = "filtered_paranmt.zip"

toxic_words_url = "https://raw.githubusercontent.com/s-nlp/detox/main/emnlp2021/style_transfer/condBERT/vocab/toxic_words.txt"
toxic_words_dest = "data/raw/"
toxic_words_name = "toxic_words.txt"

def download_file(url: str, dest: str, filename: str):
    subprocess.run(["wget", url, "-O", dest + filename], check=True)


if not os.path.exists(dataset_dest):
    os.makedirs(dataset_dest)

try:
    print("Trying to download the dataset...")
    download_file(dataset_url, dataset_dest, dataset_name)
    print(f"Dataset has been downloaded successfully to <project_folder>/{dataset_dest}")

    print("Unzipping...")
    subprocess.run(["unzip", dataset_dest + dataset_name, "-d", "data/raw/"])
    print("Dataset is ready!")

    print("Trying to download toxic words...")
    download_file(toxic_words_url, toxic_words_dest, toxic_words_name)
    print("Toxic words are ready!")
except Exception:
    print("Something went wrong\nMake sure you run this script from the project root!")
