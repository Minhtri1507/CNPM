import math

from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    cates = dao.load_Categories()

    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    page = request.args.get('page', 1)

    prods = dao.load_Products(cate_id=cate_id, kw=kw, page=int(page))

    total = dao.count_products()
    page_size = app.config['PAGE_SIZE']
    return render_template('base.html', categories = cates, products = prods, pages=math.ceil(total/page_size))


if __name__ == '__main__':
    app.run(debug=True)
