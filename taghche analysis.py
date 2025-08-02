import json
import pandas as pd

with open(r"F:\Machine Learning\taghche\taghcheh2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

books = data["pageProps"]["pageConfig"]["bookList"]["books"]
df = pd.DataFrame(books)

df["authors_count"] = df["authors"].apply(lambda authors: len(authors) if isinstance(authors, list) else 0)
df["tags_count"] = df["labels"].apply(lambda tags: len(tags) if isinstance(tags, list) else 0)

df = df.dropna(subset=["price", "numberOfPages", "rating"])

max_rating_row = df.loc[df["rating"].idxmax()]
print(f"کتابی که بیشترین امتیاز را دارد: {max_rating_row['title']} با امتیاز {max_rating_row['rating']}")

max_price_row = df.loc[df["price"].idxmax()]
print(f"گرون‌ترین کتاب: {max_price_row['title']} با قیمت {max_price_row['price']}")


# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error

# X = df[["price", "numberOfPages", "authors_count", "tags_count"]]
# y = df["rating"]

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=0
# )

# model = LinearRegression().fit(X_train, y_train)

# y_pred = model.predict(X_test)

# rmse = mean_squared_error(y_test, y_pred, squared=False)
# print(f"خطای پیش‌بینی مدل (RMSE): {rmse:.3f}")
