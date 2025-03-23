from flask import Flask, render_template,request, flash, redirect
from flask_login import current_user, login_required
from dotenv import load_dotenv
import os

# Import extensions
from extensions import db, login_manager

load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': 'suss',
    'host': os.getenv('MONGO_URI')
}

# Configure Flask-Login
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
app.static_folder = 'assets'
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = "Please login to proceed."

# Initialize MongoDB
db.init_app(app)

# ✅ Import blueprints *after* db.init_app(app)
from controllers.auth import auth_bp
from controllers.manager import manager_bp  

app.register_blueprint(auth_bp)
app.register_blueprint(manager_bp)

from models.cca import CompetitiveGroup, InterestGroup
from models.application import Application

# Routes
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("about.html", panel="our groups")

@app.route("/competitivegroups", methods=['GET', "POST"])
def competitive_groups():
    if request.method == "GET":
        group_list = CompetitiveGroup.getAllCompetitiveGroups()
        return render_template('competitiongroup.html', panel="competition groups", group_list=group_list)

@app.route("/interestgroups", methods=['GET', "POST"])
def interest_groups():
    if request.method == "GET":
        group_list = InterestGroup.getAllInterestGroups()
        return render_template('interestgroup.html', panel="interest groups", group_list=group_list)

@app.route('/apply', methods = ['POST'])
@login_required
def applyCCA():
     
    group_type = request.form.get('group_type')
    group_code = request.form.get('group_code')
    group_name = request.form.get('group_name')

    if current_user.is_authenticated:
        if "admin" in current_user.role.lower():
            flash('You do not have access to this function.', 'primary')
            return redirect(group_type)
            
        else:
            if group_type == "interestgroups" :
                group = InterestGroup.objects(code=group_code).first()
            else:
                group = CompetitiveGroup.objects(code=group_code).first()
            
            application = Application.createApplicationRandomDate(current_user, group)
           
            if application:
                date = application.date.strftime('%d %B %Y')
                flash(f'You have previously applied for {group_name} on {date} status is {application.status}.','warning')
            else:
                display_group = group_type.replace("groups", " group")
                flash(f"You have just applied for {display_group} {group_name}.","primary")
                
            return redirect(group_type)


if __name__ == "__main__":
    app.run(debug=True)
