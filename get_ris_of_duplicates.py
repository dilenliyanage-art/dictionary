student_data = {'1d1':
                {'name': ['sara'],
                 'class': ['V'],
                 'subject_interger': ['english, math, sience']
                },
'1d2':
{'name': ['sara'],
                 'class': ['V'],
                 'subject_interger': ['english, math, sience']
                },
'1d3':
{'name': ['sara'],
                 'class': ['V'],
                 'subject_interger': ['english, math, sience']
                },
'1d4':
{'name': ['sara'],
                 'class': ['V'],
                 'subject_interger': ['english, math, sience']
                },
}
result= {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)