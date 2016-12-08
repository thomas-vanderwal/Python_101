#CSV module is used to read and write CSV files
#Reading is done with two ways: csv's reader and DictReader function
#Writing is done with two ways: csv's writer and DictWriter function
#Regular reader/writer uses lists while the Dict uses dictionaries

import csv

def csv_reader(file_obj):
    """
    Read a csv file
    :param file_obj:
    :return:
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))

def csv_dict_reader(file_obj):
    """
    Read a csv file using csv.DictReader
    :param file_obj:
    :return:
    """
    reader = (csv.DictReader(file_obj, delimiter=','))
    for line in reader:
        print(line["first_name"]),
        print(line["last_name"])

def csv_writer(data, path):
    """
    Write data out to a specific path
    """

    with open(path,'w',newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

def csv_dict_writer(path, fieldnames, data):
    """
    writes a csv using csv.DictWriter
    """
    with open(path, 'w', newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    csv_path="TB_burden_countries_2016-12-07.csv"
 #   with open(csv_path, 'r') as f_obj:
  #      csv_reader(f_obj)

   # with open('data.csv') as f_obj:
    #    csv_dict_reader(f_obj)

    data = ["first_name,last_name,city".split(","),
             "Tyrese,Hirthe,Strackeport".split(","),
             "Jules,Dicki,Lake Nickolasville".split(","),
             "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    my_list = []
    fieldnames = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)
    path = "dict_output.csv"

    #csv_writer(data, path)
    csv_dict_writer(path,fieldnames,my_list)
    print(my_list)