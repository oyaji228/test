# Paloaltoのリソースチェック用のコード

## 使い方
1.resource_check_r2.shの中身でリソースチェックしたいconfigファイルのパスを指定
```
#!/usr/local/bin/zsh

dir="/Users/sunao/workspace/github/doc/vutm/hoge"
#echo $dir

python3 resource_check_r2.py $dir/device1.log
python3 resource_check_r2.py $dir/device2.log
python3 resource_check_r2.py $dir/device3.log
python3 resource_check_r2.py $dir/device4.log
python3 resource_check_r2.py $dir/device5.log
python3 resource_check_r2.py $dir/device6.log
  :
  :

```

2.resource_check_r2.shを実行

```$ ./resource_check_r2.sh  ```

3.リソース集計結果が表示される

```
**device1.log**
-servise
 -count per vsys:
 [997, 0, 0, 0, 30, 0, 48, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 10, 0, 0, 26, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 0, 3, 0, 8, 8, 10, 27, 0, 0, 0, 4, 0, 0, 0, 0, 0, 23, 0, 0, 0, 8, 0, 0, 0, 2, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 -totalcount: 280
-security rule
 -count per vsys:
 [997, 1, 6, 5, 29, 5, 32, 8, 16, 5, 9, 5, 7, 5, 12, 5, 5, 5, 8, 6, 6, 5, 5, 10, 5, 7, 5, 6, 7, 11, 33, 5, 21, 14, 5, 5, 7, 5, 5, 5, 5, 5, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 5, 5, 5, 5, 7, 5, 6, 47, 5, 9, 5, 10, 10, 29, 21, 5, 5, 6, 6, 5, 5, 5, 5, 7, 25, 5, 51, 5, 9, 5, 5, 5, 43, 15, 5, 5, 5, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
 -totalcount: 881
-url-filtering
 -count per vsys:
 [997, 0, 0, 0, 3, 1, 4, 0, 6, 0, 0, 0, 2, 0, 4, 1, 0, 0, 1, 1, 0, 0, 0, 3, 0, 3, 0, 1, 0, 2, 0, 0, 7, 8, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 19, 0, 1, 1, 1, 1, 10, 1, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 14, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 -totalcount: 108

**device2.log**
  :
  :
```

