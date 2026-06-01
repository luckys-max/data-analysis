import subprocess
import pathlib

repo = pathlib.Path(r'D:\桌面\Data')
git = pathlib.Path(r'C:\Program Files\Git\cmd\git.exe')
cmds = [
    ['status', '--branch', '--short'],
    ['log', '--oneline', '--graph', '--decorate', '--all'],
    ['ls-files', '-u'],
]
for args in cmds:
    proc = subprocess.run([str(git)] + args, cwd=repo, capture_output=True, text=True)
    print('CMD:', ' '.join(args))
    print('RC:', proc.returncode)
    print('STDOUT:')
    print(proc.stdout)
    print('STDERR:')
    print(proc.stderr)
    print('---')
