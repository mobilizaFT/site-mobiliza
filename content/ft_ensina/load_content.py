from markdown2 import markdown
from lxml import html
import os

def load_ft_ensina_videos(dict):
    video_dir = 'content/ft_ensina/videos/'
    filenames = [x for x in sorted(os.listdir(video_dir)) if x.endswith('.md')]
    content = [html.fromstring(markdown(open(video_dir+x, 'r').read())) for x in filenames]
    disciplinas = [(y, (x.xpath('//h6/text()')[0])) for (y, x) in enumerate(content, start=1)]
    titulos = [(y, x.xpath('//h4/text()')) for (y, x) in enumerate(content, start=1)]
    assuntos = [(x.xpath('//h2/text()')) for (x) in (content)]
    links = [(x.xpath('//h1/text()')) for (x) in (content)]

    videos = []
    for i in range(len(titulos)):
        for j in range(len(titulos[i][1])):
            videos.append((titulos[i][0], titulos[i][1][j], assuntos[i][j], links[i][j]))
    
    dict['DISCIPLINAS'] = disciplinas
    dict['VIDEOS'] = videos
    