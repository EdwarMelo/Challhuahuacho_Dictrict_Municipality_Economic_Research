
# =============================================================================
# =============================================================================
# ESTUDIO DE MERCADO Y ECONÓMICO DE BIENES Y SERVICIOS DE LA MUNICIPALIDAD
# DISTRITAL DE CHALLHUAHUACHO
# =============================================================================
# Elaborado por:
    # Edwar Melo Huallpartupa
# Objetivo:
    # Limpieza de Data y Asignacion de Indicadores
# =============================================================================

# 1. Importacion de modulos
import os 
import pandas as pd

# 2. Seteamos nuestro directorio de trabajo
os.chdir("/media/edwar/Archivos/ESTUDIO_CHALHUAHUACHO/Limpieza_Data")

# 3. Cargamos los datos que se encuentran en el siguiente archivo Excel:
    # "REPORTE DETALLADO 2020 Procesado.xlsx" (*Data elaborada por el Econ. Yelsin Felio Ferro Surco*)
# Especificamente la hoja 2 (En Excel), pero para Python seria 1 ya que su 
# numeracion inicia en 0
data = pd.read_excel('REPORTE DETALLADO 2020 Procesado.xlsx', sheet_name=1)
# Revisamos la data
# data.columns
# data.dtypes
# data.shape

# 4. Revisamos los valores unicos de la variable "Producto", ya que esa es
# nuestra variable de interes
# data.Producto.unique()
# data.Producto.unique().shape

# 5. Considerando que nuestro estudio se basa en aquellos productos que
# mostraron una diferencia considerable en sus precios, entonces ahora nos 
# enfocamos en esos productos y para saber cuales fueron consideraremos la
# variable "Diferencia_Px"
# Para esto seleccionaremos todos aquellos productos donde la varible 
# "Diferencia_Px" sea distinta a cero
# data[data.Diferencia_Px != 0]
# Esta data seleccionada la llamaremos "datdif"
datdif = data[data.Diferencia_Px != 0]
# Revisamos los valores unicos de la variable "Producto" de la data seleccionada
# datdif.Producto.unique()
# datdif.Producto.unique().shape
# Nos damos cuenta que el numero de valores unicos es mucho menor que en el 
# anterior caso.
# Para poder ver mejor esta data la llamaremos "prod_unicos_datdif"
prod_unicos_datdif = pd.Series(datdif.Producto.unique())
# Revisando "prod_unicos_datdif" nos podemos dar cuenta que algunos valores 
# unicos tienen errores de ortografia, y si estos errores se podrian corregir
# entonces la cantidad de valores unicos de la variable "Producto" disminuiria.

# 6. Para disminuir los valores unicos de la variable "Producto" de la data
# "prod_unicos_datdif" se tuvo hacer el trabajo de buscar esos errores y
# enlistarlos para luego reemplazarlos por el valor correcto en la data "datdif".
# Esta busqueda se puede hacer a en el mismo IDE de Spyder o exportandolo a 
# Excel de la siguiente manera:
# prod_unicos_datdif.to_excel('Unicos.xlsx') # OPCIONAL

# 7. Mientras se hace la busqueda de valores repetidos o con errores ortograficos
# en la data "prod_unicos_datdif", podemos estar reemplazando dicha informacion
# en la data "datdif" para generalizar.
# A continuacion realizaremos toda ese proceso
# 
abrazadera = ['ABARZADERA', 'ABRASADERA', 'ABRASADERAS', 'ABRAZADERA', 
              'ABRAZADERAS', 'ABRAZADORA', 'A-ABRAZADERA']
for i in datdif.Producto:
    datdif.Producto.replace(abrazadera, 'ABRAZADERA', inplace = True)
# 
escritorio = ['01 ESCRITORIO', 'ESCRITORIO','ESCRITORIOS']
for i in datdif.Producto:
    datdif.Producto.replace(escritorio, 'ESCRITORIO', inplace = True)
# 
juego = ['01 JUEGO', '06 JUEGOS','1 JUEGO','JUEGO','JUEGOS','UN JUEGO']
for i in datdif.Producto:
    datdif.Producto.replace(juego, 'JUEGO', inplace = True)
# 
mesa = ['01 MESA', 'MESA','MESA-COCHE','MESAS','UNA MESA']
for i in datdif.Producto:
    datdif.Producto.replace(mesa, 'MESA', inplace = True)
# 
mueble = ['01 MUEBLES', 'MUEBLE','MUEBLES','UN MUEBLE-ESTANTE']
for i in datdif.Producto:
    datdif.Producto.replace(mueble, 'MUEBLE', inplace = True)
# 
pack = ['01 PACK', 'PACK']
for i in datdif.Producto:
    datdif.Producto.replace(pack, 'PACK', inplace = True)
# 
modulo = ['02 MODULOS', 'MODULO']
for i in datdif.Producto:
    datdif.Producto.replace(modulo, 'MODULO', inplace = True)
# 
chinguillos = ['03 CHINGUILLOS', 'CHINGUILLOS']
for i in datdif.Producto:
    datdif.Producto.replace(chinguillos, 'CHINGUILLOS', inplace = True)
# 
tubo = ['04 TUBO', 'TUBO','TUBO:','TUBOFLEX','TUBOS']
for i in datdif.Producto:
    datdif.Producto.replace(tubo, 'TUBO', inplace = True)
