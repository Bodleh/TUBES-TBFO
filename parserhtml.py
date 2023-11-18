import re


def parse_html(html_content):
    tag_regex = r"(<!--[^>]*-->)|(<[^>]+>)|([^<]+)"
    tokens = []

    for match in re.finditer(tag_regex, html_content):
        if match.group(1):  # If it's a comment
            comment = match.group(1)
            # Split the comment into start, content, and end
            if comment.startswith('<!--') and comment.endswith('-->'):
                tokens.append('<!--' + comment[4:-3].strip())
                tokens.append('-->')
            else:
                # Handle cases with spaces like <! --comment -- >
                comment_parts = re.split(
                    r'(\s*<!\s*|\s*--\s*|\s*>|\s*--\s*>)', comment)
                tokens.extend([part for part in comment_parts if part.strip()])
        elif match.group(2):  # If it's a tag
            tag = match.group(2)
            inside_quotes = False
            quote_content = ''
            temp_token = ''

            for char in tag:
                if char == '"' and not inside_quotes:  # Opening quote
                    inside_quotes = True
                    if temp_token:  # Add the token before the quote
                        tokens.append(temp_token)
                        temp_token = ''
                    tokens.append('"')  # Add the opening quote
                    continue
                elif char == '"' and inside_quotes:  # Closing quote
                    inside_quotes = False
                    tokens.append("STR" if quote_content.strip() else "NO_STR")
                    tokens.append('"')  # Add the closing quote
                    quote_content = ''
                    continue

                if inside_quotes:
                    quote_content += char
                else:
                    if char in [' ', '=', '>', '\n', '\r', '\t']:
                        if temp_token:
                            tokens.append(temp_token)
                            temp_token = ''
                        if char == '=':
                            tokens.append(char)
                        elif char == '>':
                            tokens.append(char)
                    elif char != '<':
                        temp_token += char
                    else:
                        temp_token = char

            if temp_token:  # Add the last token if it exists
                tokens.append(temp_token)

        else:  # If it's text content
            text = match.group(3).strip()
            if text:  # If the text is not just whitespace
                tokens.append("STR")  # Append 'STR' for non-whitespace text

    return tokens


# Read the HTML file
file_html = "testuntukerror.html"
with open(file_html, 'r') as file:
    html_content = file.read()

# Parse the HTML and get tokens
tokens = parse_html(html_content)
print(tokens)
