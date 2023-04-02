import database_to_dict
from database_to_dict import *

gened_requirements = {"GA": 6, "GHW": 3, "GH": 6, "GN": 9, "GS": 6, "GQ": 6, "GWS": 9}
gened_codes = {3: "GA", 4: "GHW", 5: "GH", 6: "GN", 7: "GS", 8: "GQ", 9: "GWS"}
dotenv_path = Path('Environment Variables/.env')
load_dotenv(dotenv_path=dotenv_path)

conn = psycopg2.connect(
    host=os.getenv('host'),
    user=os.getenv('user'),
    password=os.getenv('password'),
    database=os.getenv('database'),
    port=os.getenv('port')
)
cur = conn.cursor()

ranked_courses = database_to_dict.coursesPerArea()
final_schedule=[]
for i in ranked_courses:
    for j in i:
        cur.execute("SELECT * FROM subjects WHERE Code=%s", j[1])
        current_course=cur.fetchall()
        for ran in range(3, 10):
            if current_course[0][i] == 1:
                if gened_requirements[gened_codes[i]] > 0:
                    gened_requirements[gened_codes[i]] -= current_course[0][2]
                    final_schedule+=[j[1]]
                    




