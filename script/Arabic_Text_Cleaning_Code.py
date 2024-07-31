import re
from langdetect import detect
from concurrent.futures import ProcessPoolExecutor
from more_itertools import chunked
from tqdm import tqdm

def deEmojify(text):
    regex_pattern = re.compile(
        pattern="["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                "]+", flags=re.UNICODE)
    return regex_pattern.sub(r'', text)

def clean_line(text):
    digits = r'[0-9]'
    text = deEmojify(text)
    text = re.sub(r'[؟()/#_,\-]', '', text)  # combined replacements
    text = re.sub(digits, '', text)
    text = re.sub('[\u0660-\u0669]', ' ', text)
    text = re.sub(r'\s*[a-zA-Z]+\b', '', text)
    text = text.rstrip()
    words = text.split()
    
    filtered_words = []
    for word in words:
        try:
            lang = detect(word)
            if lang in {'ar', 'fa', 'ur'}:
                filtered_words.append(word)
        except Exception:
            continue
            
    return " ".join(filtered_words)

def process_file(input_path, output_path, num_processes, lines_per_chunk):
    with open(input_path, 'r', encoding='UTF-8') as infile, \
         open(output_path, 'w', encoding='UTF-8') as outfile:
        
        with ProcessPoolExecutor(max_workers=num_processes) as executor:
            chunks = chunked(infile, lines_per_chunk)
            future_to_chunk = {executor.submit(clean_lines, chunk): chunk for chunk in chunks}
            
            with tqdm(total=len(future_to_chunk)) as progress:
                for future in future_to_chunk:
                    cleaned_lines = future.result()
                    if cleaned_lines:
                        outfile.write("\n".join(cleaned_lines) + "\n")
                    progress.update(1)

def clean_lines(lines):
    return [clean_line(line) for line in lines if line.strip()]

if __name__ == '__main__':
    input_path = r'/home/duaa/data/collected_telegram_data/novels(1-5).txt'
    output_path = r'/home/duaa/data/cleaned_telegram_data/cleaned_novels(1-5).txt'
    num_processes = 5
    lines_per_chunk = 500

    process_file(input_path, output_path, num_processes, lines_per_chunk)
