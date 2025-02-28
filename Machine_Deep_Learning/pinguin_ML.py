import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = sns.load_dataset('penguins')

sns.pairplot(df, hue='species')
plt.show()

df.isnull().sum()
df= df.dropna()

df= df.drop(['island','sex'], axis=1)

X = df.drop(['species'], axis=1)
y = df['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=119)

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")


