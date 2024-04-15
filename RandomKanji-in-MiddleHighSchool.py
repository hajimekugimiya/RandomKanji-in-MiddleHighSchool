import random
import pprint
import tkinter as tk
allKanjiJuniorHighSchool = \
['亜', '哀', '挨', '曖', '握', '扱', '宛', '嵐', '依', '威', '為',
 '畏', '尉', '萎', '偉', '椅', '彙', '違', '維', '慰', '緯', '壱', '逸', '芋', '咽', '姻', '淫',
 '陰', '隠', '韻', '唄', '鬱', '畝', '浦', '詠', '影', '鋭', '疫', '悦', '越', '謁', '閲', '炎',
 '怨', '宴', '援', '煙', '猿', '鉛', '縁', '艶', '汚', '凹', '押', '旺', '欧', '殴', '翁', '奥',
 '憶', '臆', '虞', '乙', '俺', '卸', '穏', '佳', '苛', '架', '華', '菓', '渦', '嫁', '暇', '禍',
 '靴', '寡', '箇', '稼', '蚊', '牙', '瓦', '雅', '餓', '介', '戒', '怪', '拐', '悔', '皆', '塊',
 '楷', '潰', '壊', '懐', '諧', '劾', '崖', '涯', '慨', '蓋', '該', '概', '骸', '垣', '柿', '核',
 '殻', '郭', '較', '隔', '獲', '嚇', '穫', '岳', '顎', '掛', '括', '喝', '渇', '葛', '滑', '褐',
 '轄', '且', '釜', '鎌', '刈', '甘', '汗', '缶', '肝', '冠', '陥', '乾', '勘', '患', '貫', '喚',
 '堪', '換', '敢', '棺', '款', '閑', '勧', '寛', '歓', '監', '緩', '憾', '還', '環', '韓', '艦',
 '鑑', '含', '玩', '頑', '企', '伎', '忌', '奇', '祈', '軌', '既', '飢', '鬼', '亀', '幾', '棋',
 '棄', '毀', '畿', '輝', '騎', '宜', '偽', '欺', '儀', '戯', '擬', '犠', '菊', '吉', '喫', '詰',
 '却', '脚', '虐', '及', '丘', '朽', '臼', '糾', '嗅', '窮', '巨', '拒', '拠', '虚', '距', '御',
 '凶', '叫', '狂', '享', '況', '峡', '挟', '狭', '恐', '恭', '脅', '矯', '響', '驚', '仰', '暁',
 '凝', '巾', '斤', '菌', '琴', '僅', '緊', '錦', '謹', '襟', '吟', '駆', '惧', '愚', '偶', '遇',
 '隅', '串', '屈', '掘', '窟', '繰', '勲', '薫', '刑', '茎', '契', '恵', '啓', '掲', '渓', '蛍',
 '傾', '携', '継', '詣', '慶', '憬', '稽', '憩', '鶏', '迎', '鯨', '隙', '撃', '桁', '傑', '肩',
 '倹', '兼', '剣', '拳', '軒', '圏', '堅', '嫌', '献', '遣', '賢', '謙', '鍵', '繭', '顕', '懸',
 '幻', '玄', '弦', '舷', '股', '虎', '孤', '弧', '枯', '雇', '誇', '鼓', '錮', '顧', '互', '呉',
 '娯', '悟', '碁', '勾', '孔', '巧', '甲', '江', '坑', '抗', '攻', '更', '拘', '肯', '侯', '恒',
 '洪', '荒', '郊', '貢', '控', '梗', '喉', '慌', '硬', '絞', '項', '溝', '綱', '酵', '稿', '衡',
 '購', '乞', '拷', '剛', '傲', '豪', '克', '酷', '獄', '駒', '込', '頃', '昆', '恨', '婚', '痕',
 '紺', '魂', '墾', '懇', '沙', '唆', '詐', '鎖', '挫', '采', '砕', '宰', '栽', '彩', '斎', '債',
 '催', '塞', '歳', '載', '剤', '削', '柵', '索', '酢', '搾', '錯', '咲', '刹', '拶', '撮', '擦',
 '桟', '惨', '傘', '斬', '暫', '旨', '伺', '刺', '祉', '肢', '施', '恣', '脂', '紫', '嗣', '雌',
 '摯', '賜', '諮', '侍', '慈', '餌', '璽', '軸', '𠮟', '疾', '執', '湿', '嫉', '漆', '芝', '赦',
 '斜', '煮', '遮', '邪', '蛇', '酌', '釈', '爵', '寂', '朱', '狩', '殊', '珠', '腫', '趣', '寿',
 '呪', '需', '儒', '囚', '舟', '秀', '臭', '袖', '羞', '愁', '酬', '醜', '蹴', '襲', '汁', '充',
 '柔', '渋', '銃', '獣', '叔', '淑', '粛', '塾', '俊', '瞬', '旬', '巡', '盾', '准', '殉', '循',
 '潤', '遵', '庶', '緒', '如', '叙', '徐', '升', '召', '匠', '床', '抄', '肖', '尚', '昇', '沼',
 '宵', '症', '祥', '称', '渉', '紹', '訟', '掌', '晶', '焦', '硝', '粧', '詔', '奨', '詳', '彰',
 '憧', '衝', '償', '礁', '鐘', '丈', '冗', '浄', '剰', '畳', '壌', '嬢', '錠', '譲', '醸', '拭',
 '殖', '飾', '触', '嘱', '辱', '尻', '伸', '芯', '辛', '侵', '津', '唇', '娠', '振', '浸', '紳',
 '診', '寝', '慎', '審', '震', '薪', '刃', '尽', '迅', '甚', '陣', '尋', '腎', '須', '吹', '炊',
 '帥', '粋', '衰', '酔', '遂', '睡', '穂', '随', '髄', '枢', '崇', '据', '杉', '裾', '瀬', '是',
 '姓', '征', '斉', '牲', '凄', '逝', '婿', '誓', '請', '醒', '斥', '析', '脊', '隻', '惜', '戚',
 '跡', '籍', '拙', '窃', '摂', '仙', '占', '扇', '栓', '旋', '煎', '羨', '腺', '詮', '践', '箋',
 '潜', '遷', '薦', '繊', '鮮', '禅', '漸', '膳', '繕', '狙', '阻', '租', '措', '粗', '疎', '訴',
 '塑', '遡', '礎', '双', '壮', '荘', '捜', '挿', '桑', '掃', '曹', '曽', '爽', '喪', '痩', '葬',
 '僧', '遭', '槽', '踪', '燥', '霜', '騒', '藻', '憎', '贈', '即', '促', '捉', '俗', '賊', '遜',
 '汰', '妥', '唾', '堕', '惰', '駄', '耐', '怠', '胎', '泰', '堆', '袋', '逮', '替', '滞', '戴',
 '滝', '択', '沢', '卓', '拓', '託', '濯', '諾', '濁', '但', '脱', '奪', '棚', '誰', '丹', '旦',
 '胆', '淡', '嘆', '端', '綻', '鍛', '弾', '壇', '恥', '致', '遅', '痴', '稚', '緻', '畜', '逐',
 '蓄', '秩', '窒', '嫡', '抽', '衷', '酎', '鋳', '駐', '弔', '挑', '彫', '眺', '釣', '貼', '超',
 '跳', '徴', '嘲', '澄', '聴', '懲', '勅', '捗', '沈', '珍', '朕', '陳', '鎮', '椎', '墜', '塚',
 '漬', '坪', '爪', '鶴', '呈', '廷', '抵', '邸', '亭', '貞', '帝', '訂', '逓', '偵', '堤', '艇',
 '締', '諦', '泥', '摘', '滴', '溺', '迭', '哲', '徹', '撤', '添', '塡', '殿', '斗', '吐', '妬',
 '途', '渡', '塗', '賭', '奴', '怒', '到', '逃', '倒', '凍', '唐', '桃', '透', '悼', '盗', '陶',
 '塔', '搭', '棟', '痘', '筒', '稲', '踏', '謄', '藤', '闘', '騰', '洞', '胴', '瞳', '峠', '匿',
 '督', '篤', '凸', '突', '屯', '豚', '頓', '貪', '鈍', '曇', '丼', '那', '謎', '鍋', '軟', '尼',
 '弐', '匂', '虹', '尿', '妊', '忍', '寧', '捻', '粘', '悩', '濃', '把', '覇', '婆', '罵', '杯',
 '排', '廃', '輩', '培', '陪', '媒', '賠', '伯', '拍', '泊', '迫', '剝', '舶', '薄', '漠', '縛',
 '爆', '箸', '肌', '鉢', '髪', '伐', '抜', '罰', '閥', '氾', '帆', '汎', '伴', '畔', '般', '販',
 '斑', '搬', '煩', '頒', '範', '繁', '藩', '蛮', '盤', '妃', '彼', '披', '卑', '疲', '被', '扉',
 '碑', '罷', '避', '尾', '眉', '微', '膝', '肘', '匹', '泌', '姫', '漂', '苗', '描', '猫', '浜',
 '賓', '頻', '敏', '瓶', '扶', '怖', '附', '訃', '赴', '浮', '符', '普', '腐', '敷', '膚', '賦',
 '譜', '侮', '舞', '封', '伏', '幅', '覆', '払', '沸', '紛', '雰', '噴', '墳', '憤', '丙', '併',
 '柄', '塀', '幣', '弊', '蔽', '餅', '壁', '璧', '癖', '蔑', '偏', '遍', '哺', '捕', '舗', '募',
 '慕', '簿', '芳', '邦', '奉', '抱', '泡', '胞', '俸', '倣', '峰', '砲', '崩', '蜂', '飽', '褒',
 '縫', '乏', '忙', '坊', '妨', '房', '肪', '某', '冒', '剖', '紡', '傍', '帽', '貌', '膨', '謀',
 '頰', '朴', '睦', '僕', '墨', '撲', '没', '勃', '堀', '奔', '翻', '凡', '盆', '麻', '摩', '磨',
 '魔', '昧', '埋', '膜', '枕', '又', '抹', '慢', '漫', '魅', '岬', '蜜', '妙', '眠', '矛', '霧',
 '娘', '冥', '銘', '滅', '免', '麺', '茂', '妄', '盲', '耗', '猛', '網', '黙', '紋', '冶', '弥',
 '厄', '躍', '闇', '喩', '愉', '諭', '癒', '唯', '幽', '悠', '湧', '猶', '裕', '雄', '誘', '憂',
 '融', '与', '誉', '妖', '庸', '揚', '揺', '溶', '腰', '瘍', '踊', '窯', '擁', '謡', '抑', '沃',
 '翼', '拉', '裸', '羅', '雷', '頼', '絡', '酪', '辣', '濫', '藍', '欄', '吏', '痢', '履', '璃',
 '離', '慄', '柳', '竜', '粒', '隆', '硫', '侶', '虜', '慮', '了', '涼', '猟', '陵', '僚', '寮',
 '療', '瞭', '糧', '厘', '倫', '隣', '瑠', '涙', '累', '塁', '励', '戻', '鈴', '零', '霊', '隷',
 '齢', '麗', '暦', '劣', '烈', '裂', '恋', '廉', '錬', '呂', '炉', '賂', '露', '弄', '郎', '浪',
 '廊', '楼', '漏', '籠', '麓', '賄', '脇', '惑', '枠', '湾', '腕']
pprint.pprint(random.sample(allKanjiJuniorHighSchool, 50),compact=True)
k = 49
for i in random.sample(allKanjiJuniorHighSchool, 50):
    print('"'+str(i)+'"'+"を書いてください　"+"残り"+str(k))
    input()
    k = k - 1
    1
print("フィニッシュ！")