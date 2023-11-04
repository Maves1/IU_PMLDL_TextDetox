import subprocess, os

dataset_link = "https://github.com/skoltech-nlp/detox/releases/download/emnlp2021/filtered_paranmt.zip"
dataset_dest = "data/raw/"
dataset_name = "filtered_paranmt.zip"

if not os.path.exists(dataset_dest):
    os.makedirs(dataset_dest)

try:
    print("Trying to download the dataset...")
    subprocess.run(["wget", dataset_link, "-O", dataset_dest + dataset_name], check=True)
    print("Dataset has been downloaded successfully to <project_folder>/data/raw/")

    print("Unzipping...")
    subprocess.run(["unzip", dataset_dest + dataset_name, "-d", "data/raw/"])
    print("Dataset is ready!")
except Exception:
    print("Something went wrong\nMake sure you run this script from the project root!")
