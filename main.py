import argparse

tokens = []
states = []
tf = []

def parse_dfa(file_pda: str) -> bool :
    global tf
    print(file_pda) 

def parse_html(file_html) :
    global tokens
    #parse
    print(file_html)

parser = argparse.ArgumentParser()

parser.add_argument('file1', type=str, help='The path to the PDA definition file (.txt)')
parser.add_argument('file2', type=str, help='The path to the HTML file (.html)')

args = parser.parse_args()
file_pda, file_html = args.file1, args.file2

is_txt, is_html = file_pda.endswith('.txt'), file_html.endswith('.html')
if not is_txt :
    print("Error: File 1 is not a txt file")

if not is_html :
    print("Error: File 2 is not a HTML file")

if not is_txt or not is_html :
    exit()

file_pda = open(file_pda, 'r').read()
file_html = open(file_html, 'r').read()

success_parse_pda = parse_dfa(file_pda)
parse_html(file_html)