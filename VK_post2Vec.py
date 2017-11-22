from sklearn.cross_validation import train_test_split
from gensim.models.word2vec import Word2Vec

with open('positive.csv', 'r') as infile:
    pos = infile.readlines()

with open('negative.csv', 'r') as infile:
    neg = infile.readlines()

#use 1 for positive sentiment, 0 for negative
y = np.concatenate((np.ones(len(pos)), np.zeros(len(neg))))

x_train, x_test, y_train, y_test = train_test_split(np.concatenate((pos, neg)), y, test_size=0.2)

n_dim = 300
#Initialize model and build vocab
w2v = Word2Vec(size=n_dim, min_count=10)
w2v.build_vocab(x_train)

#Train the model over train_reviews (this may take several minutes)
w2v.train(x_train)
