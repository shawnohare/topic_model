The provided Python script uses gensim's implementation of latent Dirichlet allocation to create a topic model for the English Wikipedia page.  The dump must first be downloaded and indexed and gensim itself must be installed.

To install gensim, from the command line run: pip install gensim

To get a current dump of the English Wikipedia, run: 
wget http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2

Next use gensim to index the dump.  From the command line, run: python -m gensim.scripts.make_wiki enwiki-latest-pages-articles.xml.bz2 wiki_en_output