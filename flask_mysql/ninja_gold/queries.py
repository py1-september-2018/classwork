from mysqlconnection import connectToMySQL

def get_activities(user_id):
  activities_query = """SELECT
                          activities.gold_amount AS gold_amt,
                          locations.name AS location
                        FROM activities
                        JOIN locations ON locations.id = activities.locations_id
                        WHERE activities.user_id = %(user)s
                        ORDER BY activities.created_at DESC
                        LIMIT 5;"""
  data = {
    'user': user_id
  }
  mysql = connectToMySQL('ninja_gold')
  db_activities = mysql.query_db(activities_query, data)

  activities = []
  for act in db_activities:
    if act['gold_amt'] > 0:
      activity = {
        'content': "Won {} golds from {}.".format(act['gold_amt'], act['location']),
        'css_class': "green"
      }
    else:
      activity = {
        'content': "Lost {} golds from {}.".format(act['gold_amt'], act['location']),
        'css_class': 'red'
      }
    activities.append(activity)

  print("*" * 80)
  print(activities)
  print("*" * 80)
  return activities