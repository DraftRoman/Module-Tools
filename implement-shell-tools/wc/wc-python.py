import argparse

def count_file(filename):
   
    with open(filename, 'r') as file:
        content = file.read()
    
    lines = len(content.splitlines())
    words = len(content.split())
    chars = len(content)
    
    return (lines, words, chars)
  

def format_output(lines, words, chars, filename, show_l, show_w, show_c):
    parts = []
    
    if show_l:
        parts.append(f"{lines:8}")
    if show_w:
        parts.append(f"{words:8}")
    if show_c:
        parts.append(f"{chars:8}")
    
    parts.append(filename)
    
    return " ".join(parts)

def main():
    parser = argparse.ArgumentParser(description="wc imlementation in Python")

    parser.add_argument("files", nargs="+", help="Files to process")
    parser.add_argument("-l", action="store_true", help="Show line count")
    parser.add_argument("-w", action="store_true", help="Show word count")
    parser.add_argument("-c", action="store_true", help="Show character count")

    args = parser.parse_args()

    l = args.l
    w = args.w
    c = args.c
    files = args.files
    
    if not (l or w or c):
        l = w = c = True

    total_lines = total_words = total_chars = 0
    processed_files = 0
    
    for filename in files:
        result = count_file(filename)
        if result:
            lines, words, chars = result
            print(format_output(lines, words, chars, filename, l, w, c))
            
            total_lines += lines
            total_words += words
            total_chars += chars
            processed_files += 1
    
    if processed_files > 1:
        print(format_output(total_lines, total_words, total_chars, "total", l, w, c))

if __name__ == "__main__":
    main()
