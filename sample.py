import csv
with open("project/student_clustering.csv","r") as rf:
    csv_read = csv.reader(rf)
    with open("project/new_student_clustering.csv","w") as wf:
      csv_writer = csv.writer(wf,delimiter="_") 

    for line in csv_read:
        csv_writer.writerow(line)