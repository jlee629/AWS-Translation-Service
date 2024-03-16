from chalice import Chalice
from chalicelib.translation_service import TranslationService

app = Chalice(app_name='Capabilities')
translation_service = TranslationService()

FILE = 'headlines_jungyu.txt'  

@app.route('/news', methods=['GET'], cors=True)
def get_headlines():
    headlines = translation_service.read_headlines_from_file(FILE)
    translated_headlines = []
    for headline in headlines:
        translated_text = translation_service.translate_text(headline)
        translated_headlines.append({'original_text': headline, 'translated_text': translated_text})
    return {'headlines': translated_headlines}
