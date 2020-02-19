from readabilipy import simple_json_from_html_string
import json
def readability_parser(path):
    with open(path, 'r', encoding="utf8") as f:
        html_string = f.read()
        article = simple_json_from_html_string(html_string, content_digests=False, node_indexes=False, use_readability=True)
        #article_json = json.dumps(article)
        parsed_article={}
        text=''
        for item in article['plain_text']:
            text+= item['text']
        parsed_article['title']=article['title']
        parsed_article['author']=article['byline']
        parsed_article['content']=text
        return parsed_article
      