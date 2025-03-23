all_comp_groups = [   
    {  "code": "cg_arc", 
       "name": "Archery", 
       "url": "https://sfcms.suss.edu.sg/images/default-source/content/ssc/student-life/archery.jpg?sfvrsn=ee9570fd_2", 
       "email" : "archery_cg@suss.edu", 
       "awards": 
        { "2024": {"NTU Institutional Archery Championships 2024":  
                   ["Silver Ranking - Recurve Novice Men",  
                    "3 TKO Silver - Recurve Novice Men", 
                    "TKO Bronze - Recurve Intermediate Women",  
                    "Bronze Ranking - Recurve Open Women", 
                    "Bronze Ranking - Compound Open Men",  
                    "IKO Bronze - Compound Open Women"] 
                  }, 
          "2023": {"NTU Institutional Archery Championship 2023" : 
                   ["IKO Bronze - Recurve Intermediate Women", 
                    "Team Gold - Recurve Intermediate Women", 
                    "No 2 Ranking -Recurve Open Women", 
                    "IKO Silver - Recurve Open Women", 
                    "IKO Bronze - Recurve Novice Men", 
                    "IKO Silver - Recurve Intermediate Women"], 
                   "NUS Indoors 2023" :  
                   ["Team Silver - NUS Challenge",  
                    "Team Bronze - Institutional Challenge, Recurve Intermediate Women", 
                    "Gold Ranking - Recurve Open Women"]}, 
            "2022": { "Nanyang Technological University Institutional Archery Championship":  
                     ["IKO Bronze - Recurve Intermediate Women", "Team Gold- Recurve Intermediate Women", 
                      "No 2 Ranking - Recurve Open Women", "IKO Silver - Recurve Open Women", 
                      "IKO Bronze - Recurve Novice Men", "IKO Silver - Recurve Intermediate Women"]} 
        }    
    }, 
    { "code": "cg_ath", 
       "name": "Athletics", 
       "url": "https://sfcms.suss.edu.sg/images/default-source/content/ssc/student-life/athletics.jpg?sfvrsn=eaecb22d_4", 
       "email" : "athletics_cg@suss.edu", 
       "awards": 
        { "2024": {"Institute-Varsity-Polytechnic Games 2024":  
                   ["3rd - Men 10000 Meter Run", "1st - Women 3000 Meter Race Walk", 
                    "2nd - Men 5000 Meter Run", "2nd - 6 Km Run"]}, 
          "2023": {"Institute-Varsity-Polytechnic Games 2023" :["Gold - Women's 400m ", 
                                                                   "Silver - Women's 200m", 
                                                                   "No 2 Ranking - Recurve Open Women", 
                                                                   "Silver - Women's 3000m Racewalk", 
                                                                   "Bronze - Men's 3000m Racewalk", 
                                                                   "Silver - Men's Steeplechase"], 
                    "SA All Comers 3": ["1 of 2 - Women 5000 Meter Race Walk Open Finals"], 
                    "SA All Comers 5": ["1 of 8 - Men 100 Meter Open Heats"], 
                    "SA All Comers 7": ["3 of 6 - Women 400 Meter Open Finals"], 
                    "SA All Comers 9": ["2 of 5 - Women 5000 Meter Run Open Finals"], 
                    "SA All Comers 10": ["3 of 7 - Men 800 Meter Run Open Timed Finals", 
                                         "2 of 6 - Women 100 Meter Dash Open"], 
                   "Singapore National Track & Field Championships 2023" : ["1 of 5 - Women 200 Meter Dash Open",  
                                           "2 of 5 - Men 10000 Meter Run Open", 
                                           "1 and 2 position of 3 - Women 10000 Meter Race Walk Open"], 
                    "83rd Singapore Open Track & Field Championships 2023":["1, 2 and 3 of 4 - Women 10000 Meter Race Walk Open",  
                                           "1 of 5 - Women 1500 Meter Race Walk Open"], 
                    "Pesta Sukan 2023": ["2 of 4 - Men 100 Meter Dash Masters", "1 of 5 - Men 35-39 400 Meter Dash Masters"], 
                    "Singapore University Games 2023": ["1 Bronze - Men's Team"]}, 
            "2022": { "Singapore National Track & Field Championships":  
                     ["Bronze - Women's 10000m Race Walk Open", "Bronze - Men's 10000m Race Walk Open", 
                      "Bronze - Women's 4 x 100m Relay Open"], 
                      "Institute-Varsity-Polytechnic Games 2021/2022": ["Gold - Women's 100m", "Gold - Women's 200m", 
                                                                   "Silver - Women's 3000m Walk", "Bronze - Women's 400m Hurdle"] 
                    } 
        } 
    }   
] 

from app import db
from app.models.users import User


class CCA(db.Document):
    meta = {'collection': 'ccas'}
    
    code = db.StringField(required=True, unique=True)  
    name = db.StringField(required=True)
    url = db.StringField()
    email = db.StringField()
    awards = db.DictField()
    description = db.ListField()
    highlights = db.ListField()
    category = db.StringField()
    types = db.StringField()

    @staticmethod
    def getCCA(code):
        return CCA.objects(code=code).first()

    @staticmethod
    def getAllCCAs():
        return CCA.objects()
   
def create_data_from_global():
    for d in all_comp_groups:
        group = CCA(
            code=d["code"],
            name=d["name"],
            types="Competitive",
            url=d["url"],
            email=d["email"],
            awards=d["awards"]
        )      
        group.save()
        print(f"CCA : {d['name']} is created")
        User.createUser(d["email"], d['name'], "12345", "CCA admin")

    # Add interest groups
    for d in all_int_groups:
        group = CCA(
            code=d["code"],
            name=d["name"],
            types="Interest",
            url=d["url"],
            email=d["email"],
            description=d["description"],
            highlights=d["highlights"],
            category=d["category"]
        )
        
        group.save()
        print(f"CCA : {d['name']} is created")
        User.createUser(d["email"], d['name'], "12345", "CCA admin")