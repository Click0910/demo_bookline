import re


def extract_gifs(log_file, output_file):
    # Create a Set to store the gif unique names.
    gif_names = set()

    # Open the log_file.txt file
    with open(log_file, 'r') as log:
        for line in log:
            # Search lines that return 200 GET requests status code
            match = re.search(r'GET (.*\.gif) HTTP/1\.[01]" 200', line)
            if match:
                # If there is a match add the record to the set.
                gif_names.add(match.group(1))

    # Open the file unique_gifs.txt, In case that does not exist, one file will be created
    with open(output_file, 'w') as out:
        for name in gif_names:
            # Write each name in the file.
            out.write(name + '\n')


extract_gifs('log_file.txt', 'unique_gifs.txt')
