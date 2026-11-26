import argparse
import json
from datetime import date
from pathlib import Path


def order(tasks):
    return sorted(tasks, key=lambda t: (t['done'], t['deadline'], -t['priority'], t['id']))


def load(path):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else []


def save(path, tasks):
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding='utf-8')
    tmp.replace(path)


def main():
    p = argparse.ArgumentParser(description='Deadline Planner')
    p.add_argument('--file', type=Path, default=Path('tasks.json'))
    sub = p.add_subparsers(dest='cmd', required=True)
    a = sub.add_parser('add'); a.add_argument('title'); a.add_argument('deadline', type=date.fromisoformat); a.add_argument('--priority', type=int, choices=[1,2,3], default=2)
    sub.add_parser('list')
    d = sub.add_parser('done'); d.add_argument('id', type=int)
    args = p.parse_args(); tasks = load(args.file)
    if args.cmd == 'add':
        if not args.title.strip(): p.error('Empty title')
        tasks.append(dict(id=max((t['id'] for t in tasks), default=0)+1, title=args.title, deadline=args.deadline.isoformat(), priority=args.priority, done=False)); save(args.file,tasks)
    elif args.cmd == 'done':
        for t in tasks:
            if t['id']==args.id: t['done']=True; save(args.file,tasks); break
        else: p.error('Task not found')
    else:
        for t in order(tasks):
            status = 'DONE' if t['done'] else 'OVERDUE' if t['deadline'] < date.today().isoformat() else 'OPEN'
            print(f"{t['id']} | {t['deadline']} | P{t['priority']} | {status} | {t['title']}")

if __name__ == '__main__': main()
