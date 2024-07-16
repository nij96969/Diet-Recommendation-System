from flask import Flask, render_template, url_for, flash, redirect, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from datetime import datetime
from functools import wraps
import diet_recommendation_model 

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='user')
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.role}')"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
def get_meals_data():
    # Replace this with actual data retrieval logic
    meals = {
        'Meal_1': {
            'Food_Items': ['Oatmeal with berries and nuts (1/2 cup rolled oats, 1/4 cup berries, 1/4 cup nuts), 1/2 cup almond milk',
                           '1 cup mixed greens salad with vinaigrette dressing (1 cup mixed greens, 2 tbsp vinaigrette)'],
            'Nutritional_Values': {'FatContent': '14g', 'SaturatedFatContent': '3g', 'CholesterolContent': '0mg',
                                   'SodiumContent': '200mg', 'CarbohydrateContent': '45g', 'FiberContent': '8g',
                                   'SugarContent': '10g', 'ProteinContent': '15g'},
            'Calories': 400
        },
        'Meal_2': {
            'Food_Items': ['Lentil soup with whole-wheat bread (1 cup lentil soup, 2 slices whole-wheat bread)',
                           '1 apple'],
            'Nutritional_Values': {'FatContent': '5g', 'SaturatedFatContent': '1g', 'CholesterolContent': '0mg',
                                   'SodiumContent': '300mg', 'CarbohydrateContent': '50g', 'FiberContent': '12g',
                                   'SugarContent': '10g', 'ProteinContent': '18g'},
            'Calories': 400
        },
        'Meal_3': {
            'Food_Items': ['Tofu and vegetable stir-fry with brown rice (1/2 cup tofu, 1 cup vegetables, 1/2 cup brown rice)',
                           '1 cup mixed greens salad with vinaigrette dressing (1 cup mixed greens, 2 tbsp vinaigrette)'],
            'Nutritional_Values': {'FatContent': '10g', 'SaturatedFatContent': '2g', 'CholesterolContent': '0mg',
                                   'SodiumContent': '250mg', 'CarbohydrateContent': '55g', 'FiberContent': '10g',
                                   'SugarContent': '5g', 'ProteinContent': '20g'},
            'Calories': 450
        }
    }
    return meals

@app.route("/dashboard")
@login_required
def dashboard():
    meal1 = "Grilled Chicken Salad"
    meal2 = "Quinoa and Veggie Stir Fry"
    meal3 = "Spaghetti with Marinara Sauce"
    explanation = "These meals are designed to provide a balanced diet with a mix of protein, carbohydrates, and vegetables."

    return render_template('dashboard.html', meal1=meal1, meal2=meal2, meal3=meal3, explanation=explanation)
@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        age = int(request.form['inputAge'])
        weight = int(request.form['inputWeight'])
        height = int(request.form['inputHeight'])
        gender = request.form['inputGender']
        activity = request.form['activity']
        weight_loss_plan = request.form['weightGoal']
        meals_per_day = int(request.form['meals'].split('-')[0])
        diet_type = "vegetarian"  # This should come from user input as well if needed

        json_data = diet_recommendation_model.response_generator(age, weight, height, gender, activity, weight_loss_plan, meals_per_day, diet_type)
        print(json_data["BMI"])
        return render_template('dashboard.html', meal1=json_data["Meal_Recommendations"]["Meal_1"]["Food_Items"][0]+json_data["Meal_Recommendations"]["Meal_1"]["Food_Items"][1]+str(json_data["Meal_Recommendations"]["Meal_1"]["Nutritional_Values"]), meal2=json_data["Meal_Recommendations"]["Meal_2"]["Food_Items"][0]+json_data["Meal_Recommendations"]["Meal_2"]["Food_Items"][1]+str(json_data["Meal_Recommendations"]["Meal_2"]["Nutritional_Values"]), meal3=json_data["Meal_Recommendations"]["Meal_3"]["Food_Items"][0]+json_data["Meal_Recommendations"]["Meal_3"]["Food_Items"][1]+str(json_data["Meal_Recommendations"]["Meal_3"]["Nutritional_Values"]), explanation=json_data["Explanation"])
    return render_template('profile.html')

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != 'admin':
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

@app.route("/admin")
@login_required
@admin_required
def admin_dashboard():
    return render_template('admin.html', title='Admin Dashboard')

if __name__ == '__main__':
    app.run(debug=True)
