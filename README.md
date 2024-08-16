<h1 align="center">
  <br>
  <a href="#"><img src="https://i.imgur.com/VV9gCa9.png" width="150px" alt="Nuclei"></a>
</h1>

<h4 align="center">Extract IP Port and Hostnames from shodan downloaded files with ease</h4>

<p align="center">
<a href="https://github.com/0xAgun/Shodan-Extractor/releases"><img src="https://img.shields.io/github/downloads/0xAgun/Shodan-Extractor/total">
<a href="https://github.com/0xAgun/Shodan-Extractor/graphs/contributors"><img src="https://img.shields.io/github/contributors-anon/0xAgun/Shodan-Extractor">
<a href="https://github.com/0xAgun/Shodan-Extractor/issues"><img src="https://img.shields.io/badge/versions-1.0.5-blue">
<a href="https://github.com/0xAgun/Shodan-Extractor"><img src="https://img.shields.io/github/issues-raw/0xAgun/Shodan-Extractor">
<a href="https://twitter.com/MySelfAshraful"><img src="https://img.shields.io/twitter/follow/MySelfAshraful.svg?logo=twitter"></a>
</p>

## Preview


<h3 align="center">
  <img src="https://i.imgur.com/PhWjgWL.png" alt="nuclei-flow" width="500px"></a>
  <img src="https://i.imgur.com/0SVhk4H.png" alt="nuclei-flow" width="500px"></a>
</h3>

</hr>
</td>
</tr>


| :exclamation:  **Disclaimer**  |
|---------------------------------|
| **Pleasse give the program a valid gz file**. Expect breaking the whole program  with wrong files. Review the files before using this tool. |

# Install Packages

Shodan Extractor requires **rich libary** to install successfully. Run the following command to install the latest version -

```py
pip install rich
```
</td>
</tr>

### Usage

```py
python3 main.py -h
```

This will display help menu for the tool.

```py
python3 main.py filename.gz
```
```py
python3 main.py filename.gz -o outputfilename
```

input file to extract by default it'll save the inputfilename.json if output filename is given then it'll save on that name


```py
python3 main.py -e filename.txt
```

This will save the ip:port into a file by default given it as extracted.txt the format is 127.0.0.1:8000

```py
python3 main.py -H name.txt
```

This is for saving the host file.


```py
python3 main.py c94f4160-xxxx-xxxx-xxxe.json.gz -e name.txt -H host.txt
```

we put all togather
