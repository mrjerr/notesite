from sqlalchemy import text
from flask import request, render_template, redirect, url_for, flash

from model import Note, db
from forms import NoteForm
from utils import count_unique_word


def setup_views(app):
    app.add_url_rule('/', view_func=index, methods=['GET', 'POST'])
    app.add_url_rule('/note-list', view_func=note_list)
    app.add_url_rule('/note/<int:id>', view_func=note_page)

    app.register_error_handler(404, not_found)


def index():
    if request.method == 'POST':
        form = NoteForm(request.form)

        if form.validate():
            note = Note(
                unique_word_count=count_unique_word(form.text.data),
                short_description=form.text.data[:60],
                text=form.text.data
            )

            db.session.add(note)
            db.session.commit()
            flash('Заметка №({}) успешно добавлена'.format(note.id), 'success')

            return redirect(url_for('index'))

        else:
            flash('Пожалуйста заполните форму', 'warning')
            return redirect(url_for('index'))

    if request.method == 'GET':
        form = NoteForm()
        return render_template(
                    'index.html',
                    title='Add Note',
                    form=form,
                    active_note_add=True
               )


def note_list():
    notes = Note.query.with_entities(
                            Note.id,
                            Note.unique_word_count,
                            Note.short_description
                        ).order_by(text('unique_word_count desc'))

    return render_template(
                'note_list.html',
                title='Note list',
                notes=notes,
                active_note_list=True
            )


def note_page(id):
    note = Note.query.get(id)
    if note is None:
        return render_template('404.html'), 404
    return render_template(
                'note.html',
                note=note,
           )


def not_found(error):
    return render_template('404.html'), 404
