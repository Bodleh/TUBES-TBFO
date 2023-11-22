import re


def parse_html(html_path):
    with open(html_path, 'r') as file:
        html_content = file.read()

    tag_regex = r"(<!--[\s\S]*?-->)|(<[^>]+>)|([^<]+)"
    tokens = []
    special_values = ['get', 'post', 'submit', 'reset', 'button',
                      'password', 'text', 'email', 'number', 'checkbox']
    special_tags = {'button': ['type'], 'form': ['method'], 'input': ['type']}

    for match in re.finditer(tag_regex, html_content):
        if match.group(1):  # If it's a comment
            if match.group(1):  # If it's a comment
                tokens.append('<!--')
                tokens.append('STR')  # Comment content as 'STR'
                tokens.append('-->')
        elif match.group(2):  # If it's a tag
            tag = match.group(2)
            tag_name = ''
            attribute_name = ''
            inside_quotes = False
            quote_content = ''
            temp_token = ''

            for char in tag:
                if char == '"' and not inside_quotes:
                    inside_quotes = True
                    quote_content = ''
                    tokens.append('"')  # Add opening quote to tokens
                    continue

                if char == '"' and inside_quotes:
                    inside_quotes = False
                    cleaned_tag_name = tag_name.split('<')[-1]

                    if cleaned_tag_name in special_tags and attribute_name in special_tags[cleaned_tag_name]:
                        if quote_content in special_values:
                            tokens.append(quote_content)
                        else:
                            if quote_content.lower() == 'get' or quote_content.lower() == 'post':  # To handle METHOD
                                #
                                tokens.append(quote_content.lower())
                            else:                                                                  #
                                tokens.append(
                                    "STR" if quote_content.strip() else "NO_STR")
                    else:
                        tokens.append(
                            "STR" if quote_content.strip() else "NO_STR")

                    attribute_name = ''
                    tokens.append('"')  # Add closing quote to tokens
                    continue

                if inside_quotes:
                    quote_content += char
                else:
                    if char in [' ', '=', '>', '\n', '\r', '\t']:
                        if temp_token:
                            if temp_token not in ['<', '=', '>']:
                                if not tag_name:
                                    tag_name = temp_token
                                else:
                                    attribute_name = temp_token
                            tokens.append(temp_token)
                            temp_token = ''
                        if char == '>':
                            tokens.append(char)
                            # Add 'X' after each close tag '>'
                            tokens.append('x')
                        elif char == "=":
                            tokens.append(char)
                    elif char != '<':
                        temp_token += char
                    else:
                        temp_token = char

            if temp_token:
                tokens.append(temp_token)

        else:  # If it's text content
            text = match.group(3).strip()
            if text:
                tokens.append("STR")

    return filter_tokens(tokens)


def filter_tokens(tokens):
    filtered_tokens = []
    in_title_tag = False  # Flag to track if we're inside a <title> tag
    skip_content = False  # Flag to skip content inside <title>...</title>

    for token in tokens:
        if '<title' in token.lower():
            in_title_tag = True
            skip_content = False
            filtered_tokens.append(token)
        elif '</title' in token.lower():
            in_title_tag = False
            skip_content = False
            filtered_tokens.append(token)
        elif in_title_tag and token == '>':
            skip_content = True  # Start skipping content after the '>' of <title>
            filtered_tokens.append(token)
        elif (not skip_content and token not in ['STR', 'NO_STR']) or token == 'x':
            filtered_tokens.append(token)

    return filtered_tokens
