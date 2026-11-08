import re
g=open('app/build.gradle').read()
g=re.sub(r'\n    (externalNativeBuild|splits) \{.*?\n    \}\n','\n',g,flags=re.S)
g=re.sub(r'\n    ndkVersion = "[^"]*"\n','\n',g)
open('app/build.gradle','w').write(g)
F='app/src/main/java/com/fuck/iab/FakeBinder.kt'
s=open(F,encoding='utf-8').read().replace('\r\n','\n')
s=s.replace('                3, 8 -> {','                3, 7, 8 -> {',1)
s=re.sub(r'                7 -> \{.*?\n                \}\n\n                9, 902 ->','                9, 902 ->',s,count=1,flags=re.S)
s=s.replace('flags: Int): Boolean {','flags: Int): Boolean {\n        android.util.Log.e("FKIAB","tx code="+code)',1)
o='prefs.edit(commit = true) { putString(purchaseToken, prefsData.toString()) }'
n='prefs.edit(commit = true) { putString(purchaseToken, prefsData.toString()); putString("last", JSONObject().apply { put("d", dataString); put("s", signature) }.toString()) }'
s=s.replace(o,n)
open(F,'w',encoding='utf-8',newline='\n').write(s)