# 
chicotes = ['05 CHICOTES','CHICOTE','CHICOTES','CHICOTES,']
for i in datdif.Producto:
    datdif.Producto.replace(chicotes, 'CHICOTES', inplace = True)
# 
galon = ['1 GALON','GALON','GALONERA','GALONERAS','GALONES','UN GALON']
for i in datdif.Producto:
    datdif.Producto.replace(galon, 'GALON', inplace = True)
# 
kilo = ['10 KILOS']
for i in datdif.Producto:
    datdif.Producto.replace(kilo, 'KILO', inplace = True)
# 
plancha = ['10 PLANCHAS','PLANCHA','PLANCHAS','PLANCHAS(CARTELAS)']
for i in datdif.Producto:
    datdif.Producto.replace(plancha, 'PLANCHA', inplace = True)
# 
metros = ['100 METROS','50 METROS','METRO','METROS']
for i in datdif.Producto:
    datdif.Producto.replace(metros, 'METROS', inplace = True)
# 
canaleta = ['50X CANALETA','CANALETA','CANALETAS']
for i in datdif.Producto:
    datdif.Producto.replace(canaleta, 'CANALETA', inplace = True)
# 
bidon = ['A-BIDON','BIDON','BIDONES','UN BIDON']
for i in datdif.Producto:
    datdif.Producto.replace(bidon, 'BIDON', inplace = True)
# 
llave = ['A-LLAVE','LLAVE','LLAVES','MAT-1LLAVE']
for i in datdif.Producto:
    datdif.Producto.replace(llave, 'LLAVE', inplace = True)
# 
llavero = ['LLAVERO','LLAVEROS','PORTALLAVEROS']
for i in datdif.Producto:
    datdif.Producto.replace(llavero, 'LLAVERO', inplace = True)
# 
niple = ['A-NIPLES','NIPLE','NIPLES']
for i in datdif.Producto:
    datdif.Producto.replace(niple, 'NIPLE', inplace = True)
# 
accesorios = ['ACCESORIO', 'ACCESORIOS']
for i in datdif.Producto:
    datdif.Producto.replace(accesorios, 'ACCESORIOS', inplace = True)
# 
detergente = ['ACE MARCELLA', 'DETEREGENTE','DETERGENTE','DETRGENTE']
for i in datdif.Producto:
    datdif.Producto.replace(detergente, 'DETERGENTE', inplace = True)
# 
acero = ['ACERO', 'ACEROCORRUGADO']
for i in datdif.Producto:
    datdif.Producto.replace(acero, 'ACERO', inplace = True)
# 
aceite = ['ACEITE', 'ACIETE','ACITE']
for i in datdif.Producto:
    datdif.Producto.replace(aceite, 'ACEITE', inplace = True)
# 
adaptador = ['ADAPATADOR', 'ADAPTADOR','ADAPTADORES','ADPATADOR','ADPTADORES',
             'PR ADAPTADOR']
for i in datdif.Producto:
    datdif.Producto.replace(adaptador, 'ADAPTADOR', inplace = True)
# 
adherente = ['ADHERENTE', 'ADHERENTE,','ADHERENTE,COADYUVANTE']
for i in datdif.Producto:
    datdif.Producto.replace(adherente, 'ADHERENTE', inplace = True)
# 
adhesivo = ['ADHESIVO', 'ADHESIVOS']
for i in datdif.Producto:
    datdif.Producto.replace(adhesivo, 'ADHESIVO', inplace = True)
# 
aditivo = ['ADITIVO', 'ADITIVO-IMPERMEABILIZANTE,PARA']
for i in datdif.Producto:
    datdif.Producto.replace(aditivo, 'ADITIVO', inplace = True)
# 
adquisicion = ['ADQ .TECNOPOR', 'ADQ.','ADQ.TROMPO','ADQUISCION','ADQUISICICON',
               'ADQUISICION','ADQUISICIÓN','ADQUISICION,','ADQUISICION,INSTALACION',
               'ADQUISICION,MONTAJE','ADQUISIOCION','ADQUISION','ADQUISION,',
               'ADQUSICION']
for i in datdif.Producto:
    datdif.Producto.replace(adquisicion, 'ADQUISICION', inplace = True)
# 
afiche = ['AFICHE', 'AFICHES']
for i in datdif.Producto:
    datdif.Producto.replace(afiche, 'AFICHE', inplace = True)
# 
agenda = ['AGENDA', 'AGENDAS']
for i in datdif.Producto:
    datdif.Producto.replace(agenda, 'AGENDA', inplace = True)
# 
agua = ['AGUA', 'AGUAS']
for i in datdif.Producto:
    datdif.Producto.replace(agua, 'AGUA', inplace = True)
# 
aguja = ['AGUJA', 'AGUJAS']
for i in datdif.Producto:
    datdif.Producto.replace(aguja, 'AGUJA', inplace = True)
# 
alcoholimetro = ['ALCOHOLIMETRO', 'ALCOHOLÍMETRO']
for i in datdif.Producto:
    datdif.Producto.replace(alcoholimetro, 'ALCOHOLIMETRO', inplace = True)
# 
aldaba = ['ALDABA', 'ALDABAS']
for i in datdif.Producto:
    datdif.Producto.replace(aldaba, 'ALDABA', inplace = True)
# 
algodon = ['ALGODON', 'ALGODÓN']
for i in datdif.Producto:
    datdif.Producto.replace(algodon, 'ALGODON', inplace = True)
