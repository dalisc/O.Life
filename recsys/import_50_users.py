import csv
from app.models import User, Question, Tag, Answer

CSV_PATH = 'sample.csv'

contSuccess = 0
# Remove all data from Table
# Book.objects.all().delete()

with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar=';')
    print('Loading...')
    for row in spamreader:
    #     question = Question.objects.create(text=row[0], tags=row[1])
    #     answer = Answer.objects.create(question=question, answer=row[3])
        User.objects.create(identifier=row[0])
        contSuccess += 1
    print(f'{str(contSuccess)} inserted successfully! ')