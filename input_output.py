# まず \r\n を持つファイルをバイナリで書き込む
with open('windows.txt', 'wb') as f:
    f.write(b'Hello\r\nWorld\r\n')

# バイナリモード('rb'): \r\n がそのまま見える
with open('windows.txt', 'rb') as f:
    print('バイナリ:', repr(f.read()))

# テキストモード('r'): \r\n が \n に自動変換される
with open('windows.txt', 'r', encoding='utf-8') as f:
    print('テキスト:', repr(f.read()))
