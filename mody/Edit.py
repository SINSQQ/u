import random

ed = [
    "𓆩𝑵𝒂𝒛𝒂𝒓𓆪 🖤",
    "𓆩𝑴𝒐𝒉𝒂𝒎𝒆𝒅𓆪 🖤",
    "𓆩𝑲𝒂𝒓𝒂𝒓𓆪 🖤",
    "𓆩𝑨𝒉𝒎𝒆𝒅𓆪 🖤",
    "𓆩𝑨𝒅𝒂𝒎𓆪 🖤",
    "𓆩𝑯𝒖𝒔𝒔𝒊𝒆𝒏𓆪 🖤",
    "𓆩𝑨𝒍𝒐𝒔𝒉𓆪 🖤",
    "𓆩𝑹𝒂𝒔𝒐𝒖𝒍𓆪 🖤",
    "𓆩𝑨𝒃𝒐𝒅𝒆𓆪 🖤",
    "𓆩𝑴𝒖𝒔𝒕𝒂𝒇𝒂𓆪 🖤",
    "𓆩𝑴𝒂𝒉𝒅𝒊𓆪 🖤",
    "𓆩𝑸𝒂𝒔𝒂𝒎𓆪 🖤",
    "𓆩𝑹𝒂𝒔𝒉𝒂𝒅𓆪 🖤",
    "𓆩𝑨𝒅𝒏𝒂𝒏𓆪 🖤",
    "𓆩𝑺𝒂𝒓𝒎𝒂𝒅𓆪 🖤",
    "𓆩𝑯𝒂𝒔𝒂𝒏𓆪 🖤",
    "𓆩𝒌𝒉𝒂𝒍𝒆𝒅𓆪 🖤",
    "𓆩𝑶𝒎𝒂𝒓𓆪 🖤",
    "𓆩𝑯𝒂𝒛𝒂𝒎𓆪 🖤",
    "𓆩𝑯𝒂𝒕𝒂𝒎𓆪 🖤",
    "𓆩𝑶𝒔𝒂𝒎𝒂𓆪 🖤",
    "𓆩𝑯𝒂𝒅𝒐𓆪 🖤",
    "𓆩𝑯𝒂𝒊𝒅𝒂𝒓𓆪 🖤",
    "𓆩𝑮𝒉𝒂𝒍𝒆𝒃𓆪 🖤",
    "𓆩𝑨𝒌𝒓𝒂𝒎𓆪 🖤",
    "𓆩𝑯𝒂𝒔𝒐𝒏𝒆𓆪 🖤",
    "𓆩𝑯𝒂𝒎𝒐𝒅𝒊𓆪 🖤",
    "𓆩𝒗𝒊𝒓𝒐𝒔𓆪 🖤",
    "𓆩𝑶𝒓𝒂𝒔𓆪 🖤",
    "𓆩𝑺𝒂𝒍𝒊𝒉𓆪 🖤",
    "-𓆪𝗔𝗠𝗔𝗔𝗥.𖤐𓆩",
    "-𓆪𝗠𝗔𝗟𝗘𝗞.𖤐𓆩",
    "-𓆪𝗔𝗬𝗔𝗗.𖤐𓆩",
    "-𓆪𝗥𝗔𝗙𝗜𝗗.𖤐𓆩",
    "-𓆪𝗦𝗕𝗔𝗛.𖤐𓆩",
    "-𓆪𝗔𝗕𝗔𝗦.𖤐𓆩",
    "-𓆪𝗛𝗔𝗕𝗜𝗕.𖤐𓆩",
    "• ﴾𝔸𝔹𝔸𝕊𝕊﴿ ✬",
    "• ﴾𝕆𝕋ℍ𝕄𝔸ℕ﴿  ✬",
    "• ﴾ℍ𝔸𝔻𝔼ℝ﴿ ✬",
    "• ﴾𝕊𝕀𝕁𝔸𝔻﴿ ✬",
    "• ﴾𝔸ℍ𝕄𝔼𝔻﴿ ✬",
    "⌯『𝐀𝐋𝐈』𖤍᭄𓄹",
    "⌯『𝐋𝐁𝐍𝐀 』𖤍᭄𓄹",
    "⌯『𝐀𝐒𝐄𝐄𝐋』𖤍᭄𓄹",
    "⌯『𝐒𝐇𝐄𝐑𝐄𝐍』𖤍᭄𓄹",
    "⌯『𝐌𝐔𝐒𝐓𝐀𝐅𝐀』𖤍᭄𓄹",
    "╰𝐇𝐬𝐨༆︎╮",
    "╰𝐀𝐥𝐥𝐨༆︎╮",
    "╰𝐀𝐛𝐨𝐝༆︎╮",
    "╰𝐀𝐛𝐚𝐬༆︎╮",
    "╰𝐇𝐚𝐦𝐨𝐝༆︎╮",
    "╰𝐀𝐡𝐦𝐞𝐝༆︎╮",
    "- 𓊆 𝘼𝙈𝙀𝙍 𓊇 𖤍‌",
    "- 𓊆 𝘼𝙃𝙈𝙀𝘿 𓊇 𖤍‌",
    "- 𓊆 𝙈𝙊𝙃𝘼𝙈𝙀𝘿 𓊇 𖤍‌",
    "- 𓊆 𝙃𝙐𝙎𝙎𝙀𝙄𝙉 𓊇 𖤍‌",
    "- 𓊆 𝙊𝙈𝘼𝙍 𓊇 𖤍‌",
    "- 𓊆 𝘼𝙇𝙄 𓊇 𖤍‌",
    "- ❝ ⌊𝗗𝗔𝗡𝗡𝗬 𖨬 🇺🇸.",
    "- ❝ ⌊𝗠𝗔𝗬𝗞𝗟 𖨬 🇺🇸.",
    "- ❝ ⌊𝗘𝗩𝗔𝗡 𖨬 🇺🇸.",
    "- ❝ ⌊𝗝𝗢𝗡𝗬𖨬 🇺🇸.",
    "- ❝ ⌊𝗧𝗢𝗠 𖨬 🇺🇸.",
    "“𝐌𝐎𝐇𝐀𝐌𝐄𝐃”༆",
    "““𝐇𝐔𝐒𝐒𝐄𝐈𝐍”༆”",
    "““𝐀𝐊𝐈𝐋”༆”",
    "““𝐙𝐀𝐈𝐃”༆”",
    "⌯ ˹𝙆𝙖𝙧𝙖˼ ♕︎.",
    "⌯ ˹𝙉𝙖𝙖𝙧˼ ♕︎.",
    "⌯ ˹𝙂𝙢𝙧˼ ♕︎.",
    "⌯ ˹𝘿𝙚𝙫˼ ♕︎.",
    "⌯ ˹𝙀𝙫𝙖˼ ♕︎.", 
    "「𝘔𝘦𝘳𝘰 𐃣.",
    "「𝘋𝘢𝘦𝘷 𐃣.",
    "「𝘌𝘷𝘢 𐃣.",
    "「𝘋𝘮𝘢𝘳 𐃣.",
    "「𝘑𝘮𝘳𝘢 𐃣.",
    " •〘 𝗔𝗛𝗠𝗘𝗗 𓅂 〙",
    "•〘 𝗠𝗢𝗛𝗔𝗠𝗘𝗗 𓅂 〙",
    "•〘 𝗦𝗔𝗝𝗔𝗗 𓅂 〙",
    "•〘 𝗛𝗨𝗦𝗦𝗘𝗜𝗡 𓅂 〙",
    "•〘 𝗦𝗔𝗜𝗙 𓅂 〙",
    "•〘 𝗔𝗟𝗦𝗛 𓅂 〙",
    "𓂄‌‌‌𝐀𝐥𝐢 #𝟏 ",
    "𓂄‌‌‌𝐒𝐚𝐢𝐟 #𝟏 ",
    "𓂄‌‌‌𝐒𝐚𝐥𝐚𝐦 #𝟏 ",
    "𓂄‌‌‌𝐒𝐝𝐚𝐚𝐦 #𝟏 ",
    "𓂄‌‌‌𝐀𝐡𝐦𝐞𝐝 #𝟏 ",
    "𓂄‌‌‌𝐇𝐮𝐬𝐬𝐞𝐢𝐧 #𝟏 ",
    "𓂄‌‌‌𝐌𝐨𝐡𝐚𝐦𝐞𝐝 #𝟏 ",
    "- 𝙼𝙾𝙷𝙰𝙼𝙼𝙴𝙳🇮🇶➢",
    "- 𝙷𝚄𝚂𝚂𝙴𝙸𝙽🇮🇶➢",
    "- 𝙰𝙷𝙼𝙴𝙳🇮🇶➢",
    "- 𝚂𝙰𝙹𝙰𝙳🇮🇶➢",
    "- 𝙰𝙼𝙴𝚁🇮🇶➢",
    "- 𝚂𝙰𝙼𝚁🇮🇶➢",
    "- 𝙰𝙱𝙾𝙳🇮🇶➢",
    "- 𝙰𝙻𝙸🇮🇶➢",    
    "𓆩𝚁𝙾𝙽𝙴𓆪  🇺🇸.",
    "𓆩𝙴𝚅𝙰𝙽𓆪  🇺🇸.",
    "𓆩𝙹𝙰𝙺𓆪  🇺🇸.",
    "𓆩𝚃𝙾𝙼𓆪  🇺🇸.",
    "𓆩𝙹𝙾𝙽𓆪  🇺🇸.",
    "𓆩𝙰𝙷𝙼𝙸𝙳𓆪🎗️ ꙰",
    "𓆩𝙰𝙻𝙾𝚂𝙷𓆪🎗️ ꙰",
    "𓆩𝚂𝙰𝙹𝙰𝙳𓆪🎗️ ꙰",
    "𓆩𝚂𝙱𝙰𝙰𝙷𓆪🎗️ ꙰",
    "𓆩𝙷𝙰𝙸𝚃𝙷𝙼𓆪🎗️ ꙰",
    "𓆩𝙷𝚄𝚂𝚂𝙴𝙸𝙽𓆪🎗️ ꙰",
    "𓆩𝙼𝚄𝙷𝙰𝙼𝙼𝙰𝙳𓆪🎗️ ꙰",
    "𓆩𝑻𝒂𝑩𝒐𓆪 💞.",
    "𓆩𝑺𝒂𝒇𝒐𓆪 💞.",
    "𓆩𝑻𝒐𝒎𝒂𓆪 💞.",
    "𓆩𝒁𝒂𝒉𝒐𓆪 💞.",
    "𓆩𝑲𝒂𝒎𝒂𝒓𓆪 💞.",
    "𓆩𝑮𝒉𝒂𝒔𝒔𝒂𝒒𓆪 💞.",
    "𓆩𝑭𝒂𝒕𝒎𝒊𝒂𓆪 💞.",
    "𓆩𝑯𝒂𝒅𝒐𓆪 💞.",
    "𓆩𝑯𝒂𝒃𝒐𓆪 💞.",
    "𓆩𝑩𝒂𝒏𝒐𓆪 💞.",
    "𓆩𝑫𝒖𝒉𝒐𓆪 💞.",
    "𓆩𝑱𝒂𝒏𝒐𓆪 💞.",
    "𓆩𝑹𝒆𝒎𝒆𓆪💞.",
    "𓆩𝑯𝒂𝒋𝒂𝒓𓆪 💞.",
    "𓆩𝑨𝒚𝒂𓆪 💞.",
    "𓆩𝑺𝒉𝒂𝒉𝒂𝒅𓆪 💞.",
    "𓆩𝑹𝒂𝒈𝒉𝒂𝒅𓆪 💞.",
    "𓆩𝒁𝒂𝒊𝒏𝒂𓆪 💞.",
    "𓆩𝑨𝒚𝒂𝒕𓆪 💞.",
    "𓆩𝑴𝒂𝒓𝒊𝒆𝒎𓆪 💞.",
    "𓆩𝑯𝒂𝚠𝒓𝒂𝒂𓆪 💞.",
    "𓆩𝑭𝒂𝒕𝒆𓆪 💞.",
    "𓆩𝑫𝒂𝒏𝒐𓆪 💞.",
    "𓆩𝑮𝒉𝒂𝒅𝒂𓆪 💞.",
    "𓆩𝒁𝒂𝒊𝒏𝒂𓆪 💞.",
    "𓆩𝑹𝒖𝒂𝒚𝒅𝒂𓆪 💞.",
    "𝑩𝒂𝒏𝒆𝒆𝒏𓆪 💞.",
    "𓆩𝑴𝒆𝒎𝒆𓆪 💞.",
    "𓆩𝑵𝒂𝒃𝒂𓆪 💞.",
    "𓆩𝑵𝒂𝒅𝒂𓆪 💞.",
    "𓄼 𝘚 𝘖 𝘚 ༆ 𓄹.",
    "𓄼 𝘛 𝘖 𝘛 ༆ 𓄹.",
    "𓄼 𝘕 𝘖 𝘕 ༆ 𓄹.",
    "𓄼 𝘍 𝘖 𝘍 ༆ 𓄹.",
    "𓄼 𝘑 𝘖 𝘑  ༆ 𓄹.",
    "𓄼 𝘒 𝘖 𝘒 ༆ 𓄹.",
    "𓄼 𝘛 𝘕 𝘖 ༆ 𓄹.",
    "•˹𝙻𝚈𝙽𝙽˼⛈💞.",
    "•˹𝙽𝙾𝙾𝚁˼⛈💞.",
    "•˹𝚂𝙰𝙼𝙰𝚁˼⛈💞.",
    "•˹𝙽𝙾𝚁𝙷𝙰𝙽˼⛈💞.",
    "•˹𝙺𝙰𝚆𝚃𝙷𝙴𝚁˼⛈💞.",
    "•˹𝚃𝙰𝙱𝙰𝚁𝙰𝚀˼⛈💞.",
    "•˹𝚂𝙰𝙱𝚁𝙴𝙴𝙽˼⛈💞.",
    "•𝙼𝙰𝚁𝚈𝙰𝙼⋆  🧚🏻‍♀♥️ .",
    "•𝙱𝙰𝚃𝙾𝙻⋆ 🧚🏻‍♀♥️ .",
    "•𝙰𝙼𝙾𝙽⋆  🧚🏻‍♀♥️ .",
    "•𝚉𝙰𝙽𝙾𝚂𝙷𝙰⋆ 🧚🏻‍♀♥️ .",
    "•𝚉𝙰𝙷𝚁𝙰𝙰⋆  🧚🏻‍♀♥️ .",
    "•𝙱𝙰𝙽𝙴𝙽⋆ 🧚🏻‍♀♥️ .",
    "⌯ ˹ʀɴᴏѕʜ˼❀ .",
    "⌯ ˹ᴍᴇᴍᴏ˼❀ .",
    "⌯ ˹ʜᴏʀᴇ˼ ❀ .",
    "⌯ ˹ѕᴀʀᴀ˼ ❀ .",
    "⌯ ˹ѕᴏѕ˼  ❀ .",
    "『𓆩 𝚃𝙱𝙾 𓆪』𐂂𓄹",
    "『𓆩 𝙷𝙽𝙾 𓆪』 𐂂𓄹",
    "『𓆩 𝙰𝙽𝙾 𓆪』𐂂𓄹",
    "『𓆩 𝙰𝚉𝙾 𓆪』𐂂𓄹",
    "『𓆩 𝙳𝙷𝙾 𓆪』𐂂𓄹",
    "『𓆩 𝙰𝚂𝙾 𓆪』𐂂𓄹",
    "𓄼ʳᵃⁿᵉᵃ.",
    "‹ 𓄼ʰᵒʳ.",
    "‹ 𓄼ⁿⁿᵒ.",
    "‹  𓄼ˢᵃʳᵃ.",
    "‹  𓄼ˢᵉʰᵃᵐ.",
    "‹  𓄼ʰᵃᵈᵉʳ.",
    "‹𓄼ᵐⁿᵃʳ.",
    "‹  𓄼ᵃʳᵒᵃ.",
    "‹  𓄼ᵐᵃˡⁱᵈ.",
    "‹𓄼ⁿⁿˢʰ.",
    "𝄇 𝗦𝗢𝗦𝗢𝆹𝅥𝅮 𝄆💘",
    "𝄇 𝗡𝗢𝗡𝗔𝆹𝅥𝅮 𝄆💘",
    "𝄇 𝗝𝗢𝗝𝗔 𝆹𝅥𝅮  𝄆💘",
    "𝄇 𝗠𝗘𝗠𝗔𝆹𝅥𝅮𝄆💘",
    "𝄇 𝗞𝗢𝗞𝗔𝆹𝅥𝅮 𝄆💘",
    "ʰᵈᵒ ،💒💕",
    "ᶬᵉᶬ ،💒💕",
    "ᴬᵞᴬ ،💒💕",
    "ᴬˢᵒ ،💒💕",
    "ᶠᵒˢ ،💒💕",
    "ˢᵉᶮ ،💒💕",
    "• мαяɪαм🚴🏽‍♀️💞..",
    "• zαyиαв🚴🏽‍♀️💞..",
    "• sαяαн🚴🏽‍♀️💞..",
    "• zαняα🚴🏽‍♀️💞..",
    "• sнαɪмαα🚴🏽‍♀️💞.",
    "ᯓ 𝙄𝙏𝙎 - 𝗔 𝗦 𝗢 𓍰 .💕",
    "ᯓ 𝙄𝙏𝙎 - 𝗧 𝗕 𝗢 𓍰 .💕",
    "ᯓ 𝙄𝙏𝙎 - 𝗔 𝗡 𝗢 𓍰 .💕",
    "ᯓ 𝙄𝙏𝙎 - 𝗕 𝗡 𝗢 𓍰 .💕",
    "ᯓ 𝙄𝙏𝙎 - 𝗥 𝗡 𝗢 𓍰 .💕",
    "‹ 𝑯𝑱𝑶| 🇮🇶،",
    "‹ 𝑺𝑱𝑶 | 🇮🇶،",
    "‹ 𝑨𝑺𝑶| 🇮🇶،",
    "‹ 𝑨𝑵𝑶| 🇮🇶،",
    "‹ 𝑨𝑭𝑶| 🇮🇶،",
    "‹ 𝑻𝑩𝑶| 🇮🇶،",
    "‹ 𝒁𝑵𝑶| 🇮🇶،",
    "‹ 𝒁𝑯𝑶| 🇮🇶،",
    "˹ᴀɴᴏᴏ˼ ❀ ꙰ .”",
    "˹ᴛɴᴏᴏ˼❀ ꙰ .”",
    "˹ᴛʙᴏᴏ˼❀ ꙰ .”",
    "˹ᴊɴᴏᴏ˼❀ ꙰ .”",
    "˹ʜᴅᴏᴏ˼❀ ꙰ .”",
    "⌯ ˢʰᵃʰᵃᵈ .",
    "⌯ ᵃᵉʳⁿᵃʳᵈ .",
    "⌯ ˢᵃᵈᵉᵍ .",
    "⌯ ʰⁱⁿᵒᵒ .",
    "⌯ ⁿᵒᵒʳ .",
    "⌯ ᵃˡᵃᵃ .",
    "⌯ ᵃʰᵐᵉᵈ .",
    "⌯ ᵃʷˢ .",
    "⌯ 𝗧𝗢𝗧𝗔 𓋜𐂂،",
    "⌯ 𝗭𝗢𝗞𝗔𓋜𐂂،",
    "⌯ 𝗟𝗜𝗡𝗔 𓋜𐂂،",
    "⌯ 𝗛𝗔𝗡𝗔 𓋜𐂂،",
    "⌯ 𝗭𝗢𝗭𝗔 𓋜𐂂،",
    "⌯˹𝙼𝙰𝚁𝚈𝙰𝙼˼ ⸙.",
    "⌯˹𝚃𝙰𝙱𝙰𝚁𝙺˼ ⸙.",
    "⌯˹𝚉𝙰𝚈𝙽𝙰𝙱˼ ⸙.",
    "⌯˹𝚉𝙰𝙷𝚁𝙰˼ ⸙.",
    "⌯˹𝚁𝙴𝙰𝙼˼ ⸙.",
    "⌯˹𝙳𝙾𝙷𝙰˼ ⸙.",
    "⌯˹𝚂𝙰𝙹𝙰˼ ⸙.",
    "⌯˹𝙰𝚂𝙴𝙻˼ ⸙.",   
    "- 𝑎𝑠𝑜 𐇲.",
    "- 𝑎𝑛𝑜 𐇲.",
    "- 𝑡𝑏𝑜 𐇲.",
    "- 𝑡𝑛𝑜 𐇲.",
    "- 𝒛𝒉𝒐 𐇲.",
    "- 𝒛𝒏𝒐 𐇲.",
    "- 𝒉𝒅𝒐 𐇲.",
    "- 𝒉𝒃𝒐 𐇲",
    "𖥻 𓆩𝙍𝙚𝙚𝙢𓆪،𖤍",
    "𖥻 𓆩𝙕𝙖𝙮𝙣𝙖𝙗𓆪،𖤍",
    "𖥻 𓆩𝙁𝙖𝙩𝙚𝙢𝙖𓆪،𖤍",
    "𖥻 𓆩𝙍𝙖𝙤𝙖𝙣𓆪،𖤍",
    "𖥻 𓆩𝙅𝙖𝙣𝙖𝙩𓆪،𖤍",
    "𖥻 𓆩𝙕𝙖𝙝𝙧𝙖𓆪،𖤍",
    "𖥻 𓆩𝙉𝙤𝙨𝙖𓆪،𖤍",
    "- 𝙎 𝘼 𝙉 𝘿 𝙍 𝙄 𝙇 𝘼 : 🇺🇸Ꮠ",
    "- 𝙍 𝘽 𝘼 𝙉 𝙕 𝙇 : 🇺🇸Ꮠ",
    "- 𝙉 𝘼 𝙍 𝙏 𝙊 : 🇺🇸Ꮠ",
    "- 𝙎 𝘼 𝙇 𝙇 𝙔 : 🇺🇸Ꮠ",
    "- 𝙅 𝙀 𝙍 𝙔 : 🇺🇸Ꮠ",
    "- 𝙏 𝙊 𝙈 : 🇺🇸Ꮠ",
    "- 𝘽 𝙀 𝙉 : 🇺🇸Ꮠ",
    "𓂐 𝙀𝙇𝙄𝙕𝘼𝘽𝙀𝙏𝙃 𖠛.",
    "𓂐 𝘼𝙈𝘼𝙉𝘿𝘼 𖠛.",
    "𓂐 𝘼𝙉𝘿𝙍𝙀𝘼 𖠛.",
    "𓂐 𝙀𝙈𝙀𝙇𝙔 𖠛.",
    "𓂐𝙀𝙍𝙄𝙆𝘼 𖠛.",
    "𓂐 𝙀𝙑𝘼 𖠛.",
    "𓂐 𝘼𝙈𝙔 𖠛.",       
    "王娟", "李强", "张敏", "刘伟", "陈静",
    "杨勇", "赵艳", "黄军", "周秀英", "吴刚",
    "朱丽", "马云", "胡军", "郭丽", "林涛",
    "何燕", "高明", "梁敏", "郑阳", "罗鑫"
    "王伟", "李静", "张磊", "刘娜", "陈涛",
    "杨芳", "赵勇", "黄露", "周强", "吴丽",
    "朱明", "马红", "胡燕", "郭刚", "林婷",
    "何宇", "高娟", "梁强", "郑蕾", "罗艳",
    "秦华", "韩刚", "张燕", "梅勇", "杜静",
    "许明", "王艳", "冯强", "陈霞", "董华",
    "程雷", "曹娜", "康阳", "洪敏", "潘峰",
    "石秀英", "朱亚男", "冯欣", "马海燕", "李玲",
    "陈龙", "王凯", "杨林", "刘云", "黄洁",
    "周建国", "吴小华", "朱莉", "马云龙", "胡建华",
    "郭瑞", "林静", "何建平", "高磊", "梁宇",
    "郑军", "罗秀英", "秦刚", "韩丽", "张建军",
    "梅丽", "杜伟", "许婷", "王婷", "冯丽",
    "陈伟", "董杰", "程玉", "曹刚", "康丽",
    "洪峰", "潘芳", "石建华", "朱敏", "冯娜",
    "马建平", "李建军", "陈秀英", "杨磊", "刘建华",
    "黄玉", "周伟", "吴建军", "朱秀兰", "马秀英",
    "胡秀兰", "郭刚", "林伟", "何秀英", "高婷",
    "梁建华", "郑玉", "罗军", "秦秀英", "韩建华",
    "张秀英", "梅建军", "杜秀英", "许秀兰", "王建军",
    "冯秀英", "陈建军", "董秀英", "程建华", "曹秀兰",
    "康建军", "洪秀英", "潘建华", "石秀兰", "朱建华",
    "冯玉", "马建华", "李秀兰", "陈建华", "杨秀英",
    "刘建华", "黄建华", "周建华", "吴秀兰", "朱建华",
    "马秀兰", "胡建华", "郭秀英", "林建华", "何秀兰",
    "高建华", "梁秀英", "郑建华", "罗建华", "秦建华",
    "韩秀英", "张建华", "梅秀英", "杜建华", "许建华",
    "王建华", "冯建华", "陈建华", "董建华", "程秀英",
    "曹建华", "康秀英", "洪建华", "潘秀英", "石建华"       
]

