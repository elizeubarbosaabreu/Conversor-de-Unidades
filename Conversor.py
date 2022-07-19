class Conversor:
    
    def __init__(self, valorInicial):
        self.valorInicial = 0
        self.unidades = ['mm','cm', 'dm', 'm', 'dam', 'hm', 'km', # Comprimento
                    '--', 'mg', 'cg', 'dg', 'g', 'dag', 'hg', 'kg', # Massa
                         ]
    def conversor(self, unidade, valorInicial):
        self.unidade = unidade
        self.valorInicial = valorInicial
        
        if unidade in ('' or '--'):
            return 'Unidade ainda não cadastrada'
        
# mm para outros
        if unidade == 'mm':
            msg = f'''{valorInicial/10} cm
{valorInicial/100} dm
{valorInicial/1000} m
{valorInicial/10000} dam
{valorInicial/100000} hm
{valorInicial/1000000} km
'''
            
# cm para outros
        if unidade == 'cm':
            msg = f'''{valorInicial*10} mm
{valorInicial/10} dm
{valorInicial/100} m
{valorInicial/1000} dam
{valorInicial/10000} hm
{valorInicial/100000} km
'''
            
# dm para outros
        if unidade == 'dm':
            msg = f'''{valorInicial*100} mm
{valorInicial*10} cm
{valorInicial/10} m
{valorInicial/100} dam
{valorInicial/1000} hm
{valorInicial/10000} km
'''
# m para outros
        if unidade == 'm':
            msg = f'''{valorInicial*1000} mm
{valorInicial*100} cm
{valorInicial*10} dm
{valorInicial/10} dam
{valorInicial/100} hm
{valorInicial/1000} km
'''
# dam para outros
        if unidade == 'dam':
            msg = f'''{valorInicial*10000} mm
{valorInicial*1000} cm
{valorInicial*100} dm
{valorInicial*10} m
{valorInicial/10} hm
{valorInicial/100} km
'''
            
# hm para outros
        if unidade == 'hm':
            msg = f'''{valorInicial*100000} mm
{valorInicial*10000} cm
{valorInicial*1000} dm
{valorInicial*100} m
{valorInicial*10} dam
{valorInicial/10} km
'''
            
# km para outros
        if unidade == 'km':
            msg = f'''{valorInicial*1000000} mm
{valorInicial*100000} cm
{valorInicial*10000} dm
{valorInicial*1000} m
{valorInicial*100} dam
{valorInicial*10} hm
'''

# mg para outros
        if unidade == 'mg':
            msg = f'''{valorInicial/10} cg
{valorInicial/100} dg
{valorInicial/1000} g
{valorInicial/10000} dag
{valorInicial/100000} hg
{valorInicial/1000000} kg
'''
            
# cg para outros
        if unidade == 'cg':
            msg = f'''{valorInicial*10} mg
{valorInicial/10} dg
{valorInicial/100} g
{valorInicial/1000} dag
{valorInicial/10000} hg
{valorInicial/100000} kg
'''
            
# dg para outros
        if unidade == 'dg':
            msg = f'''{valorInicial*100} mg
{valorInicial*10} cg
{valorInicial/10} g
{valorInicial/100} dag
{valorInicial/1000} hg
{valorInicial/10000} kg
'''
# g para outros
        if unidade == 'g':
            msg = f'''{valorInicial*1000} mg
{valorInicial*100} cg
{valorInicial*10} dg
{valorInicial/10} dag
{valorInicial/100} hg
{valorInicial/1000} kg
'''
# dag para outros
        if unidade == 'dag':
            msg = f'''{valorInicial*10000} mg
{valorInicial*1000} cg
{valorInicial*100} dg
{valorInicial*10} g
{valorInicial/10} hm
{valorInicial/100} kg
'''
            
# hg para outros
        if unidade == 'hg':
            msg = f'''{valorInicial*100000} mg
{valorInicial*10000} cg
{valorInicial*1000} dg
{valorInicial*100} g
{valorInicial*10} dag
{valorInicial/10} kg
'''
            
# kg para outros
        if unidade == 'kg':
            msg = f'''{valorInicial*1000000} mg
{valorInicial*100000} cg
{valorInicial*10000} dg
{valorInicial*1000} g
{valorInicial*100} dag
{valorInicial*10} hg
'''    
            
        return(msg)    
    
        
if __name__ == "__main__" :
    ## usado para testes
    calculo = Conversor(0)
    print(calculo.conversor('kg', 1))
    unidades = (calculo.unidades)
