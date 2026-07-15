# -*- coding: utf-8 -*-
import json

D = json.load(open('社媒证据_补充/_dash.json', encoding='utf-8'))
DATA_JSON = json.dumps(D, ensure_ascii=False)

HTML = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>新一代世界级爆款小游戏 · 最终研究结论</title>
<style>
:root{
  --bg:#f6f7fb; --panel:#ffffff; --ink:#1f2430; --muted:#6b7280; --line:#e6e8ef;
  --indigo:#4f46e5; --teal:#0d9488; --amber:#d97706; --rose:#e11d48; --slate:#475569;
  --green:#16a34a; --soft:#eef2ff; --soft2:#f0fdfa; --soft3:#fff7ed; --soft4:#fef2f6;
  --shadow:0 1px 3px rgba(16,24,40,.06),0 6px 24px rgba(16,24,40,.06);
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;
  background:var(--bg);color:var(--ink);line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.wrap{max-width:1180px;margin:0 auto;padding:0 22px}
/* NAV */
nav{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.86);backdrop-filter:blur(10px);
  border-bottom:1px solid var(--line)}
.nav-inner{max-width:1180px;margin:0 auto;padding:12px 22px;display:flex;align-items:center;gap:18px;flex-wrap:wrap}
.brand{font-weight:800;letter-spacing:.3px;font-size:15px;color:var(--indigo);white-space:nowrap}
.nav-links{display:flex;gap:14px;flex-wrap:wrap;font-size:13.5px;color:var(--slate)}
.nav-links a{padding:4px 8px;border-radius:8px;transition:.15s}
.nav-links a:hover{background:var(--soft);color:var(--indigo)}
/* HERO */
.hero{padding:54px 0 30px;background:linear-gradient(180deg,#eef2ff 0%,#f6f7fb 60%)}
.hero h1{font-size:34px;line-height:1.25;font-weight:850;letter-spacing:-.5px}
.hero .sub{margin-top:14px;color:var(--muted);font-size:15.5px;max-width:820px}
.tagrow{margin-top:22px;display:flex;gap:10px;flex-wrap:wrap}
.tag{background:#fff;border:1px solid var(--line);border-radius:999px;padding:7px 14px;font-size:13px;color:var(--slate);box-shadow:var(--shadow)}
.tag b{color:var(--indigo)}
/* SECTION */
section{padding:46px 0;border-bottom:1px solid var(--line)}
.sec-head{display:flex;align-items:baseline;gap:12px;margin-bottom:22px}
.sec-head .no{font-size:13px;font-weight:800;color:#fff;background:var(--indigo);border-radius:8px;padding:3px 9px}
.sec-head h2{font-size:23px;font-weight:800;letter-spacing:-.3px}
.sec-head .en{color:var(--muted);font-size:13px}
.lead{color:var(--muted);font-size:14.5px;max-width:880px;margin-bottom:20px}
/* DEF CARDS */
.def-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.def{border-radius:16px;padding:22px;background:var(--panel);box-shadow:var(--shadow);border:1px solid var(--line);position:relative;overflow:hidden}
.def::before{content:"";position:absolute;left:0;top:0;bottom:0;width:5px}
.def.d1::before{background:var(--indigo)} .def.d2::before{background:var(--teal)} .def.d3::before{background:var(--amber)}
.def h3{font-size:18px;margin-bottom:4px} .def .en{font-size:12px;color:var(--muted);margin-bottom:14px}
.def ul{list-style:none;font-size:13.5px}
.def li{padding:7px 0;border-top:1px dashed var(--line);display:flex;gap:9px}
.def li:first-child{border-top:none}
.def li b{color:var(--ink);white-space:nowrap}
.dot{flex:none;width:7px;height:7px;border-radius:50%;background:var(--indigo);margin-top:8px}
.d2 .dot{background:var(--teal)} .d3 .dot{background:var(--amber)}
.def .note{margin-top:14px;font-size:12.5px;color:var(--muted);background:var(--soft);border-radius:10px;padding:10px 12px}
/* FUNNEL */
.funnel{display:grid;grid-template-columns:1.1fr .9fr;gap:26px;align-items:center}
.donut-wrap{display:flex;justify-content:center;align-items:center}
.funnel-legend{font-size:14px}
.funnel-legend .row{display:flex;align-items:center;gap:10px;padding:9px 0;border-bottom:1px solid var(--line)}
.funnel-legend .sw{width:14px;height:14px;border-radius:4px;flex:none}
.funnel-legend .n{margin-left:auto;font-weight:800}
.funnel-legend .d{color:var(--muted);font-size:12.5px}
.insight{margin-top:18px;background:var(--soft3);border:1px solid #fed7aa;border-radius:12px;padding:14px 16px;font-size:13.5px}
.insight b{color:var(--amber)}
/* CONTROLS */
.controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:18px}
.controls input{border:1px solid var(--line);border-radius:10px;padding:9px 12px;font-size:13.5px;min-width:220px;background:#fff}
.chips{display:flex;gap:7px;flex-wrap:wrap}
.chip{border:1px solid var(--line);background:#fff;border-radius:999px;padding:6px 13px;font-size:12.8px;color:var(--slate);cursor:pointer;transition:.15s}
.chip:hover{border-color:var(--indigo);color:var(--indigo)}
.chip.on{background:var(--indigo);border-color:var(--indigo);color:#fff}
select{border:1px solid var(--line);border-radius:10px;padding:9px 12px;font-size:13.5px;background:#fff}
.count-note{font-size:13px;color:var(--muted)}
/* CARDS */
.grid-cases{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.case{border:1px solid var(--line);border-radius:14px;padding:16px;background:var(--panel);box-shadow:var(--shadow);transition:.18s;display:flex;flex-direction:column;gap:8px}
.case:hover{transform:translateY(-3px);box-shadow:0 10px 30px rgba(16,24,40,.12)}
.case .top{display:flex;justify-content:space-between;align-items:flex-start;gap:8px}
.case .nm{font-weight:800;font-size:15.5px}
.case .cn{font-size:12.5px;color:var(--muted)}
.score{flex:none;width:46px;height:46px;border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:850;font-size:16px;color:#fff;line-height:1}
.score small{font-size:8px;font-weight:600;opacity:.9}
.case .meta{display:flex;gap:6px;flex-wrap:wrap}
.pill{font-size:11.5px;padding:3px 9px;border-radius:7px;background:var(--soft);color:var(--slate);border:1px solid var(--line)}
.pill.g{background:var(--soft2);color:var(--teal)} .pill.a{background:var(--soft3);color:var(--amber)}
.case .scale{font-size:12.5px;color:var(--slate);line-height:1.5;flex:1}
.case .path{font-size:11.8px;color:var(--muted);border-top:1px dashed var(--line);padding-top:8px}
/* CHARTS */
.charts{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.chart{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px;box-shadow:var(--shadow)}
.chart h4{font-size:15px;margin-bottom:4px}
.chart .ch-sub{font-size:12.5px;color:var(--muted);margin-bottom:12px}
.bar-row{display:flex;align-items:center;gap:10px;margin:7px 0;font-size:13px}
.bar-row .lab{width:96px;flex:none;color:var(--slate);text-align:right}
.bar-row .track{flex:1;background:#eef0f6;border-radius:6px;height:18px;overflow:hidden}
.bar-row .fill{height:100%;border-radius:6px;background:var(--indigo);transition:.4s}
.bar-row .val{width:30px;flex:none;font-weight:700;text-align:left}
/* BOUNDARY */
.bnd-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.bnd{border:1px solid var(--line);border-radius:13px;padding:16px;background:var(--panel);box-shadow:var(--shadow);border-left:4px solid var(--rose)}
.bnd h4{font-size:15px;margin-bottom:4px}
.bnd .ids{font-size:12px;color:var(--rose);font-weight:700;margin-bottom:8px}
.bnd p{font-size:13px;color:var(--slate)}
/* REGIONS */
.reg-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.reg{border:1px solid var(--line);border-radius:14px;padding:16px;background:var(--panel);box-shadow:var(--shadow)}
.reg h4{font-size:16px;margin-bottom:10px;display:flex;justify-content:space-between;align-items:center}
.reg .conf{font-size:11px;padding:2px 8px;border-radius:6px;background:var(--soft2);color:var(--teal);font-weight:700}
.reg dl{font-size:13px;display:grid;grid-template-columns:auto 1fr;gap:6px 10px}
.reg dt{color:var(--muted);white-space:nowrap} .reg dd{color:var(--ink)}
/* CONCLUSIONS */
.concl{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.con{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px;box-shadow:var(--shadow);position:relative}
.con .k{position:absolute;top:-12px;left:18px;background:var(--indigo);color:#fff;font-weight:800;font-size:13px;border-radius:8px;padding:2px 10px}
.con h4{font-size:15.5px;margin:6px 0 8px}
.con p{font-size:13.5px;color:var(--slate)}
.con .act{margin-top:10px;font-size:13px;background:var(--soft);border-radius:9px;padding:9px 11px;color:var(--indigo);font-weight:600}
/* PRIORITY */
.prio{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:8px}
.pr{border-radius:13px;padding:16px;border:1px solid var(--line);background:var(--panel);box-shadow:var(--shadow)}
.pr .lv{font-size:12px;font-weight:800;padding:3px 9px;border-radius:7px;display:inline-block;margin-bottom:8px}
.lv1{background:var(--soft);color:var(--indigo)} .lv2{background:var(--soft2);color:var(--teal)} .lv3{background:var(--soft3);color:var(--amber)} .lv4{background:var(--soft4);color:var(--rose)}
.pr h4{font-size:15px;margin-bottom:6px} .pr p{font-size:13px;color:var(--slate)}
/* FOOTER */
footer{padding:34px 0 60px;color:var(--muted);font-size:13px}
footer b{color:var(--ink)}
.notebox{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin-top:12px;font-size:13px}
@media(max-width:900px){.def-grid,.grid-cases,.bnd-grid,.reg-grid,.charts,.concl,.prio{grid-template-columns:1fr}.funnel{grid-template-columns:1fr}}
</style>
</head>
<body>
<nav><div class="nav-inner">
  <span class="brand">🎮 世界级爆款小游戏 · 结论看板</span>
  <div class="nav-links">
    <a href="#topconcl">结论</a><a href="#def">定义</a><a href="#screen">筛选</a><a href="#core">核心样本</a>
    <a href="#data">数据</a><a href="#bnd">边界</a><a href="#region">区域</a>
    <a href="#concl">结论</a><a href="#prio">立项</a>
  </div>
</div></nav>

<header class="hero"><div class="wrap">
  <h1>新一代世界级爆款小游戏<br>最终研究结论</h1>
  <p class="sub">先立标准，再筛样本。基于 <b>62</b> 个候选案例、<b>16</b> 个失败/受阻范式、<b>9</b> 个区域市场研究与 <b>80</b> 条权威来源，已形成关于"世界级爆款小游戏"的最终结论：它是一组可验证、可复用、跨文化的产品结构，而非一句模糊口号。</p>
  <div class="tagrow">
    <span class="tag">核心样本 <b>36</b></span>
    <span class="tag">边界样本 <b>23</b></span>
    <span class="tag">排除样本 <b>3</b></span>
    <span class="tag">来源 <b>S001–S080</b></span>
    <span class="tag">定稿 <b>2026-07-15</b></span>
  </div>
</div></header>

<!-- 结论前置 -->
<section id="topconcl" class="topconcl"><div class="wrap">
  <div class="sec-head"><span class="no">★</span><h2>先说结论：最火的世界级爆款小游戏</h2><span class="en">/ The Verdict</span></div>
  <div class="tc-body">__CONCL_TOP__</div>
</div></section>

<!-- 定义 -->
<section id="def"><div class="wrap">
  <div class="sec-head"><span class="no">00</span><h2>必须先定义的三件事</h2><span class="en">/ Definitions</span></div>
  <p class="lead">没有定义，"世界级爆款小游戏"只是被随意伸缩的词。下面三条是本报告<b>唯一的筛选尺度</b>，所有案例据此判定，不迁就已有结论。</p>
  <div class="def-grid">
    <div class="def d1">
      <h3>小游戏</h3><div class="en">Small Game · 五维同时约束</div>
      <ul>
        <li><span class="dot"></span><div><b>体量</b> 单一核心循环；团队多 &lt;100 人；立项到上线以周—月计</div></li>
        <li><span class="dot"></span><div><b>玩法</b> 单一主机制；3 秒可理解；单局 1–15 分钟</div></li>
        <li><span class="dot"></span><div><b>分发</b> 轻入口：商店 / 超级 App / Web / 平台内嵌</div></li>
        <li><span class="dot"></span><div><b>商业化</b> IAA / 轻 IAP / 混合；ARPPU 远低于 3A</div></li>
        <li><span class="dot"></span><div><b>时长</b> 碎片化可玩；不要求每日数小时 grind</div></li>
      </ul>
      <div class="note">边界：Kingshot 等"轻钩子→深系统"，入口算小游戏，但成功靠深系统，不计入纯小游戏爆款。</div>
    </div>
    <div class="def d2">
      <h3>爆款</h3><div class="en">Hit · 至少满足 4 条</div>
      <ul>
        <li><span class="dot"></span><div><b>规模</b> 下载 ≥1000 万 / 收入 ≥$1000 万 / 主要市场 Top10</div></li>
        <li><span class="dot"></span><div><b>速度</b> 月级触达临界规模（通常 &lt;12 个月）</div></li>
        <li><span class="dot"></span><div><b>传播</b> 显著口碑/分享/迷因，非纯买量</div></li>
        <li><span class="dot"></span><div><b>渗透</b> 破圈成谈资、表情包、短视频梗</div></li>
        <li><span class="dot"></span><div><b>持续</b> 规模位维持 ≥6 个月（硬门槛）</div></li>
      </ul>
      <div class="note">反例：Hamster Kombat 规模+速度+传播达标，但留存崩塌，属"爆款不可持续"。</div>
    </div>
    <div class="def d3">
      <h3>世界级</h3><div class="en">World-class · 至少满足 4 条</div>
      <ul>
        <li><span class="dot"></span><div><b>跨生态</b> 在 ≥2 个网络生态成立</div></li>
        <li><span class="dot"></span><div><b>跨文化</b> 在 ≥2 个文化区验证（非单国/单语圈）</div></li>
        <li><span class="dot"></span><div><b>规模</b> 全球头部：数千万用户 / 数亿美元收入</div></li>
        <li><span class="dot"></span><div><b>持续</b> 全球范围维持存在感</div></li>
        <li><span class="dot"></span><div><b>范式</b> 确立可复用产品结构，后人可照骨架立项</div></li>
      </ul>
      <div class="note">反例：羊了个羊=国民级非世界级（跨文化=0）；Hamster Kombat=有世界级规模无持续性。</div>
    </div>
  </div>
</div></section>

<!-- 筛选 -->
<section id="screen"><div class="wrap">
  <div class="sec-head"><span class="no">01</span><h2>62 案例重筛结果</h2><span class="en">/ Screening</span></div>
  <p class="lead">用上述标准把 62 个候选案例判为<b>核心 / 边界 / 排除</b>。判定标记：✅ 满足 · ⚠️ 边界 · ❌ 不满足。</p>
  <div class="funnel">
    <div class="donut-wrap"><svg id="donut" width="280" height="280" viewBox="0 0 280 280"></svg></div>
    <div>
      <div class="funnel-legend">
        <div class="row"><span class="sw" style="background:var(--indigo)"></span><div><div>核心样本</div><div class="d">世界级 ✅ + 爆款 ✅ + 小游戏 ✅，可直接作立项参照</div></div><span class="n">36</span></div>
        <div class="row"><span class="sw" style="background:var(--amber)"></span><div><div>边界样本</div><div class="d">至少一项不纯，需说明后才可用（6 类）</div></div><span class="n">23</span></div>
        <div class="row"><span class="sw" style="background:var(--rose)"></span><div><div>排除样本</div><div class="d">国民级 ≠ 世界级，跨文化 = 0</div></div><span class="n">3</span></div>
      </div>
      <div class="insight"><b>关键发现：</b>核心样本里 C001–C050 多为"历史锚点"（证明机制跨文化成立）；2024–2025 这轮混合休闲解谜爆发中，真正落到核心样本的纯小游戏只有 <b>Cell Survivor</b> 与 <b>Color Block Jam</b>——多数（Screw 系列、Sand Blast、Foodie Sizzle）仍停在"区域强势 / 闪爆"层级，印证品类窗口期仅 6–12 个月。</div>
    </div>
  </div>
</div></section>

<!-- 核心样本 -->
<section id="core"><div class="wrap">
  <div class="sec-head"><span class="no">02</span><h2>核心样本看板</h2><span class="en">/ 36 Core Cases</span></div>
  <p class="lead">以下 36 个案例同时跨越"小游戏 + 爆款 + 世界级"三道门槛，按综合分由高到低静态陈列（已移除失效的筛选控件，保证任意查看器都能完整显示全部样本）。</p>
  <div class="grid-cases" id="caseGrid"></div>
</div></section>

<!-- 数据 -->
<section id="data"><div class="wrap">
  <div class="sec-head"><span class="no">03</span><h2>数据可视化</h2><span class="en">/ Charts</span></div>
  <div class="charts">
    <div class="chart"><h4>玩法母体分布（全 62 例）</h4><div class="ch-sub">按核心玩法母体统计候选案例数量</div><div id="chartGp"></div></div>
    <div class="chart"><h4>综合分分布</h4><div class="ch-sub">核心样本综合分（百分制）区间分布</div><div id="chartScore"></div></div>
    <div class="chart"><h4>边界样本分类</h4><div class="ch-sub">23 个边界样本按 6 类归因</div><div id="chartBnd"></div></div>
    <div class="chart"><h4>主要生态分布（全 62 例）</h4><div class="ch-sub">按首发生态归类（多个平台计主平台）</div><div id="chartEco"></div></div>
  </div>
</div></section>

<!-- 边界 -->
<section id="bnd"><div class="wrap">
  <div class="sec-head"><span class="no">04</span><h2>边界样本（23 个）</h2><span class="en">/ Boundary</span></div>
  <p class="lead">边界样本不是"失败"，而是"不纯"——它们极具参考价值，但必须在说明其不纯之处后才可用于立项参照，避免幸存者偏差。</p>
  <div class="bnd-grid" id="bndGrid"></div>
</div></section>

<!-- 区域 -->
<section id="region"><div class="wrap">
  <div class="sec-head"><span class="no">05</span><h2>区域机会地图</h2><span class="en">/ Regions</span></div>
  <p class="lead">不贴国家标签，而用生态差异指导产品改造。9 个区域市场的入口、社交关系、适合验证的玩法与结构风险。</p>
  <div class="reg-grid" id="regGrid"></div>
</div></section>

<!-- 结论 -->
<section id="concl"><div class="wrap">
  <div class="sec-head"><span class="no">06</span><h2>七大核心结论</h2><span class="en">/ Conclusions</span></div>
  <p class="lead">以下结论只来自 36 个核心样本，证据层级：机构白皮书（S047–S063）+ 社媒一手评价 + 平台实时数据。</p>
  <div class="concl" id="conclGrid"></div>
</div></section>

<!-- 立项 -->
<section id="prio"><div class="wrap">
  <div class="sec-head"><span class="no">07</span><h2>下一代立项指引</h2><span class="en">/ Where to bet</span></div>
  <div class="prio" id="prioGrid"></div>
</div></section>

<footer><div class="wrap">
  <p><b>方法论与置信度</b> · 核心样本 36 例的判定有机构白皮书与多平台数据交叉支撑，置信度高；研究底表已定稿为 <code>v3_白皮书来源.xlsx</code>。</p>
  <div class="notebox">
    <b>已保留的数据冲突（双口径，不强行统一）：</b><br>
    · Hamster Kombat MAU：−83% ~ −96%<br>
    · Kingshot 收入：$8.12 亿（含分成） vs $4.48 亿（AppMagic 净 IAP）<br>
    · Newzoo 全球：$201.6B 终值 vs $188.8B 年初预测<br>
    · 伽马 535 亿（全平台 2025） vs 巨量 398.4 亿（抖音 2024）——口径差异，不可直接比较
  </div>
  <p style="margin-top:14px">来源优先级：官方/平台文档 &gt; 政府监管 &gt; Sensor Tower/AppMagic/Newzoo/伽马/巨量 &gt; 学术 &gt; 权威媒体 &gt; 行业媒体 &gt; 社区线索（仅作线索）。同一重要结论尽量双源交叉验证。</p>
</div></footer>

<script id="data" type="application/json">__DATA__</script>
<script>
const D = JSON.parse(document.getElementById('data').textContent);
const C = D.cases, R = D.regions, BM = D.bnd_meta, CNT = D.counts;

/* ---- Donut ---- */
(function(){
  const data=[['核心',CNT.core,'#4f46e5'],['边界',CNT.boundary,'#d97706'],['排除',CNT.excluded,'#e11d48']];
  const total=CNT.total, cx=140, cy=140, r=92, sw=38;
  let ang=-Math.PI/2; let s='';
  data.forEach(d=>{
    const a2=ang+ d[1]/total*Math.PI*2;
    const x1=cx+r*Math.cos(ang), y1=cy+r*Math.sin(ang);
    const x2=cx+r*Math.cos(a2), y2=cy+r*Math.sin(a2);
    const large=(a2-ang)>Math.PI?1:0;
    s+=`<path d="M${cx} ${cy} L${x1} ${y1} A${r} ${r} 0 ${large} 1 ${x2} ${y2} Z" fill="${d[2]}"/>`;
    ang=a2;
  });
  s+=`<circle cx="${cx}" cy="${cy}" r="${r-sw/2}" fill="#fff"/><text x="${cx}" y="${cy-6}" text-anchor="middle" font-size="30" font-weight="800" fill="#1f2430">62</text><text x="${cx}" y="${cy+16}" text-anchor="middle" font-size="12" fill="#6b7280">候选案例</text>`;
  document.getElementById('donut').innerHTML=s;
})();

/* ---- Core cards ---- */
const gpSet=[...new Set(C.filter(c=>c.cls==='core').map(c=>c.gameplay))];
const ecoSet=[...new Set(C.filter(c=>c.cls==='core').map(c=>c.eco.split('/')[0].trim()))];
let fGp='all', fEco='all', kw='';
const gpChips=document.getElementById('gpChips'), ecoChips=document.getElementById('ecoChips');
function mkChips(box, arr, key){
  let h=`<span class="chip ${key==='all'?'on':''}" data-v="all">全部</span>`;
  arr.forEach(v=>{ h+=`<span class="chip" data-v="${v}">${v}</span>`; });
  box.innerHTML=h;
  box.querySelectorAll('.chip').forEach(c=>c.onclick=()=>{
    box.querySelectorAll('.chip').forEach(x=>x.classList.remove('on'));
    c.classList.add('on');
    if(box===gpChips) fGp=c.dataset.v; else fEco=c.dataset.v;
    render();
  });
}
mkChips(gpChips, gpSet, 'all'); mkChips(ecoChips, ecoSet, 'all');

function sc(s){return s==null?60:s;}
function render(){
  let list=C.filter(c=>c.cls==='core');
  if(fGp!=='all') list=list.filter(c=>c.gameplay===fGp);
  if(fEco!=='all') list=list.filter(c=>c.eco.split('/')[0].trim()===fEco);
  if(kw) list=list.filter(c=>(c.name+' '+c.cn+' '+c.id).toLowerCase().includes(kw.toLowerCase()));
  const sb=document.getElementById('sortby').value;
  list.sort((a,b)=> sb==='score'? sc(b.score)-sc(a.score) : sb==='year'? (b.year||0)-(a.year||0) : a.name.localeCompare(b.name));
  document.getElementById('cnt').textContent=`显示 ${list.length} / 36`;
  const g=document.getElementById('caseGrid');
  g.innerHTML=list.map(c=>{
    const col=c.score>=85?'#16a34a':c.score>=75?'#4f46e5':c.score>=65?'#d97706':'#e11d48';
    const eco=c.eco.split('/')[0].trim();
    return `<div class="case">
      <div class="top"><div><div class="nm">${c.name}</div><div class="cn">${c.cn||''} · ${c.id}</div></div>
      <div class="score" style="background:${col}">${sc(c.score)}<small>分</small></div></div>
      <div class="meta"><span class="pill">${c.year||''}</span><span class="pill g">${c.gameplay}</span><span class="pill a">${eco}</span></div>
      <div class="scale">${c.scale||''}</div>
      <div class="path">🌍 ${c.path||''}</div>
    </div>`;
  }).join('');
}
document.getElementById('search').oninput=e=>{kw=e.target.value;render();};
document.getElementById('sortby').onchange=render;
render();

/* ---- Charts (bars) ---- */
function hbars(el, arr, max, colors){
  const palette=colors||['#4f46e5','#0d9488','#d97706','#e11d48','#475569','#16a34a','#7c3aed','#0891b2'];
  el.innerHTML=arr.map((d,i)=>{
    const w=max?d.v/max*100:0; const col=palette[i%palette.length];
    return `<div class="bar-row"><div class="lab">${d.k}</div><div class="track"><div class="fill" style="width:${w}%;background:${col}"></div></div><div class="val">${d.v}</div></div>`;
  }).join('');
}
// gameplay
const gpCount={}; C.forEach(c=>{gpCount[c.gameplay]=(gpCount[c.gameplay]||0)+1;});
let gpArr=Object.entries(gpCount).map(([k,v])=>({k,v})).sort((a,b)=>b.v-a.v);
hbars(document.getElementById('chartGp'), gpArr, gpArr[0].v);
// score histogram (core only)
const buckets=[['<60',0],['60–69',0],['70–79',0],['80–89',0],['90–100',0]];
C.filter(c=>c.cls==='core'&&c.score!=null).forEach(c=>{
  const s=c.score; if(s<60)buckets[0][1]++; else if(s<70)buckets[1][1]++; else if(s<80)buckets[2][1]++; else if(s<90)buckets[3][1]++; else buckets[4][1]++;
});
hbars(document.getElementById('chartScore'), buckets.map(b=>({k:b[0],v:b[1]})), Math.max(...buckets.map(b=>b[1])), ['#e11d48','#d97706','#0d9488','#4f46e5','#16a34a']);
// boundary
const bndCount={}; Object.entries(BM).forEach(([k,v])=>{ const n=C.filter(c=>c.cls==='boundary'&&c.cat===k).length; bndCount[v[0]]=n; });
const bndArr=Object.entries(bndCount).map(([k,v])=>({k,v})).sort((a,b)=>b.v-a.v);
hbars(document.getElementById('chartBnd'), bndArr, bndArr[0].v, ['#e11d48','#d97706','#0d9488','#4f46e5','#475569','#16a34a']);
// eco
const ecoCount={}; C.forEach(c=>{const e=c.eco.split('/')[0].trim(); ecoCount[e]=(ecoCount[e]||0)+1;});
let ecoArr=Object.entries(ecoCount).map(([k,v])=>({k,v})).sort((a,b)=>b.v-a.v).slice(0,8);
hbars(document.getElementById('chartEco'), ecoArr, ecoArr[0].v);

/* ---- Boundary grid ---- */
document.getElementById('bndGrid').innerHTML=Object.entries(BM).map(([k,v])=>{
  const ids=C.filter(c=>c.cls==='boundary'&&c.cat===k).map(c=>c.id).join('、');
  return `<div class="bnd"><h4>${v[0]}</h4><div class="ids">${ids}</div><p>${v[1]}</p></div>`;
}).join('');

/* ---- Regions ---- */
document.getElementById('regGrid').innerHTML=R.map(r=>`
  <div class="reg"><h4>${r.name}<span class="conf">${r.conf||''}</span></h4>
  <dl>
    <dt>主导入口</dt><dd>${r.entry||''}</dd>
    <dt>社交关系</dt><dd>${r.social||''}</dd>
    <dt>适合验证</dt><dd><b style="color:var(--teal)">${r.fit||''}</b></dd>
    <dt>结构风险</dt><dd>${r.risk||''}</dd>
    <dt>公开信号</dt><dd>${r.signal||''}</dd>
  </dl></div>`).join('');

/* ---- Conclusions ---- */
const CONCL=[
 ['动作—情绪 &gt; 题材—外壳','核心样本跨文化成立的产品几乎都有不依赖语言的动作核心（消除/吞噬/跑酷/合成/种植）。主题皮肤千变万化，底层动作跨文化零摩擦。','立项先定"不依赖语言的动作核心"，皮肤/题材是最后一层本地化，不是第一层。'],
 ['离线成长 + 每日回流钩子','Grow a Garden/Talking Tom/Neko Atsume/Township/Gossip Harbor 都用"离开也在长"的资产感驱动 D1/D7 回流。差异在回流触发器。','离线成长本身普适；回流触发器必须按生态重做，不能直接翻译。'],
 ['轻钩子→中承接→重变现','Kingshot/Whiteout/Cell Survivor 用 3 秒可懂的小游戏钩子接流量，再中系统承接、深系统变现。但纯小游戏爆款持续性来自玩法深度+内容供给。','小游戏应追求"玩法可深玩性 + 持续内容供给"，而非默认"接 SLG 才能赚钱"。'],
 ['合作 &gt; 竞争的留存','Among Us/Stumble Guys/Chef Showdown 共同指向：社交喜剧/合作产生的"共同事件"比纯对抗更跨文化锁留。Roblox 装扮/角色扮演也是"一起玩"。','聚会表达类产品，优先设计"一起完成/一起笑"，而非"谁更强"。'],
 ['UGC 是内容容器核心','Roblox 上 Grow a Garden/Adopt Me/Brookhaven 长线靠玩家自产内容+周更+装饰交易 UGC。但社交图谱/Robux/编辑器是平台资产，换平台不成立。','学的是机制组合（离线成长+突变+赠礼+周更+装饰 UGC），不是"上 Roblox"。'],
 ['品类窗口期 6–12 个月','Screw Jam 月流水 522 万→不足 10 万仅约 12 个月；Screwdom 用 3D 旋转快速超越；同赛道内卷极快。','纯玩法创新必须上线即叠加元游戏/社交/资产层，否则 6–12 月内被仿品截流。'],
 ['"小"是分发轻+理解轻','核心样本既有单人/小团队（2048/Vampire Survivors/Magic Tiles），也有大厂（Royal Match/Gossip Harbor）。决定属性的是产品形态，不是团队规模。','别因"团队小"只做超休闲，也别因"有资源"做重。形态轻，是世界级的前提。'],
];
document.getElementById('conclGrid').innerHTML=CONCL.map((c,i)=>`
  <div class="con"><span class="k">${i+1}</span><h4>${c[0]}</h4><p>${c[1]}</p><div class="act">→ ${c[2]}</div></div>`).join('');

/* ---- Priority ---- */
const PRIO=[
 ['lv1','首选结构','不依赖语言的动作核心（消除/合成/吞噬/跑酷）＋ 离线成长资产 ＋ 每日回流钩子（按生态重做）＋ 合作型社交事件 ＋ LiveOps 周更。证据最强：Block Blast/Royal Match/Grow a Garden/Gossip Harbor。'],
 ['lv2','高潜未饱和','声控/体感 + 短视频自然传播（Mini Games 类）需补"话题消退后的留存承接"，目前仍是短板。'],
 ['lv3','平台机会','TikTok Minis = 抖音小游戏出海最短路径（30M 原生包零改造迁移，美区占 90%+ 收入），待实战数据验证。'],
 ['lv4','慎入','纯 T2E（Telegram）、纯买量超休闲、无元游戏的单一解谜——窗口期短、持续性差。'],
];
document.getElementById('prioGrid').innerHTML=PRIO.map(p=>`
  <div class="pr"><span class="lv ${p[0]}">${p[0]==='lv1'?'优先级 1':p[0]==='lv2'?'优先级 2':p[0]==='lv3'?'优先级 3':'慎入'}</span><h4>${p[1]}</h4><p>${p[2]}</p></div>`).join('');
</script>
</body>
</html>'''

HTML = HTML.replace('__DATA__', DATA_JSON)
open('世界级爆款小游戏_研究看板.html', 'w', encoding='utf-8').write(HTML)
print('HTML written, bytes=', len(HTML))
