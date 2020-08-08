from bs4 import BeautifulSoup
import os


def insert_data_to_base_template(dictionary_data, img_src_path):
    base_html = open(os.path.join('html_template', 'index_base.html'))
    soup = BeautifulSoup(base_html, features="html.parser")

    for key in dictionary_data:
        row_span = len(dictionary_data[key])
        new_tr = '<tr><td rowspan="' + str(row_span) + '">' + key + '</td>'
        new_tr = new_tr + '<td>' + dictionary_data[key][0] + '</td><td><img src="' + os.path.join(img_src_path, dictionary_data[key][0].split()[0] + '.jpg') + '" width="100" height="100"/></td>'
        for val in dictionary_data[key][1:]:
            new_tr = new_tr + '<tr><td>' + val + '</td><td><img src="' + os.path.join(img_src_path, val.split()[0] + '.jpg') + '" width="100" height="100"/></td></tr>'
        new_tr = new_tr + '</tr>'
        soup.tbody.append(BeautifulSoup(new_tr, 'html.parser'))

    with open(os.path.join('html_template', 'index.html'), 'w') as file:
        file.write(str(soup))

