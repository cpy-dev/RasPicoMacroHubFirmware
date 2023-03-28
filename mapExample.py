def customFunction():
  click(K.R, hold=K.WINDOWS)
  write('cmd')
  click(K.ENTER)

macroMap = (
    Action(macro11, lambda : [click(K.C, hold=K.CONTROL)]),

    Action(macro12, lambda : [click(K.V, hold=K.CONTROL)]),
    
    Action(macro13, lambda : [write('myUsername')]),
    
    Action(macro14, lambda : [write('superSecretPassword')]),
    
    Action(macro21, lambda : [customFunction()]),
    
    Action(macro22, lambda : []),
    
    Action(macro23, lambda : []),
    
    Action(macro24, lambda : []),
    
    Action(macro31, lambda : []),
    
    Action(macro32, lambda : []),
    
    Action(macro33, lambda : []),
    
    Action(macro34, lambda : [])
)

