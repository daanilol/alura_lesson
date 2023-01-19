from media_aritimetica import *
from media_geometrica import *


l = [5, 5, 5]
ar = MediaAritimetica(l)
m_ar = ar.calcula()

geo = MediaGeometrica(l)
m_geo = geo.calcula()


print(f'MA: {m_ar}')
print(f'GEO: {m_geo}')