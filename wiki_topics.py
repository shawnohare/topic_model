from __future__ import print_function
import numpy as np
import logging, gensim

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO)
    
# load the preprocessed data    
id2word = gensim.corpora.Dictionary.load_from_text('data/wiki_en_output_wordids.txt')

# convert the corpus to the matrix market format
mm = gensim.corpora.MmCorpus('data/wiki_en_output_tfidf.mm')

# build the model.  This will probably take a few hours.
model = gensim.models.ldamodel.LdaModel(
          corpus=mm,
          id2word=id2word,
          num_topics=100,
          update_every=1,
          chunksize=10000,
          passes=1)
# save the model to the file for future use
model.save('wiki_lda.pkl')
# to load this model use
# model = gensim.models.ldamodel.LdaModel.load('wiki_lda.pkl')

topics = [model[doc] for doc in mm]
lens = np.array([len(t) for t in topics])
# print the average number of topics per document
print(np.mean(lens))
# print the percentage of documents with less than 10 topics
# For this idiom, note that the Booleans in np.mean(lens <= 10)
# are considered as 0 or 1 when calculating the mean
print(np.mean(lens <= 10))

# Record how often each topic is mentioned
counts = np.zeros(100)
for doc_top in topics:
    for ti,_ in doc_toc:
        counts[ti] += 1

# Show the most talked about topic
words = model.show_topic(counts.argmax(), 64)



