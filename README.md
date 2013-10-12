
Indexing Wikipedia

To get a current dump of the English Wikipedia, run: 
wget http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2

From the command line, run: python -m gensim.scripts.make_wiki enwiki-latest-pages-articles.xml.bz2 wiki_en_output