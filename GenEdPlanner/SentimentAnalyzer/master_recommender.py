import database_to_dict
from database_to_dict import *

gened_requirements = {"GA": 6, "GHW": 3, "GH": 6, "GN": 9, "GS": 6, "GQ": 6, "GWS": 9}
gened_codes = {3: "GA", 4: "GHW", 5: "GH", 6: "GN", 7: "GS", 8: "GQ", 9: "GWS"}
dotenv_path = Path('Environment Variables/.env')
load_dotenv(dotenv_path=dotenv_path)

conn = psycopg2.connect(
    host=os.getenv('ec2-54-208-11-146.compute-1.amazonaws.com'),
    user=os.getenv('tgxctmcewoorja'),
    password=os.getenv('e4f9aa0cf321fbd283c50f3d4da4e7a801db06d0f39c668b0c252bad947c1211'),
    database=os.getenv('df8cah15kt4kr9'),
    port=os.getenv('5432')
)
cur = conn.cursor()

ranked_courses = database_to_dict.coursesPerArea("Philosophy, Math, Physics, Painting, Photography, French, Spanish, Linguistics, Snowboarding")
print(ranked_courses)
final_schedule=[]
for i in ranked_courses:
    for j in i:
        cur.execute("SELECT * FROM subjects WHERE Code='"+j[1]+"';")
        current_course=cur.fetchall()
        for ran in range(3, 10):
            if current_course[0][ran] == 1:
                if gened_requirements[gened_codes[ran]] > 0:
                    gened_requirements[gened_codes[ran]] -= current_course[0][2]
                    final_schedule+=[j[1]]
final_schedule = list(set(final_schedule))
print(final_schedule)



