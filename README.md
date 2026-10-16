# bcrypt Cost Factor Analysis

**Project:** Evaluating the Impact of bcrypt Cost Factors on Password Recovery  
**Author:** Sai Abhishek D  
**Environment:** Ubuntu 24.04.4 LTS, Python 3, Python `bcrypt`, John the Ripper Jumbo

## Objective
Compare bcrypt password-verification time at cost factors 10, 12, and 14, and demonstrate wordlist-based recovery of a known test password using John the Ripper.

> **Ethical scope:** This is a local educational demonstration using synthetic test data only. Do not test hashes or systems without authorization.

## Repository contents
- `bcrypt_benchmark.py` — times five bcrypt verification trials for each cost factor and reports the median.
- `john_commands.md` — commands for John the Ripper Jumbo.
- `requirements.txt` — Python dependency.
- `hashes/` — sample bcrypt hashes.
- `words.txt` — demonstration wordlist containing the known test password.
- `.gitignore` — ignores Python cache and virtual environment files.

## Requirements and setup
Install Python dependency:

```bash
python3 -m pip install -r requirements.txt
```

Run the benchmark:

```bash
python3 bcrypt_benchmark.py
```

The program creates a fresh salted bcrypt hash for each cost factor, verifies the correct password five times, and reports median elapsed time. Exact timings vary by machine and system load.

## John the Ripper demonstration
See [`john_commands.md`](john_commands.md). Replace `john` with the path to your John the Ripper Jumbo executable if needed.

## Example results
One recorded run on the project machine:

| Cost factor | Median verification time |
|---:|---:|
| 10 | 40.55 ms |
| 12 | 160.56 ms |
| 14 | 664.15 ms |

In that run, cost 12 took about **3.96×** as long as cost 10, and cost 14 took about **16.38×** as long. These are example measurements, not guaranteed timings. Run the script to obtain results for your own environment.

## Interpretation
- Increasing bcrypt's cost factor increases the work required for each password verification.
- More expensive verification also makes repeated password guesses more computationally expensive.
- John the Ripper's wordlist attack tests candidate passwords; it does not decrypt a hash.
- The sample wordlist deliberately contains the known test password, so this demonstrates a candidate match rather than guessing an unknown password.

## Limitations
This is a small educational experiment, not a comprehensive password-cracking benchmark. The results are based on five verification trials per cost factor and will vary with hardware, system load, and software versions.
