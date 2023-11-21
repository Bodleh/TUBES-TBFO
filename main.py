import argparse
from htmlparser import parse_html
from pdaparser import parse_pda, process, printPDA

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

pda = parse_pda(file_pda)
printPDA(pda) #Debugging
tokens = parse_html(file_html)
print(tokens) #Debugging
process(pda, tokens)