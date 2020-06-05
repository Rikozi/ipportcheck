[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![python](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/downloads/)
[![GitHub version](https://d25lcipzij17d.cloudfront.net/badge.svg?id=gh&type=6&v=1.0&x2=0)](http://badge.fury.io/gh/boennemann%2Fbadges)
# ipportcheck
IP port check is a python script it scans all the IP are in a world that is connected on the port that you have specified that gives information about where IP from (country) and an operating system and another port that connects on IP
Then you can do
```bash
$python3 ipportcheck.py --help
_______________
< Hello, world! >
---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )/\/
                ||----w |
                ||     ||   https://github.com/Rikozi/ipportcheck

Usage: python3 ipportcheck.py [options]
options:
-p / --port :: Port that do you want to get
ex:
   python3 ipportcheck.py -p 80
   python3 ipportcheck.py -port 80
   ```
![alt text](https://raw.githubusercontent.com/Rikozi/ipportcheck/master/example.png?raw=true)

## Bugs and enhancements

For bug reports or enhancements, please open an [issue](https://github.com/Rikozi/ipportcheck/issues) here.
## Install SET

```bash
git clone https://github.com/Rikozi/ipportcheck.git
cd ipportcheck
python3 setup.py
python3 ipportcheck.py
```
