from flask import Flask, render_template, request
from gpt_for_study import gpt_for_book
import openai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    # Get the form data from the request
    api_key = request.form.get('api_key')
    topic = request.form.get('topic')
    num_chapter = int(request.form.get('num_chapter'))
    make_for_whom = request.form.get('make_for_whom')

    # Set the OpenAI API key
    openai.api_key = api_key

    # Call gpt_for_book() function with the form data
    chapters, books = gpt_for_book(topic, num_chapter, make_for_whom)
    formatted_chapters = [f"Chapter {i+1}. {chapter}" for i, chapter in enumerate(chapters)]
    formatted_books = [book.replace("\n", "<br>") for book in books]

    return render_template('result.html', topic = topic, chapters=formatted_chapters, books=formatted_books)

if __name__ == '__main__':
    app.run(debug=True)
