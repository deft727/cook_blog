from collections import defaultdict

def group(files):
    owners=defaultdict(list)
    for file,owner in files.items():
        owners[owner].append(file)
    return owners

files = {
    'input.txt':'Randy',
    'code.py':'Stan',
    'output.py':'Randy'
}

print(group(files))