# 
alicate = ['ALICATE', 'ALICATES']
for i in datdif.Producto:
    datdif.Producto.replace(alicate, 'ALICATE', inplace = True)
# 
alimentos = ['ALIMENTO', 'ALIMENTOS']
for i in datdif.Producto:
    datdif.Producto.replace(alimentos, 'ALIMENTOS', inplace = True)
# 
alambre = ['ALAMBRE', 'ALMBRE']
for i in datdif.Producto:
    datdif.Producto.replace(alambre, 'ALAMBRE', inplace = True)
# 
anaquel = ['ANAQUEL', 'ANAQUELES']
for i in datdif.Producto:
    datdif.Producto.replace(anaquel, 'ANAQUEL', inplace = True)
# 
andamio = ['ANDAMIO', 'ANDAMIOS']
for i in datdif.Producto:
    datdif.Producto.replace(andamio, 'ANDAMIO', inplace = True)
# 
anillo = ['ANILLO', 'ANILLOS']
for i in datdif.Producto:
    datdif.Producto.replace(anillo, 'ANILLO', inplace = True)
# 
antiparasitario = ['ANTIPARASITARIO']
for i in datdif.Producto:
    datdif.Producto.replace(antiparasitario, 'ANTIPARASITARIO', inplace = True)
# 
aposito = ['APOSITO', 'APOSITOS']
for i in datdif.Producto:
    datdif.Producto.replace(aposito, 'APOSITO', inplace = True)
# 
archivador = ['ARCHIVADOR', 'ARCHIVADORES','ARCHIVERO']
for i in datdif.Producto:
    datdif.Producto.replace(archivador, 'ARCHIVADOR', inplace = True)
# 
arco = ['ARCO', 'ARCOS']
for i in datdif.Producto:
    datdif.Producto.replace(arco, 'ARCO', inplace = True)
# 
arpillera = ['ARPELLIRA', 'ARPILLERA']
for i in datdif.Producto:
    datdif.Producto.replace(arpillera, 'ARPILLERA', inplace = True)
# 
arveja = ['ARVEJA', 'ARVEJITAS']
for i in datdif.Producto:
    datdif.Producto.replace(arveja, 'ARVEJA', inplace = True)
# 
asfalto = ['ASFALTO', 'ASFALTICAS']
for i in datdif.Producto:
    datdif.Producto.replace(asfalto, 'ASFALTO', inplace = True)
# 
aspersor = ['ASPERSOR', 'ASPERSORES']
for i in datdif.Producto:
    datdif.Producto.replace(aspersor, 'ASPERSOR', inplace = True)
# 
autoperforante = ['AUTOPERFORANTE', 'AUTOPERFORANTES']
for i in datdif.Producto:
    datdif.Producto.replace(autoperforante, 'AUTOPERFORANTE', inplace = True)
# 
wincha = ['B-WINCHA', 'WINCHA','WINCHAS','WINCHE']
for i in datdif.Producto:
    datdif.Producto.replace(wincha, 'WINCHA', inplace = True)
# 
balde = ['BALDE', 'BALDES']
for i in datdif.Producto:
    datdif.Producto.replace(balde, 'BALDE', inplace = True)
# 
balon = ['BALON', 'BALONES']
for i in datdif.Producto:
    datdif.Producto.replace(balon, 'BALON', inplace = True)
# 
banco = ['BANCO', 'BANCOS','SILLA-BANCOS']
for i in datdif.Producto:
    datdif.Producto.replace(banco, 'BANCO', inplace = True)
# 
bandas = ['BAND', 'BANDAS']
for i in datdif.Producto:
    datdif.Producto.replace(bandas, 'BANDAS', inplace = True)
# 
banner = ['BANNER', 'BANER']
for i in datdif.Producto:
    datdif.Producto.replace(banner, 'BANNER', inplace = True)
# 
barbiquejo = ['BARBEQUEJO', 'BARBIQUEJO','BARBIQUEJOS']
for i in datdif.Producto:
    datdif.Producto.replace(barbiquejo, 'BARBIQUEJO', inplace = True)
# 
barniz = ['BARNIS', 'BARNIZ']
for i in datdif.Producto:
    datdif.Producto.replace(barniz, 'BARNIZ', inplace = True)
# 
barreta = ['BARRETA', 'BARRETAS','BARRA']
for i in datdif.Producto:
    datdif.Producto.replace(barreta, 'BARRETA', inplace = True)
# 
bebidas = ['BEBDIDAS', 'BEBIDA','BEBIDAS']
for i in datdif.Producto:
    datdif.Producto.replace(bebidas, 'BEBIDAS', inplace = True)
# 
boligrafo = ['BILIGRAFO', 'BOLIGRAFO','BOLIGRAFO(LAPICERO)','LAPECERO','LAPICERO',
             'LAPICEROS','LAPISERO','LAPISEROS','PORTALAPICEROS']
for i in datdif.Producto:
    datdif.Producto.replace(boligrafo, 'BOLIGRAFO', inplace = True)
# 
vinifan = ['VINIFAN', 'BINIFAN']
for i in datdif.Producto:
    datdif.Producto.replace(vinifan, 'VINIFAN', inplace = True)
# 
biodigestor = ['BIODEGESTOR', 'BIODIGESTOR']
for i in datdif.Producto:
    datdif.Producto.replace(biodigestor, 'BIODIGESTOR', inplace = True)
# 
bisagra = ['BISAGRA', 'BISAGRAS']
for i in datdif.Producto:
    datdif.Producto.replace(bisagra, 'BISAGRA', inplace = True)
