import os
import threading
import time

def search_keywords_in_file(file_path, keywords, results):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    if keyword not in results:
                        results[keyword] = []
                    results[keyword].append(file_path)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def threaded_search(file_list, keywords):
    results = {}
    threads = []

    for file_path in file_list:
        thread = threading.Thread(target=search_keywords_in_file, args=(file_path, keywords, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

if __name__ == "__main__":
    file_list = ["file1.txt", "file2.txt", "file3.txt"]  # Список файлів для обробки
    keywords = ["keyword1", "keyword2", "keyword3"]  # Список ключових слів

    start_time = time.time()
    results = threaded_search(file_list, keywords)
    end_time = time.time()

    print(f"Threaded search results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")