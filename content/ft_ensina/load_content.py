from markdown2 import markdown
from lxml import html
import json
import os

def load_ft_ensina_videos(dict):
    video_dir = 'content/ft_ensina/videos/'
    all_data = []
    filenames = [x for x in sorted(os.listdir(video_dir)) if x.endswith('.md')]
    for i, item in enumerate(filenames, start=1):
        content = html.fromstring(markdown(open(video_dir+item, 'r').read()))
        all_data.append({
            "numero": i,
            "disciplina": content.xpath('//h1/text()')[0],
            "titulos": content.xpath('//h2/text()'),
            "assuntos": content.xpath('//h4/text()'),
            "links": content.xpath('//h6/text()')
        })
    
    dict['FT_ENSINA_CONTENT'] = (all_data)
    