import nltk
import csv
from nltk.tokenize import word_tokenize # or use some other tokenizer
from tqdm import tqdm
import pickle
"""
def clean(string):
    new_str = [s for s in string if s.isalnum()]
    new_str = ''.join(new_str)
    new_str = new_str.lower()
    return new_str

articles = {}
filename = 'data/trojmiasto.csv'
stopwords = ""
with open("stopwords.txt", 'r', encoding='utf-8') as rfile:
    stopwords = rfile.read()

stopwords = stopwords.split('\n')

with open(filename, 'r', encoding="utf-8") as rfile:
    reader = csv.DictReader(rfile, delimiter = ',', quotechar='"')
    for row in reader:
        words = row['Title'].split(' ')
        words = [clean(w) for w in words if w not in stopwords]
        words = ' '.join(words)
        articles[words] = row['Category']


train = [(k, v) for k,v in articles.items()]
train = train[25971]
print('here')
all_words = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in tqdm(train)]
print('here')
"""
f = open('my_classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

"""testing_set = t
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)
"""
train = [("Truskawki - bomba witaminowa dla zdrowia i urody", "Zdrowie"),
        ("Rodzinne pikniki. Nowa formuła firmowej integracji","Praca"),
        ("Atom Trefl Sopot zostaje w Orlen Lidze","Sport","39")]
all_words = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in tqdm(train)]
#print(t)
print(classifier.labels())
print(train[0][0], classifier.classify(t[0][0]))
print(train[1][0], classifier.classify(t[1][0]))
print(train[2][0], classifier.classify(t[2][0]))
classifier.show_most_informative_features()
#print(classifier.prob_classify(t[0][0]).samples())