ib = [
    "التجارب هي أفضل معلم.",
    "- نحنُ ألفاشلون وطنياً نجحنا أخيرا في حب الوطن .🤍.",
    "- أحبيني بعيدا عن مدينتي ألتي شبعت نوم .🤍.",
    "- ملامحي تتحدث نيابة عن كُل ألتعب ألذي في داخلي .🤍",
    "- تـجي أعزمڪہ ؏ غده وأشربك ﭼـاي مهيل من أدينات أمي .🖤.",
    "- أريدُ أن أهدء لعام أثنان ثلاثة لقد شعرت دائماً بالكثير من القلق أريد أن أهدء فحسب .🤍.",
    "- تگلها شبيها عيونـﭻ تعبانه عمت عين السادس الخلاﭺ هيـﭻ ذبلانه .🖤.",
    "- أنا بحاجة جداً إلى الجلوس قربه النافذة  بيوم ماطر وهادئ .🤍.",
    "- كُنت مهماً لدرجه أنني أعطيتُك أغنيتي المفظلة .🤍.",
    "- تگـله أتعب وأتعب و أرد مڪسوره وأنتجي ؏ صوت سوالفك .🖤.",
    "- تگوله أبقى وياي مثل ڪل يوم ساندني كولشي بدونك يتعب .🖤.",
    "- هل هُناك مغزى من ألعيش هل أستحق حتى أن أعيش .🤍.",
    "- بأمكان الأنسان أن يكون صديق لكثير من الأشياء غير البشر .🤍.",
    "- جنـﭻ بغـداد بسوالفها والحله بلطافتها والبصره بسمارها .🖤.",
    "- وهكذا كنتُ بالڪاد أخرجٌ من غرفتي في الأيام ألتالية .🤍.",
    "- تجـي تلـوليلي شويه ؏ صوتـڪہ وتضمني بين أديناتك .🖤.",
    "- هادئة ولا تشغلها الأحداث أليومية هيَ في مسارُها وألعالم بذلك ألمسار يُغرد لذاتهِ .🤍.",
    "- تگـوله شرايك الليله نغير المسار أنت تجي تنام ؏ صوتي وألعب بشعرك .🖤.",    
    "الابتسامة هي لغة لا تحتاج إلى ترجمة.",
    "الحب أقوى عندما يكون بسيطًا.",
    "الصداقة كنز لا يفنى.",
    "الحياة قصيرة، استمتع بها.",
    "العمل الجاد هو السلم إلى النجاح.",
    "على كل فراق وعودة.",
    "القراءة تغذية للعقل.",
    "الصبر مفتاح الفرج.",
    "ابتسم في وجه الحياة، وستبتسم إليك.",
    "المحاولة والإصرار يصنعان المستحيل.",
    "النجاح يبدأ حينما تتوقف عن التذمر.",
    "العقل طريق إلى النور.",
    "الصداقة الحقيقية كنز نفيس.",
    "الموهبة هي هدية، الفعل هو احتفال بها.",
    "لا تحكم على الآخرين من خلال مظهرهم.",
    "اعمل بصمت ولكن اجعل صداه هائلًا.",
    "لا تنتظر الفرصة، قم بخلقها.",
    "التفاؤل طريقك إلى النجاح.",
    "الحياة مليئة بالمفاجآت.",
    "الرضا بما لديك يجعلك أغنى.",
    "العقل الإيجابي يخلق حياة إيجابية.",
    "اجعل اليوم أفضل من الأمس.",
    "كن مثل الفراشة، ابدأ رحلتك بتحطيم القيود.",
    "المحبة تبدأ من الداخل.",
    "اعمل بذكاء ولا تتوقف عن التعلم.",
    "الكتب هي أفضل رفاق للإنسان.",
    "لا تيأس أبدًا، فالأمل يولد من الصبر.",
    "العقلانية هي مفتاح الحياة الناجحة.",
    "الجودة أفضل من الكمية.",
    "تعلم من الأمس، عيش اليوم، آمل في الغد.",
    "التفكير الإيجابي يغير الحياة.",
    "استمتع باللحظة الحالية.",
    "العمل الجماعي يحقق النجاح.",
    "التنوع يجعل الحياة أكثر إشراقا.",
    "تقدير الناس يعكس تقديرك لذاتك.",
    "الأمل هو شعلة تضيء طريقك في الظلام.",
    "احترم الآخرين كما تحترم نفسك.",
    "كن شخصًا إيجابيًا في علاقاتك.",
    "استمتع باللحظات البسيطة في الحياة.",
    "تخطى العقبات بروح الإصرار.",
    "تطوير الذات يعزز جودة الحياة.",
    "التحديات تصقل شخصيتك.",
    "لا تفقد الأمل في وجه التحديات.",
    "الإخفاق هو خطوة نحو النجاح.",
    "اجعل الفشل درسًا للنجاح المستقبلي.",
    "الإيمان بالنفس يفتح أبواب الفرص.",
    "اجتهد في كل ما تفعله.",
    "تفاءل حتى تصبح الحياة أفضل.",
    "الاستماع فن يعزز الفهم.",
    "الاعتناء بنفسك يسهم في السعادة.",
    "الصداقة تبني جسورًا للتواصل.",
    "النجاح يبدأ من داخلك.",
    "تعلم من أخطائك ونجح في المرة التالية.",
    "الأهداف الكبيرة تتطلب خطوات صغيرة.",
    "النية الحسنة تخلق طريقًا للتحقيق.",
    "التصميم والعزيمة يجعلانك تحقق أهدافك.",
    "كن صادقًا في كل تعاملاتك.",
    "العقلانية تقود إلى اتخاذ القرارات الصحيحة.",
    "العمل بجد يزرع ثمار النجاح.",
    "التسامح يعزز السلام الداخلي.",
    "الحب والاحترام يغذيان العلاقات.",
    "كن مفتونًا بالتحديات لتحقيق النجاح.",
    "النجاح يأتي لأولئك الذين لا يستسلمون.",
    "الرغبة الصادقة تبني الطريق للتحقيق.",
    "العقل المفتوح يفتح أفقًا للفهم.",
    "كن مؤمنًا بإمكانياتك.",
    "المرونة تجعلك تتكيف مع التغييرات.",
    "القوة تأتي من التفاؤل.",
    "الشكر يبني جسور الامتنان.",
    "التكنولوجيا تسهم في تقدم الحضارة.",
    "المعرفة قوة.",
    "الصحة هي ثروة حقيقية.",
    "الحياة مغامرة، استمتع بها.",
    "الحب هو لغة القلوب.",
    "التعلم مستمر، لا تتوقف عنه.",
    "النجاح يتطلب تضحيات.",
    "التفكير الإيجابي يحول الصعاب إلى فرص.",
    "كن داعمًا للآخرين في رحلتهم.",
    "القيادة تبدأ بالتحفيز والإلهام.",
    "الاستقامة تجعلك قويًا في الظروف الصعبة.",
    "الأمل ينير طريقك في الظلام.",
    "التفكير الإيجابي يخلق طاقة إيجابية حولك.",
    "احترم الآخرين كما تحترم نفسك.",
    "تعلم من تجارب الآخرين.",
    "النية الصافية تخلق نتائج صافية.",
    "التعاون يجعل العمل أسهل وأكثر فعالية.",
    "الاستمرارية تقود إلى النجاح.",
    "لا تضيع الوقت في الشكوى، استثمره في التحسين.",
    "الاستفادة من الفرص تحقق النجاح.",
    "الاستماع الفعّال يقوي العلاقات.",
    "الحكمة تأتي من الخبرة.",
    "العمل بجدان يزرع ثمار الرضا.",
    "الصبر يجعل الطريق أسهل.",
    "العقل الإيجابي ينقل الجبال.",
    "كن جيدًا فيما تفعل، والنجاح سيتبع.",
    "لا تدع الفشل يحد من طموحك.",
    "الصداقة الحقيقية تثري الحياة.",  
    "- 𝙃𝙚𝙡𝙡𝙤 : 𝙞'𝙢 𝙣𝙤𝙩 𝙛𝙞𝙣𝙚, 𝙘𝙖𝙣 𝙮𝙤𝙪 𝙝𝙪𝙜 𝙢𝙚?",
    "- 𝙃𝙚𝙡𝙡𝙤 : 𝙞'𝙢 𝙏𝙞𝙧𝙚𝙙, 𝙘𝙖𝙣 𝙮𝙤𝙪  𝙝𝙪𝙜 𝙢𝙚?",
    "- 𝙃𝙚𝙡𝙡𝙤 : 𝙇𝙞𝙛𝙚 𝙞𝙨 𝙙𝙞𝙛𝙛𝙞𝙘𝙪𝙡𝙩 𝘽𝙪𝙩 𝙣𝙤𝙩 𝙞𝙢𝙥𝙤𝙨𝙨𝙞𝙗𝙡𝙚",
    "- 𝘏𝘦𝘭𝘭𝘰 : 𝘠𝘰𝘶 𝘢𝘭𝘭 𝘩𝘢𝘷𝘦 𝘦𝘭𝘦𝘤𝘵𝘳𝘰𝘯𝘪𝘤 𝘍𝘢𝘯𝘵𝘢𝘴𝘪𝘴𝘦",
    "- 𝙃𝙚𝙡𝙡𝙤 : 𝗶 𝗮𝗺 𝗩𝗲𝗿𝘆 D̶e̶p̶r̶e̶s̶s̶e̶d̶",
    "- 𝙝𝙚𝙡𝙡𝙤 : 𝙞'𝙢 𝙨𝙤 𝙗𝙖𝙙 𝙤 𝙬𝙖𝙡𝙠 𝙖𝙬𝙖𝙮",
    "- 𝙃𝙚𝙡𝙡𝙤 : 𝙞'𝙢 𝙞𝙣 𝙨𝙤 𝙢𝙪𝙘𝙝 𝙋𝙖𝙞𝙣",
    "- 𝙃𝙚𝙡𝙡𝙤 : 𝙏𝙝𝙚 𝙀𝙣𝙙 𝙞𝙨 𝙖𝙨 𝙫𝙞𝙡𝙚 𝙖𝙨 𝙎𝙣𝙖𝙠𝙚 𝙑𝙚𝙢𝙤𝙣",
    "- 𝙃𝙚𝙡𝙡𝙤 : 𝙞 𝙈𝙞𝙨𝙨𝙚𝙙 𝙖 𝙇𝙤𝙩 𝙬𝙝𝙚𝙣 𝙬𝙞𝙡𝙡 𝙬𝙚 𝙢𝙚𝙚𝙩",
    "𝙃𝙚𝙡𝙡𝙤 : 𝙇𝙞𝙩𝙩𝙡𝙚 𝙋𝙧𝙚𝙨𝙚𝙣𝙘𝙚 𝙊𝙛 𝙜𝙧𝙚𝙖𝙩 𝙨𝙩𝙖𝙣𝙙𝙞𝙣𝙜",
    "𝙃𝙚𝙡𝙡𝙤 : 𝘿𝙞𝙙 𝙮𝙤𝙪 𝙢𝙞𝙨𝙨 𝙢𝙚 ?!",
    "𝙃𝙚𝙡𝙡𝙤 : 𝘿𝙤 𝙔𝙤𝙪 𝙡𝙤𝙫𝙚 𝙢𝙚 ? :/",
    "𝙃𝙚𝙡𝙡𝙤 : 𝘿𝙤 𝙔𝙤𝙪 𝙎𝙩𝙞𝙡𝙡 𝙇𝙤𝙫𝙚 𝙢𝙚? :)",
    "你是一朵绽放的花朵，散发着芬芳。",
    "生活就像一本未完成的书，等待我们填写精彩的篇章。",
    "勇气是穿越困境的风帆，让我们向前航行。",
    "爱是心灵的火焰，温暖我们的每一个瞬间。",
    "每一天都是我们成长的机会，塑造更好的自己。",
    "在星空中，你是那一颗璀璨的恒星，闪耀着希望之光。",
    "梦想是远方的灯塔，引领我们航行向着成功的海域。",
    "奋斗是通向辉煌的阶梯，一步一个脚印不断向前。",
    "希望是心灵的音乐，奏响着美好的生命旋律。",
    "友谊是一座坚实的桥梁，连接着我们的心与心。",
    "智慧如同明亮的星辰，照亮我们前行的黑暗之路。",
    "创造力是开启新世界的钥匙，点燃未知的奇迹。",
    "感恩是生活的甘露，滋润着每一片心灵的土壤。",
    "坚持是成功的基石，承受风雨后见彩虹的勇气。",
    "热情是生命的火花，点燃对生活的无限热爱。",
    "在困境中，我们发现内在的坚韧，战胜挑战。",
    "快乐是心灵的颜色，让生命变得绚烂多彩。",
    "冒险是生命的调味品，为旅途增添激情和神秘。",
    "理解是心与心的默契，建立深厚的情感纽带。",
    "希望如同清晨的曙光，驱散黑暗，照亮前路。",
    "信心是迈向成功的步伐，坚定不移地前行。",
    "善良是心灵的花朵，在世界上洒下美丽的馨香。",
    "拼搏是生命的旋律，奏响着奋斗的乐章。",
    "青春是梦想的驿站，等待我们迎接未来的风景。",
    "珍惜是心灵的镜子，映照出生命中真挚的美好。",
    "坚韧是战胜逆境的力量，铸就不可撼动的坚强。",
    "包容是心灵的海洋，容纳世界上各种美好和不完美。",
    "智慧是人生的导航仪，指引我们走向正确的方向。",
    "努力是成就梦想的钥匙，开启成功之门。",
    "思考是心灵的探险，发现无限可能性的旅程。",
    "顺流而下，如同船行大海，轻松面对人生波涛。",
    "宽容是心灵的庇护所，消除仇恨，培育爱的花园。",
    "阳光如同心灵的暖流，温暖寒冷的时光。",
    "创新是改变命运的魔法，塑造未来的奇迹。",
    "责任是生命的使命，肩负着创造美好的责任。",
    "勤奋如同沐浴清风，焕发身心的清新。",
    "成长是心智的花开，一点一滴汇聚成丰硕的果实。",
    "坚持是克服困难的法宝，铸就不可摧毁的力量。",
    "感悟是心灵的收获，提炼出生命中的智慧。",
    "梦幻如同星空的波光，勾勒出美好的未来。",
    "勇攀高峰，就像飞翔的鹰，迎接无限可能。",
    "忍耐是生命的耕耘，等待收获的季节。",
    "微笑如同阳光的温暖，融化生命中的阴霾。",
    "奉献是心灵的灯塔，引领我们前行的方向。",
    "坚强是人生的盾牌，抵御生命中的风雨。",
    "谦卑如同河流，滋润心田，流淌出宽容和宁静。",
    "刻苦是成功的伴侣，共同谱写辉煌的乐章。",
    "理想是人生的指南，指引我们航向美好的明天。",
    "拥抱是心灵的交响曲，奏响着真挚的情感。",
    "豁达是心灵的风景，欣赏生命中的美好。",
    "毅力如同跃过障碍的马匹，冲破困境。",
    "追求是生命的旅程，寻找前行的方向。",
    "独立是心灵的翅膀，飞翔向着理想的天空。",
    "守望是心灵的灯塔，照亮黑暗中的方向。",
    "静心如同湖水，映照出心灵的宁静和清澈。",
    "坚毅是登上成功巅峰的力量，战胜一切困难。",
    "感激是生活的旋律，奏响着对幸福的赞美。",
    "奇迹如同彩虹，跨越生命中的雨季，带来希望。",
    "胜利是努力的结晶，它让人生的旅途更加精彩。",
    "默契是心灵的默示录，让友情之花绽放。",
    "微风如同心灵的悠扬旋律，轻轻拂过生命。",
    "感性如同五彩斑斓的画笔，勾勒出生命的多彩。",
    "毅力是生命的引擎，推动我们前行的力量。",
    "阳光是心灵的抚慰，温暖生活中的寒冷。",
    "奋发如同劲舞的旋律，奏响成功的华丽交响曲。",
    "沉思如同夜空的繁星，闪烁出深邃的智慧。",
    "勇往直前，就像破浪前行的船只，穿越人生的风雨。",
    "悲欢离合如同生命的交响曲，奏响着丰富的人生。",
    "智者如同指南针，为我们指引通往成功的方向。",
    "奔跑是生命的节奏，追逐梦想的旋律。",
    "理解如同和弦的谐音，营造出和谐的人际关系。",
    "希冀是心灵的风筝，飞翔向着远方的蓝天。",
    "微笑如同生命的草原，绽放出青春的芳香。",
    "奉献是心灵的花朵，绽放出无尽的美丽。",
    "信任如同坚固的桥梁，连接着人与人的心。",
    "热爱是生命的润滑剂，使一切变得顺畅而美好。",
    "决心是征服困难的旗帜，高悬在成功的巅峰。",
    "谅解是心灵的春雨，滋润着人际关系的土壤。",
    "睿智如同明亮的月光，照亮我们前行的夜路。",
    "拼搏如同激流奔涌，冲刷出生命的坚韧。",
    "欢笑如同夏日的阳光，温暖着我们的心田。",
    "坚定如同橡树的根基，扎根在成功的土地上。",
    "虔诚如同清晨的祈祷，抚慰心灵的深处。",
    "感动如同美妙的音符，弹奏着真挚的情感。",
    "奋力如同翱翔的雄鹰，展翅向着成功的天空。",
    "平静如同湖面的宁静，反映出心灵的澄澈。",
    "青春如同绚烂的花朵，散发出生命的芬芳。",
    "责任如同河流的水流，滋润着生命的土壤。",
    "欣赏是心灵的画框，呈现出美好的风景。",
    "坚韧如同巍峨的山峰，屹立在成功的高峰。",
    "思考如同航行的指南针，引领我们走向明天。",
    "善良如同春日的微风，温暖着我们的心房。",
    "努力如同清晨的阳光，照亮前行的道路。",
    "成长如同绽放的花朵，展现出生命的美丽。",
    "坚持如同沙漠的风，吹拂着生命的韧性。",
    "感激是生命的礼物，点亮心灵的喜悦。",
    "奇迹如同春天的花蕾，孕育着无尽的可能。",
    "胜利如同骏马的奔腾，驰骋在成功的草原。",
    "默契如同交响乐团的合奏，奏响着和谐的旋律。",
    "微风如同心灵的拂面，轻轻吹散生活的疲惫。",
    "感性如同梦幻的彩虹，渲染出生命的多彩。",
    "毅力如同奔跑的马匹，冲破困境的藩篱。",
    "追求如同冉冉升起的朝阳，照亮生命的黑夜。",
    "独"        
]

