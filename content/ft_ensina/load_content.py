from markdown2 import markdown
import os

vid_dir = 'content/ft_ensina/videos/'

def evaluate_line(line):
    if len(line) > 1:
        return line[1].lstrip()
    return ''

def load_ft_ensina(dict):
    fnms = []
    disc = []
    vid = []
    for file in os.listdir(vid_dir):
        if file.endswith('.txt'):
            fnms.append(file)

    disc_number = 1
    for f in sorted(fnms):
        content = open(f'{vid_dir}{f}', 'r').read()
        content = content.split('****')
        content_index = 0
        disc_name = ''
        for c in content:
            c = c.split('\n')
            if(content_index == 0):
                disc_name = c[0].split('>')[1].lstrip()
                disc.append((disc_name, disc_number))
            else:
                vid_info = {}
                titulo = ""
                assunto = ""
                link = ""
                for line in c:
                    line = line.split('>')
                    if(len(line) >= 1):
                        if line[0] == 'titulo':
                            titulo = evaluate_line(line)
                        if line[0] == 'assunto':
                            assunto = evaluate_line(line)
                        if line[0] == 'link':
                            link = evaluate_line(line)
                vid.append((disc_number, link, titulo, assunto))
            content_index+=1
        disc_number += 1

    dict['VIDEOS'] = vid
    dict['DISCIPLINAS'] = disc
