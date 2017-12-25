# exportFormattxt
Export mysql datas use txt file

### Set yourself mysql conifg
Copy `config.example.ini` and renamed `config.ini` then set it by yourself:
```
[mysql]
host: 127.0.0.1
user: root
password: root
db: youselfdb
port: 3306
```

### Input some id in id.txt
Input some id, like
```
1
2
3
```

### Use
`python ExportRes.py`
then
```
please enter you want to search table (like games_view or softwares_view): games_view
please enter you want to display status (like show or hide): show
please enter you want to search fields (like id, name, level): id,name,level,level_number
```

### Finally
It will export named export.xlsx file in file folder

