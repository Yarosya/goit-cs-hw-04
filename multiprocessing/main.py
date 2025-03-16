import os
import multiprocessing
import time

def search_keywords_in_file(file_path, keywords, result_queue):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    result_queue.put((keyword, file_path))
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def multiprocess_search(file_list, keywords):
    result_queue = multiprocessing.Queue()
    processes = []

    for file_path in file_list:
        process = multiprocessing.Process(target=search_keywords_in_file, args=(file_path, keywords, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = {}
    while not result_queue.empty():
        keyword, file_path = result_queue.get()
        if keyword not in results:
            results[keyword] = []
        results[keyword].append(file_path)

    return results

if __name__ == "__main__":
    file_list = ["file1.txt", "file2.txt", "file3.txt"]
    keywords = ["keyword1", "keyword2", "keyword3"]

    start_time = time.time()
    results = multiprocess_search(file_list, keywords)
    end_time = time.time()

    print(f"Multiprocess search results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")