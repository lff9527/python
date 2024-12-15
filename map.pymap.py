import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 创建一个新的matplotlib图形
plt.figure(figsize=(8, 6))

# 定义中国的经纬度范围
llcrnrlon = 73.6713
llcrnrlat = 3.8456
urcrnrlon = 135.0956
urcrnrlat = 53.5479

# 创建Basemap实例，选择Robinson投影，并传入边界范围参数来确定显示区域
# lon_0用于指定地图中心的经度，resolution用于指定地图分辨率，可选值有'c'（粗糙）、'l'（低）、'i'（中等）、'h'（高）、'f'（精细）
m = Basemap(projection='robin', lon_0=100, resolution='l',
            llcrnrlon=llcrnrlon, llcrnrlat=llcrnrlat,
            urcrnrlon=urcrnrlon, urcrnrlat=urcrnrlat)

# 绘制海岸线和国家边界
m.drawcoastlines()
m.drawcountries()

# 绘制地图边界并填充颜色，以及填充大陆颜色、设置湖泊颜色
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral', lake_color='aqua')

# 显示图像
plt.show()
