# LastPwn ';-- have my LastPass passwords been pwned?

You can check single passwords using haveibeenpwned.com's [web interface](https://haveibeenpwned.com/Passwords) or its awesome [REST API](https://haveibeenpwned.com/API/v2#PwnedPasswords)

But how can you check all my LastPass passwords against HIBP? There is [this tool](https://gist.github.com/Tenzer/b8aa3cfa09a7e1396a0661de6bf35633) which works pretty well but it won't work for those of us who are paranoid and don't like the idea of revealing even 5 hex digits of their precious password hashes.

So can you do it offline? Yes. Download the [pwned passwords list](https://haveibeenpwned.com/Passwords) (make sure to get SHA1 one ordered by hash), unpack the file, and ~~grep through it~~ run this tool.

If you are on Linux, create a directory in /dev/shm to store LastPass exported CSV file in RAM rather than on the disk:

```
mkdir /dev/shm/pws
```

Go to LastPass → Account Options → Advanced → Export → LastPass CSV File and save it as e.g. /dev/shm/pws/lastpass.csv

And then:
```
python3 lastpwn.py /dev/shm/pws/lastpass.csv <path-to>/pwned-passwords-sha1-ordered-by-hash-v4.txt
```

## Performance

Since the program is comparing two ordered lists, the processing takes virtually the same amount of time whether you have 10 passwords or 1 million passwords in the CSV file.