# 
bloqueador = ['BLOQUEADOR', 'BLOQUEDOR']
for i in datdif.Producto:
    datdif.Producto.replace(bloqueador, 'BLOQUEADOR', inplace = True)
# 
bloqueta = ['BLOCK','BLOQUER','BLOQUETA','BLOQUETAS','LADRILLO','LADRILLOS']
for i in datdif.Producto:
    datdif.Producto.replace(bloqueta, 'BLOQUETA', inplace = True)
# 
bolsa = ['BOLSA','BOLSAS']
for i in datdif.Producto:
    datdif.Producto.replace(bolsa, 'BOLSA', inplace = True)
# 
briquetera = ['BRIQUETERA','BRIQUETERAS']
for i in datdif.Producto:
    datdif.Producto.replace(briquetera, 'BRIQUETERA', inplace = True)
# 
broca = ['BROCA','BROCAS']
for i in datdif.Producto:
    datdif.Producto.replace(broca, 'BROCA', inplace = True)
# 
brocha = ['BROCHA','BROCHAS']
for i in datdif.Producto:
    datdif.Producto.replace(brocha, 'BROCHA', inplace = True)
# 
buguies = ['BUGUIES','BUGUIS']
for i in datdif.Producto:
    datdif.Producto.replace(buguies, 'BUGUIES', inplace = True)
# 
cachimba = ['CACHIMBA','CACHIMBAS']
for i in datdif.Producto:
    datdif.Producto.replace(cachimba, 'CACHIMBA', inplace = True)
# 
caja = ['CAJA','CAJAS']
for i in datdif.Producto:
    datdif.Producto.replace(caja, 'CAJA', inplace = True)
# 
cal = ['CAL EN','CAL HIDRATADA']
for i in datdif.Producto:
    datdif.Producto.replace(cal, 'CAL', inplace = True)
# 
calamina = ['CALAMINA','CALAMINAS']
for i in datdif.Producto:
    datdif.Producto.replace(calamina, 'CALAMINA', inplace = True)
# 
calzados = ['CALZADO','CALZADOS']
for i in datdif.Producto:
    datdif.Producto.replace(calzados, 'CALZADOS', inplace = True)
# 
camara = ['CAMARA','CAMARAS']
for i in datdif.Producto:
    datdif.Producto.replace(camara, 'CAMARA', inplace = True)
# 
camisa = ['CAMISA','CAMISAS','CAMISETAS','CAMISETAS,']
for i in datdif.Producto:
    datdif.Producto.replace(camisa, 'CAMISA', inplace = True)
# 
canasta = ['CANASTAS','CANASTILLA']
for i in datdif.Producto:
    datdif.Producto.replace(canasta, 'CANASTA', inplace = True)
# 
candado = ['CANDADO','CANDADOS']
for i in datdif.Producto:
    datdif.Producto.replace(candado, 'CANDADO', inplace = True)
# 
carretilla = ['CARRETILLA','CARRETILLAS']
for i in datdif.Producto:
    datdif.Producto.replace(carretilla, 'CARRETILLA', inplace = True)
# 
cartel = ['CARTEL','CARTELES']
for i in datdif.Producto:
    datdif.Producto.replace(cartel, 'CARTEL', inplace = True)
# 
carton = ['CARTON','CARTONETAS']
for i in datdif.Producto:
    datdif.Producto.replace(carton, 'CARTON', inplace = True)
# 
cartucho = ['CARTUCHO','CARTUCHOS']
for i in datdif.Producto:
    datdif.Producto.replace(cartucho, 'CARTUCHO', inplace = True)
# 
cartulina = ['CARTULINA','CARTULINAS','CARTULINAS,']
for i in datdif.Producto:
    datdif.Producto.replace(cartulina, 'CARTULINA', inplace = True)
# 
casaca = ['CASACA','CASACAS']
for i in datdif.Producto:
    datdif.Producto.replace(casaca, 'CASACA', inplace = True)
# 
casco = ['CASCO','CASCOS']
for i in datdif.Producto:
    datdif.Producto.replace(casco, 'CASCO', inplace = True)
# 
cd = ['CD','CD +','CD 70MB/80MIN','CD EN','CD INCLUYE','CD R','CD REGRABABLE',
      'CD ROM','CD RW','CD RW,','CD Y/O','CD-R','CD, INCLUYE','CD/DVD','CD+SOBRE',
      'CDR EN','CDS','CDS CONO','CDS-DVD-R','CDS,']
for i in datdif.Producto:
    datdif.Producto.replace(cd, 'CD', inplace = True)
# 
ceramica = ['CERAMICA','CERAMICO','MAYOLICA']
for i in datdif.Producto:
    datdif.Producto.replace(ceramica, 'CERAMICA', inplace = True)
# 
cerradura = ['CERRADURA','CERRADURAS','CERROJO','CHAPA']
for i in datdif.Producto:
    datdif.Producto.replace(cerradura, 'CERRADURA', inplace = True)
# 
chaleco = ['CHALECO','CHALECOS']
for i in datdif.Producto:
    datdif.Producto.replace(chaleco, 'CHALECO', inplace = True)
# 
chinches = ['CHINCHE','CHINCHES']
for i in datdif.Producto:
    datdif.Producto.replace(chinches, 'CHINCHES', inplace = True)
