"""Chinese-English team name mapping for top 5 European leagues.

Covers: Premier League, Serie A, La Liga, Bundesliga, Ligue 1.
Includes common abbreviations, nicknames, and historical team names.
Automatically built from known mappings + DB validation.
"""
from __future__ import annotations

import re
from typing import Optional

# ---- Premier League ----
PREMIER_LEAGUE = {
    # English name → [Chinese variants]
    "Arsenal": ["阿森纳", "兵工厂", "枪手"],
    "Aston Villa": ["阿斯顿维拉", "维拉", "阿斯顿"],
    "Bournemouth": ["伯恩茅斯", "伯恩茅夫"],
    "Brentford": ["布伦特福德", "布伦特", "宾福特"],
    "Brighton": ["布莱顿", "白礼顿", "布莱"],
    "Burnley": ["伯恩利", "般尼"],
    "Chelsea": ["切尔西", "车路士", "蓝军"],
    "Crystal Palace": ["水晶宫"],
    "Everton": ["埃弗顿", "爱华顿"],
    "Fulham": ["富勒姆", "富咸"],
    "Hull": ["赫尔城", "赫尔", "侯城"],
    "Ipswich": ["伊普斯维奇", "伊普斯", "叶士域治"],
    "Leeds": ["利兹联", "利兹", "列斯联"],
    "Leicester": ["莱斯特城", "莱斯特", "李斯特城"],
    "Liverpool": ["利物浦", "红军"],
    "Man City": ["曼城", "曼彻斯特城"],
    "Man United": ["曼联", "曼彻斯特联"],
    "Newcastle": ["纽卡斯尔", "纽卡斯尔联", "纽卡素"],
    "Norwich": ["诺维奇", "诺域治"],
    "Nott'm Forest": ["诺丁汉森林", "诺丁汉"],
    "Sheffield United": ["谢菲尔德联", "谢菲联", "锡菲联"],
    "Southampton": ["南安普顿", "修咸顿"],
    "Tottenham": ["热刺", "托特纳姆"],
    "Watford": ["沃特福德", "屈福特"],
    "West Brom": ["西布朗", "西布朗维奇"],
    "West Ham": ["西汉姆", "西汉姆联", "韦斯咸"],
    "Wolves": ["狼队", "狼", "伍尔弗汉普顿"],
    "Coventry": ["考文垂", "高云地利"],
    "Luton": ["卢顿", "卢顿镇"],
    "Sunderland": ["桑德兰", "新特兰"],
    "Swansea": ["斯旺西", "史云斯"],
    "Stoke": ["斯托克城"],
    "Middlesbrough": ["米德尔斯堡"],
    "Cardiff": ["加的夫", "卡迪夫"],
    "Blackburn": ["布莱克本"],
    "Bolton": ["博尔顿"],
    "Portsmouth": ["朴茨茅斯"],
    "Wigan": ["维冈"],
    "Birmingham": ["伯明翰"],
    "Reading": ["雷丁"],
    "QPR": ["女王公园", "女王公园巡游者"],
    "Derby": ["德比郡"],
    "Huddersfield": ["哈德斯菲尔德"],
}

# ---- Serie A ----
SERIE_A = {
    "AC Milan": ["AC米兰", "米兰"],
    "Atalanta": ["亚特兰大", "阿特兰大"],
    "Bologna": ["博洛尼亚"],
    "Cagliari": ["卡利亚里"],
    "Como": ["科莫"],
    "Empoli": ["恩波利"],
    "Fiorentina": ["佛罗伦萨", "费伦天拿"],
    "Genoa": ["热那亚"],
    "Inter": ["国际米兰", "国米"],
    "Juventus": ["尤文图斯", "尤文"],
    "Lazio": ["拉齐奥"],
    "Lecce": ["莱切"],
    "Monza": ["蒙扎"],
    "Napoli": ["那不勒斯", "拿波里"],
    "Parma": ["帕尔马"],
    "Roma": ["罗马"],
    "Torino": ["都灵"],
    "Udinese": ["乌迪内斯"],
    "Venezia": ["威尼斯"],
    "Verona": ["维罗纳"],
    "Sassuolo": ["萨索洛", "莎索罗"],
    "Salernitana": ["萨勒尼塔纳"],
    "Spezia": ["斯佩齐亚"],
    "Cremonese": ["克雷莫内塞", "克雷莫纳"],
    "Sampdoria": ["桑普多利亚"],
    "Benevento": ["贝内文托"],
}

# ---- La Liga ----
LA_LIGA = {
    "Alaves": ["阿拉维斯"],
    "Ath Bilbao": ["毕尔巴鄂竞技", "毕尔巴鄂"],
    "Ath Madrid": ["马德里竞技", "马竞"],
    "Barcelona": ["巴塞罗那", "巴萨"],
    "Betis": ["皇家贝蒂斯", "贝蒂斯"],
    "Celta": ["塞尔塔", "塞尔塔维戈"],
    "Espanol": ["西班牙人"],
    "Getafe": ["赫塔费", "赫塔菲"],
    "Girona": ["赫罗纳"],
    "Las Palmas": ["拉斯帕尔马斯"],
    "Leganes": ["莱加内斯"],
    "Mallorca": ["马洛卡", "马略卡"],
    "Osasuna": ["奥萨苏纳"],
    "Real Madrid": ["皇家马德里", "皇马"],
    "Real Sociedad": ["皇家社会", "黑社会"],
    "Sevilla": ["塞维利亚", "西维尔"],
    "Valencia": ["瓦伦西亚", "巴伦西亚"],
    "Vallecano": ["巴列卡诺"],
    "Valladolid": ["巴拉多利德"],
    "Villarreal": ["比利亚雷亚尔", "维拉利尔"],
    "Elche": ["埃尔切"],
    "Cadiz": ["加的斯"],
    "Granada": ["格拉纳达"],
    "Levante": ["莱万特"],
    "Huesca": ["韦斯卡"],
    "Tenerife": ["特内里费"],
}

