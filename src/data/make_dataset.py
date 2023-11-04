import subprocess

dataset_link = "https://github.com/skoltech-nlp/detox/releases/download/emnlp2021/filtered_paranmt.zip"
dataset_dest = "data/raw/filtered_paranmt.zip"

try:
    print("Trying to download the dataset...")
    subprocess.run(["wget", dataset_link, "-O", dataset_dest], check=True)
    print("Dataset has been downloaded successfully to <project_folder>/data/raw/")

    print("Unzipping...")
    subprocess.run(["unzip", dataset_dest, "-d", "data/raw/"])
    print("Dataset is ready!")
except Exception:
    print("Something went wrong\nMake sure you run this script from the project root!")
