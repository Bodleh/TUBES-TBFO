l = ['<html',  '<head', '>', '<title', 'STR', '</title', '<link', 'rel', '=', '"', 'NO_STR', 'href', '=', '"', 'NO_STR', '"', '>', '<script', 'src', '=', '"', 'NO_STR', '"', '>', '</script', '>', '</head', '>', '<body', '>', '<link', '>', '<h1', '>', '</h1', '>', '<h2', '>', '</h2', '>', '<h3', '>', '</h3', '>', '<h4', '>', '</h4', '>', '<h5', '>', '</h5', '>', '<h6', '>', '</h6', '>', '<p', 'class', '=', '"', 'STR', '"', 'id', '=', '"', 'STR', '"', 'style', '=', '"', 'NO_STR', '"', '>', '</p', '>', '<br', '>', '<em', '>', '</em', '>', '<b', '>', '</b', '>', '<abbr', '>', '</abbr', '>', '<strong', '>', '</strong', '>', '<small', '>', '</small', '>', '<hr', '>', '<!--','!--', 'STR','-->','--', '<div', '>', '<div', '>', '</div', '>', '</div', '>', '<a', 'href', '=', '"', 'NO_STR', '"', '>', '</a', '>', '<img', 'src', '=', '"', 'NO_STR', '"', 'alt', '=', '"', 'NO_STR', '"', '>', '<button', 'type', '=', '"', 'STR', '"', '>', '</button', '>', '<form', 'action', '=', '"', 'STR', '"', 'method', '=', '"', 'STR', '"', '>', '</form', '>', '<form', 'action', '=', '"', 'STR', '"', 'method', '=', '"', 'STR', '"', '>', '</form', '>', '<input', 'type', '=', '"', 'STR', '"', 'id', '=', '"', 'NO_STR', '"', '>', '<input', 'type', '=', '"', 'STR', '"', 'id', '=', '"', 'NO_STR', '"', '>', '<table', '>', '<tr', '>', '</tr', '>', '<td', '>', '</td', '>', '<th', '>', '</th', '>', '</table', '>', '</body', '>', '<script', '>', '</script', '>', '</html', '>', 'GET', 'POST', 'submit', 'reset', 'button','password','text','email','number','checkbox']

l_unique = []
for el in l :
    if el not in l_unique :
        l_unique.append(el)

for el in l_unique:
    print(el)
