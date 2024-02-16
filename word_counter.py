import os
import requests

# Function to get the IP address of the machine
def get_ip_address():
    try:
        response = requests.get('https://jsonip.com')
        ip_address = response.json()['ip']
        return ip_address
    except Exception as e:
        print("Error retrieving IP address:", e)
        return None

# Function to count number of words in a text file
def count_words(file_path):
    with open(file_path, 'r') as file:
        return len(file.read().split())

# Directory of the text files
directory = '/home/data'

# Listing all text files in the directory
data_files = [file for file in os.listdir(directory) if file.endswith('.txt')]

# Counting number of words in all text files
word_counts = {}
for file in data_files:
    file_path = os.path.join(directory, file)
    word_counts[file] = count_words(file_path)
total_words = sum(word_counts.values())

# Finding the top 3 words with maximum counts in IF.txt
if_file_path = os.path.join(directory, 'IF.txt')
with open(if_file_path, 'r') as if_file:
    if_words = if_file.read().split()
    if_word_counts = {}
    for word in if_words:
        if_word_counts[word] = if_word_counts.get(word, 0) + 1
    top_words = sorted(if_word_counts.items(), key=lambda x: x[1], reverse=True)[:3]

# Getting the IP address
ip_address = get_ip_address()

# Writing the output to result.txt
output_file_path = '/home/output/result.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(f"List of text files: {', '.join(data_files)}\n")
    for file, count in word_counts.items():
        output_file.write(f"Total number of words in {file}: {count}\n")
    output_file.write(f"Grand total number of words: {total_words}\n")
    output_file.write("Top 3 words with maximum counts in IF.txt:\n")
    for word, count in top_words:
        output_file.write(f"{word}: {count}\n")
    if ip_address:
        output_file.write(f"IP Address of the machine: {ip_address}\n")
    else:
        output_file.write("Failed to retrieve IP address.\n")

# Printing the output to console
with open(output_file_path, 'r') as result_file:
    for line in result_file:
        print(line.strip())
