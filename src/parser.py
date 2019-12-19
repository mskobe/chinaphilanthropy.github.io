import xlrd
import json
class Donation:
    id, amount, month, date, orig, dest, cause = 0, '', '', '', '', '', ''
    def __init__(self, id, amount, month, date, orig, dest, cause):
        self.id, self.amount, self.month, self.date, self.orig, self.dest, self.cause = id, amount, month, date, orig, dest, cause
    def pprint(self):
        print({
            "id": self.id,
            "amount": self.amount,
            "month": self.month,
            "date": self.date,
            "orig": self.orig,
            "dest": self.dest,
            "cause": self.cause
        })
    def tojson(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "month": self.month,
            "date": self.date,
            "orig": self.orig,
            "dest": self.dest,
            "cause": self.cause
        }
data = xlrd.open_workbook('alldonation.xlsx')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
all = alleviation = culture = disaster = education = environment = health = unspecified = []
for i in range(1, nrows):
    row = table.row_values(i)
    month = int(row[6]) if isinstance(row[6], float) else ''
    date = int(row[7]) if isinstance(row[7], float) else ''
    cause = row[17]
    data = {
            "id": i,
            "amount": row[5],
            "month": month,
            "date": date,
            "orig": row[9],
            "dest": row[11],
            "cause": cause
        }
    all.append(data)
    if cause == 'Social Welfare & Poverty Alleviation': alleviation.append(data)
    if cause == 'Culture': culture.append(data)
    if cause == 'Disaster Relief': disaster.append(data)
    if cause == 'Education': education.append(data)
    if cause == 'Environment': environment.append(data)
    if cause == 'Public Health': health.append(data)
    if cause == 'Unspecified': unspecified.append(data)
with open('all.json', 'w') as f:
    json.dump(all, f)
with open('alleviation.json', 'w') as f:
    json.dump(alleviation, f)
with open('culture.json', 'w') as f:
    json.dump(culture, f)
with open('disaster.json', 'w') as f:
    json.dump(disaster, f)
with open('education.json', 'w') as f:
    json.dump(education, f)
with open('environment.json', 'w') as f:
    json.dump(environment, f)
with open('health.json', 'w') as f:
    json.dump(health, f)
with open('unspecified.json', 'w') as f:
    json.dump(unspecified, f)
