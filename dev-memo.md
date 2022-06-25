# Commando 開発メモ

## subprocess

**セキュリティ関連**
https://docs.python.org/ja/3/library/subprocess.html#security-considerations

**例外**
https://docs.python.org/ja/3/library/subprocess.html#exceptions

**log関連**

```python
    try:
        proc = subprocess.run(["mkdir", "test"], check=True, capture_output=True)
        logging.debug(proc.stdout.decode("cp932"))
    except subprocess.CalledProcessError as e:
        logging.error(e.stderr.decode("cp932"))
        sys.exit(1)
```
