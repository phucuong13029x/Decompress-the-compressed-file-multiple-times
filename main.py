import gzip
import os


INPUT_DIRECTORY = 'D:\\Un'
OUTPUT_DIRECTORY = 'D:\\Un'
GZIP_EXTENSION = '.gz'
MORE_EXTENSION = '.1'

while True:
    process = 0
    for file in os.scandir(INPUT_DIRECTORY):
        if file.name.lower().endswith(GZIP_EXTENSION):
            process += 1
            output_path = os.path.join(OUTPUT_DIRECTORY, file.name[:-len(GZIP_EXTENSION)])
            print('[+] Decompressing', file.path, 'to', output_path)
            with gzip.open(file.path, 'rb') as file:
                with open(output_path, 'wb') as output_file: output_file.write(file.read())
            os.remove(os.path.join(INPUT_DIRECTORY, file.name))
        elif file.name.lower().endswith(MORE_EXTENSION):
            process += 1
            prename, ext = os.path.splitext(file.name)
            os.rename(os.path.join(INPUT_DIRECTORY, file.name), os.path.join(OUTPUT_DIRECTORY, prename))
    if process == 0: break