# ---- Bundesliga ----
BUNDESLIGA = {
    "Augsburg": ["奥格斯堡"],
    "Bayern Munich": ["拜仁慕尼黑", "拜仁"],
    "Bochum": ["波鸿"],
    "Dortmund": ["多特蒙德", "多特"],
    "Ein Frankfurt": ["法兰克福"],
    "Freiburg": ["弗赖堡", "弗莱堡"],
    "Heidenheim": ["海登海姆"],
    "Hoffenheim": ["霍芬海姆"],
    "Holstein Kiel": ["荷尔斯泰因基尔", "基尔"],
    "Leverkusen": ["勒沃库森", "利华古逊"],
    "M'gladbach": ["门兴格拉德巴赫", "门兴"],
    "Mainz": ["美因茨"],
    "RB Leipzig": ["莱比锡红牛", "莱比锡"],
    "St Pauli": ["圣保利"],
    "Stuttgart": ["斯图加特"],
    "Union Berlin": ["柏林联合"],
    "Werder Bremen": ["云达不莱梅", "不莱梅"],
    "Wolfsburg": ["沃尔夫斯堡"],
    "FC Koln": ["科隆"],
    "Hertha": ["柏林赫塔"],
    "Schalke 04": ["沙尔克04", "沙尔克"],
    "Dusseldorf": ["杜塞尔多夫"],
    "Hamburg": ["汉堡"],
    "Nurnberg": ["纽伦堡"],
    "Paderborn": ["帕德博恩"],
    "Darmstadt": ["达姆施塔特"],
}

# ---- Ligue 1 ----
LIGUE_1 = {
    "Angers": ["昂热"],
    "Auxerre": ["欧塞尔"],
    "Brest": ["布雷斯特"],
    "Le Havre": ["勒阿弗尔"],
    "Lens": ["朗斯"],
    "Lille": ["里尔"],
    "Lyon": ["里昂"],
    "Marseille": ["马赛"],
    "Monaco": ["摩纳哥"],
    "Montpellier": ["蒙彼利埃"],
    "Nantes": ["南特"],
    "Nice": ["尼斯"],
    "Paris SG": ["巴黎圣日耳曼", "巴黎", "大巴黎"],
    "Reims": ["兰斯"],
    "Rennes": ["雷恩"],
    "St Etienne": ["圣埃蒂安"],
    "Strasbourg": ["斯特拉斯堡"],
    "Toulouse": ["图卢兹"],
    "Bordeaux": ["波尔多"],
    "Lorient": ["洛里昂"],
    "Metz": ["梅斯"],
    "Clermont": ["克莱蒙"],
    "Troyes": ["特鲁瓦"],
    "Ajaccio": ["阿雅克肖"],
}

# Combined lookup: Chinese → English
_CN_TO_EN: dict[str, str] = {}

def _build_lookup() -> None:
    """Build combined Chinese→English lookup from all league mappings."""
    if _CN_TO_EN:
        return
    for league_map in [PREMIER_LEAGUE, SERIE_A, LA_LIGA, BUNDESLIGA, LIGUE_1]:
        for en_name, cn_names in league_map.items():
            for cn in cn_names:
                cn_lower = cn.lower().strip()
                if cn_lower not in _CN_TO_EN:
                    _CN_TO_EN[cn_lower] = en_name


def cn_to_en(cn_name: str) -> Optional[str]:
    """Translate Chinese team name to English.

    Handles: full names, abbreviations, nicknames, partial matches.
    Returns None if no match found.
    """
    _build_lookup()
    cn = cn_name.strip()
    cn_lower = cn.lower()

    # Exact match
    if cn_lower in _CN_TO_EN:
        return _CN_TO_EN[cn_lower]

    # Partial match: if cn_name contains a known Chinese name
    for cn_key, en_name in _CN_TO_EN.items():
        if cn_key in cn_lower or cn_lower in cn_key:
            return en_name

    # Try removing trailing characters (e.g. "阿森纳FC" → "阿森纳")
    cleaned = re.sub(r'[^\u4e00-\u9fff]', '', cn)
    cleaned_lower = cleaned.lower()
    for cn_key, en_name in _CN_TO_EN.items():
        if cn_key in cleaned_lower or cleaned_lower in cn_key:
            return en_name

    return None


def en_to_cn(en_name: str) -> str:
    """Translate English team name to its most common Chinese form."""
    _build_lookup()
    for league_map in [PREMIER_LEAGUE, SERIE_A, LA_LIGA, BUNDESLIGA, LIGUE_1]:
        if en_name in league_map:
            return league_map[en_name][0]
    return en_name


def team_in_model(cn_name: str, model_teams: set) -> bool:
    """Check if a Chinese-named team exists in the model's team set."""
    en = cn_to_en(cn_name)
    return en is not None and en in model_teams


def translate_match(cn_home: str, cn_away: str) -> tuple[Optional[str], Optional[str]]:
    """Translate both teams in a match. Returns (en_home, en_away)."""
    return cn_to_en(cn_home), cn_to_en(cn_away)
