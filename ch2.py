__all__ = ['ch2']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['MFWSTAT'])
@Js
def PyJs_anonymous_1_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['d', 'e'])
    pass
    if var.get('window').get('ActiveXObject'):
        #for JS loop
        var.put('d', Js(12.0))
        while (var.get('d')>Js(0.0)):
            try:
                try:
                    var.put('e', var.get('ActiveXObject').create((Js('ShockwaveFlash.ShockwaveFlash.')+var.get('d'))))
                    return (var.get('d')+Js('.0'))
                except PyJsException as PyJsTempException:
                    PyJsHolder_66_27504359 = var.own.get('f')
                    var.force_own_put('f', PyExceptionToJs(PyJsTempException))
                    try:
                        pass
                    finally:
                        if PyJsHolder_66_27504359 is not None:
                            var.own['f'] = PyJsHolder_66_27504359
                        else:
                            del var.own['f']
                        del PyJsHolder_66_27504359
            finally:
                    (var.put('d',Js(var.get('d').to_number())-Js(1))+Js(1))
    else:
        if (var.get('navigator').get('plugins') and var.get('navigator').get('plugins').get('length')):
            #for JS loop
            var.put('d', Js(0.0))
            while (var.get('d')<var.get('navigator').get('plugins').get('length')):
                try:
                    if (var.get('navigator').get('plugins').get(var.get('d')).get('name').callprop('indexOf', Js('Shockwave Flash'))!=(-Js(1.0))):
                        return var.get('navigator').get('plugins').get(var.get('d')).get('description').callprop('split', Js(' ')).get('2')
                finally:
                        (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    return Js('Not enabled')
PyJs_anonymous_1_._set_name('anonymous')
@Js
def PyJs_anonymous_2_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.put('a', var.get('document').get('URL'))
    return var.get('encodeURIComponent')(var.get('a'))
PyJs_anonymous_2_._set_name('anonymous')
@Js
def PyJs_anonymous_3_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'd', 'c'])
    var.put('b', Js(''))
    var.put('d', var.get('window').get('location').get('hostname'))
    var.put('c', var.get('d').callprop('replace', JsRegExp('/\\.(com|net|org|cn$)\\.?.*/'), Js('')))
    if (var.get('c').callprop('lastIndexOf', Js('.'))==(-Js(1.0))):
        var.put('b', (Js('.')+var.get('d')))
    else:
        var.put('c', var.get('c').callprop('substring', var.get('c').callprop('lastIndexOf', Js('.'))))
        var.put('b', var.get('d').callprop('substring', var.get('d').callprop('lastIndexOf', var.get('c'))))
    return var.get('b')
PyJs_anonymous_3_._set_name('anonymous')
@Js
def PyJs_anonymous_4_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return (var.get('NaN') if (Js(0.0)>var.get('a')) else ((Js(0.0)|(var.get('Math').callprop('random')*(Js(1.0)<<var.get('a')))) if (Js(30.0)>=var.get('a')) else (((Js(0.0)|(Js(1073741824.0)*var.get('Math').callprop('random')))+(Js(1073741824.0)*(Js(0.0)|(var.get('Math').callprop('random')*(Js(1.0)<<(var.get('a')-Js(30.0))))))) if (Js(53.0)>=var.get('a')) else var.get('NaN'))))
PyJs_anonymous_4_._set_name('anonymous')
@Js
def PyJs_anonymous_5_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a'])
    var.put('a', (-Js(1.0)))
    var.put('c', (-Js(1.0)))
    def PyJs_LONG_6_(var=var):
        return (PyJsComma(var.put('a', var.get('document').get('documentElement').get('clientWidth')),var.put('c', var.get('document').get('documentElement').get('clientHeight'))) if (var.get('document').get('documentElement') and (var.get('document').get('documentElement').get('clientWidth') or var.get('document').get('documentElement').get('clientHeight'))) else ((var.get('document').get('body') and (var.get('document').get('body').get('clientWidth') or var.get('document').get('body').get('clientHeight'))) and PyJsComma(var.put('a', var.get('document').get('body').get('clientWidth')),var.put('c', var.get('document').get('body').get('clientHeight')))))
    (PyJsComma(var.put('a', var.get('window').get('innerWidth')),var.put('c', var.get('window').get('innerHeight'))) if (Js('number')==var.get('window').get('innerWidth').typeof()) else PyJs_LONG_6_())
    return ((var.get('a')+Js('x'))+var.get('c'))