# 
chompa = ['CHOMPA','CHOMPAS']
for i in datdif.Producto:
    datdif.Producto.replace(chompa, 'CHOMPA', inplace = True)
# 
sierra = ['CIERRA','SIERRA']
for i in datdif.Producto:
    datdif.Producto.replace(sierra, 'SIERRA', inplace = True)
# 
silicona = ['CILICONA','SILICONA','SILICONAS']
for i in datdif.Producto:
    datdif.Producto.replace(silicona, 'SILICONA', inplace = True)
# 
cilindro = ['CILINDRO','CILINDROMETALICO','CILINDROS']
for i in datdif.Producto:
    datdif.Producto.replace(cilindro, 'CILINDRO', inplace = True)
# 
cincel = ['CINCEL','CINCELES','CINSEL','SINCEL']
for i in datdif.Producto:
    datdif.Producto.replace(cincel, 'CINCEL', inplace = True)
# 
cinta = ['CINTA','CINTAS']
for i in datdif.Producto:
    datdif.Producto.replace(cinta, 'CINTA', inplace = True)
# 
cizalla = ['CISALLA','CIZALLA','CIZAYA']
for i in datdif.Producto:
    datdif.Producto.replace(cizalla, 'CIZALLA', inplace = True)
# 
clavos = ['CLAVO','CLAVOS']
for i in datdif.Producto:
    datdif.Producto.replace(clavos, 'CLAVOS', inplace = True)
# 
clips = ['CLIP','CLIPS']
for i in datdif.Producto:
    datdif.Producto.replace(clips, 'CLIPS', inplace = True)
# 
cocina = ['COCINA','COCINAS']
for i in datdif.Producto:
    datdif.Producto.replace(cocina, 'COCINA', inplace = True)
# 
codo = ['CODO','CODOS']
for i in datdif.Producto:
    datdif.Producto.replace(codo, 'CODO', inplace = True)
# 
colchon = ['COLCHAS','COLCHON','COLCHONES','COLCHONETA','COLCHONETAS']
for i in datdif.Producto:
    datdif.Producto.replace(colchon, 'COLCHON', inplace = True)
# 
comba = ['COMBA','COMBAS','COMBO','COMBOS']
for i in datdif.Producto:
    datdif.Producto.replace(comba, 'COMBA', inplace = True)
# 
compactador = ['COMPACTADOR','COMPACTADORA']
for i in datdif.Producto:
    datdif.Producto.replace(compactador, 'COMPACTADOR', inplace = True)
# 
conductor = ['COND','CONDUCTOR']
for i in datdif.Producto:
    datdif.Producto.replace(conductor, 'CONDUCTOR', inplace = True)
# 
conector = ['CONECTOR','CONECTORES']
for i in datdif.Producto:
    datdif.Producto.replace(conector, 'CONECTOR', inplace = True)
# 
cono = ['CONO','CONOS']
for i in datdif.Producto:
    datdif.Producto.replace(cono, 'CONO', inplace = True)
# 
cordel = ['CORDEL','CORDELL','CORDON']
for i in datdif.Producto:
    datdif.Producto.replace(cordel, 'CORDEL', inplace = True)
# 
corrector = ['CORECTOR','CORRECTOR','CORRECTORES']
for i in datdif.Producto:
    datdif.Producto.replace(corrector, 'CORRECTOR', inplace = True)
# 
correa = ['CORREA','CORREAJE','CORREAS']
for i in datdif.Producto:
    datdif.Producto.replace(correa, 'CORREA', inplace = True)
# 
cortador = ['CORTA','CORTADOR','CORTADORA']
for i in datdif.Producto:
    datdif.Producto.replace(cortador, 'CORTADOR', inplace = True)
# 
cortaviento = ['CORTAVIENTO','CORTAVIENTOS']
for i in datdif.Producto:
    datdif.Producto.replace(cortaviento, 'CORTAVIENTO', inplace = True)
# 
cruceta = ['CRUCETA','CRUCETAS','CRUZ','CRUZETAS']
for i in datdif.Producto:
    datdif.Producto.replace(cruceta, 'CRUCETA', inplace = True)
# 
cuaderno = ['CUADERNILLO','CUADERNO','CUADERNOS']
for i in datdif.Producto:
    datdif.Producto.replace(cuaderno, 'CUADERNO', inplace = True)
# 
cutter = ['CUTER','CUTTER','CUTTERS']
for i in datdif.Producto:
    datdif.Producto.replace(cutter, 'CUTTER', inplace = True)
# 
desinfectante = ['DESINFECTANTE','DESINFECTANTES']
for i in datdif.Producto:
    datdif.Producto.replace(desinfectante, 'DESINFECTANTE', inplace = True)
# 
diesel = ['DIESEL','DIÉSEL','DIESSEL']
for i in datdif.Producto:
    datdif.Producto.replace(diesel, 'DIESEL', inplace = True)
# 
disco = ['DISCO','DISCOS']
for i in datdif.Producto:
    datdif.Producto.replace(disco, 'DISCO', inplace = True)
# 
dolocordralan = ['DOLOCOLDRALAN','DOLOCORDRALAN']
for i in datdif.Producto:
    datdif.Producto.replace(dolocordralan, 'DOLOCORDRALAN', inplace = True)
# 
dvd = ['DVD','DVD AUDIOVISUAL','DVD EN']
for i in datdif.Producto:
    datdif.Producto.replace(dvd,'DVD', inplace = True)
