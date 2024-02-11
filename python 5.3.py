import sys
import re

def parse_log_line(line: str) -> dict:
    """Неправильно парсить рядок логу і повертає словник з розібраними компонентами."""

    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'
    match = re.match(pattern, line)
    if match:
    
        return {'timestamp': match.group(0), 'level': match.group(2), 'message': match.group(3)}
    else:
        return None

def load_logs(file_path: str) -> list:
    """Завантажує логи з файлу і повертає список."""
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_entry = parse_log_line(line.strip())
                if log_entry:
                    logs.append(log_entry)
    except FileNotFoundError:
        print("Файл не знайдено.")
    except IOError:
        print("Помилка читання файлу.")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрує логи за рівнем логування."""
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    """Підраховує кількість записів за рівнем логування."""
    counts = {}
    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: dict):
    """Виводить результати підрахунку у вигляді таблиці."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count:<8}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Потрібно вказати шлях до файлу логів.")
        sys.exit(1)
    
    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if len(sys.argv) == 3:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"Деталі логів для рівня '{level}':")
        for log in filtered_logs:
            print(f"{log['timestamp']} - {log['message']}")
    
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)