PyJs_anonymous_5_._set_name('anonymous')
@Js
def PyJs_anonymous_7_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return (((var.get('screen').get('width')+Js('x'))+var.get('screen').get('height')) if var.get('screen') else Js('-1x-1'))
PyJs_anonymous_7_._set_name('anonymous')
@Js
def PyJs_anonymous_8_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return (var.get('navigator').get('userLanguage') if var.get('navigator').get('userLanguage') else (var.get('navigator').get('language') if var.get('navigator').get('language') else (var.get('navigator').get('browserLanguage') if var.get('navigator').get('browserLanguage') else Js('unknown'))))
PyJs_anonymous_8_._set_name('anonymous')
@Js
def PyJs_anonymous_9_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    pass
    var.put('a', ((var.get('document').get('characterSet') or var.get('document').get('charset')) or Js('unknown')))
    return var.get('a')
PyJs_anonymous_9_._set_name('anonymous')
@Js
def PyJs_anonymous_10_(b, a, this, arguments, var=var):
    var = Scope({'b':b, 'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'a'])
    return PyJsStrictNeq(var.get('b').callprop('indexOf', var.get('a')),(-Js(1.0)))
PyJs_anonymous_10_._set_name('anonymous')
@Js
def PyJs_anonymous_11_(j, h, g, this, arguments, var=var):
    var = Scope({'j':j, 'h':h, 'g':g, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'i', 'g', 'j', 'h'])
    var.put('i', Js(''))
    var.put('e', var.get(u"this").callprop('_getDomain'))
    if var.get('g'):
        var.put('i', var.get('Date').create((var.get('Date').create().callprop('getTime')+(var.get('g')*Js(3600000.0)))))
        var.put('i', (Js('; expires=')+var.get('i').callprop('toGMTString')))
    var.get('document').put('cookie', ((((((var.get('j')+Js('='))+var.get('encodeURIComponent')(var.get('h')))+var.get('i'))+Js(';domain='))+var.get('e'))+Js(';path=/; ')))
PyJs_anonymous_11_._set_name('anonymous')
@Js
def PyJs_anonymous_12_(f, this, arguments, var=var):
    var = Scope({'f':f, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'g', 'd', 'h', 'f'])
    var.put('h', Js(''))
    var.put('d', (var.get('f')+Js('=')))
    if (var.get('document').get('cookie').get('length')>Js(0.0)):
        var.put('g', var.get('document').get('cookie').callprop('indexOf', var.get('d')))
        if (var.get('g')!=(-Js(1.0))):
            var.put('g', var.get('d').get('length'), '+')
            var.put('e', var.get('document').get('cookie').callprop('indexOf', Js(';'), var.get('g')))
            if (var.get('e')==(-Js(1.0))):
                var.put('e', var.get('document').get('cookie').get('length'))
            var.put('h', var.get('decodeURIComponent')(var.get('document').get('cookie').callprop('substring', var.get('g'), var.get('e'))))
    return var.get('h')
PyJs_anonymous_12_._set_name('anonymous')
@Js
def PyJs_anonymous_13_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.put('a', var.get(u"this").callprop('_getCookie', Js('__mfwvn')))
    if var.get('isNaN')(var.get('a')):
        var.put('a', Js(0.0))
    return var.get('a')
PyJs_anonymous_13_._set_name('anonymous')
@Js
def PyJs_anonymous_14_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'c', 'a'])
    var.put('a', var.get(u"this").callprop('_getCookie', Js('__mfwlt')))
    var.put('b', var.get('parseInt')(((+var.get('Date').create())/Js(1000.0)), Js(10.0)))
    if var.get('isNaN')(var.get('a')):
        var.put('a', Js(0.0))
    var.put('c', var.get('parseInt')((var.get('b')-var.get('a'))))
    var.get(u"this").callprop('_setCookie', Js('__mfwlt'), var.get('b'), (Js(24.0)*Js(365.0)))
    return var.get('c')
PyJs_anonymous_14_._set_name('anonymous')
@Js
def PyJs_anonymous_15_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'a'])
    var.put('b', var.get(u"this").callprop('_getCookie', Js('__mfwlv')))
    var.put('a', var.get(u"this").callprop('_getVisitn'))
    if var.get('isNaN')(var.get('b')):
        var.put('b', Js(0.0))
    if ((((+var.get('Date').create())/Js(1000.0))-var.get('b'))>Js(7200.0)):
        var.put('b', var.get('parseInt')(((+var.get('Date').create())/Js(1000.0)), Js(10.0)))
        (var.put('a',Js(var.get('a').to_number())+Js(1))-Js(1))
        var.get(u"this").callprop('_setCookie', Js('__mfwlv'), var.get('b'), (Js(24.0)*Js(365.0)))
        var.get(u"this").callprop('_setCookie', Js('__mfwvn'), var.get('a'), (Js(24.0)*Js(365.0)))
    return var.get('b')
