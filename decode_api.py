__all__ = ['ch']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['mxPageGuid'])
@Js
def PyJsHoisted_mxPageGuid_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    pass
PyJsHoisted_mxPageGuid_.func_name = 'mxPageGuid'
var.put('mxPageGuid', PyJsHoisted_mxPageGuid_)
pass
@Js
def PyJs_anonymous_0_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a'])
    var.put('a', var.get('mxPageGuid').get('_getRandomInt'))
    var.put('c', var.get('mxPageGuid').get('_hexAligner'))
    return ((((((((var.get('c')(var.get('a')(Js(32.0)), Js(8.0))+Js('-'))+var.get('c')(var.get('a')(Js(16.0)), Js(4.0)))+Js('-'))+var.get('c')((Js(16384.0)|var.get('a')(Js(12.0))), Js(4.0)))+Js('-'))+var.get('c')((Js(32768.0)|var.get('a')(Js(14.0))), Js(4.0)))+Js('-'))+var.get('c')(var.get('a')(Js(48.0)), Js(12.0)))
PyJs_anonymous_0_._set_name('anonymous')
var.get('mxPageGuid').put('generate', PyJs_anonymous_0_)
@Js
def PyJs_anonymous_1_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return (var.get('NaN') if (Js(0.0)>var.get('a')) else ((Js(0.0)|(var.get('Math').callprop('random')*(Js(1.0)<<var.get('a')))) if (Js(30.0)>=var.get('a')) else (((Js(0.0)|(Js(1073741824.0)*var.get('Math').callprop('random')))+(Js(1073741824.0)*(Js(0.0)|(var.get('Math').callprop('random')*(Js(1.0)<<(var.get('a')-Js(30.0))))))) if (Js(53.0)>=var.get('a')) else var.get('NaN'))))
PyJs_anonymous_1_._set_name('anonymous')
var.get('mxPageGuid').put('_getRandomInt', PyJs_anonymous_1_)
@Js
def PyJs_anonymous_2_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    @Js
    def PyJs_anonymous_3_(c, b, this, arguments, var=var):
        var = Scope({'c':c, 'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['c', 'b', 'd', 'e', 'f'])
        #for JS loop
        var.put('d', var.get('c').callprop('toString', var.get('a')))
        var.put('e', (var.get('b')-var.get('d').get('length')))
        var.put('f', Js('0'))
        while (Js(0.0)<var.get('e')):
            try:
                ((var.get('e')&Js(1.0)) and var.put('d', (var.get('f')+var.get('d'))))
            finally:
                    PyJsComma(var.put('e', Js(1.0), '>>>'),var.put('f', var.get('f'), '+'))
        return var.get('d')
    PyJs_anonymous_3_._set_name('anonymous')
    return PyJs_anonymous_3_
PyJs_anonymous_2_._set_name('anonymous')
var.get('mxPageGuid').put('_getIntAligner', PyJs_anonymous_2_)
pass


# Add lib to the module scope
ch = var.to_python()