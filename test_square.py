from subprocess import run, PIPE

def test_square():
    res = run(['python3', 'square.py', '5'], stdout=PIPE)
    assert int(res.stdout.strip()) == 25

def test_square():
    res = run(['python3', 'square.py', '-5'], stdout=PIPE)
    assert int(res.stdout.strip()) == 25
