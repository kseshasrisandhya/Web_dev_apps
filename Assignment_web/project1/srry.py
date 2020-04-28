@app.route('/book/<string:isbn_id>')
def isbn(isbn_id):
        sel_book = Book.query.filter(Book.isbn == isbn_id).all()
        for j in sel_book:
            isbn = j.isbn
            author = j.author
            title = j.title
            year = j.year
        total_reviews = db.session.query(Review).filter(Review.isbn == isbn)
        return render_template('bookpage.html',name = session['username'], isbn = isbn, author = author, year = year,title= title,total_reviews = total_reviews)

@app.route('/review', methods =['GET','POST'])
def review():
    if request.method == 'POST':
        rating = request.form.get('review_tags')
        review = request.form.get('review_value')
        name = session['username']
        temp = list(request.form.items())
        print(temp[2][0])
        # ob = Review.query.get(name,isbn)
        # print(ob)
        try:
            data = Review(username = name, isbn = temp[2][0], rating = rating, review = review) 
            db.session.add(data)
            db.session.commit()
        except exc.IntegrityError:
            return render_template('bookpage.html',message = 'You have already given review')
    return render_template('bookpage.html',name = session['username'], message1 = 'review submitted succesfully.')








    <html>
    <head>
    </head>
    <body>
        <h1>{{author}}</h1>
        <h1>{{title}}</h1>
        <h1>{{year}}</h1>
        <h1>{{isbn}}</h1>
        <form action="{{ url_for('review') }}" method="POST">
            <div class="form-group">
                <label for="Rating">Rating:</label>
                <select class="form-control" name="review_tags" id="SearchType">
                    <option value="0">0</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
                <input type="text" placeholder="review here" name="review_value" required style="width: 25%; margin-top: 20px;">
                <button type="submit" name = "{{isbn}}" form-action="search" class="searchbtn" value="searching">Submit</button><br>
            </div>
        </form>
        {{ message }}
        <br>
        <br>
        <br>
    {% if total_reviews %}
        {% for k in total_reviews%}
            <div class="reviews">
                <p> username: {{ k.username }}</p>
                <p> Rating: {{ k.rating }}</p>
                <p> review: {{ k.review }}</p>
            </div>
        {% endfor %}
    {% endif %}
    </body>
</html>