# John the Ripper Jumbo — demonstration commands

Run these commands from the repository root. The sample hashes use a known demonstration password, `demo123`, included in `words.txt`.

If `john` is not on your PATH, replace `john` below with the full path to your John the Ripper Jumbo executable.

## Cost factor 10

```bash
john --format=bcrypt --wordlist=words.txt hashes/bcrypt_cost_10.txt
john --show --format=bcrypt hashes/bcrypt_cost_10.txt
```

## Cost factor 12

```bash
john --format=bcrypt --wordlist=words.txt hashes/bcrypt_cost_12.txt
john --show --format=bcrypt hashes/bcrypt_cost_12.txt
```

## Cost factor 14

```bash
john --format=bcrypt --wordlist=words.txt hashes/bcrypt_cost_14.txt
john --show --format=bcrypt hashes/bcrypt_cost_14.txt
```

If John reports that the password was already cracked, use the corresponding `--show` command to display the recovered result.

**Notes:** These are synthetic demonstration hashes. Recovery time depends on hardware, configuration, and system load. Only test hashes when you have authorization.