ch = ["猫", "狗", "鸟", "鱼", "兔子", "龙", "熊猫", "象", "蝴蝶", "草原", "山", "河", "海洋", "星星", "月亮", "太阳", "花", "树", "草", "蓝天", "白云", "风", "雨", "雪", "电脑", "手机", "汽车", "自行车", "服装", "鞋子", "帽子", "手提包", "爱", "心", "亲吻", "婚姻", "家庭", "朋友", "笑容", "幸福", "成功", "学业", "工作", "旅行", "音乐", "电影", "艺术", "文学", "食物", "饮料", "美食", "健康", "运动", "假期", "梦想", "冒险", "教育", "科学", "技术", "创新", "环境", "保护", "慈善", "志愿者", "和平", "友谊", "团结", "信任", "合作", "领导", "政府", "政治", "法律", "社会", "经济", "移民", "文化", "宗教", "节日", "传统", "现代", "国际", "语言", "文字", "阅读", "写作", "绘画", "音乐会", "舞蹈", "戏剧", "时尚", "设计", "制造业", "电子商务", "金融", "投资", "股市", "创业", "环保", "可持续发展", "新能源", "城市规划", "交通", "高速铁路", "航空", "海运", "人工智能", "机器人", "太空探索", "星际旅行", "基因工程", "生命科学", "医疗", "疫苗", "大学", "学科", "研究", "科学家", "教授", "学生", "语言学", "历史学", "数学", "物理学", "化学", "生物学", "外交", "国际关系", "军事", "警察", "司法", "人权", "民主", "社交媒体", "电视", "广播", "报纸", "网络", "游戏", "艺术品", "收藏", "摄影", "漫画", "喜剧", "悲剧", "爱情片", "恐怖片", "科幻片", "动作片", "纪录片", "时装", "运动服", "风衣", "旗袍", "西装", "礼服", "休闲装", "时尚设计师", "时装表演", "时尚杂志", "高跟鞋", "运动鞋", "皮包", "钱包", "珠宝", "手表", "太阳镜", "戒指", "领带", "围巾", "手套", "毛衣", "丝绸", "棉布", "皮革", "毛皮", "高尔夫球", "足球", "篮球", "游泳", "登山", "滑雪", "自行车赛", "赛车", "马术", "瑜伽", "武术", "舞蹈比赛", "艺术节", "体育比赛", "冠军", "勇气", "希望", "忍耐", "快乐", "幽默", "美丽", "勤奋", "耐心", "尊重"]

