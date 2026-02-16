
import argparse


parser = argparse.ArgumentParser(
    prog="wc program",
    description="Implements the cat program"
)

parser.add_argument("paths", nargs='+', type=str, help="The path to process")
parser.add_argument('-l', '--lines', action="store_true", help='Ouput number of lines')
parser.add_argument('-w', '--words', action="store_true", help='Ouput number of words')
parser.add_argument('-c', '--chars', action="store_true", help='Ouput number of characters')

args = parser.parse_args()
is_lines_option = args.lines
is_words_option = args.words
is_chars_option = args.chars


def extract_lines(content):
    lines = content.split('\n')
    if lines and lines[-1] == '':
        lines = lines[:-1]
    return lines

def extract_words(content):
    return content.split(' ')

def extract_chars(content):
    return list(content)

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def get_lines_words_chars_count(file_path):
    content = read_file_content(file_path)
    lines = extract_lines(content)
    words = extract_words(content)
    chars = extract_chars(content)
    return  [len(lines), len(words), len(chars)]


def print_selected_counts(file_path):
    lines_words_chars_count = get_lines_words_chars_count(file_path)
    
    lines_count = lines_words_chars_count[0]
    words_count = lines_words_chars_count[1]
    chars_count = lines_words_chars_count[2]

    if is_lines_option: print(lines_count, file_path)
    elif is_words_option: print(words_count, file_path)
    elif is_chars_option: print(chars_count, file_path)
    else: print(lines_count, words_count, chars_count, file_path)

def print_total_lines(lines_words_chars_count, total):
     total_lines = sum(count[0] for count in lines_words_chars_count)
     total_words = sum(count[1] for count in lines_words_chars_count)
     total_chars = sum(count[2] for count in lines_words_chars_count)
     
     if is_lines_option: print(total_lines, total)
     elif is_words_option: print(total_words, total)
     elif is_chars_option: print(total_chars, total)
     else: print(total_lines, total_words, total_chars, total)

def print_file_statistics():
    lines_words_chars_count = []
    if len(args.paths) == 1:
        print_selected_counts(args.paths[0])
    else:
        for file_path in args.paths:
            result = get_lines_words_chars_count(file_path)
            lines_words_chars_count.append(result)
            print_selected_counts(file_path)
        print_total_lines(lines_words_chars_count, 'total')

print_file_statistics()
