F='app/src/main/java/com/fuck/iab/MainModule.kt'
s=open(F,encoding='utf-8').read().replace('\r\n','\n')
s=s.replace('                hookOnServiceConnected(classLoader, bridge)','                hookOnServiceConnected(classLoader, bridge)\n                hookProxyBilling(classLoader)',1)
m='''    private fun hookProxyBilling(cl: ClassLoader) {
        try {
            val m = cl.loadClass("com.android.billingclient.api.ProxyBillingActivity").getDeclaredMethod("onCreate", Bundle::class.java)
            hook(m).intercept { c ->
                val a = c.thisObject as Activity
                try {
                    val r = a.getSharedPreferences(fuck_iab(), 0).getString("last", null)
                    if (r != null) {
                        val j = JSONObject(r)
                        val i = Intent()
                        i.putExtra(INAPP_PURCHASE_DATA(), j.getString("d"))
                        i.putExtra(INAPP_DATA_SIGNATURE(), j.getString("s"))
                        i.putExtra(RESPONSE_CODE(), 0)
                        a.setResult(Activity.RESULT_OK, i)
                        a.finish()
                        return@intercept
                    }
                } catch (e: Throwable) {}
                c.proceed()
            }
        } catch (e: Throwable) {}
    }

    private fun readScriptForPackage('''
s=s.replace('    private fun readScriptForPackage(',m,1)
open(F,'w',encoding='utf-8',newline='\n').write(s)
