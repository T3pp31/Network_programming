# ネットワークプログラムを試すためのリポジトリ
動作確認済み:Python3.9.4
RustとPython

# 注意事項(必ず読んでください)
ポートスキャン，盗聴等，不正アクセスにも使える技術が実装されているが，**決して第3者のサーバに対して実行しないようにしてください**.不正アクセスの事前調査とみなされる可能性があります．
本リポジトリに存在するプログラムを利用し，不正アクセスに利用したとしても，本リポジトリ所有者は一切の責任を負いません．

Although it implements techniques that can be used for unauthorized access, such as port scanning, eavesdropping, etc., it should never be run against a third party's server. **Never run against a third party server**, as it may be considered as a preliminary investigation for unauthorized access.
The owner of this repository is not responsible for the use of the programs in this repository for unauthorized access.


# 免責
このリポジトリに存在するコードを利用し，いかなる不利益を被っても，本リポジトリの所有者は一切責任を負いません．

The owner of this repository is not responsible for any disadvantage you may suffer by using the code in this repository.

# Python
## port_scanner
開いているポート番号を探すことができる．
### tcp_scan.py
3wayhandshakeで接続し，開いているポートを特定します．
ログが残りやすい

### syn_portscan.py
synパケットを投げて，syn+ackが帰って来ればポートが空いてる．
rst+ackが帰ってきたらポートは閉じている
ステルススキャン


### thread_port_scanner.py
socketを使ったポートスキャナー．実行速度が速い．
https://www.finddevguides.com/Python-penetration-testing-network-scanner
上記のサイトを参考

## sniffing(盗聴) 
[参考](https://www.finddevguides.com/Python-penetration-testing-network-packet-sniffing)
特定のネットワークを通過するすべての通信を監視，キャプチャできる．
保護されているトラフィックと保護されていないトラフィックの両方を見ることができる．
以下は簡単に盗聴できるプロトコル
HTTP:暗号化せずにクリアテキストで情報を送信するために使用される
SMTP:電子メールの転送に使用される
POP:サーバからメールを受信するために使用
FTP:ファイル送信に使われる
IMAP:メール転送
Telnet:遠隔操作とか

## arp_spoofing
[参考](https://www.finddevguides.com/Python-penetration-testing-arp-spoofing)
悪意のある攻撃者がローカルエリアネットワークを介して偽造されたARP要求を送信する攻撃の一種
スイッチを過負荷にさせ，ネットワークパケットを盗聴しやすくする

## watching_pcap
pcapの中身を見る
watch_pcapの方は，ポート番号を指定できる
watch_pcap2は何も指定できない
watch_pcap3は

## client.py & server.py
socket通信を用いたclient,serverモデル

## syn_scan.py
synパケットを投げる

## main.py
いろんな機能まとめたやつ

## 3way_handshake.py
3wayハンドシェイクを実現するクラス