# 
electrodo = ['ELECTRODO','ELECTRODOS']
for i in datdif.Producto:
    datdif.Producto.replace(electrodo,'ELECTRODO', inplace = True)
# 
engrapador = ['EMGRAMPADOR','EMGRANPADOR','ENGRAMPADOR','ENGRANPADOR','ENGRANPADORA',
              'ENGRAPADOR','ENGRAPADORA']
for i in datdif.Producto:
    datdif.Producto.replace(engrapador,'ENGRAPADOR', inplace = True)
# 
enchufe = ['ENCHUFE','ENCHUFES']
for i in datdif.Producto:
    datdif.Producto.replace(enchufe,'ENCHUFE', inplace = True)
# 
engrasador = ['ENGRASADOR','ENGRASADORA']
for i in datdif.Producto:
    datdif.Producto.replace(engrasador,'ENGRASADOR', inplace = True)
# 
equipo = ['EQUIPO','EQUIPOS']
for i in datdif.Producto:
    datdif.Producto.replace(equipo,'EQUIPO', inplace = True)
# 
escoba = ['ESCOBA','ESCOBAS','ESCOBILLA','ESCOBILLAS','ESCOBILLETA','ESCOBILLON',
          'ESCOBILLONES']
for i in datdif.Producto:
    datdif.Producto.replace(escoba,'ESCOBA', inplace = True)
# 
escuadra = ['ESCUADRA','ESCUADRAS']
for i in datdif.Producto:
    datdif.Producto.replace(escuadra,'ESCUADRA', inplace = True)
# 
esparadrapo = ['ESPADRAFO','ESPADRAPO','ESPARADRAPO']
for i in datdif.Producto:
    datdif.Producto.replace(esparadrapo,'ESPARADRAPO', inplace = True)
# 
espatula = ['ESPATULA','ESPATULAS']
for i in datdif.Producto:
    datdif.Producto.replace(espatula,'ESPATULA', inplace = True)
# 
espejo = ['ESPEJO','ESPEJOS']
for i in datdif.Producto:
    datdif.Producto.replace(espejo,'ESPEJO', inplace = True)
# 
estante = ['ESTANTES','ESTANTE']
for i in datdif.Producto:
    datdif.Producto.replace(estante,'ESTANTE', inplace = True)
# 
extension = ['EXTENCION','EXTENCIONES','EXTENSION','EXTENSIÓN']
for i in datdif.Producto:
    datdif.Producto.replace(extension,'EXTENSION', inplace = True)
# 
extintor = ['EXTINTOR','EXTINTORES']
for i in datdif.Producto:
    datdif.Producto.replace(extintor,'EXTINTOR', inplace = True)
# 
faja = ['FAJA','FAJAS']
for i in datdif.Producto:
    datdif.Producto.replace(faja,'FAJA', inplace = True)
# 
fastener = ['FASTENER','FASTENERS','FASTER']
for i in datdif.Producto:
    datdif.Producto.replace(fastener,'FASTENER', inplace = True)
# 
fideos = ['FIDEO','FIDEOS']
for i in datdif.Producto:
    datdif.Producto.replace(fideos,'FIDEOS', inplace = True)
# 
fierro = ['FIERRO','FIERROS']
for i in datdif.Producto:
    datdif.Producto.replace(fierro,'FIERRO', inplace = True)
# 
file = ['FILE','FILES']
for i in datdif.Producto:
    datdif.Producto.replace(file,'FILE', inplace = True)
# 
filtro = ['FILTRO','FILTROS']
for i in datdif.Producto:
    datdif.Producto.replace(filtro,'FILTRO', inplace = True)
# 
fluorescente = ['FLORECENTE','FLUORECENTE','FLUORESCENTE','FOCO','FOCOS']
for i in datdif.Producto:
    datdif.Producto.replace(fluorescente,'FLUORESCENTE', inplace = True)
# 
folder = ['FOLDER','FOLDERES','FOLEADOR','FOLIADOR','FOLIADORES','FOLICULO','FORDER']
for i in datdif.Producto:
    datdif.Producto.replace(folder,'FOLDER', inplace = True)
# 
formato = ['FORMATO','FORMATOS']
for i in datdif.Producto:
    datdif.Producto.replace(formato,'FORMATO', inplace = True)
# 
franela = ['FRANELA','FRANELAS']
for i in datdif.Producto:
    datdif.Producto.replace(franela,'FRANELA', inplace = True)
# 
frazada = ['FRASADA','FRAZADA','FRAZADAS']
for i in datdif.Producto:
    datdif.Producto.replace(frazada,'FRAZADA', inplace = True)
# 
frasco = ['FRASCO','FRASCOS','PMSG/FRASCOS(25ML)']
for i in datdif.Producto:
    datdif.Producto.replace(frasco,'FRASCO', inplace = True)
# 
funda = ['FUNDA','FUNDAS']
for i in datdif.Producto:
    datdif.Producto.replace(funda,'FUNDA', inplace = True)
# 
gancho = ['GANCHO','GANCHOS']
for i in datdif.Producto:
    datdif.Producto.replace(gancho,'GANCHO', inplace = True)
# 
gasa = ['GASA','GASAS']
for i in datdif.Producto:
    datdif.Producto.replace(gasa,'GASA', inplace = True)
# 
gaseosa = ['GASEOSA','GASEOSAS']
for i in datdif.Producto:
    datdif.Producto.replace(gaseosa,'GASEOSA', inplace = True)
