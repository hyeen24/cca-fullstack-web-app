
from models.users import User
from models.cca import CCA
from datetime import datetime , timedelta
from random import choices
from extensions import db

class Application(db.Document):
    meta = {'collection': 'applications'}
    student = db.ReferenceField(User, required=True)
    group = db.ReferenceField(CCA, required=True)
    date = db.DateTimeField()
    status = db.StringField()
    
    @staticmethod
    def getApplication(app_id=None):
        application = Application.objects(id=app_id).first()

        if application:
            return application

    @staticmethod
    def getApplications(User=None, group=None, status=None):
        print("Entering get all applications.....")
        if group and status:
            "CCA and status given"
            applications = Application.objects(group=group, status=status)
        elif group:
            print("CCA Given")
            applications = Application.objects(group=group)
        else:
            print("No input given")
            applications = Application.objects()

        return applications.order_by('group', 'status', 'student.email')
    
    @staticmethod
    def updateApplication(new_status, doc_id=None):
        application = Application.getApplication(doc_id)
        if application:
            application.status = new_status
            application.save()
            return True
        else: 
            return False
            print("No such application.")

    @staticmethod
    def deleteApplication(doc_id):
        application = Application.getApplication(doc_id)
        if application:
            application.delete()
            return True
        else:
            print("No such application")
            return False

    @staticmethod
    def createApplicationRandomDate(user, group):
        dates = []
        for i in range(7) :
            dates.append(datetime.today() - timedelta(days=i+1)) 

        random_date = choices(dates)
        application = Application.createApplication(user,group, random_date[0])
        return application

    @staticmethod
    def createApplication(User, group, date):
        application = Application.objects(student=User, group=group).first()
        if not application:
           Application(student=User, group=group, date=date, status="Pending").save()
           print("New application have been created")
        return application