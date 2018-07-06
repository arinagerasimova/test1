
>>> import nltk
>>> nltk.download('punkt')
>>> from nltk import word_tokenize,sent_tokenize



>>> text="London is the capital of Great Britain. It is one of the greatest cities in the world. It is an important business and financial centre. It is an intellectual centre, too."
>>> sent_text=sent_tokenize(text)
>>> sent_text
>>> len(sent_text)


>>> text.split()
>>> word_text=word_tokenize(text)
>>> word_text



>>> text1=nltk.Text(word_text)
>>> text1.concordance("London")



>>> wnl=nltk.stem.WordNetLemmatizer()
>>> [wnl.lemmatize(w) for w in word_text]



>>> nltk.download('averaged_perceptron_tagger')
>>> from nltk import pos_tag
>>> nltk.pos_tag(word_text)
>>> text_pos=nltk.pos_tag(word_text)
>>> text_pos_dict=dict(text_pos)
>>> text_pos_dict
>>> text_indexing=nltk.Index((value,key) for (key,value) in text_pos_dict.items())
>>> text_indexing["NN"]





>>> from nltk import FreqDist  
>>> fd=FreqDist(word_text)
>>> fd["cake"]
>>> fd["It"]