# 
gasolina = ['GASHOL','GASOHOL','GASOLINA']
for i in datdif.Producto:
    datdif.Producto.replace(gasolina,'GASOLINA', inplace = True)
# 
goma = ['GOMA','GOMAS']
for i in datdif.Producto:
    datdif.Producto.replace(goma,'GOMA', inplace = True)
# 
gorro = ['GORRA','GORRAS','GORRO','GORROS']
for i in datdif.Producto:
    datdif.Producto.replace(gorro,'GORRO', inplace = True)
# 
gps = ['GPS','GPS NAVEGADOR']
for i in datdif.Producto:
    datdif.Producto.replace(gps,'GPS', inplace = True)
# 
grapas = ['GRAMPAS','GRAPA','GRAPAS']
for i in datdif.Producto:
    datdif.Producto.replace(grapas,'GRAPAS', inplace = True)
# 
grifa = ['GRIFA','GRIFAS']
for i in datdif.Producto:
    datdif.Producto.replace(grifa,'GRIFA', inplace = True)
# 
griferia = ['GRIFERIA','GRIFO','GRIFOS']
for i in datdif.Producto:
    datdif.Producto.replace(griferia,'GRIFERIA', inplace = True)
# 
guantes = ['GUANTE','GUANTES']
for i in datdif.Producto:
    datdif.Producto.replace(guantes,'GUANTES', inplace = True)
# 
guillotina = ['GUILLOTINA','GUILLOTINAS']
for i in datdif.Producto:
    datdif.Producto.replace(guillotina,'GUILLOTINA', inplace = True)
# 
hojas = ['HOJA','HOJAS']
for i in datdif.Producto:
    datdif.Producto.replace(hojas,'HOJAS', inplace = True)
# 
hojuelas = ['HOJUELA','HOJUELAS']
for i in datdif.Producto:
    datdif.Producto.replace(hojuelas,'HOJUELA', inplace = True)
# 
hormigon = ['HORMIGON','HORMIGÓN']
for i in datdif.Producto:
    datdif.Producto.replace(hormigon,'HORMIGON', inplace = True)
# 
impermeabilizante = ['IMPERMEABILIZANTE','IMPERMIABILIZANTE']
for i in datdif.Producto:
    datdif.Producto.replace(impermeabilizante,'IMPERMEABILIZANTE', inplace = True)
# 
imprimante = ['IMPREMANTE','IMPRIMANTE','IMPRIMANTES']
for i in datdif.Producto:
    datdif.Producto.replace(imprimante,'IMPRIMANTE', inplace = True)
# 
impresora = ['IMPRESORA','IMPRESORA,']
for i in datdif.Producto:
    datdif.Producto.replace(impresora,'IMPRESORA', inplace = True)
# 
inodoro = ['INODORO','INODOROS']
for i in datdif.Producto:
    datdif.Producto.replace(inodoro,'INODORO', inplace = True)
# 
instrumentos = ['INSTRUMENTO','INSTRUMENTOS']
for i in datdif.Producto:
    datdif.Producto.replace(instrumentos,'INSTRUMENTOS', inplace = True)
# 
interruptor = ['INTERRUPTOR','INTERUPTOR']
for i in datdif.Producto:
    datdif.Producto.replace(interruptor,'INTERRUPTOR', inplace = True)
# 
jabon = ['JABON','JABÓN','JABONERA']
for i in datdif.Producto:
    datdif.Producto.replace(jabon,'JABON', inplace = True)
# 
kit = ['KIT DE','KIT PARA','KIT VETERINARIO']
for i in datdif.Producto:
    datdif.Producto.replace(kit,'KIT', inplace = True)
# 
lapiz = ['LAPICES','LAPIZ','LÁPIZ','PORTAMINAS','PORTAMINA']
for i in datdif.Producto:
    datdif.Producto.replace(lapiz,'LAPIZ', inplace = True)
# 
lavatorio = ['LAVADERO','LAVADOR','LAVADORES','LAVAMANOS','LAVATORIO','LAVATORIOS']
for i in datdif.Producto:
    datdif.Producto.replace(lavatorio,'LAVATORIO', inplace = True)
# 
lejia = ['LEGIA','LEJIA','LEJÍA']
for i in datdif.Producto:
    datdif.Producto.replace(lejia,'LEJIA', inplace = True)
# 
libreta = ['LIBRETA','LIBRETAS']
for i in datdif.Producto:
    datdif.Producto.replace(libreta,'LIBRETA', inplace = True)
# 
lijar = ['LIJA','LIJAR']
for i in datdif.Producto:
    datdif.Producto.replace(lijar,'LIJAR', inplace = True)
# 
linterna = ['LINTERNA','LINTERNAS']
for i in datdif.Producto:
    datdif.Producto.replace(linterna,'LINTERNA', inplace = True)
# 
manguera = ['MAGUERA','MANGUERA','MANGUERA_100_MTS','MANGUERRA']
for i in datdif.Producto:
    datdif.Producto.replace(manguera,'MANGUERA', inplace = True)
# 
mascarilla = ['MASCARILLA','MASCARILLA/RESPIRADOR','MASCARILLAS','MASCARRILLA']
for i in datdif.Producto:
    datdif.Producto.replace(mascarilla,'MASCARILLA', inplace = True)
# 
plumon = ['PLUMON','PLUMÓN','PLUMONES']
for i in datdif.Producto:
    datdif.Producto.replace(plumon,'PLUMON', inplace = True)
