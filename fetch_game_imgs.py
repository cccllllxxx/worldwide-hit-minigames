# -*- coding: utf-8 -*-
"""三路真实配图抓取：维基 REST 封面 -> Steam 商店图 -> Google Play 图标。
非商用内部研究看板用途；失败则保留字母占位。"""
import urllib.request, json, re, os, time, sys

PROXY = {'http': 'http://127.0.0.1:7897', 'https': 'http://127.0.0.1:7897'}
OP = urllib.request.build_opener(urllib.request.ProxyHandler(PROXY))
HDR = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) Chrome/120 Safari/537.36'}

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
os.makedirs(ASSETS, exist_ok=True)
JSON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'game_img.json')

# id -> {wiki: 维基标题, steam: Steam 搜索词, play: Google Play 包名}
MAP = {
 'C001': {'wiki':'Block Blast','steam':'Block Blast','play':'com.metta.blockblast'},
 'C007': {'wiki':'Archero','steam':'Archero','play':'com.habby.archero'},
 'C008': {'wiki':'Survivor.io','steam':'Survivor.io','play':'com.habby.survivorio'},
 'C012': {'wiki':'Steal a Brainrot','steam':'Steal a Brainrot'},
 'C013': {'wiki':'Dress to Impress (video game)','steam':'Dress to Impress'},
 'C014': {'wiki':'Brookhaven (video game)','steam':'Brookhaven'},
 'C015': {'wiki':'Adopt Me!','steam':'Adopt Me'},
 'C016': {'wiki':'Stumble Guys','steam':'Stumble Guys','play':'com.scopely.stumbleguys'},
 'C022': {'wiki':'Candy Crush Saga','steam':'Candy Crush Saga','play':'com.king.candycrushsaga'},
 'C023': {'wiki':'Fruit Ninja','steam':'Fruit Ninja','play':'com.halfbrick.fruitninja'},
 'C025': {'wiki':'Crossy Road','steam':'Crossy Road','play':'com.yodo1.crossyroad'},
 'C026': {'wiki':'Slither.io','steam':'Slither.io','play':'com.slitherplus.slither.io'},
 'C033': {'wiki':'I Am Cat','steam':'I Am Cat'},
 'C034': {'wiki':'Ludo King','steam':'Ludo King','play':'com.ludo.king'},
 'C035': {'wiki':'Gossip Harbor','steam':'Gossip Harbor','play':'com.mergegames.gossiphabor'},
 'C036': {'wiki':'Project Makeover','steam':'Project Makeover','play':'com.babycare.gamerprojectmakeover'},
 'C037': {'wiki':'Matchington Mansion','steam':'Matchington Mansion','play':'com.matchington.mansion'},
 'C038': {'wiki':'Travel Frog','steam':'Travel Frog','play':'com.hitdot.frog'},
 'C043': {'wiki':'Gardenscapes','steam':'Gardenscapes','play':'com.playrix.gardenscapes'},
 'C044': {'wiki':'Township (video game)','steam':'Township','play':'com.playrix.township'},
 'C045': {'wiki':'Brain Out','steam':'Brain Out','play':'com.relaxingbraintraining.brainout'},
 'C046': {'wiki':'Paper.io 2','steam':'Paper.io 2','play':'io.paper2'},
 'C047': {'wiki':'Helix Jump','steam':'Helix Jump','play':'com.apps.vortex.helixjump'},
 'C048': {'wiki':'Hole.io','steam':'Hole.io','play':'com.apps.unny.holeio'},
 'C049': {'wiki':'Magic Tiles 3','steam':'Magic Tiles 3','play':'com.kooapps.magictiles3'},
 'C050': {'wiki':'Royal Kingdom','steam':'Royal Kingdom','play':'com.dreamgames.royalkingdom'},
 'C059': {'wiki':'Cell Survivor','steam':'Cell Survivor'},
 'C061': {'wiki':'Color Block Jam','steam':'Color Block Jam','play':'com.roomcality.colorblockjam'},
 'C003': {'wiki':'Whiteout Survival','steam':'Whiteout Survival','play':'com.starfun.whiteoutsurvival.gp'},
}

def get(url, binary=False, ref=None, timeout=30):
    h = dict(HDR)
    if ref: h['Referer'] = ref
    req = urllib.request.Request(url, headers=h)
    r = OP.open(req, timeout=timeout)
    data = r.read()
    return data if binary else data.decode('utf-8', 'ignore')

def wiki_img(title):
    try:
        url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(title)
        d = json.loads(get(url))
        return d.get('thumbnail', {}).get('source')
    except Exception:
        return None

def steam_img(term):
    try:
        s = "https://store.steampowered.com/api/storesearch/?term=" + urllib.parse.quote(term) + "&l=english&cc=US"
        d = json.loads(get(s))
        if not d.get('items'): return None
        aid = d['items'][0]['id']
        d2 = json.loads(get(f"https://store.steampowered.com/api/appdetails?appids={aid}"))
        return d2[str(aid)]['data'].get('header_image')
    except Exception:
        return None

def play_img(pkg):
    try:
        url = f"https://play.google.com/store/apps/details?id={pkg}&hl=en&gl=US"
        html = get(url)
        m = re.search(r'<meta property="og:image" content="([^"]+)"', html)
        return m.group(1) if m else None
    except Exception:
        return None

def download(url, path):
    try:
        data = get(url, binary=True, ref=url, timeout=40)
        if len(data) < 1500:  # 太小视为破图/占位
            return False
        with open(path, 'wb') as f:
            f.write(data)
        return True
    except Exception:
        return False

def main():
    img_map = {}
    jp = JSON_PATH
    if os.path.exists(jp):
        try: img_map = json.load(open(jp))
        except Exception: img_map = {}
    todo = [k for k in MAP if not img_map.get(k)]
    print(f"待抓取: {len(todo)} 个")
    for i, cid in enumerate(todo, 1):
        m = MAP[cid]
        url = None
        for src, fn in [('wiki', lambda: wiki_img(m.get('wiki'))),
                        ('steam', lambda: steam_img(m.get('steam'))),
                        ('play', lambda: play_img(m.get('play')) if m.get('play') else None)]:
            try:
                u = fn()
            except Exception:
                u = None
            if u:
                url = u
                print(f"[{i}/{len(todo)}] {cid}: {src} -> {u[:55]}")
                break
        if url:
            path = os.path.join(ASSETS, cid + '.jpg')
            if download(url, path):
                img_map[cid] = 'assets/' + cid + '.jpg'
            else:
                img_map[cid] = ''
            time.sleep(1.2)
        else:
            img_map[cid] = ''
            print(f"[{i}/{len(todo)}] {cid}: 三路均未命中（保留字母占位）")
            time.sleep(0.4)
    json.dump(img_map, open(jp, 'w'), ensure_ascii=False, indent=1)
    hit = sum(1 for v in img_map.values() if v)
    print(f"完成：命中 {hit}/{len(img_map)}")

if __name__ == '__main__':
    import urllib.parse
    main()
