from collections import Counter
import sys
import re

def parse_log_line(line: str) -> dict:
    #log line validation check 
    if re.match(r'(\d{4}(?:-\d{2}){2} \d{2}(?::\d{2}){2}) ([A-Z]+) (.*)',line):
        #convert log line into parsed dict
        parsed_line = {"date":line.split(' ')[0],"time":line.split(' ')[1],"level":line.split(' ')[2],"message":" ".join(line.split(' ')[3:])}
        return parsed_line
    
def load_logs(file_path: str) -> list:
    with open(file_path, 'r', encoding='utf-8') as fh:
        #create list with parsed log lines in dict type
        logs = list(filter(lambda x: x is not None,(map(parse_log_line,fh.readlines()))))
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    #filter log records by level criteria and return filtered dict list
    return list(filter(lambda x: x['level'].lower() == level.lower(),logs))

def count_logs_by_level(logs: list) -> dict:
    #count numbers of each level
    counts = dict(Counter(item['level'] for item in logs))
    return counts

def display_log_counts(counts: dict):
    #display formatted text
    header = '{:^17}|{:^10}'.format('Рівень логування','Кількість')
    separator = '-' * 17 + '|' + '-' * 10
    print(header,separator,sep='\n')
    for k,v in counts.items():
        print('{:<17}|{:<10}'.format(k,v))
    return None

if __name__ == "__main__":
    try:
        filename=sys.argv[1]
        logs=load_logs(filename)
        display_log_counts(count_logs_by_level(logs))
        if len(sys.argv)==3:
            logs=filter_logs_by_level(logs,sys.argv[2])
            if logs:
                print(f"Деталі логів для рівня {sys.argv[2]}:")
                print(''.join(map(lambda x: f"{x['date']} {x['time']} - {x['message']}",logs)))
    except Exception as e:
        print(f"Error: {e}") 
