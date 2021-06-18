import os


def download_github_code(path):
    filename = path.rsplit('/')[-1]
    os.system('shred -u {}'.format(filename))
    os.system('wget -q https://raw.githubusercontent.com/Alenush/mds_nlp_2021/main/{} -O {}'.format(path, filename))


def setup():
    download_github_code('utils/grading.py')
