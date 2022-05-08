from flask_wtf import FlaskForm
from flask_ckeditor import CKEditor, CKEditorField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from mastermindweb import app

ckeditor = CKEditor(app)

class BlogPostForm(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later
    title = StringField('Title', validators=[DataRequired()])
    text = CKEditorField('Text', validators=[DataRequired()])
    submit = SubmitField('Post')