chme = ["团体", "群组", "糖心", "主播", "运动的", "游戏", "时间", "赚", "团体", "群组", "糖心", "主播", "运动的", "游戏", "时间", "赚"]

ch_ed = [
    "王娟", "李强", "张敏", "刘伟", "陈静",
    "杨勇", "赵艳", "黄军", "周秀英", "吴刚",
    "朱丽", "马云", "胡军", "郭丽", "林涛",
    "何燕", "高明", "梁敏", "郑阳", "罗鑫"
    "王伟", "李静", "张磊", "刘娜", "陈涛",
    "杨芳", "赵勇", "黄露", "周强", "吴丽",
    "朱明", "马红", "胡燕", "郭刚", "林婷",
    "何宇", "高娟", "梁强", "郑蕾", "罗艳",
    "秦华", "韩刚", "张燕", "梅勇", "杜静",
    "许明", "王艳", "冯强", "陈霞", "董华",
    "程雷", "曹娜", "康阳", "洪敏", "潘峰",
    "石秀英", "朱亚男", "冯欣", "马海燕", "李玲",
    "陈龙", "王凯", "杨林", "刘云", "黄洁",
    "周建国", "吴小华", "朱莉", "马云龙", "胡建华",
    "郭瑞", "林静", "何建平", "高磊", "梁宇",
    "郑军", "罗秀英", "秦刚", "韩丽", "张建军",
    "梅丽", "杜伟", "许婷", "王婷", "冯丽",
    "陈伟", "董杰", "程玉", "曹刚", "康丽",
    "洪峰", "潘芳", "石建华", "朱敏", "冯娜",
    "马建平", "李建军", "陈秀英", "杨磊", "刘建华",
    "黄玉", "周伟", "吴建军", "朱秀兰", "马秀英",
    "胡秀兰", "郭刚", "林伟", "何秀英", "高婷",
    "梁建华", "郑玉", "罗军", "秦秀英", "韩建华",
    "张秀英", "梅建军", "杜秀英", "许秀兰", "王建军",
    "冯秀英", "陈建军", "董秀英", "程建华", "曹秀兰",
    "康建军", "洪秀英", "潘建华", "石秀兰", "朱建华",
    "冯玉", "马建华", "李秀兰", "陈建华", "杨秀英",
    "刘建华", "黄建华", "周建华", "吴秀兰", "朱建华",
    "马秀兰", "胡建华", "郭秀英", "林建华", "何秀兰",
    "高建华", "梁秀英", "郑建华", "罗建华", "秦建华",
    "韩秀英", "张建华", "梅秀英", "杜建华", "许建华",
    "王建华", "冯建华", "陈建华", "董建华", "程秀英",
    "曹建华", "康秀英", "洪建华", "潘秀英", "石建华"    
]