PyJs_anonymous_15_._set_name('anonymous')
@Js
def PyJs_anonymous_16_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'c', 'a'])
    if var.get('mfwSendLog').callprop('checkEnviroment'):
        return Js(False)
    var.put('c', var.get(u"this").callprop('_getParams'))
    var.put('a', (var.get('window').get('Env').get('TONGJI_HOST') if var.get('window').get('Env').get('TONGJI_HOST') else Js('tongji.mafengwo.cn')))
    var.put('b', (((Js('https://') if (Js('https:')==var.get('document').get('location').get('protocol')) else Js('http://'))+var.get('a'))+Js('/stat_click.gif')))
    var.get('mfwSendLog').callprop('init', var.get('b'), var.get('c'))
PyJs_anonymous_16_._set_name('anonymous')
@Js
def PyJs_anonymous_17_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return var.get('mfwCommonEnv').callprop('getCliInfo')
PyJs_anonymous_17_._set_name('anonymous')
@Js
def PyJs_anonymous_18_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['k', 'w', 'n', 'h', 'a', 'e', 'i', 'r', 'p', 'g', 'o', 'x', 'q', 'c', 'u', 's', 'b', 'v', 'j', 'm', 'f'])
    var.put('p', var.get('document'))
    var.put('k', var.get('window').get('location'))
    var.put('g', var.get('parseInt')(((+var.get('Date').create())/Js(1000.0)), Js(10.0)))
    var.put('w', Js('1.2'))
    var.put('n', (var.get('encodeURIComponent')(var.get('k').get('host')) or Js('-')))
    var.put('f', (var.get('encodeURIComponent')(var.get('p').get('referrer')) or Js('direct')))
    var.put('r', var.get('encodeURIComponent')(var.get('p').get('title')))
    var.put('o', var.get(u"this").callprop('_getWindowSize'))
    var.put('m', var.get(u"this").callprop('_getScreenSize'))
    var.put('j', var.get(u"this").callprop('_getSystemLang'))
    var.put('i', var.get(u"this").callprop('_getRandomInt', Js(32.0)))
    var.put('x', (var.get(u"this").callprop('_getCururl') or Js('-')))
    var.put('b', var.get(u"this").callprop('_getFlash'))
    var.put('u', var.get(u"this").callprop('_getVisitlv'))
    var.put('h', (var.get(u"this").callprop('_getVisitn') or Js('1')))
    var.put('s', var.get(u"this").callprop('_getChartset'))
    var.put('e', (var.get(u"this").callprop('_getTimeOnPage') or Js('0')))
    var.put('a', var.get(u"this").callprop('_getCliInfo'))
    var.put('c', var.get('window').get('Env').get('uPageId'))
    var.put('v', (var.get('window').get('Env').get('salesId') or Js('0')))
    PyJs_Object_19_ = Js({'t':var.get('g'),'hn':var.get('n'),'u':var.get('x'),'r':var.get('f'),'lv':var.get('u'),'vn':var.get('h'),'ws':var.get('o'),'sc':var.get('m'),'sl':var.get('j'),'fl':var.get('b'),'cs':var.get('s'),'dt':var.get('r'),'sts':var.get('e'),'pid':var.get('c'),'brn':var.get('a').get('brn'),'brv':var.get('a').get('brv'),'dev':var.get('a').get('dev'),'os':var.get('a').get('os_name'),'os_ver':var.get('a').get('os_ver'),'sid':var.get('v'),'ver':var.get('w'),'rdm':var.get('i')})
    var.put('q', PyJs_Object_19_)
    return var.get('q')
PyJs_anonymous_18_._set_name('anonymous')
PyJs_Object_0_ = Js({'_getFlash':PyJs_anonymous_1_,'_getCururl':PyJs_anonymous_2_,'_getDomain':PyJs_anonymous_3_,'_getRandomInt':PyJs_anonymous_4_,'_getWindowSize':PyJs_anonymous_5_,'_getScreenSize':PyJs_anonymous_7_,'_getSystemLang':PyJs_anonymous_8_,'_getChartset':PyJs_anonymous_9_,'_includes':PyJs_anonymous_10_,'_setCookie':PyJs_anonymous_11_,'_getCookie':PyJs_anonymous_12_,'_getVisitn':PyJs_anonymous_13_,'_getTimeOnPage':PyJs_anonymous_14_,'_getVisitlv':PyJs_anonymous_15_,'_run':PyJs_anonymous_16_,'_getCliInfo':PyJs_anonymous_17_,'getParams':PyJs_anonymous_18_})
var.put('MFWSTAT', PyJs_Object_0_)
pass


# Add lib to the module scope
ch2 = var.to_python()