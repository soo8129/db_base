# DB base

## Introduction
'DB base'는 티베로 데이터베이스 연결을 쉽게 하기 위한 설정 파일들과 티베로 드라이버, 데이터베이스 클래스가 포함되어 있습니다

## Dependencies
* pyodbc=4.0.39
* unixodbc
* python3

## Installation
odbc.ini, odbcinst.ini 파일을 /etc 폴더에 넣어주시고 libtbodbc.so 드라이버파일은 /workspace 폴더에 넣어주시면 됩니다

## Example
```console
$isql NDB
```
