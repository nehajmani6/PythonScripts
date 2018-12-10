import csv


class CreateCSV:

    def __init__(self, file_name):
        self.file_name = file_name
        self.create_csv_file(file_name)

    def create_csv_file(self, file_name):

        with open(file_name) as file:
            total_log_list = [['Remote Address', 'Time Local', 'Request', 'Status', 'Body Bytes Sent', 'HTTP Referer',
                               'HTTP User Agent', 'HTTP-X-Forward For', 'Request Id', 'Unknown Column', 'Unknown Column']]
            lines = file.readlines()
            for each_line in lines:
                list_each_line = each_line.split()
                user_agent = ''
                for i in range(11, len(list_each_line) - 3):
                    if i == 11:
                        user_agent += list_each_line[i][1:]
                        user_agent += " "
                    elif i == (len(list_each_line) - 4):
                        user_agent += list_each_line[i][:len(list_each_line[i]) - 1]
                    else:
                        user_agent += list_each_line[i]
                        user_agent += " "
                list_each_line_final = [list_each_line[0][1:], list_each_line[3][1:]+" "+list_each_line[4][:len(list_each_line[4])-1],
                                        list_each_line[5][1:]+" "+list_each_line[6]+" "+list_each_line[7][:len(list_each_line[7]) - 1], list_each_line[8], list_each_line[9],
                                        list_each_line[10][1:len(list_each_line[10])-1], user_agent, list_each_line[len(list_each_line) - 3],
                                        list_each_line[len(list_each_line) - 1][:len(list_each_line[len(list_each_line) - 1]) - 1]]
                total_log_list.append(list_each_line_final)
            with open('nginx-access.csv', 'w+') as csvfile:
                w = csv.writer(csvfile)
                # w.writerows(lines)
                w.writerows(total_log_list)
        print("csv file 'nginx-access.csv' is successfully created")


create_csv_file = CreateCSV("nginx-access.log")
