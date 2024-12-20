# from flask import Flask, render_template, request
# import pickle
# import numpy as np
#
# app = Flask(__name__)
#
# popular_df = pickle.load(open('popular.pkl', 'rb'))
# pt = pickle.load(open('pt.pkl', 'rb'))
# books = pickle.load(open('books.pkl', 'rb'))
# similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))
#
#
# @app.route('/')
# def index():
#     return render_template('index2.html',
#                            book_name=list(popular_df['Book-Title'].values),
#                            author=list(popular_df['Book-Author'].values),
#                            image=list(popular_df['Image-URL-M'].values),
#                            votes=list(popular_df['num-ratings'].values),
#                            rating=list(popular_df['avg_rating'].values) if 'avg_rating' in popular_df else [
#                                                                                                                'N/A'] * len(
#                                popular_df))
#
#
# @app.route('/recommend')
# def recommend_ui():
#     return render_template('recommend2.html')
#
#
# @app.route('/recommend_books', methods=['POST'])
# def recommend():
#     user_input = request.form.get('user_input').lower()
#     matching_books = [book for book in pt.index if user_input in book.lower()]
#
#     if not matching_books:
#         return render_template('recommend2.html', data=[], message="No books found matching your input")
#
#     search_book = matching_books[0]
#     index = np.where(pt.index == search_book)[0][0]
#     similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]
#
#     data = []
#     for i in similar_items:
#         item = []
#         temp_df = books[books['Book-Title'] == pt.index[i[0]]]
#         item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
#         item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
#         item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
#
#         # Use a default value if avg_rating is not available
#         avg_rating = temp_df['avg_rating'].values[0] if 'avg_rating' in temp_df else "N/A"
#         item.append(avg_rating)  # Add rating to item
#         data.append(item)
#
#     return render_template('recommend2.html', search_book=search_book, data=data)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, request
# import pickle
# import numpy as np
#
# app = Flask(__name__)
#
# popular_df = pickle.load(open('popular.pkl', 'rb'))
# pt = pickle.load(open('pt.pkl', 'rb'))
# books = pickle.load(open('books.pkl', 'rb'))
# similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))
#
#
# @app.route('/')
# def index():
#     return render_template('index2.html',
#                            book_name=list(popular_df['Book-Title'].values),
#                            author=list(popular_df['Book-Author'].values),
#                            image=list(popular_df['Image-URL-M'].values),
#                            votes=list(popular_df['num-ratings'].values),
#                            rating=list(popular_df['avg_rating'].values) if 'avg_rating' in popular_df else [
#                                'N/A'] * len(popular_df))
#
#
# @app.route('/recommend')
# def recommend_ui():
#     return render_template('recommend2.html')
#
#
# @app.route('/recommend_books', methods=['POST'])
# def recommend():
#     user_input = request.form.get('user_input').lower()
#     matching_books = [book for book in pt.index if user_input in book.lower()]
#
#     if not matching_books:
#         return render_template('recommend2.html', data=[], message="No books found matching your input")
#
#     search_book = matching_books[0]
#     index = np.where(pt.index == search_book)[0][0]
#     similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]
#
#     data = []
#     for i in similar_items:
#         item = []
#         temp_df = books[books['Book-Title'] == pt.index[i[0]]]
#
#         item.append(temp_df['Book-Title'].values[0])  # Get book title
#         item.append(temp_df['Book-Author'].values[0])  # Get author
#         item.append(temp_df['Image-URL-M'].values[0])  # Get image URL
#
#         # Use a default value if avg_rating is not available
#         avg_rating = temp_df['avg_rating'].values[0] if 'avg_rating' in temp_df and not temp_df['avg_rating'].isnull().any() else "N/A"
#         item.append(avg_rating)  # Add rating to item
#
#         data.append(item)
#
#     return render_template('recommend2.html', search_book=search_book, data=data)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the pickled data
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index2.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num-ratings'].values),
                           rating=list(popular_df['avg_rating'].values) if 'avg_rating' in popular_df else ['N/A'] * len(popular_df))


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend2.html')


@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input').lower()
    matching_books = [book for book in pt.index if user_input in book.lower()]

    if not matching_books:
        return render_template('recommend2.html', data=[], message="No books found matching your input")

    search_book = matching_books[0]
    index = np.where(pt.index == search_book)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]

        item.append(temp_df['Book-Title'].values[0])  # Get book title
        item.append(temp_df['Book-Author'].values[0])  # Get author
        item.append(temp_df['Image-URL-M'].values[0])  # Get image URL

        # Use a default value if avg_rating is not available
        # avg_rating = temp_df['avg_rating'].values[0] if 'avg_rating' in temp_df and not temp_df['avg_rating'].isnull().any() else "N/A"
        # item.append(avg_rating)  # Add rating to item

        data.append(item)

    return render_template('recommend2.html', search_book=search_book, data=data)


if __name__ == '__main__':
    app.run(debug=True)

