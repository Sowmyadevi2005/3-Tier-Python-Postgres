from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Item

main = Blueprint('main', __name__)

@main.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@main.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        item_name = request.form.get('item_name')
        item_description = request.form.get('item_description')
        if item_name and item_description:
            new_item = Item(name=item_name, description=item_description)
            db.session.add(new_item)
            db.session.commit()
            return redirect(url_for('main.index'))
    return render_template('create.html')

@main.route('/view/<int:item_id>')
def view_item(item_id):
    item = Item.query.get_or_404(item_id)
    return render_template('view.html', item=item)

@main.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = Item.query.get_or_404(item_id)
    if request.method == 'POST':
        item.name = request.form.get('item_name')
        item.description = request.form.get('item_description')
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit.html', item=item)

@main.route('/delete/<int:item_id>')
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('main.index'))

