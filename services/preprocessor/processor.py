import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
# download nltk files
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger_eng')
# Get English stopwords and tokenize
stop_words = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()

class Processor:
    @staticmethod
    def run(text):
        print("Processor Run.")
        clean = Processor.clean_text(text)
        no_sw = Processor.rmv_stop_words(clean)
        lemma = Processor.lemmatization(no_sw)
        return lemma

    @staticmethod
    def clean_text(text):
        #remove links & users references
        keyword = "https://t.co/"
        split_text = text.split()
        clean_text = ""
        for i in split_text:
            # get rid of links
            if (keyword not in i) and (i[0] != "@"):
                clean_text += " " + i
        #remove symbols
        clean_str = re.sub(r'[^A-Za-z0-9 ]+', "", clean_text)
        return clean_str

    @staticmethod
    def rmv_stop_words(text):
        tokens = word_tokenize(text.lower())
        # Remove stopwords
        filtered_tokens = [word for word in tokens if word not in stop_words]
        return  " ".join(filtered_tokens)

    @staticmethod
    def lemmatization (text):
        tokens = word_tokenize(text)
        tagged_tokens = pos_tag(tokens)

        def get_wordnet_pos(tag):
            if tag.startswith('J'):
                return 'a'
            elif tag.startswith('V'):
                return 'v'
            elif tag.startswith('N'):
                return 'n'
            elif tag.startswith('R'):
                return 'r'
            else:
                return 'n'

        lemmatized_sentence = []

        for word, tag in tagged_tokens:
            if word.lower() == 'are' or word.lower() in ['is', 'am']:
                lemmatized_sentence.append(word)
            else:
                lemmatized_sentence.append(lemmatizer.lemmatize(word, get_wordnet_pos(tag)))

        return ' '.join(lemmatized_sentence)