# 
post_it = ['POS IT','POSISTS','POSIT','POSIT-IT','POSITH','POSITHE','POSSITS',
           'POST','POST-','POST-IT','POSTIT']
for i in datdif.Producto:
    datdif.Producto.replace(post_it,'POST IT', inplace = True)
# 
rastrillo = ['RASTILLO','RASTRILLO','RASTRILLOS']
for i in datdif.Producto:
    datdif.Producto.replace(rastrillo,'RASTRILLO', inplace = True)
# 
resaltador = ['RESALLTADOR','RESALTADOR','RESALTADOR.','RESALTADORES']
for i in datdif.Producto:
    datdif.Producto.replace(resaltador,'RESALTADOR', inplace = True)
# 
rollizo = ['ROLLISOS','ROLLIZO','ROLLIZOS']
for i in datdif.Producto:
    datdif.Producto.replace(rollizo,'ROLLIZO', inplace = True)
# 
sacagrapas = ['SACAGRAMPAS','SACAGRAPA','SACAGRAPAS']
for i in datdif.Producto:
    datdif.Producto.replace(sacagrapas,'SACAGRAPA', inplace = True)
# 
senaletica = ['SEÑALETICA','SEÑALETICAS','SEÑALIZACION','SEÑALIZACIÓN','SEÑALIZACIONES']
for i in datdif.Producto:
    datdif.Producto.replace(senaletica,'SENALETICA', inplace = True)
# 
sika = ['SIKA','SIKADUR','SIKADUR-32','SIKAFLEX','SIKAFLEX-IIFC']
for i in datdif.Producto:
    datdif.Producto.replace(sika,'SIKA', inplace = True)
# 
silla = ['SILLA','SILLAS','SILLON']
for i in datdif.Producto:
    datdif.Producto.replace(silla,'SILLA', inplace = True)
# 
socket = ['SOCKET','SOKET','SOKET','SOQUETS']
for i in datdif.Producto:
    datdif.Producto.replace(socket,'SOCKET', inplace = True)
# 
sumidero = ['SUMEDERO','SUMIDERO','SUMIDEROS']
for i in datdif.Producto:
    datdif.Producto.replace(sumidero,'SUMIDERO', inplace = True)
# 
suministro = ['SUMIN.','SUMINISTRO','SUMINISTRO,','SUMINISTROS']
for i in datdif.Producto:
    datdif.Producto.replace(suministro,'SUMINISTRO', inplace = True)
# 
tablas = ['TABLA','TABLAS','TABLONES','TABLETA']
for i in datdif.Producto:
    datdif.Producto.replace(tablas,'TABLAS', inplace = True)
# 
tecnoport = ['TECKNOPORT','TECNOPOR','TECNOPORT']
for i in datdif.Producto:
    datdif.Producto.replace(tecnoport,'TECNOPORT', inplace = True)
# 
tee = ['TEE','TEE 1"','TEE 1/2','TEE 3/4','TEE 3/4"','TEE DE','TEE F°G°','TEE HIDRO',
       'TEE PVC','TEE PVC-SAL','TEE SANITARIA']
for i in datdif.Producto:
    datdif.Producto.replace(tee,'TEE', inplace = True)
# 
yee = ['YEE 2"X2"','YEE 4"X4"','YEE DE','YEE PVC','YEE REDUCIDA','YEE SANITARIA']
for i in datdif.Producto:
    datdif.Producto.replace(yee,'YEE', inplace = True)

# 8. Una vez hecha la limpieza, revisamos los datos unicos de la variable
# "Producto" en la data "datdif"
# datdif.Producto.unique().shape
# Y como podemos observar, los datos unicos se redujeron de manera considerable
# a comparacion de antes
# Ahora esto valores unicos los exportaremos a Excel para poder asignarles
# los indicadores IPC, IUPC e IPM
pd.Series(datdif.Producto.unique()).to_excel('unicos_indicadores.xlsx')
# -----------------------------------------------------------------------------

# 9. Una vez asignado los indicadores a cada producto, este se tiene que volver
# a cargar para poder generalizar en la data "datdif"
indicadores = pd.read_excel('unicos_indicadores.xlsx',sheet_name=1) # (*Asignacion de indicadores elaborada por la Mgt. Pamela Torres Toledo*)

# 10. Ahora extraemos los indicadores en listas para poder generalizar
IPC = list(indicadores.MATERIALES[indicadores.INDICE == 'IPC'])
IUPC = list(indicadores.MATERIALES[indicadores.INDICE == 'IUPC'])
IPM = list(indicadores.MATERIALES[indicadores.INDICE == 'IPM'])

# 11. Generamos una variable extra llamada "Indicador" en la data "datdif" con 
# la copia de la variable "Producto"
datdif["Indicador"] = datdif.Producto.copy()

# 12. Reemplazamos los indicadores en la variable "Indicador" de la data "datdif"
# 
for x in datdif.Indicador:
    datdif.Indicador.replace(IPC, 'IPC', inplace = True)
# 
for x in datdif.Indicador:
    datdif.Indicador.replace(IUPC, 'IUPC', inplace = True)
# 
for x in datdif.Indicador:
    datdif.Indicador.replace(IPM, 'IPM', inplace = True)

# 13. Una vez reemplazada con los indicadores, podremos exportarla para otros
# estudios adicionales
datdif.to_excel('DATA_PROCESADA.xlsx')

# *** Cusco 26 de Noviembre de 2021 ***

# ============================================================================
