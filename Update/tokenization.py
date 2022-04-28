import nltk
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
import string
import re
import inflect
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
digit_converter = inflect.engine()
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
lemmatizer = WordNetLemmatizer()

def lowercase_reduction(input_string):
    return input_string.lower()

def convert_digit_to_text(input_string):
    temp_string = []
    words_of_string = input_string.split()

    for i in range(len(words_of_string)):
        if(words_of_string[i].isdigit()==True):
            temp_string.append(digit_converter.number_to_words(words_of_string[i]))

        else:
            temp_string.append(words_of_string[i])

    
    digitized_string = ' '.join(temp_string)
    return digitized_string


def removal_of_stopwords(input_string):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(input_string)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    final_string=""
    for word in filtered_text:
        final_string=final_string + " " + word
    return final_string

def stemming_func(input_string):
    word_tokens = word_tokenize(input_string)
    stems_words = [stemmer.stem(word) for word in word_tokens]
    final_string=""
    for word in stems_words:
        final_string=final_string + " " + word
    
    return final_string

def punctuation_and_whitespace_removal(input_string):
    converter = str.maketrans('', '', string.punctuation)
    temp_string = input_string.translate(converter)
    return  " ".join(temp_string.split())

def lemmatization_func(input_string):
    word_tokens = word_tokenize(input_string)
    lemmas = [lemmatizer.lemmatize(word, pos ='v') for word in word_tokens]
    final_string=""
    for word in lemmas:
        final_string=final_string + " " + word
    
    return final_string

def tokenization(text_string):
    returned_string = lowercase_reduction(text_string)
    returned_string1=convert_digit_to_text(returned_string)
    returned_string2=punctuation_and_whitespace_removal(returned_string1)
    returned_string3=removal_of_stopwords(returned_string2)
    #final_string=stemming_func(returned_string3)
    final_string=lemmatization_func(returned_string3)
    return final_string


def main():
    stri=tokenization("HI my NAmE is blah blah ....... blahhhhh         Aasish prateek and he is a boy who is 20 year old about to turn 21. He loves playing basketball and football")
    print(stri)

if __name__ == "__main__":
    main()