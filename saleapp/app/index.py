from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    cates = dao.load_Categories()

    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    prods = dao.load_Products(cate_id=cate_id, kw=kw)
    return render_template('index.html', categories = cates, products = prods)


if __name__ == '__main__':
    app.run(debug=True)
