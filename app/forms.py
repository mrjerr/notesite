from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators


class NoteForm(FlaskForm):
    text = TextAreaField(
        label='text',
        render_kw={"rows": 18, "cols": 100},
        validators=[
            validators.DataRequired()
        ]
    )
