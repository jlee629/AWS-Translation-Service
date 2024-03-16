import boto3

class TranslationService:
    def __init__(self):
        self.translate_client = boto3.client('translate')

    def translate_text(self, text, source_language_code='auto', target_language_code='en'):
        try:
            response = self.translate_client.translate_text(
                Text=text,
                SourceLanguageCode=source_language_code,
                TargetLanguageCode=target_language_code
            )
            return response['TranslatedText']
        except Exception as e:
            error_message = str(e)
            if "UnsupportedLanguagePairException" in error_message:
                return "Language not supported"
            else:
                print(f"Error translating text: {e}")
                return "Translation error"

    def read_headlines_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                headlines = [line.strip() for line in file.readlines()]
            return headlines
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return []
