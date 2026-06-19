# inputt = """THE FIRE BURNED STEADY AS KARO THE EL
# Ƨ'ꓷ⅃ЯOW ƎHT ИƎHW ,OӘA ӘИO⅃ .ƎꓘOᑫƧ ЯƎꓷ
#  BONES WERE STILL SOFT AND THE SKIES 
# AMYꓘƧ ƎHT ƎЯƎW ƎЯƎHT ,MЯOTƧ HTIW ꓷ⅃IW
# KERS. VAST BIRDS, BROAD OF WING, CIRC
# T⅃IUꓭ YƎHT ƎЯƎHW ƧꟻꟻI⅃Ɔ HӘIH ƎHT ӘИI⅃
#  THEIR NESTS. A BOY, WHOSE NAME HAS B
# ƧꓷЯIꓭ ƎƧƎHT ꓷƎHƆTAW ,ƎMIT OT TƧO⅃ ИƎƎ
#  OFTEN. HE LONGED TO FLY AS THEY DID,
# ƎƎꟻ ƧIH ꓷИUOꓭ ӘИI⅃⅃Aꟻ ꟻO ЯAƎꟻ HӘUOHT 
# T TO THE STONE. ONE DAY, A NEST SLIPP
# T ӘИI⅃ꓭMUT ,ꟻꟻI⅃Ɔ TƧƎ⅃⅃AT ƎHT MOЯꟻ ꓷƎ
# OWARD RUIN. THE BOY RAN, SWIFT AND UN
#  .ƧMЯA ƧIH ИI TI THӘUAƆ ꓷИA ,ӘИIꓘИIHT
# THE SKYMAKERS REJOICED ABOVE HIM, VOI
# ЯƎVIЯ ꓷИA ꓷИIW-MЯOTƧ ƎꓘI⅃ ӘИIӘИIЯ ƧƎƆ
# . THEY LIFTED HIM UP, SAFE IN THEIR E
# UO⅃Ɔ ƎHT OTИI MIH ꓷƎIЯЯAƆ ꓷИA ,ƎƆAЯꓭM
# DS. HE RETURNED AT LAST, THE GROUND B
# ꓘƧ ƎHT TUꓭ ,ƎMAƧ ƎHT ⅃⅃ITƧ MIH HTAƎИƎ
# Y FOREVER CARRIED IN HIS HEART. AND S
#  HTЯAƎ ƎHT - ЯƎꓭMƎMƎЯ ƎW ,ИƎЯꓷ⅃IHƆ ,O
# BELONGS TO ALL WHO WALK IT, BUT THE S
# .HƆAƎЯ OT ƧƎЯAꓷ OHW ƎИO ƎHT ƧЯOVAꟻ Yꓘ"""

inputt='''THE FIRE BURNED STEADY AS KARO THE EL
Ƨ'ꓷ⅃ЯOW ƎHT ИƎHW ,OӘA ӘИO⅃ .ƎꓘOᑫƧ ЯƎꓷ
 BONES WERE STILL SOFT AND THE SKIES 
AMYꓘƧ ƎHT ƎЯƎW ƎЯƎHT ,MЯOTƧ HTIW ꓷ⅃IW
KERS. VAST BIRDS, BROAD OF WING, CIRC
T⅃IUꓭ YƎHT ƎЯƎHW ƧꟻꟻI⅃Ɔ HӘIH ƎHT ӘИI⅃
 THEIR NESTS. A BOY, WHOSE NAME HAS B
ƧꓷЯIꓭ ƎƧƎHT ꓷƎHƆTAW ,ƎMIT OT TƧO⅃ ИƎƎ
 OFTEN. HE LONGED TO FLY AS THEY DID,
ƎƎꟻ ƧIH ꓷИUOꓭ ӘИI⅃⅃Aꟻ ꟻO ЯAƎꟻ HӘUOHT 
T TO THE STONE. ONE DAY, A NEST SLIPP
T ӘИI⅃ꓭMUT ,ꟻꟻI⅃Ɔ TƧƎ⅃⅃AT ƎHT MOЯꟻ ꓷƎ
OWARD RUIN. THE BOY RAN, SWIFT AND UN
 .ƧMЯA ƧIH ИI TI THӘUAƆ ꓷИA ,ӘИIꓘИIHT
THE SKYMAKERS REJOICED ABOVE HIM, VOI
ЯƎVIЯ ꓷИA ꓷИIW-MЯOTƧ ƎꓘI⅃ ӘИIӘИIЯ ƧƎƆ
. THEY LIFTED HIM UP, SAFE IN THEIR E
UO⅃Ɔ ƎHT OTИI MIH ꓷƎIЯЯAƆ ꓷИA ,ƎƆAЯꓭM
DS. HE RETURNED AT LAST, THE GROUND B
ꓘƧ ƎHT TUꓭ ,ƎMAƧ ƎHT ⅃⅃ITƧ MIH HTAƎИƎ
Y FOREVER CARRIED IN HIS HEART. AND S
 HTЯAƎ ƎHT - ЯƎꓭMƎMƎЯ ƎW ,ИƎЯꓷ⅃IHƆ ,O
BELONGS TO ALL WHO WALK IT, BUT THE S
.HƆAƎЯ OT ƧƎЯAꓷ OHW ƎИO ƎHT ƧЯOVAꟻ Yꓘ'''


def cipherr(stri, keystri):
    print(stri)
    res = ''.join([keystri.get(i, i) for i in stri if i not in "-.',."])
    # res=''.join([keystri.get(i, i) for i in stri if i!=','])
    print(res)
    return res


alphabetcor = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabetrev = 'AꓭƆꓷƎꟻӘHIႱꓘ⅃MИOᑫϘЯƧTUVWXYऽ'
w = dict(zip(alphabetrev, alphabetcor))

inputt = inputt.split('\n')

c = 1
cor = []

for i in inputt:
    if c % 2 == 0:
        cor.append(cipherr(i, w)[::-1])
    # else:
    #     cor.append(''.join([j for j in i if j not in "-.',."]))
    else:
        cor.append(cipherr(i,dict(zip(alphabetcor, alphabetcor))))
    c += 1
correctinput = ''.join(cor)
print(correctinput)

# print(',' == ',')
word=[]
for i in correctinput.split(' '):
    if len(i)==5 and i not in word:
        word.append(i)
print(sorted(word)[19])
print(sorted(word))
