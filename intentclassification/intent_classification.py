import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.svm import LinearSVC


class IntentClassifier:
    def __init__(self):

        self.data = pd.read_csv('./intentclassification/data1.csv')
        # đào tạo khi khởi tạo
        self.train()

        """
        Lấy văn bản, chuyển đổi nó thành một vectơ đếm từ, sau đó chuyển đổi văn bản đó thành một vectơ
        Các giá trị TF-IDF, sau đó sử dụng giá trị đó để huấn luyện bộ phân loại LinearSVC
        """

    def train(self):

        X_train, y_train = self.data['text'], self.data['intent']
        self.count_vect = CountVectorizer()
        X_train_counts = self.count_vect.fit_transform(X_train)
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        self.svm = LinearSVC().fit(X_train_tfidf, y_train)

    def predict(self, text):

        return self.svm.predict(self.count_vect.transform({text}))[0]


intent_classifier = IntentClassifier()

# print(intent_classifier.predict("tiềm kiếm"))
# print(intent_classifier.predict("tạm biệt"))
# print(intent_classifier.predict("nghe nhạc"))