ch_ib = [
    "你是一朵绽放的花朵，散发着芬芳。",
    "生活就像一本未完成的书，等待我们填写精彩的篇章。",
    "勇气是穿越困境的风帆，让我们向前航行。",
    "爱是心灵的火焰，温暖我们的每一个瞬间。",
    "每一天都是我们成长的机会，塑造更好的自己。",
    "在星空中，你是那一颗璀璨的恒星，闪耀着希望之光。",
    "梦想是远方的灯塔，引领我们航行向着成功的海域。",
    "奋斗是通向辉煌的阶梯，一步一个脚印不断向前。",
    "希望是心灵的音乐，奏响着美好的生命旋律。",
    "友谊是一座坚实的桥梁，连接着我们的心与心。",
    "智慧如同明亮的星辰，照亮我们前行的黑暗之路。",
    "创造力是开启新世界的钥匙，点燃未知的奇迹。",
    "感恩是生活的甘露，滋润着每一片心灵的土壤。",
    "坚持是成功的基石，承受风雨后见彩虹的勇气。",
    "热情是生命的火花，点燃对生活的无限热爱。",
    "在困境中，我们发现内在的坚韧，战胜挑战。",
    "快乐是心灵的颜色，让生命变得绚烂多彩。",
    "冒险是生命的调味品，为旅途增添激情和神秘。",
    "理解是心与心的默契，建立深厚的情感纽带。",
    "希望如同清晨的曙光，驱散黑暗，照亮前路。",
    "信心是迈向成功的步伐，坚定不移地前行。",
    "善良是心灵的花朵，在世界上洒下美丽的馨香。",
    "拼搏是生命的旋律，奏响着奋斗的乐章。",
    "青春是梦想的驿站，等待我们迎接未来的风景。",
    "珍惜是心灵的镜子，映照出生命中真挚的美好。",
    "坚韧是战胜逆境的力量，铸就不可撼动的坚强。",
    "包容是心灵的海洋，容纳世界上各种美好和不完美。",
    "智慧是人生的导航仪，指引我们走向正确的方向。",
    "努力是成就梦想的钥匙，开启成功之门。",
    "思考是心灵的探险，发现无限可能性的旅程。",
    "顺流而下，如同船行大海，轻松面对人生波涛。",
    "宽容是心灵的庇护所，消除仇恨，培育爱的花园。",
    "阳光如同心灵的暖流，温暖寒冷的时光。",
    "创新是改变命运的魔法，塑造未来的奇迹。",
    "责任是生命的使命，肩负着创造美好的责任。",
    "勤奋如同沐浴清风，焕发身心的清新。",
    "成长是心智的花开，一点一滴汇聚成丰硕的果实。",
    "坚持是克服困难的法宝，铸就不可摧毁的力量。",
    "感悟是心灵的收获，提炼出生命中的智慧。",
    "梦幻如同星空的波光，勾勒出美好的未来。",
    "勇攀高峰，就像飞翔的鹰，迎接无限可能。",
    "忍耐是生命的耕耘，等待收获的季节。",
    "微笑如同阳光的温暖，融化生命中的阴霾。",
    "奉献是心灵的灯塔，引领我们前行的方向。",
    "坚强是人生的盾牌，抵御生命中的风雨。",
    "谦卑如同河流，滋润心田，流淌出宽容和宁静。",
    "刻苦是成功的伴侣，共同谱写辉煌的乐章。",
    "理想是人生的指南，指引我们航向美好的明天。",
    "拥抱是心灵的交响曲，奏响着真挚的情感。",
    "豁达是心灵的风景，欣赏生命中的美好。",
    "毅力如同跃过障碍的马匹，冲破困境。",
    "追求是生命的旅程，寻找前行的方向。",
    "独立是心灵的翅膀，飞翔向着理想的天空。",
    "守望是心灵的灯塔，照亮黑暗中的方向。",
    "静心如同湖水，映照出心灵的宁静和清澈。",
    "坚毅是登上成功巅峰的力量，战胜一切困难。",
    "感激是生活的旋律，奏响着对幸福的赞美。",
    "奇迹如同彩虹，跨越生命中的雨季，带来希望。",
    "胜利是努力的结晶，它让人生的旅途更加精彩。",
    "默契是心灵的默示录，让友情之花绽放。",
    "微风如同心灵的悠扬旋律，轻轻拂过生命。",
    "感性如同五彩斑斓的画笔，勾勒出生命的多彩。",
    "毅力是生命的引擎，推动我们前行的力量。",
    "阳光是心灵的抚慰，温暖生活中的寒冷。",
    "奋发如同劲舞的旋律，奏响成功的华丽交响曲。",
    "沉思如同夜空的繁星，闪烁出深邃的智慧。",
    "勇往直前，就像破浪前行的船只，穿越人生的风雨。",
    "悲欢离合如同生命的交响曲，奏响着丰富的人生。",
    "智者如同指南针，为我们指引通往成功的方向。",
    "奔跑是生命的节奏，追逐梦想的旋律。",
    "理解如同和弦的谐音，营造出和谐的人际关系。",
    "希冀是心灵的风筝，飞翔向着远方的蓝天。",
    "微笑如同生命的草原，绽放出青春的芳香。",
    "奉献是心灵的花朵，绽放出无尽的美丽。",
    "信任如同坚固的桥梁，连接着人与人的心。",
    "热爱是生命的润滑剂，使一切变得顺畅而美好。",
    "决心是征服困难的旗帜，高悬在成功的巅峰。",
    "谅解是心灵的春雨，滋润着人际关系的土壤。",
    "睿智如同明亮的月光，照亮我们前行的夜路。",
    "拼搏如同激流奔涌，冲刷出生命的坚韧。",
    "欢笑如同夏日的阳光，温暖着我们的心田。",
    "坚定如同橡树的根基，扎根在成功的土地上。",
    "虔诚如同清晨的祈祷，抚慰心灵的深处。",
    "感动如同美妙的音符，弹奏着真挚的情感。",
    "奋力如同翱翔的雄鹰，展翅向着成功的天空。",
    "平静如同湖面的宁静，反映出心灵的澄澈。",
    "青春如同绚烂的花朵，散发出生命的芬芳。",
    "责任如同河流的水流，滋润着生命的土壤。",
    "欣赏是心灵的画框，呈现出美好的风景。",
    "坚韧如同巍峨的山峰，屹立在成功的高峰。",
    "思考如同航行的指南针，引领我们走向明天。",
    "善良如同春日的微风，温暖着我们的心房。",
    "努力如同清晨的阳光，照亮前行的道路。",
    "成长如同绽放的花朵，展现出生命的美丽。",
    "坚持如同沙漠的风，吹拂着生命的韧性。",
    "感激是生命的礼物，点亮心灵的喜悦。",
    "奇迹如同春天的花蕾，孕育着无尽的可能。",
    "胜利如同骏马的奔腾，驰骋在成功的草原。",
    "默契如同交响乐团的合奏，奏响着和谐的旋律。",
    "微风如同心灵的拂面，轻轻吹散生活的疲惫。",
    "感性如同梦幻的彩虹，渲染出生命的多彩。",
    "毅力如同奔跑的马匹，冲破困境的藩篱。",
    "追求如同冉冉升起的朝阳，照亮生命的黑夜。",
    "独"    
]

rs = ["👍","🤩","🎉","🔥","❤️","🥰","🥱","🥴","🌚","🍌","💔","🤨","😐","🖕","😈","👎","😁","😢","💩","🤮","🤔","🤯","🤬","💯","😍","🕊","🐳","🤝","👨","🦄","🎃","🤓","👀","👻","🗿","🍾","🍓","⚡️","🏆","🤡","🌭","🆒","🙈","🎅","🎄","☃️","💊"]
rsa = ["👍", "🤩", "🎉", "🔥", "❤️", "🥰", "😁", "💯", "😍", "🕊", "🤝", "👨", "🦄", "🎃", "🤓", "👀", "🍾", "🍓", "⚡️", "🏆"]
rsb = ["🥱", "🥴", "🌚", "💔", "🤨", "😐", "🖕", "😈", "👎", "😢", "💩", "🤮", "🤔", "🤯", "🤬", "🐳", "🌭", "🙈", "🤡", "🍌"]