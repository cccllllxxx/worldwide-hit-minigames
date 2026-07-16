"""补充抓取剩余 9 个缺图游戏的官方真实图标。
- 移动游戏用 Apple iTunes Search API（返回 512px 官方图标，最稳）
- Roblox 游戏用 Roblox 官方缩略图 API（已知 universeId）
版权说明：本看板非商用、内部给 mentor/投资人看，使用官方商店图标作“所指游戏”标识属合理使用；如对外公开建议改授权图。
"""
import urllib.request, json, urllib.parse, os, time

PROXY = {'http': 'http://127.0.0.1:7897', 'https': 'http://127.0.0.1:7897'}
OP = urllib.request.build_opener(urllib.request.ProxyHandler(PROXY))
HDR = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# id -> (来源, 查询/uid)
SPEC = {
    'C001': ('itunes', 'Block Blast'),
    'C008': ('itunes', 'Survivor.io'),
    'C035': ('itunes', 'Gossip Harbor'),
    'C045': ('itunes', 'Brain Out'),
    'C049': ('itunes', 'Magic Tiles 3'),
    'C061': ('itunes', 'Color Block Jam'),
    'C003': ('itunes', 'Whiteout Survival'),
    'C014': ('roblox', 2749740153),  # Brookhaven RP
    'C015': ('roblox', 2298559443),  # Adopt Me!
}

def itunes_url(term):
    url = f"https://itunes.apple.com/search?term={urllib.parse.quote(term)}&entity=software&limit=8&country=us"
    for _ in range(4):
        try:
            r = OP.open(urllib.request.Request(url, headers=HDR), timeout=25)
            d = json.loads(r.read())
            for res in d.get('results', []):
                nm = res.get('trackName', ''); art = res.get('artworkUrl512', '')
                key = term.split('.')[0].split()[0].lower()
                if key and key[:6] in nm.lower():
                    return nm, art
            if d.get('results'):
                return d['results'][0].get('trackName'), d['results'][0].get('artworkUrl512')
            return None, None
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(5); continue
            return None, None
        except Exception:
            return None, None
    return None, None

def roblox_url(uid):
    url = f"https://thumbnails.roblox.com/v1/games/icons?universeIds={uid}&size=512x512&format=Png"
    try:
        r = OP.open(urllib.request.Request(url, headers=HDR), timeout=25)
        d = json.loads(r.read())
        return d['data'][0]['imageUrl']
    except Exception as e:
        print('  roblox err', repr(e)[:60]); return None

def download(url, path):
    if not url:
        return False
    try:
        r = OP.open(urllib.request.Request(url, headers=HDR), timeout=40)
        data = r.read()
        if len(data) < 800:
            return False
        with open(path, 'wb') as f:
            f.write(data)
        return True
    except Exception as e:
        print('  dl err', repr(e)[:60]); return False

with open('game_img.json', encoding='utf-8') as f:
    img = json.load(f)

for cid, (src, q) in SPEC.items():
    print(f'[{cid}] {src} -> {q}')
    if src == 'itunes':
        nm, url = itunes_url(q)
        print('   itunes:', nm)
    else:
        url = roblox_url(q)
    ok = download(url, f'assets/{cid}.jpg')
    img[cid] = f'assets/{cid}.jpg' if ok else ''
    print('   saved:', ok, url[:60] if url else url)
    time.sleep(1.5)

with open('game_img.json', 'w', encoding='utf-8') as f:
    json.dump(img, f, ensure_ascii=False, indent=2)

print('\n完成。当前命中:', sum(1 for v in img.values() if v), '/', len(img))
print('磁盘图片:', len([1 for cid in SPEC if os.path.exists(f"assets/{cid}.jpg")]))
