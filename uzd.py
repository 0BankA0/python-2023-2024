import csv
def salidzini_csv():
    with open('csv1.csv', 'r', encoding='utf-8') as a:
      render = csv.reader(a)
      file2 = []
      for row in render:
        file2.append(row)

    with open('csv2.csv', 'r', encoding='utf-8') as b:
        render2 = csv.reader(b)
        file1 = []
        for row2 in render2:
           file1.append(row2)

    if len(row) == len(row2):
       print('Ir vienādi!')
    else:
       print("nav vienādi")
salidzini_csv()


def jsons():
  print("nesapratu")


jsons()

