import emoji
import numpy as np
import io
import os
import glob
import string
import re

from langdetect import detect
import time
import re
import multiprocessing as mp
from itertools import filterfalse
from more_itertools import chunked
from tqdm import tqdm


def deEmojify(text):
    regrex_pattern = re.compile(pattern="["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)


print("script execution begins")


counter = 0


def clean_line(row):

    start_time = time.time()

    initialized = True

    User = ''
    digits = r'[0-9]'
    text_array = row
    text_array = deEmojify(text_array)
    text_array = text_array.replace('#', '')
    text_array = text_array.replace('(' , '') #added
    text_array = text_array.replace(')', '')  #added
    text_array = text_array.replace('؟', '')  # added
    text_array = text_array.replace('/', '')  # added
    text_array = text_array.replace('_', ' ')  # added
    text_array = text_array.replace('-', ' ')  # added
    text_array = text_array.replace('،', '\n')  # added
    text_array = re.sub(digits, '', text_array) #added
    text_array = re.sub('[\u0660-\u0669]', ' ', text_array) #added
    text_array = re.sub(r'\s*[a-zA-Z]+\b', '', text_array) #added

    text_array = text_array.rstrip()
    text_array = text_array.split()

    filtered_text_array = []
    # if counter > 490:
    #      break
    for word in text_array:
        try:
            lang = detect(word)
        #  print(lang)
            if lang == 'ar' or lang == 'fa' or lang == 'ur':
                #  print(word + '   :  added')
                filtered_text_array.append(word)
        #  else:
        #  print(word + '   :  deleted')
        except Exception:
            #  print("#"+word + '   :  deleted')
            pass
    new_text_array = " ".join(filtered_text_array)
    return new_text_array


def launch(path):
    start_time = time.time()

    file = open(r'/home/duaa/data/collected_telegram_data/novels(1-5).txt', "r", encoding='UTF-8')
    lines = file.readlines()
    output_ = list(map(clean_line, lines))
    end_time = time.time()
    print(f"the files is cleaned and it took {end_time - start_time}")


if __name__ == '__main__':

    # Note
    # open python script
    # then import multiprocessing as mp
    # then check the total number of processers you have in your machine by writing the following code
    # first mp.cpu_count()
    # make sure num_processes is less than mp.cpu_count() else you will be running multithreading and this will reduce the speed of multiprocessing
    #counter2 = 0
    num_processes = 5
    lines_per_chunk = 500
    # processes = []
    # # for rank in range(num_processes):
    # pool = mp.Pool(num_processes)
    # pool.map(launch, "/home/muhammed/Documents/theory_4.txt")
    # file = open("/home/muhammed/Documents/theory_4.txt", "r")

    # lines_for_multiprocess = file.readlines()
    # start_time = time.time()
    # output_files = list(map(clean_line, lines_for_multiprocess))
    # end_time = time.time()
    # print(f"the files is cleaned and it tooks {end_time - start_time}")

    with open(r'/home/duaa/data/collected_telegram_data/novels(1-5).txt', 'r', encoding='UTF-8') as infile:
        with open(r'/home/duaa/data/cleaned_telegram_data/cleaned_novels(1-5).txt', "a+", encoding='UTF-8') as outfile:
            with mp.Pool(num_processes) as pool:
                processed = pool.imap(clean_line, infile, lines_per_chunk) # process lines in chunks
                output_lines = filterfalse(lambda s: len(s.strip()) == 0, processed) # remove whitespaces
                with tqdm() as progress:
                    for lines in chunked(output_lines, lines_per_chunk*num_processes):
                        outfile.write("\n".join(lines))
                        progress.update(len(lines))

   # file_name = csvfile.split('.')
   # file_name = file_name[0]
   # file_name = file_name.split('/')
   # file_name = file_name[len(file_name) - 1]
   # print('saving file : ' + file_name)

