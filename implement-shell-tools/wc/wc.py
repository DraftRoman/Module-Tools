import argparse
import os

parser = argparse.ArgumentParser(description="wc command")
parser.add_argument("files",nargs="+",help="File(s) or directory to read")
parser.add_argument("-l", dest="lines", action="store_true", help="count the number of lines")
parser.add_argument("-w", dest="words", action="store_true", help="count the number of words")
parser.add_argument("-c", dest="chars", action="store_true", help="count the number of characters")
args = parser.parse_args()

total_lines = 0
total_words = 0
total_chars = 0
file_counter=0


def totals(line_count,word_count,char_count):
    global total_lines,total_words,total_chars
    total_lines += line_count
    total_words += word_count
    total_chars += char_count

def output(line_count ,word_count ,char_count,filename,args):
    if not(args.lines or args.words or args.chars):
        return f"{line_count}\t{word_count}\t{char_count}\t{filename}"
    output=[]
    if args.lines:
        output.append(str(line_count))
    if args.words:
        output.append(str(word_count))    
    if args.chars:
        output.append(str(char_count))
    output.append(filename)  
    return "\t".join(output)    

def count_file(path):
    with open(path) as f:
        text = f.read()
    return (
        len(text.splitlines()),
        len(text.split()),
        len(text),
    )
for file in args.files:
    if os.path.isdir(file):
        for f in os.listdir(file):
            path=os.path.join(file,f)
            if os.path.isfile(path):
                file_counter +=1
                line_count, word_count, char_count = count_file(path)
                print(output(line_count, word_count, char_count, path, args))
                totals(line_count, word_count, char_count)
                


    else:
        file_counter +=1
        line_count, word_count, char_count = count_file(file)
        print(output(line_count, word_count, char_count, file, args))
        totals(line_count, word_count, char_count)

if file_counter > 1:
    print(output(total_lines, total_words, total_chars, "total", args))

